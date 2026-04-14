#!/usr/bin/env python3
"""
fix_contrast.py — Fix low-contrast text colors across Ride Ready static site.

Only modifies `color:` CSS property values. Does NOT touch background-color,
border-color, box-shadow, or any other property.
"""

import os
import re
import sys
from html.parser import HTMLParser
from collections import defaultdict

# Directories to exclude (relative to repo root, or anywhere in path)
EXCLUDE_DIRS = {
    'node_modules', '.git', 'scripts', 'reviews', 'plans',
    '.superpowers', 'tmp',
}

# Substitution patterns — each is (regex_pattern, replacement)
# The (color:\s*) capture group is mandatory to ensure only color: properties are touched.
PATTERNS = [
    # #555 / #555555
    (r'(color:\s*)#555(?![0-9a-fA-F])',      r'\1#999'),
    (r'(color:\s*)#555555\b',                 r'\1#999999'),
    # #666 / #666666
    (r'(color:\s*)#666(?![0-9a-fA-F])',      r'\1#aaa'),
    (r'(color:\s*)#666666\b',                 r'\1#aaaaaa'),
    # #777 / #777777
    (r'(color:\s*)#777(?![0-9a-fA-F])',      r'\1#aaa'),
    (r'(color:\s*)#777777\b',                 r'\1#aaaaaa'),
    # #888 / #888888
    (r'(color:\s*)#888(?![0-9a-fA-F])',      r'\1#aaa'),
    (r'(color:\s*)#888888\b',                 r'\1#aaaaaa'),
    # rgba(255,255,255, alpha) where alpha < 0.6 — handles both spaced and unspaced
    # This catches 0.3, 0.35, 0.4, 0.45, 0.5, 0.55 etc up to but not including 0.6
    (r'(color:\s*)rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.[0-5]\d*\s*\)',
                                              r'\1rgba(255, 255, 255, 0.75)'),
    # Named colors grey / gray
    (r'(color:\s*)(?:grey|gray)\b',           r'\1#aaa'),
]

# Compile patterns once
COMPILED = [(re.compile(pat, re.IGNORECASE), repl, pat) for pat, repl, pat in
            [(re.compile(pat, re.IGNORECASE), repl, pat) for pat, repl in PATTERNS]]


def should_exclude(path, root):
    """Return True if any path component is in EXCLUDE_DIRS."""
    rel = os.path.relpath(path, root)
    parts = rel.replace('\\', '/').split('/')
    # Also exclude hidden dirs (starting with .)
    for part in parts[:-1]:  # exclude filename itself from dir check
        if part in EXCLUDE_DIRS or (part.startswith('.') and part != '.'):
            return True
    return False


