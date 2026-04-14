#!/usr/bin/env python3
"""
generate_sitemap.py — regenerate sitemap.xml for rideready.app
"""

import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://rideready.app"
OUTPUT = REPO_ROOT / "sitemap.xml"

# Directories to skip entirely (relative names, matched against each path component)
SKIP_DIRS = {
    "node_modules", ".git", "scripts", "reviews", "plans", ".superpowers",
}

# Standalone HTML files to exclude by name
SKIP_FILES = {"404.html", "thank-you.html"}

# Per-date crowd-calendar pages (YYYY-MM-DD dir) are thin templates — omit from
# sitemap to avoid low-quality-content signals. They carry <meta robots=noindex>
# and stay discoverable via the monthly crowd-calendar index.
DATE_DIR_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def should_skip(path: Path) -> bool:
    """Return True if this path (or any ancestor dir) should be excluded."""
    rel = path.relative_to(REPO_ROOT)
    for part in rel.parts[:-1]:  # directory parts only
        if part in SKIP_DIRS or part.startswith("."):
            return True
        if DATE_DIR_RE.match(part):
            return True
    if path.name in SKIP_FILES:
        return True
    return False


def collect_html_files() -> list[Path]:
    files = []
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dp = Path(dirpath)
        # Prune skip dirs in-place so os.walk doesn't descend into them
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIRS and not d.startswith(".")
        ]
        for fname in filenames:
            if fname.endswith(".html"):
                p = dp / fname
                if not should_skip(p):
                    files.append(p)
    return files


def url_for(path: Path) -> str:
    """Derive the public URL for a given HTML file path."""
    rel = path.relative_to(REPO_ROOT)
    parts = rel.parts

    if path.name == "index.html":
        if len(parts) == 1:
            # Root index.html → https://rideready.app/
            return BASE_URL + "/"
        else:
            # Subdirectory index.html → directory URL with trailing slash
            dir_path = "/".join(parts[:-1])
            return BASE_URL + "/" + dir_path + "/"
    else:
        # Standalone .html file → full path, no trailing slash
        return BASE_URL + "/" + "/".join(parts)


def git_lastmod(path: Path) -> str:
    """Return YYYY-MM-DD lastmod using git log, falling back to mtime."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(path)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
        iso = result.stdout.strip()
        if iso:
            # Parse ISO 8601 date (e.g. 2026-04-14T12:34:56+00:00) → YYYY-MM-DD
            return iso[:10]
    except Exception:
        pass
    # Fallback: filesystem mtime
    mtime = path.stat().st_mtime
    return datetime.fromtimestamp(mtime, tz=timezone.utc).strftime("%Y-%m-%d")


def heuristics(url: str) -> tuple[str, str]:
    """Return (priority, changefreq) for a URL."""
    path = url.removeprefix(BASE_URL)

    # Root
    if path == "/":
        return "1.0", "weekly"

    # /parks/<park>/ — exactly two path segments after root
    # e.g. /parks/kings-island/
    park_landing = re.match(r"^/parks/[^/]+/$", path)
    if park_landing:
        return "0.9", "weekly"

    # /parks/<park>/crowd-calendar/  or  /parks/<park>/queues/*
    crowd_or_queue = re.match(
        r"^/parks/[^/]+/(crowd-calendar|queues)(/.*)?$", path
    )
    if crowd_or_queue:
        return "0.8", "weekly"

    # Everything else
    return "0.7", "monthly"


def build_sitemap(entries: list[dict]) -> str:
    """Render sorted entries as a valid sitemap XML string."""
    sorted_entries = sorted(entries, key=lambda e: e["loc"])

    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for e in sorted_entries:
        lines.append("  <url>")
        lines.append(f"    <loc>{e['loc']}</loc>")
        lines.append(f"    <lastmod>{e['lastmod']}</lastmod>")
        lines.append(f"    <changefreq>{e['changefreq']}</changefreq>")
        lines.append(f"    <priority>{e['priority']}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main():
    html_files = collect_html_files()

    entries = []
    for path in html_files:
        loc = url_for(path)
        lastmod = git_lastmod(path)
        priority, changefreq = heuristics(loc)
        entries.append(
            {"loc": loc, "lastmod": lastmod, "changefreq": changefreq, "priority": priority}
        )

    xml_content = build_sitemap(entries)

    OUTPUT.write_text(xml_content, encoding="utf-8")

    print(f"Written {len(entries)} URLs to {OUTPUT}")
    return len(entries)


if __name__ == "__main__":
    main()
