#!/usr/bin/env python3
"""
fix_date_prev_next.py

Rewrites the Previous Day / Next Day nav links on every per-date crowd-calendar
page so they point to the actually existing adjacent dates (skipping closed-park
dates that have no generated page).

- If no prev date exists (earliest page), the prev <a> is replaced with a <span>
  that has identical layout but is visually de-emphasised (opacity:0.35).
- Same for next when this is the latest page.
- Files are only written when a change is actually needed.
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARKS_DIR = os.path.join(REPO_ROOT, "parks")

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Patterns to match the existing prev/next anchors.
# We match by the trailing text so we don't accidentally touch other links.
# The href group captures whatever date path is currently there.
PREV_A_RE = re.compile(
    r'<a\s+href="([^"]+)"\s+style="color:var\(--muted\);text-decoration:none;font-size:14px;padding:8px 0;">&#x2190; Previous Day</a>',
    re.DOTALL,
)
NEXT_A_RE = re.compile(
    r'<a\s+href="([^"]+)"\s+style="color:var\(--muted\);text-decoration:none;font-size:14px;padding:8px 0;">Next Day &#x2192;</a>',
    re.DOTALL,
)

# Disabled span replacements (keep layout, remove link)
PREV_SPAN = '<span style="color:var(--muted);text-decoration:none;font-size:14px;padding:8px 0;opacity:0.35;">&#x2190; Previous Day</span>'
NEXT_SPAN = '<span style="color:var(--muted);text-decoration:none;font-size:14px;padding:8px 0;opacity:0.35;">Next Day &#x2192;</span>'


def make_prev_a(park_slug: str, date: str) -> str:
    href = f"/parks/{park_slug}/crowd-calendar/{date}/"
    return (
        f'<a href="{href}" style="color:var(--muted);text-decoration:none;'
        f'font-size:14px;padding:8px 0;">&#x2190; Previous Day</a>'
    )


def make_next_a(park_slug: str, date: str) -> str:
    href = f"/parks/{park_slug}/crowd-calendar/{date}/"
    return (
        f'<a href="{href}" style="color:var(--muted);text-decoration:none;'
        f'font-size:14px;padding:8px 0;">Next Day &#x2192;</a>'
    )


def process_park(park_slug: str) -> tuple[int, int]:
    """Returns (modified_count, already_correct_count)."""
    cal_dir = os.path.join(PARKS_DIR, park_slug, "crowd-calendar")
    if not os.path.isdir(cal_dir):
        return 0, 0

    # Collect existing date dirs
    dates = sorted(
        d for d in os.listdir(cal_dir)
        if DATE_RE.match(d) and os.path.isfile(os.path.join(cal_dir, d, "index.html"))
    )

    if not dates:
        return 0, 0

    modified = 0
    already_correct = 0

    for i, date in enumerate(dates):
        page = os.path.join(cal_dir, date, "index.html")
        prev_date = dates[i - 1] if i > 0 else None
        next_date = dates[i + 1] if i < len(dates) - 1 else None

        with open(page, "r", encoding="utf-8") as fh:
            original = fh.read()

        content = original

        # --- Prev link ---
        prev_match = PREV_A_RE.search(content)
        if prev_match:
            if prev_date is None:
                desired_prev = PREV_SPAN
            else:
                desired_prev = make_prev_a(park_slug, prev_date)

            if prev_match.group(0) != desired_prev:
                content = content[:prev_match.start()] + desired_prev + content[prev_match.end():]
        else:
            # Check if prev is already a span (possibly already disabled)
            prev_span_re = re.compile(
                r'<span[^>]+>&#x2190; Previous Day</span>'
            )
            prev_span_match = prev_span_re.search(content)
            if prev_span_match:
                if prev_date is not None:
                    # Should be a link now
                    desired_prev = make_prev_a(park_slug, prev_date)
                    if prev_span_match.group(0) != desired_prev:
                        content = content[:prev_span_match.start()] + desired_prev + content[prev_span_match.end():]
                else:
                    # Already a span and should be disabled — check if content matches
                    if prev_span_match.group(0) != PREV_SPAN:
                        content = content[:prev_span_match.start()] + PREV_SPAN + content[prev_span_match.end():]
            else:
                print(f"  WARNING: no prev nav found in {park_slug}/{date}/index.html")

        # --- Next link ---
        next_match = NEXT_A_RE.search(content)
        if next_match:
            if next_date is None:
                desired_next = NEXT_SPAN
            else:
                desired_next = make_next_a(park_slug, next_date)

            if next_match.group(0) != desired_next:
                content = content[:next_match.start()] + desired_next + content[next_match.end():]
        else:
            # Check if next is already a span
            next_span_re = re.compile(
                r'<span[^>]+>Next Day &#x2192;</span>'
            )
            next_span_match = next_span_re.search(content)
            if next_span_match:
                if next_date is not None:
                    desired_next = make_next_a(park_slug, next_date)
                    if next_span_match.group(0) != desired_next:
                        content = content[:next_span_match.start()] + desired_next + content[next_span_match.end():]
                else:
                    if next_span_match.group(0) != NEXT_SPAN:
                        content = content[:next_span_match.start()] + NEXT_SPAN + content[next_span_match.end():]
            else:
                print(f"  WARNING: no next nav found in {park_slug}/{date}/index.html")

        if content != original:
            with open(page, "w", encoding="utf-8") as fh:
                fh.write(content)
            modified += 1
            print(f"  MODIFIED  {park_slug}/{date}/index.html"
                  f"  prev={prev_date or 'NONE'}  next={next_date or 'NONE'}")
        else:
            already_correct += 1

    return modified, already_correct


def spot_check():
    """Print specific nav values for the requested spot-check files."""
    checks = [
        ("busch-gardens-williamsburg", "2026-03-15"),
        ("busch-gardens-williamsburg", "2026-03-17"),
        ("busch-gardens-williamsburg", "2026-03-13"),  # earliest
        ("busch-gardens-williamsburg", "2026-04-08"),  # latest (at time of writing)
    ]
    print()
    print("=" * 60)
    print("SPOT CHECK")
    print("=" * 60)
    for park_slug, date in checks:
        page = os.path.join(PARKS_DIR, park_slug, "crowd-calendar", date, "index.html")
        if not os.path.isfile(page):
            print(f"  {park_slug}/{date}: FILE NOT FOUND")
            continue
        with open(page, "r", encoding="utf-8") as fh:
            content = fh.read()
        prev_m = PREV_A_RE.search(content)
        next_m = NEXT_A_RE.search(content)
        prev_span_m = re.search(r'<span[^>]+>&#x2190; Previous Day</span>', content)
        next_span_m = re.search(r'<span[^>]+>Next Day &#x2192;</span>', content)

        prev_val = prev_m.group(1) if prev_m else ("[SPAN/disabled]" if prev_span_m else "NOT FOUND")
        next_val = next_m.group(1) if next_m else ("[SPAN/disabled]" if next_span_m else "NOT FOUND")

        print(f"  {park_slug}/{date}")
        print(f"    prev href: {prev_val}")
        print(f"    next href: {next_val}")


def main():
    parks = sorted(
        d for d in os.listdir(PARKS_DIR)
        if os.path.isdir(os.path.join(PARKS_DIR, d)) and d != "index.html"
    )

    total_modified = 0
    total_correct = 0

    print("Processing parks...")
    print()

    for park_slug in parks:
        m, c = process_park(park_slug)
        total_modified += m
        total_correct += c
        if m or c:
            print(f"  {park_slug}: {m} modified, {c} already correct")

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Files modified      : {total_modified}")
    print(f"  Files already correct: {total_correct}")
    print(f"  Total pages processed: {total_modified + total_correct}")

    spot_check()

    return 0


if __name__ == "__main__":
    sys.exit(main())
