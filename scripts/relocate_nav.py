#!/usr/bin/env python3
"""Move the injected .site-nav block to be the first child of <body>,
outside any container wrapper. Also strengthen inline styles to resist
per-page `nav { ... }` CSS rules.
"""
import re
from pathlib import Path

ROOT = Path("/Users/kevinschneider/Code/detroittigers.github.io")

# Match the canonical nav we injected (begins with class="site-nav no-print")
SITE_NAV_RE = re.compile(
    r'\s*<nav class="site-nav no-print"[^>]*>.*?</nav>\s*',
    re.DOTALL,
)

BODY_RE = re.compile(r"<body[^>]*>", re.IGNORECASE)


def should_skip(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith((".worktrees/", "node_modules/", ".git/",
                       ".superpowers/")):
        return True
    return False


# Rewrite the nav markup with hardened inline styles.
NAV_STYLE_BLOCK = """<style>
    @media print { .site-nav { display: none !important; } }
    .site-nav-inner { display:flex; justify-content:space-between; align-items:center; max-width:1100px; margin:0 auto; gap:16px; }
    .site-nav-links { display:flex; gap:18px; align-items:center; flex-wrap:wrap; }
    .site-nav-brand { display:flex; align-items:center; gap:10px; text-decoration:none; }
    .site-nav-brand span { color:#fff; font-weight:700; font-size:1.1rem; letter-spacing:-0.5px; }
    .site-nav a.site-nav-link { color:#fff; text-decoration:none; font-size:0.95rem; font-weight:500; }
    .site-nav a.site-nav-secondary { color:#ccc; text-decoration:none; font-size:0.95rem; font-weight:500; }
    .site-nav-cta { background:rgba(255,255,255,0.1); color:#fff !important; padding:8px 16px; border-radius:99px; text-decoration:none; font-weight:600; font-size:0.9rem; border:1px solid rgba(255,255,255,0.2); white-space:nowrap; }
    @media (max-width: 680px) {
      .site-nav { padding:10px 14px !important; }
      .site-nav-inner { flex-direction:column; align-items:stretch; gap:10px; }
      .site-nav-links { width:100%; justify-content:flex-start; gap:14px; }
      .site-nav-cta { margin-left:auto; }
    }
    @media (max-width: 430px) {
      .site-nav-secondary { display:none; }
    }
  </style>"""


def canonical_for(ref: str, ct: str) -> str:
    return (
        '<nav class="site-nav no-print" style="display:block !important; '
        'padding:14px 20px !important; border-bottom:1px solid #1a1a1a !important; '
        'background:#000 !important; margin:0 !important; width:100% !important; '
        'box-sizing:border-box !important; position:relative; z-index:10;">\n'
        f'  {NAV_STYLE_BLOCK}\n'
        '  <div class="site-nav-inner">\n'
        '    <a class="site-nav-brand" href="/">\n'
        '      <img alt="Ride Ready" src="/images/logo.png" style="height:32px; width:auto;" />\n'
        '      <span>Ride Ready</span>\n'
        '    </a>\n'
        '    <div class="site-nav-links">\n'
        '      <a class="site-nav-link" href="/parks/">Parks</a>\n'
        '      <a class="site-nav-link" href="/crowds/">Crowds</a>\n'
        '      <a class="site-nav-secondary" href="/compare/official-apps/">Why Us?</a>\n'
        f'      <a class="site-nav-cta" href="https://apps.apple.com/us/app/ride-ready/id6748330847?ct={ct}" data-ref="{ref}">Download Free</a>\n'
        '    </div>\n'
        '  </div>\n'
        '</nav>'
    )


# Extract existing ref/ct from the current nav so we keep per-page tracking.
DATA_REF_RE = re.compile(r'data-ref="([^"]+)"')
CT_RE = re.compile(r'\?ct=([^"&]+)')


def main():
    updated = 0
    scanned = 0
    for p in sorted(ROOT.rglob("*.html")):
        if should_skip(p):
            continue
        scanned += 1
        try:
            html = p.read_text()
        except Exception:
            continue

        m = SITE_NAV_RE.search(html)
        if not m:
            continue

        # Pull ref/ct out of the existing nav
        ref_m = DATA_REF_RE.search(m.group())
        ct_m = CT_RE.search(m.group())
        ref = ref_m.group(1) if ref_m else "site-nav"
        ct = ct_m.group(1) if ct_m else "smartbanner-site-nav"

        # Remove the existing nav
        html_no_nav = html[:m.start()] + html[m.end():]

        # Re-insert right after <body>
        body_m = BODY_RE.search(html_no_nav)
        if not body_m:
            continue
        insert_at = body_m.end()
        new_nav = "\n" + canonical_for(ref, ct) + "\n"
        new_html = html_no_nav[:insert_at] + new_nav + html_no_nav[insert_at:]

        if new_html != html:
            p.write_text(new_html)
            updated += 1

    print(f"Scanned {scanned}, updated {updated}")


if __name__ == "__main__":
    main()
