#!/usr/bin/env python3
"""
inject_og_images.py

Injects og:image and twitter:image fallback tags into every HTML page on
the Ride Ready static site that is missing them. Pages that already have
both tags are left untouched.

Image selection logic (priority order):
  1. parks/<park>/crowd-calendar/ path → og-crowd-calendar-<park>.png
     (only when that file exists in images/og/)
  2. Fallback: og-default.png

Insertion anchors (in priority order):
  - After last <meta property="og:  line (when og: block exists)
  - After <link rel="canonical"  line
  - After </title>  line
  - SKIP: log a warning and leave file untouched
"""

import os
import re
import random
from html.parser import HTMLParser

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {
    "node_modules", ".git", "scripts", "reviews",
    "plans", ".superpowers", "tmp",
}

BASE_URL = "https://rideready.app"

# Parks that have crowd-calendar OG images available
CROWD_CAL_PARKS = {
    "busch-gardens-tampa",
    "busch-gardens-williamsburg",
    "canadas-wonderland",
    "carowinds",
    "cedar-point",
    "epic-universe",
    "islands-of-adventure",
    "kings-dominion",
    "kings-island",
    "seaworld-orlando",
    "six-flags-great-adventure",
    "six-flags-great-america",
    "six-flags-over-georgia",
    "universal-studios-florida",
}

OG_DIR = os.path.join(REPO_ROOT, "images", "og")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def pick_image(rel_path: str) -> str:
    """
    Given a path relative to REPO_ROOT, return the image filename to use.
    rel_path uses forward slashes and starts without a leading slash.
    """
    # Normalise to forward slashes
    rel_path = rel_path.replace(os.sep, "/")
    parts = rel_path.split("/")
    # Pattern: parks/<park>/crowd-calendar/...
    if len(parts) >= 3 and parts[0] == "parks" and parts[2] == "crowd-calendar":
        park = parts[1]
        if park in CROWD_CAL_PARKS:
            fname = f"og-crowd-calendar-{park}.png"
            if os.path.exists(os.path.join(OG_DIR, fname)):
                return fname
    return "og-default.png"


def detect_indent(content: str) -> str:
    """Guess predominant indent style from the head section (2 or 4 spaces)."""
    head_match = re.search(r"<head[^>]*>(.*?)</head>", content, re.S | re.I)
    region = head_match.group(1) if head_match else content[:2000]
    two_space = len(re.findall(r"^\s{2}(?!\s)<", region, re.M))
    four_space = len(re.findall(r"^\s{4}(?!\s)<", region, re.M))
    return "  " if two_space >= four_space else "    "


def build_full_block(image_filename: str, indent: str) -> str:
    """Return the full og:image + twitter block (5 lines)."""
    url = f"{BASE_URL}/images/og/{image_filename}"
    return (
        f'{indent}<meta property="og:image" content="{url}" />\n'
        f'{indent}<meta property="og:image:width" content="2400" />\n'
        f'{indent}<meta property="og:image:height" content="1260" />\n'
        f'{indent}<meta name="twitter:card" content="summary_large_image" />\n'
        f'{indent}<meta name="twitter:image" content="{url}" />\n'
    )


def build_twitter_only_block(og_image_url: str, indent: str, need_card: bool) -> str:
    """Return just the twitter:image line (and optionally twitter:card)."""
    lines = ""
    if need_card:
        lines += f'{indent}<meta name="twitter:card" content="summary_large_image" />\n'
    lines += f'{indent}<meta name="twitter:image" content="{og_image_url}" />\n'
    return lines


# ---------------------------------------------------------------------------
# HTML validation helper
# ---------------------------------------------------------------------------

class HeadValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.in_head = False
        self.depth = 0

    def handle_starttag(self, tag, attrs):
        del attrs
        self.depth += 1
        if tag == "head":
            self.in_head = True

    def handle_endtag(self, tag):
        self.depth -= 1
        if tag == "head":
            self.in_head = False

    def handle_error(self, message):
        self.errors.append(message)


def validate_html(content: str) -> bool:
    parser = HeadValidator()
    try:
        parser.feed(content)
        return len(parser.errors) == 0
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Core injection logic
# ---------------------------------------------------------------------------

