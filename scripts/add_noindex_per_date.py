#!/usr/bin/env python3
"""
Add <meta name="robots" content="noindex,follow"> to every per-date
crowd-calendar page: parks/<park>/crowd-calendar/YYYY-MM-DD/index.html

Rules:
- If the file already has a robots meta tag with exactly "noindex,follow", skip (already done).
- If the file has a robots meta tag with ANY OTHER content, log a warning and do NOT modify.
- Otherwise, insert the noindex tag immediately after the <meta charset line.

Run from the repo root or anywhere — uses the script's own location to find the repo root.
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE_RE = re.compile(r"[\\/]parks[\\/][^\\/]+[\\/]crowd-calendar[\\/]\d{4}-\d{2}-\d{2}[\\/]index\.html$")
NOINDEX_TAG = '  <meta name="robots" content="noindex,follow" />'

scanned = 0
modified = 0
skipped = 0
warnings = 0

for dirpath, dirnames, filenames in os.walk(os.path.join(REPO_ROOT, "parks")):
    for fname in filenames:
        if fname != "index.html":
            continue
        full_path = os.path.join(dirpath, fname)
        # Normalise to forward slashes for regex matching on all platforms
        norm_path = full_path.replace("\\", "/")
        if not DATE_RE.search(norm_path):
            continue

        scanned += 1

        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check for any existing robots meta tag (case-insensitive search within <head>)
        robots_match = re.search(
            r'<meta\s[^>]*name=["\']robots["\'][^>]*>',
            content,
            re.IGNORECASE,
        )
        if robots_match:
            tag_text = robots_match.group(0)
            if re.search(r'noindex,follow', tag_text, re.IGNORECASE):
                print(f"SKIP (already has noindex,follow): {norm_path}")
                skipped += 1
            else:
                print(f"WARNING (unexpected robots tag, not modified): {tag_text!r}  in  {norm_path}", file=sys.stderr)
                warnings += 1
            continue

        # Insert after the <meta charset line
        new_content, n_subs = re.subn(
            r'(<meta\s+charset=["\'][^"\']*["\'][^>]*>)',
            r'\1\n' + NOINDEX_TAG,
            content,
            count=1,
        )
        if n_subs == 0:
            print(f"WARNING (no <meta charset> found, skipping): {norm_path}", file=sys.stderr)
            warnings += 1
            continue

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        modified += 1

print()
print("=== Summary ===")
print(f"  Scanned : {scanned}")
print(f"  Modified: {modified}")
print(f"  Skipped (already had noindex,follow): {skipped}")
print(f"  Warnings: {warnings}")
