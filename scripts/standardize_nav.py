#!/usr/bin/env python3
"""Standardize top nav across the Ride Ready site.

Strategy: find the first <nav>...</nav> or <header class="header">...</header>
inside <body> before <main>/content, replace with canonical nav markup.
If no nav/header exists, insert the canonical nav right after <body> or the
outermost top-level <div class="container"> opening.

Skips methodology (per user) and per-date crowd calendar pages (intentional
minimal nav).
"""

import re
import sys
from pathlib import Path

ROOT = Path("/Users/kevinschneider/Code/detroittigers.github.io")

# Canonical nav — self-contained with an inner max-width wrapper so it
# renders consistently whether placed as a direct body child or inside an
# existing container.
CANONICAL = """<nav class="site-nav no-print" style="padding: 14px 20px; border-bottom: 1px solid #1a1a1a; background: #000;">
  <style>@media print { .site-nav { display: none !important; } }</style>
  <div style="display: flex; justify-content: space-between; align-items: center; max-width: 1100px; margin: 0 auto; gap: 16px;">
    <a href="/" style="display: flex; align-items: center; gap: 10px; text-decoration: none;">
      <img alt="Ride Ready" src="/images/logo.png" style="height: 32px; width: auto;" />
      <span style="color: white; font-weight: 700; font-size: 1.1rem; letter-spacing: -0.5px;">Ride Ready</span>
    </a>
    <div style="display: flex; gap: 18px; align-items: center; flex-wrap: wrap;">
      <a href="/parks/" style="color: white; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Parks</a>
      <a href="/crowds/" style="color: white; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Crowds</a>
      <a href="/compare/official-apps/" style="color: #ccc; text-decoration: none; font-size: 0.95rem; font-weight: 500;">Why Us?</a>
      <a href="https://apps.apple.com/us/app/ride-ready/id6748330847?ct=__CT__" data-ref="__REF__" style="background: rgba(255,255,255,0.1); color: white; padding: 8px 16px; border-radius: 99px; text-decoration: none; font-weight: 600; font-size: 0.9rem; border: 1px solid rgba(255,255,255,0.2); white-space: nowrap;">Download Free</a>
    </div>
  </div>
</nav>"""


def ref_for(path: Path) -> str:
    """Derive a data-ref slug from the file path."""
    rel = path.relative_to(ROOT).as_posix()
    rel = rel.removesuffix("/index.html").removesuffix(".html")
    if rel in ("", "index"):
        return "home-nav"
    slug = rel.replace("/", "-")
    # keep short-ish
    return f"{slug}-nav"


def canonical_for(path: Path) -> str:
    ref = ref_for(path)
    ct = f"smartbanner-{ref}".replace("-nav", "")
    return CANONICAL.replace("__REF__", ref).replace("__CT__", ct)


# Skip list
def should_skip(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith((".worktrees/", "node_modules/", ".git/",
                       ".superpowers/")):
        return True
    if rel.startswith("methodology/"):
        return True
    # per-date crowd calendar pages
    if re.match(r"parks/[^/]+/crowd-calendar/\d{4}-\d{2}-\d{2}/", rel):
        return True
    for prefix in ("tmp/", "scripts/", "reviews/", "plans/", "reports/",
                   "docs/", "app/", "waitlist/", "privacy/", "terms/",
                   "go/"):
        if rel.startswith(prefix):
            return True
    if rel in ("privacy.html", "terms.html", "404.html"):
        return True
    return False


# Regex: find first top-level <nav>...</nav> in the document. Because of
# nested navs (breadcrumbs), we only want the FIRST one that appears near
# <body> start. We'll scan from <body> and grab the first <nav ...> ... </nav>
# OR <header class="header"> ... </header>.

NAV_RE = re.compile(r"<nav\b[^>]*>.*?</nav>", re.DOTALL | re.IGNORECASE)
HEADER_HERO_RE = re.compile(r'<header\s+class="header"[^>]*>.*?</header>',
                            re.DOTALL | re.IGNORECASE)
BODY_RE = re.compile(r"<body[^>]*>", re.IGNORECASE)
CONTAINER_OPEN_RE = re.compile(r'<div\s+class="container"[^>]*>', re.IGNORECASE)


SITE_NAV_SIGNALS = ('href="/parks/"', "images/logo.png", '"nav-cta"',
                    "Download Free</a>", '"site-nav"')


def process(path: Path) -> str:
    html = path.read_text()
    body_m = BODY_RE.search(html)
    if not body_m:
        return "no-body"
    body_end = body_m.end()

    new_nav = canonical_for(path)

    # Look for existing site nav in first 8000 chars of body. Any <nav>
    # containing site-nav signals is treated as the one to replace. This
    # handles navs nested inside arbitrary wrappers (sticky-footer, container).
    search_window = html[body_end:body_end + 8000]
    for m in re.finditer(r"<nav\b[^>]*>.*?</nav>", search_window,
                         re.DOTALL | re.IGNORECASE):
        block = m.group()
        if any(sig in block for sig in SITE_NAV_SIGNALS):
            abs_start = body_end + m.start()
            abs_end = body_end + m.end()
            new_html = html[:abs_start] + new_nav + html[abs_end:]
            if new_html != html:
                path.write_text(new_html)
            return "replaced-nav"

    # No existing site nav — insert at anchor (after <div class="container">
    # if it opens near top of body, else right after <body>).
    anchor_window = html[body_end:body_end + 500]
    container_m = CONTAINER_OPEN_RE.search(anchor_window)
    if container_m and container_m.start() < 300:
        anchor = body_end + container_m.end()
    else:
        anchor = body_end
    new_html = html[:anchor] + "\n    " + new_nav + "\n" + html[anchor:]
    if new_html != html:
        path.write_text(new_html)
    return "inserted"


def main():
    dry_run = "--dry" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = []
    if only:
        files = [ROOT / p for p in only]
    else:
        files = [p for p in ROOT.rglob("*.html") if not should_skip(p)]

    counts = {}
    for f in files:
        if should_skip(f):
            continue
        try:
            if dry_run:
                html = f.read_text()
                body_m = BODY_RE.search(html)
                if not body_m:
                    action = "no-body"
                else:
                    body_end = body_m.end()
                    sw = html[body_end:body_end + 8000]
                    found = False
                    for m in re.finditer(r"<nav\b[^>]*>.*?</nav>", sw,
                                         re.DOTALL | re.IGNORECASE):
                        if any(sig in m.group() for sig in SITE_NAV_SIGNALS):
                            found = True
                            break
                    action = "would-replace-nav" if found else "would-insert"
            else:
                action = process(f)
        except Exception as e:
            action = f"error: {e}"
        counts[action] = counts.get(action, 0) + 1
        print(f"{action:30s} {f.relative_to(ROOT)}")
    print("---")
    for k, v in sorted(counts.items()):
        print(f"{v:4d}  {k}")


if __name__ == "__main__":
    main()