def process_file(path: str):
    """
    Returns (modified: bool, action: str, skip_reason: str | None).
    action is one of: 'both', 'twitter_only', 'skipped', 'unchanged'.
    """
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            original = fh.read()
    except Exception as e:
        return False, "skipped", f"read error: {e}"

    content = original

    has_og_image = bool(re.search(r'property=["\']og:image["\']', content))
    has_twitter_image = bool(re.search(r'name=["\']twitter:image["\']', content))
    has_twitter_card = bool(re.search(r'name=["\']twitter:card["\']', content))

    if has_og_image and has_twitter_image:
        return False, "unchanged", None

    rel_path = os.path.relpath(path, REPO_ROOT)
    indent = detect_indent(content)

    # ------------------------------------------------------------------
    # Case 1: Both missing → inject full block
    # ------------------------------------------------------------------
    if not has_og_image:
        image_filename = pick_image(rel_path)
        new_block = build_full_block(image_filename, indent)

        # Anchor A: after last <meta property="og:  line
        og_meta_lines = list(re.finditer(r'[^\n]*property=["\']og:[^\n]*\n', content))
        if og_meta_lines:
            last_og = og_meta_lines[-1]
            insert_pos = last_og.end()
            new_content = content[:insert_pos] + new_block + content[insert_pos:]
        else:
            # Anchor B: after <link rel="canonical"  line
            canonical_m = re.search(r'[^\n]*rel=["\']canonical["\'][^\n]*\n', content, re.I)
            if canonical_m:
                insert_pos = canonical_m.end()
                new_content = content[:insert_pos] + new_block + content[insert_pos:]
            else:
                # Anchor C: after </title>
                title_m = re.search(r'</title[^>]*>\n?', content, re.I)
                if title_m:
                    insert_pos = title_m.end()
                    new_content = content[:insert_pos] + new_block + content[insert_pos:]
                else:
                    return False, "skipped", "no og:, canonical, or title anchor found"

        with open(path, "w", encoding="utf-8") as fh:
            fh.write(new_content)
        return True, "both", None

    # ------------------------------------------------------------------
    # Case 2: has og:image but missing twitter:image
    # ------------------------------------------------------------------
    # Extract existing og:image URL
    og_url_m = re.search(r'<meta\s[^>]*property=["\']og:image["\'][^>]*content=["\']([^"\']+)["\']', content)
    if not og_url_m:
        og_url_m = re.search(r'<meta\s[^>]*content=["\']([^"\']+)["\'][^>]*property=["\']og:image["\']', content)

    if not og_url_m:
        return False, "skipped", "has og:image attr but could not extract URL"

    og_image_url = og_url_m.group(1)
    twitter_block = build_twitter_only_block(og_image_url, indent, need_card=not has_twitter_card)

    # Insert immediately after the og:image line (or its multi-line block)
    og_image_line_m = re.search(r'[^\n]*property=["\']og:image["\'][^\n]*\n', content)
    if not og_image_line_m:
        return False, "skipped", "could not locate og:image line for twitter insertion"

    insert_pos = og_image_line_m.end()
    new_content = content[:insert_pos] + twitter_block + content[insert_pos:]

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new_content)
    return True, "twitter_only", None


# ---------------------------------------------------------------------------
# Walk and process
# ---------------------------------------------------------------------------

def main():
    stats = {"both": 0, "twitter_only": 0, "unchanged": 0, "skipped": 0}
    skipped_files = []
    modified_files = []

    for dirpath, dirs, files in os.walk(REPO_ROOT):
        # Prune skip dirs and hidden dirs in-place
        dirs[:] = sorted(
            d for d in dirs
            if d not in SKIP_DIRS and not d.startswith(".")
        )
        for fname in files:
            if not fname.endswith(".html"):
                continue
            full_path = os.path.join(dirpath, fname)
            modified, action, reason = process_file(full_path)
            stats[action] += 1
            if action == "skipped":
                skipped_files.append((full_path, reason))
                print(f"  SKIP  {os.path.relpath(full_path, REPO_ROOT)}: {reason}")
            elif modified:
                modified_files.append((full_path, action))

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print("\n=== inject_og_images.py results ===")
    print(f"  Modified (full block injected):    {stats['both']}")
    print(f"  Modified (twitter-only injected):  {stats['twitter_only']}")
    print(f"  Already complete (untouched):      {stats['unchanged']}")
    print(f"  Skipped:                           {stats['skipped']}")
    if skipped_files:
        print("\n  Skipped files:")
        for p, r in skipped_files:
            print(f"    {os.path.relpath(p, REPO_ROOT)}: {r}")

    # ------------------------------------------------------------------
    # Verification pass: count tags and spot-check 10 random modified files
    # ------------------------------------------------------------------
    print("\n=== Verification ===")
    total_html = 0
    total_og_image = 0
    total_twitter_image = 0

    all_html = []
    for dirpath, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = sorted(
            d for d in dirs
            if d not in SKIP_DIRS and not d.startswith(".")
        )
        for fname in files:
            if not fname.endswith(".html"):
                continue
            full_path = os.path.join(dirpath, fname)
            all_html.append(full_path)
            try:
                c = open(full_path, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            total_html += 1
            if re.search(r'property=["\']og:image["\']', c):
                total_og_image += 1
            if re.search(r'name=["\']twitter:image["\']', c):
                total_twitter_image += 1

    print(f"  Total HTML files:          {total_html}")
    print(f"  Pages with og:image:       {total_og_image}")
    print(f"  Pages with twitter:image:  {total_twitter_image}")

    # Spot check
    sample = modified_files[:]
    random.shuffle(sample)
    sample = sample[:10]
    parse_errors = 0
    print(f"\n  Spot-checking {len(sample)} randomly sampled modified files with html.parser:")
    for path, action in sample:
        try:
            c = open(path, encoding="utf-8", errors="replace").read()
            parser = HTMLParser()
            parser.feed(c)
            # Quick sanity: check expected tags exist
            has_og = bool(re.search(r'property=["\']og:image["\']', c))
            has_tw = bool(re.search(r'name=["\']twitter:image["\']', c))
            status = "OK" if (has_og and has_tw) else "MISSING_TAGS"
            print(f"    [{status}] ({action}) {os.path.relpath(path, REPO_ROOT)}")
        except Exception as e:
            parse_errors += 1
            print(f"    [PARSE_ERROR] {os.path.relpath(path, REPO_ROOT)}: {e}")

    if parse_errors:
        print(f"\n  WARNING: {parse_errors} parse error(s) in sample.")
    else:
        print("\n  All sampled files parsed without errors.")


if __name__ == "__main__":
    main()
