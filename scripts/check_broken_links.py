#!/usr/bin/env python3
"""
check_broken_links.py

Crawls every HTML file in the rideready.app static site and reports
internal broken links.

Output: reviews/2026-04-14-audit-response/broken-links.csv
"""

import os
import csv
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse
from collections import defaultdict

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_HOST = "rideready.app"

EXCLUDE_DIRS = {
    "node_modules",
    ".git",
    "scripts",
    "reviews",
    "plans",
    ".superpowers",
}

EXCLUDE_NAMES = {
    "Archive.zip",
}

OUTPUT_DIR = os.path.join(REPO_ROOT, "reviews", "2026-04-14-audit-response")
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "broken-links.csv")


# ---------------------------------------------------------------------------
# HTML parser – extracts <a href> and <link href> targets
# ---------------------------------------------------------------------------

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "a":
            href = (attrs_dict.get("href") or "").strip()
            if href:
                self.links.append(href)
        elif tag == "link":
            rel = (attrs_dict.get("rel") or "").strip().lower()
            if rel in ("canonical", "alternate"):
                href = (attrs_dict.get("href") or "").strip()
                if href:
                    self.links.append(href)


def extract_links(html_path: str) -> list[str]:
    try:
        with open(html_path, "r", encoding="utf-8", errors="replace") as fh:
            content = fh.read()
    except OSError:
        return []
    parser = LinkExtractor()
    parser.feed(content)
    return parser.links


# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------

def resolve_internal_path(href: str, source_file: str) -> str | None:
    """
    Given an href that has already been classified as internal and a source
    HTML file path (absolute), return the absolute filesystem path that the
    href points to.  Returns None if resolution is not possible.
    """
    # Strip fragment and query string
    parsed = urlparse(href)
    path = parsed.path
    if not path:
        return None

    if path.startswith("/"):
        # Root-relative
        abs_path = os.path.join(REPO_ROOT, path.lstrip("/"))
    else:
        # Relative to the directory containing the source file
        abs_path = os.path.join(os.path.dirname(source_file), path)

    # Normalise (resolve ../ etc.)
    abs_path = os.path.normpath(abs_path)

    # If path ends with / → index.html
    if href.rstrip("?#").endswith("/") or path.endswith("/"):
        return os.path.join(abs_path, "index.html")

    # If path has a file extension, use as-is
    _, ext = os.path.splitext(abs_path)
    if ext:
        return abs_path

    # No extension: try <path>.html, then <path>/index.html
    # Return a sentinel that means "check both"
    return abs_path  # caller will try .html and /index.html


def check_path_exists(abs_path: str, original_href: str) -> tuple[bool, str, str]:
    """
    Returns (exists, resolved_path_used, reason).
    """
    parsed = urlparse(original_href)
    path = parsed.path
    _, ext = os.path.splitext(abs_path)
    ends_with_slash = path.endswith("/")

    if ends_with_slash:
        # Must be index.html
        candidate = abs_path if abs_path.endswith("index.html") else os.path.join(abs_path, "index.html")
        if os.path.isfile(candidate):
            return True, candidate, ""
        return False, candidate, "index.html not found for trailing-slash path"

    if ext:
        if os.path.isfile(abs_path):
            return True, abs_path, ""
        return False, abs_path, "file not found"

    # No extension – try .html then /index.html
    candidate_html = abs_path + ".html"
    candidate_index = os.path.join(abs_path, "index.html")
    if os.path.isfile(candidate_html):
        return True, candidate_html, ""
    if os.path.isfile(candidate_index):
        return True, candidate_index, ""
    # Neither exists
    return False, candidate_index, "neither .html nor /index.html found"


# ---------------------------------------------------------------------------
# Link classification
# ---------------------------------------------------------------------------

SKIP_SCHEMES = {"mailto", "tel", "javascript", "data"}


def classify_href(href: str) -> str:
    """
    Returns one of: 'skip', 'external', 'internal'
    """
    href = href.strip()
    if not href or href.startswith("#"):
        return "skip"

    parsed = urlparse(href)

    if parsed.scheme in SKIP_SCHEMES:
        return "skip"

    if parsed.scheme in ("http", "https"):
        host = parsed.netloc.lower().lstrip("www.")
        if host == SITE_HOST or host == f"www.{SITE_HOST}":
            return "internal"
        return "external"

    # Relative paths (no scheme)
    return "internal"


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def find_html_files() -> list[str]:
    html_files = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        # Prune excluded dirs in-place
        rel_dir = os.path.relpath(dirpath, REPO_ROOT)
        # Check if any component of the path is excluded
        parts = rel_dir.split(os.sep)
        if any(p in EXCLUDE_DIRS or p.startswith(".") for p in parts if p != "."):
            dirnames.clear()
            continue
        # Also prune from dirnames so os.walk won't recurse into them
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDE_DIRS and not d.startswith(".")
        ]
        for fname in filenames:
            if fname in EXCLUDE_NAMES:
                continue
            if fname.endswith(".html"):
                html_files.append(os.path.join(dirpath, fname))
    return sorted(html_files)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    html_files = find_html_files()
    print(f"Found {len(html_files)} HTML files to scan.")

    broken: list[dict] = []
    total_internal = 0

    # Track broken targets → set of source files (for priority ranking)
    broken_target_sources: dict[str, set] = defaultdict(set)

    for source_file in html_files:
        links = extract_links(source_file)
        source_rel = os.path.relpath(source_file, REPO_ROOT)

        for href in links:
            kind = classify_href(href)
            if kind != "internal":
                continue

            total_internal += 1

            # Strip fragment before passing to resolver
            parsed = urlparse(href)
            href_no_fragment = parsed._replace(fragment="").geturl()

            resolved_base = resolve_internal_path(href_no_fragment, source_file)
            if resolved_base is None:
                continue

            exists, resolved_path, reason = check_path_exists(resolved_base, href_no_fragment)
            resolved_rel = os.path.relpath(resolved_path, REPO_ROOT)

            if not exists:
                broken.append({
                    "source_file": source_rel,
                    "href": href,
                    "resolved_path": resolved_rel,
                    "reason": reason,
                })
                broken_target_sources[resolved_rel].add(source_rel)

    # Write CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["source_file", "href", "resolved_path", "reason"])
        writer.writeheader()
        writer.writerows(broken)

    # Summary
    print()
    print("=" * 60)
    print("BROKEN LINK AUDIT SUMMARY")
    print("=" * 60)
    print(f"HTML files scanned   : {len(html_files)}")
    print(f"Internal links checked: {total_internal}")
    print(f"Broken links found   : {len(broken)}")
    print()

    # Top 10 most-referenced broken targets
    if broken_target_sources:
        ranked = sorted(broken_target_sources.items(), key=lambda x: -len(x[1]))
        print("Top 10 most-referenced broken targets (by number of source pages):")
        print(f"  {'References':>10}  Target")
        print(f"  {'-'*10}  {'-'*50}")
        for target, sources in ranked[:10]:
            print(f"  {len(sources):>10}  {target}")
    else:
        print("No broken internal links found.")

    print()
    print(f"Full results written to: {os.path.relpath(OUTPUT_CSV, REPO_ROOT)}")

    return 0 if not broken else 1


if __name__ == "__main__":
    sys.exit(main())