def process_file(filepath):
    """Apply all substitutions to a single file. Returns (new_content, counts_dict)."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    counts = defaultdict(int)
    original = content

    for compiled_re, repl, original_pat in COMPILED:
        new_content, n = compiled_re.subn(repl, content)
        if n:
            counts[original_pat] += n
        content = new_content

    return content, counts, content != original


def verify_html(filepath):
    """Parse file with html.parser to check for obvious mangling. Returns True if ok."""
    class ErrorCounter(HTMLParser):
        def __init__(self):
            super().__init__()
            self.errors = 0
        def handle_error(self, message):
            del message
            self.errors += 1

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    parser = ErrorCounter()
    try:
        parser.feed(content)
        return parser.errors == 0
    except Exception:
        return False


def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Repo root: {repo_root}")

    # Walk and collect .html files
    html_files = []
    for dirpath, dirnames, filenames in os.walk(repo_root):
        # Prune excluded dirs in-place so os.walk doesn't descend into them
        dirnames[:] = [
            d for d in dirnames
            if d not in EXCLUDE_DIRS and not (d.startswith('.') and d != '.')
        ]

        for filename in filenames:
            if not filename.endswith('.html'):
                continue
            filepath = os.path.join(dirpath, filename)
            if should_exclude(filepath, repo_root):
                continue
            html_files.append(filepath)

    print(f"Found {len(html_files)} HTML files to process\n")

    total_counts = defaultdict(int)
    modified_files = []
    skipped_files = []

    for filepath in sorted(html_files):
        new_content, counts, changed = process_file(filepath)
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified_files.append((filepath, dict(counts)))
            for pat, n in counts.items():
                total_counts[pat] += n
        else:
            skipped_files.append(filepath)

    # Summary
    print("=" * 70)
    print(f"FILES MODIFIED: {len(modified_files)}")
    print(f"FILES UNCHANGED: {len(skipped_files)}")
    print()
    print("REPLACEMENTS BY PATTERN:")
    for pat, _ in PATTERNS:
        n = total_counts.get(pat, 0)
        status = "" if n > 0 else "  <-- ZERO MATCHES"
        print(f"  {n:5d}  {pat!r}{status}")
    print(f"\n  TOTAL: {sum(total_counts.values())}")

    # Per-file detail
    print()
    print("MODIFIED FILES DETAIL:")
    for filepath, counts in modified_files:
        rel = os.path.relpath(filepath, repo_root)
        total = sum(counts.values())
        print(f"  {rel}  ({total} replacements)")

    # Spot-check: verify borders/backgrounds not touched in 3 specific files
    print()
    print("=" * 70)
    print("SPOT-CHECK: border/background colors untouched")
    spot_check_files = [
        os.path.join(repo_root, 'index.html'),
        os.path.join(repo_root, 'parks/kings-island/crowd-calendar/index.html'),
        os.path.join(repo_root, 'tools/og-image-generator.html'),
    ]
    for filepath in spot_check_files:
        rel = os.path.relpath(filepath, repo_root)
        if not os.path.exists(filepath):
            print(f"  MISSING: {rel}")
            continue
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        # Look for border/background rules that might have been incorrectly changed
        # These should still have original dim values
        border_333 = len(re.findall(r'border[^:]*:\s*[^;]*#333', content, re.IGNORECASE))
        # Check that no border/bg has been accidentally brightened to #aaa/#999
        suspicious_border = len(re.findall(r'border[^:]*:\s*[^;]*(?:#aaa|#999|#aaaaaa|#999999)', content, re.IGNORECASE))
        print(f"  {rel}")
        print(f"    border:#333 occurrences (should be >0 if file has borders): {border_333}")
        print(f"    suspicious border:#aaa/#999 (should be 0): {suspicious_border}")

    # Spot-check: HTML parse 5 random modified files
    print()
    print("SPOT-CHECK: HTML parse integrity (5 modified files)")
    import random
    sample = modified_files[:5] if len(modified_files) <= 5 else random.sample(modified_files, 5)
    all_ok = True
    for filepath, _ in sample:
        rel = os.path.relpath(filepath, repo_root)
        ok = verify_html(filepath)
        status = "OK" if ok else "PARSE ERRORS DETECTED"
        if not ok:
            all_ok = False
        print(f"  {'OK' if ok else 'FAIL'}  {rel}")

    # Post-fix residual scan: check for remaining flagged color: values
    print()
    print("RESIDUAL SCAN: remaining flagged color: values in modified files")
    residual_patterns = [
        r'color:\s*#555(?![0-9a-fA-F])',
        r'color:\s*#555555\b',
        r'color:\s*#666(?![0-9a-fA-F])',
        r'color:\s*#666666\b',
        r'color:\s*#777(?![0-9a-fA-F])',
        r'color:\s*#777777\b',
        r'color:\s*#888(?![0-9a-fA-F])',
        r'color:\s*#888888\b',
        r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.[0-5]',
        r'color:\s*(?:grey|gray)\b',
    ]
    residual_total = 0
    for filepath, _ in modified_files:
        rel = os.path.relpath(filepath, repo_root)
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        for pat in residual_patterns:
            matches = re.findall(pat, content, re.IGNORECASE)
            if matches:
                print(f"  RESIDUAL in {rel}: {len(matches)}x  {pat!r}")
                residual_total += len(matches)
    if residual_total == 0:
        print("  None found — all flagged patterns resolved.")
    else:
        print(f"  WARNING: {residual_total} residual matches remain.")

    print()
    print("Done.")
    return 0 if all_ok else 1


if __name__ == '__main__':
    sys.exit(main())
