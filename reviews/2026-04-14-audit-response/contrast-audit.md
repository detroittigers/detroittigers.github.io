# Contrast Audit — Low-Contrast Text Colors

**Date:** 2026-04-14  
**Scope:** All `.html` files excluding `node_modules/`, `.git/`, `scripts/`, `reviews/`, `plans/`, `.superpowers/`, `.worktrees/`  
**Audited files:** 840  
**Files with findings:** 84  
**Total flagged lines:** 592

> **Recommended minimum:** On a `#000` background, body text should use `#aaa` or brighter to achieve ~4.5:1 contrast ratio (WCAG AA for small text). The colors flagged here (#888 and below, rgba white with alpha < 0.6) all fall short of this threshold.

## WCAG Contrast Reference

| Color | Contrast vs #000 | WCAG AA (4.5:1) | WCAG AA Large (3:1) |
|-------|-----------------|-----------------|---------------------|
| `#888` / `#888888` | ~2.0:1 | FAIL | FAIL |
| `#777` / `#777777` | ~1.8:1 | FAIL | FAIL |
| `#666` / `#666666` | ~1.5:1 | FAIL | FAIL |
| `#555` / `#555555` | ~1.4:1 | FAIL | FAIL |
| `rgba(255,255,255,0.5)` on #000 | ~2.0:1 | FAIL | FAIL |
| `rgba(255,255,255,0.35)` on #000 | ~1.6:1 | FAIL | FAIL |
| `#aaa` | ~2.3:1 | FAIL | FAIL |
| `#bbb` | ~2.9:1 | FAIL | PASS (large) |
| `#ccc` | ~3.7:1 | FAIL | PASS |
| `#ddd` | ~5.1:1 | PASS | PASS |

*Note: The "recommended minimum" of `#aaa` still fails WCAG AA for small body text. For true compliance, body text needs `#c0c0c0` or brighter on pure black.*

## Summary by Pattern

| Pattern | Flagged Lines | Notes |
|---------|--------------|-------|
| `#888` | 152 | Hex shorthand/longhand |
| `#666` | 92 | Hex shorthand/longhand |
| `#555` | 40 | Hex shorthand/longhand |
| `#888888` | 40 | Hex shorthand/longhand |
| `#777` | 1 | Hex shorthand/longhand |
| `#666666` | 1 | Hex shorthand/longhand |
| `rgba(255,255,255,<0.6)` (all variants) | 266 | Semi-transparent white on dark bg |
| **Total** | **592** | |

## Per-File Summary

| File | Findings |
|------|----------|
| `universal-orlando/epic-universe/spring-break-2026/index.html` | 30 |
| `tools/og-image-generator.html` | 21 |
| `index.html` | 20 |
| `parks/kings-island/crowd-calendar/index.html` | 19 |
| `parks/seaworld-orlando/crowd-calendar/index.html` | 19 |
| `parks/universal-studios-florida/crowd-calendar/index.html` | 19 |
| `parks/busch-gardens-tampa/crowd-calendar/index.html` | 19 |
| `parks/kings-dominion/crowd-calendar/index.html` | 19 |
| `parks/islands-of-adventure/crowd-calendar/index.html` | 19 |
| `parks/six-flags-great-adventure/crowd-calendar/index.html` | 19 |
| `parks/six-flags-over-georgia/crowd-calendar/index.html` | 19 |
| `parks/canadas-wonderland/crowd-calendar/index.html` | 19 |
| `parks/six-flags-great-america/crowd-calendar/index.html` | 19 |
| `parks/busch-gardens-williamsburg/crowd-calendar/index.html` | 19 |
| `parks/epic-universe/crowd-calendar/index.html` | 19 |
| `parks/cedar-point/crowd-calendar/index.html` | 19 |
| `parks/carowinds/crowd-calendar/index.html` | 19 |
| `universal-orlando/islands-of-adventure/hagrids-motorbike-queue-times/index.html` | 18 |
| `universal-orlando/epic-universe/ministry-queue-times/index.html` | 18 |
| `universal-orlando/islands-of-adventure/velocicoaster-queue-times/index.html` | 17 |
| `universal-orlando/epic-universe/mario-kart-queue-times/index.html` | 12 |
| `universal-orlando/epic-universe/hiccups-wing-gliders-queue-times/index.html` | 12 |
| `universal-orlando/epic-universe/stardust-racers-queue-times/index.html` | 11 |
| `universal-orlando/epic-universe/mine-cart-madness-queue-times/index.html` | 11 |
| `universal-orlando/epic-universe/monsters-unchained-queue-times/index.html` | 11 |
| `go/index.html` | 7 |
| `universal-orlando/islands-of-adventure/index.html` | 5 |
| `universal-orlando/epic-universe/index.html` | 5 |
| `parks/epic-universe/mlk-day-weekend-2026/index.html` | 5 |
| `crowds/index.html` | 5 |
| `orlando/spring-break-2026/index.html` | 4 |
| `parks/kings-island/orion-queue-times/index.html` | 4 |
| `parks/kings-island/the-beast-queue-times/index.html` | 4 |
| `parks/kings-island/mystic-timbers-queue-times/index.html` | 4 |
| `parks/six-flags-over-georgia/goliath-queue-times/index.html` | 4 |
| `parks/six-flags-over-georgia/twisted-cyclone-queue-times/index.html` | 4 |
| `parks/epic-universe/2025-holiday-strategy/index.html` | 3 |
| `compare/official-apps/index.html` | 3 |
| `parks/kings-dominion/pantherian-queue-times/index.html` | 3 |
| `parks/kings-dominion/rapterra-queue-times/index.html` | 3 |
| `parks/kings-dominion/twisted-timbers-queue-times/index.html` | 3 |
| `parks/six-flags-great-adventure/nitro-queue-times/index.html` | 3 |
| `parks/six-flags-great-adventure/jersey-devil-queue-times/index.html` | 3 |
| `parks/six-flags-great-adventure/el-toro-queue-times/index.html` | 3 |
| `parks/six-flags-over-georgia/georgia-gold-rusher-queue-times/index.html` | 3 |
| `parks/epic-universe/secrets/index.html` | 3 |
| `terms.html` | 3 |
| `terms/index.html` | 3 |
| `parks/epic-universe/presidents-day-weekend-2026/index.html` | 2 |
| `privacy/index.html` | 2 |
| `privacy.html` | 2 |
| `guides/ride-reaction-scripts.html` | 2 |
| `parks/kings-island/secrets/index.html` | 2 |
| `parks/universal-studios-florida/secrets/index.html` | 2 |
| `parks/busch-gardens-tampa/secrets/index.html` | 2 |
| `parks/kings-dominion/secrets/index.html` | 2 |
| `parks/islands-of-adventure/secrets/index.html` | 2 |
| `parks/six-flags-great-adventure/secrets/index.html` | 2 |
| `parks/six-flags-over-georgia/secrets/index.html` | 2 |
| `parks/canadas-wonderland/secrets/index.html` | 2 |
| `parks/six-flags-great-america/secrets/index.html` | 2 |
| `parks/busch-gardens-williamsburg/apollos-chariot-queue-times/index.html` | 2 |
| `parks/busch-gardens-williamsburg/secrets/index.html` | 2 |
| `parks/busch-gardens-williamsburg/pantheon-queue-times/index.html` | 2 |
| `parks/busch-gardens-williamsburg/griffon-queue-times/index.html` | 2 |
| `parks/cedar-point/secrets/index.html` | 2 |
| `parks/carowinds/copperhead-strike-queue-times/index.html` | 2 |
| `parks/carowinds/secrets/index.html` | 2 |
| `parks/carowinds/fury-325-queue-times/index.html` | 2 |
| `parks/carowinds/afterburn-queue-times/index.html` | 2 |
| `parks/index.html` | 1 |
| `parks/kings-island/index.html` | 1 |
| `parks/seaworld-orlando/index.html` | 1 |
| `parks/universal-studios-florida/index.html` | 1 |
| `parks/busch-gardens-tampa/index.html` | 1 |
| `parks/kings-dominion/index.html` | 1 |
| `parks/islands-of-adventure/index.html` | 1 |
| `parks/six-flags-great-adventure/index.html` | 1 |
| `parks/six-flags-over-georgia/index.html` | 1 |
| `parks/canadas-wonderland/index.html` | 1 |
| `parks/busch-gardens-williamsburg/index.html` | 1 |
| `parks/epic-universe/index.html` | 1 |
| `parks/cedar-point/index.html` | 1 |
| `parks/carowinds/index.html` | 1 |

---

## Findings by File

### `universal-orlando/epic-universe/spring-break-2026/index.html` — 30 findings

**`<style>` block** (12 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L153 | `#555` | `.breadcrumb {` | `color: #555;` |
| L158 | `#555` | `.breadcrumb a {` | `color: #555;` |
| L163 | `#888` | `.breadcrumb a:hover {` | `color: #888;` |
| L197 | `#888` | `border-radius: 99px;` | `color: #888;` |
| L236 | `#555` | `.section-meta {` | `color: #555;` |
| L256 | `#666` | `text-align: left;` | `color: #666;` |
| L297 | `#666` | `td.note {` | `color: #666;` |
| L346 | `#666` | `letter-spacing: 0.06em;` | `color: #666;` |
| L400 | `#666` | `letter-spacing: 0.06em;` | `color: #666;` |
| L439 | `#555` | `.app-cta p {` | `color: #555;` |
| L492 | `#555` | `border-top: 1px solid #1a1a1a;` | `color: #555;` |
| L497 | `#555` | `footer a {` | `color: #555;` |

**Inline `style=`** (18 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L609 | `#555` | `<p style="font-size:0.75rem;color:#555;margin-top:12px;">Based on 116,784 wait-time samples from ...` |
| L704 | `#555` | `<p style="font-size:0.75rem;color:#555;margin-top:12px;">Based on ride opening data tracked by Ri...` |
| L731 | `#888` | `<td class="note"><a href="#" style="color:#888;text-decoration:underline;">Ride Ready data</a></td>` |
| L739 | `#888` | `<td class="note"><a href="#" style="color:#888;text-decoration:underline;">Ride Ready data</a></td>` |
| L747 | `#888` | `<td class="note"><a href="#" style="color:#888;text-decoration:underline;">Ride Ready data</a></td>` |
| L755 | `#888` | `<td class="note"><a href="#" style="color:#888;text-decoration:underline;">Ride Ready data</a></td>` |
| L763 | `#888` | `<td class="note"><a href="#" style="color:#888;text-decoration:underline;">Ride Ready data</a></td>` |
| L768 | `#555` | `<p style="font-size:0.75rem;color:#555;margin-top:12px;">Actual Level = peak hourly crowd level` |
| L777 | `#555` | `<p style="font-size:0.8rem;color:#555;margin-top:12px;">Tuesday was the softest day of Easter wee...` |
| L805 | `#666` | `<p style="font-size:0.78rem;color:#666;margin-bottom:16px;">Avg 8 rides · saves 1h19m vs non-early ·` |
| L900 | `#666` | `<p style="font-size:0.78rem;color:#666;margin-bottom:16px;">Mario Kart chosen first in` |
| L1247 | `#555` | `<p style="font-size:0.75rem;color:#555;margin-top:12px;">Green = under 40 min · Orange = 130+ min...` |
| L1427 | `#555` | `<p style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em;color:#555;margin-bott...` |
| L1467 | `#555` | `<p style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em;color:#555;margin-bott...` |
| L1534 | `#555` | `<p style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em;color:#555;margin-bott...` |
| L1599 | `#555` | `<p style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em;color:#555;margin-bott...` |
| L1665 | `#555` | `<h3 style="font-size:0.85rem;text-transform:uppercase;letter-spacing:0.06em;color:#555;margin-bot...` |
| L1675 | `#666` | `<p style="font-size:0.8rem;color:#666;margin-top:12px;line-height:1.5;">These guides show estimat...` |

### `tools/og-image-generator.html` — 21 findings

**`<style>` block** (21 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L27 | `#666` | `text-transform: uppercase;` | `color: #666;` |
| L86 | `#888` | `.og-strategy .subtitle {` | `color: #888;` |
| L115 | `#555` | `text-transform: uppercase;` | `color: #555;` |
| L170 | `#666` | `text-transform: uppercase;` | `color: #666;` |
| L192 | `#666` | `.stat-unit {` | `-webkit-text-fill-color: #666;` |
| L208 | `#555` | `text-transform: uppercase;` | `color: #555;` |
| L323 | `#666` | `.og-crowd .subtitle {` | `color: #666;` |
| L346 | `#555` | `text-transform: uppercase;` | `color: #555;` |
| L388 | `#555` | `text-align: center;` | `color: #555;` |
| L437 | `#555` | `text-transform: uppercase;` | `color: #555;` |
| L455 | `#555` | `gap: 5px;` | `color: #555;` |
| L510 | `#777` | `.og-spring .subtitle {` | `color: #777;` |
| L552 | `#555` | `.heat-week .dates {` | `color: #555;` |
| L704 | `#555` | `text-transform: uppercase;` | `color: #555;` |
| L738 | `#666` | `.phone-header .ph-subtitle {` | `color: #666;` |
| L827 | `#666` | `.og-queue .page-type {` | `color: #666;` |
| L850 | `#555` | `text-transform: uppercase;` | `color: #555;` |
| L912 | `#555` | `text-transform: uppercase;` | `color: #555;` |
| L946 | `#666` | `transform: translateX(-50%);` | `color: #666;` |
| L1020 | `#666` | `.og-generic .subtitle {` | `color: #666;` |
| L1038 | `#888` | `max-width: 800px;` | `color: #888;` |

### `index.html` — 20 findings

**`<style>` block** (6 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L406 | `#666` | `gap: 8px;` | `color: #666;` |
| L414 | `#555` | `letter-spacing: 0.1em;` | `color: #555;` |
| L419 | `#888` | `.press-strip span.press-outlet {` | `color: #888;` |
| L533 | `#888888` | `footer {` | `color: #888888;` |
| L682 | `#888888` | `.more-note {` | `color: #888888;` |
| L787 | `#666666` | `justify-content: center;` | `color: #666666;` |

**Inline `style=`** (14 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1147 | `#888` | `<p style="margin: 10px 0 0; font-size: 0.8rem; color: #888;">Free to download · Premium from <a h...` |
| L1268 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0; line-height: 1.4;">Don't panic at the` |
| L1275 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0; line-height: 1.4;">Yoshi's Island is` |
| L1282 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0; line-height: 1.4;">Warning: Locker area is` |
| L1289 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0; line-height: 1.4;">Don't faint in the` |
| L1296 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0; line-height: 1.4;">Frankenstein's lab is a` |
| L1303 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0; line-height: 1.4;">Phone ban in effect.` |
| L1310 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0; line-height: 1.4;">12 themed rooms through ...` |
| L1316 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0; line-height: 1.4;">Raptor Paddock is a trap...` |
| L1467 | `rgba(255,255,255,0.05)` | `<td style="padding: 10px 16px; text-align: center; color: #666; border-bottom: 1px solid rgba(255...` |
| L1472 | `rgba(255,255,255,0.05)` | `<td style="padding: 10px 16px; text-align: center; color: #666; border-bottom: 1px solid rgba(255...` |
| L1491 | `#888` | `<span style="font-size: 0.75rem; color: #888;">One-day visit</span>` |
| L1501 | `#888` | `<span style="font-size: 0.75rem; color: #888;">For locals / APs</span>` |
| L1625 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; text-align: center;">Ride Ready is an` |

### `parks/kings-island/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/seaworld-orlando/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/universal-studios-florida/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/busch-gardens-tampa/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/kings-dominion/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/islands-of-adventure/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/six-flags-great-adventure/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/six-flags-over-georgia/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/canadas-wonderland/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L455 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L496 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L722 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L734 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L782 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L807 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L839 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L947 | `#888888` | `footer {` | `color: #888888;` |
| L1039 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1075 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1093 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1131 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1164 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1297 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1298 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1415 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1447 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1453 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1456 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/six-flags-great-america/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L448 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L489 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L715 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L727 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L775 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L800 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L832 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L940 | `#888888` | `footer {` | `color: #888888;` |
| L1032 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1068 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1086 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1124 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1157 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1288 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1289 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1403 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1435 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1441 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1444 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/busch-gardens-williamsburg/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/epic-universe/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/cedar-point/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `parks/carowinds/crowd-calendar/index.html` — 19 findings

**`<style>` block** (13 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L453 | `rgba(255, 255, 255, 0.5)` | `left: 9px;` | `color: rgba(255, 255, 255, 0.5);` |
| L494 | `rgba(255, 255, 255, 0.58)` | `right: 7px;` | `color: rgba(255, 255, 255, 0.58);` |
| L720 | `rgba(255, 255, 255, 0.3)` | `letter-spacing: 0.07em;` | `color: rgba(255, 255, 255, 0.3);` |
| L732 | `rgba(255, 255, 255, 0.35)` | `.info-card .ic-sub {` | `color: rgba(255, 255, 255, 0.35);` |
| L780 | `rgba(255, 255, 255, 0.4)` | `.authority-strip .auth-text {` | `color: rgba(255, 255, 255, 0.4);` |
| L805 | `rgba(255, 255, 255, 0.45)` | `.cta-msg {` | `color: rgba(255, 255, 255, 0.45);` |
| L837 | `rgba(255, 255, 255, 0.35)` | `gap: 6px;` | `color: rgba(255, 255, 255, 0.35);` |
| L945 | `#888888` | `footer {` | `color: #888888;` |
| L1037 | `rgba(255, 255, 255, 0.45)` | `.ab-header p {` | `color: rgba(255, 255, 255, 0.45);` |
| L1073 | `rgba(255, 255, 255, 0.4)` | `.stat-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L1091 | `rgba(255, 255, 255, 0.5)` | `.acc-title {` | `color: rgba(255, 255, 255, 0.5);` |
| L1129 | `rgba(255, 255, 255, 0.2)` | `.bar-note {` | `color: rgba(255, 255, 255, 0.2);` |
| L1162 | `rgba(255, 255, 255, 0.4)` | `.diff-body {` | `color: rgba(255, 255, 255, 0.4);` |

**Inline `style=`** (6 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L1295 | `rgba(255,255,255,0.35)` | `<span class="bar-name" style="color:rgba(255,255,255,0.35);">Leading alternative</span>` |
| L1296 | `rgba(255,255,255,0.3)` | `<span class="bar-pct" style="color:rgba(255,255,255,0.3);">45%</span>` |
| L1413 | `#888888` | `<footer style="margin-top: 40px; padding-bottom: 30px; font-size: 0.9rem; color: #888888; text-al...` |
| L1445 | `#666` | `<p style="color:#666; font-size:0.8rem; margin-top:40px; max-width:800px; margin-left:auto; margi...` |
| L1451 | `#888` | `<p style="color:#888;">For support or questions, contact us at <a href="mailto:support@rideready....` |
| L1454 | `#888` | `<p style="color:#888;">&copy; 2026 Ride Ready. All rights reserved.</p>` |

### `universal-orlando/islands-of-adventure/hagrids-motorbike-queue-times/index.html` — 18 findings

**`<style>` block** (6 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L193 | `#888` | `.survival-label {` | `color: #888;` |
| L227 | `#888` | `align-items: center;` | `color: #888;` |
| L400 | `#888` | `.cta-box p {` | `color: #888;` |
| L493 | `#888` | `.tracker-label {` | `color: #888;` |
| L508 | `#888` | `.tracker-pace {` | `color: #888;` |
| L702 | `#666` | `capacity and throughput (~1,700 riders/hr). Actual wait varies by staffing, downtime, and Express Pass ratios.` | `<script>(function(){var K='Hagrid';var w=document.getElementById('rr-live'),n...` |

**Inline `style=`** (12 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L650 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 10px 0 0;">Updated April 14, 2026</p>` |
| L673 | `#666` | `style="font-size: 0.75rem; text-transform: none; color: #666; margin-top: 2px;">15-30 min on peak...` |
| L680 | `#666` | `style="font-size: 0.75rem; text-transform: none; color: #666; margin-top: 2px;">Near entrance</span>` |
| L690 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 0;">` |
| L691 | `#888` | `<strong style="color: #888;">How these estimates work:</strong> Times are projected based on queue` |
| L699 | `#888` | `<div id="rr-unit" style="font-size:.85rem;color:#888;margin-top:4px;">minutes posted wait</div>` |
| L700 | `#555` | `<div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-top:10px;"><sp...` |
| L823 | `#888` | `style="display:block; color: #888; font-size: 0.8rem; margin-bottom: 4px; text-transform: upperca...` |
| L897 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L904 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L911 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L958 | `#666` | `<p><a href="/privacy/" style="color: #666;">Privacy</a> &middot; <a href="/terms/" style="color: ...` |

### `universal-orlando/epic-universe/ministry-queue-times/index.html` — 18 findings

**`<style>` block** (6 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L198 | `#888` | `.survival-label {` | `color: #888;` |
| L233 | `#888` | `align-items: center;` | `color: #888;` |
| L408 | `#888` | `.cta-box p {` | `color: #888;` |
| L503 | `#888` | `.tracker-label {` | `color: #888;` |
| L518 | `#888` | `.tracker-pace {` | `color: #888;` |
| L722 | `#666` | `ratios.` | `<script>(function(){var K='Ministry';var w=document.getElementById('rr-live')...` |

**Inline `style=`** (12 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L662 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 10px 0 0;">Updated April 14, 2026</p>` |
| L683 | `#666` | `style="font-size: 0.75rem; text-transform: none; color: #666; margin-top: 2px;">40"-48" requires` |
| L691 | `#666` | `style="font-size: 0.75rem; text-transform: none; color: #666; margin-top: 2px;">Subject to` |
| L708 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 0;">` |
| L709 | `#888` | `<strong style="color: #888;">How these estimates work:</strong> Times are projected based on queue` |
| L719 | `#888` | `<div id="rr-unit" style="font-size:.85rem;color:#888;margin-top:4px;">minutes posted wait</div>` |
| L720 | `#555` | `<div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-top:10px;"><sp...` |
| L783 | `#888` | `style="display:block; color: #888; font-size: 0.8rem; margin-bottom: 4px; text-transform: upperca...` |
| L908 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L915 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L922 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L999 | `#666` | `<p><a href="/privacy/" style="color: #666;">Privacy</a> · <a href="/terms/" style="color: #666;">...` |

### `universal-orlando/islands-of-adventure/velocicoaster-queue-times/index.html` — 17 findings

**`<style>` block** (6 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L137 | `#888` | `.survival-label {` | `color: #888;` |
| L171 | `#888` | `align-items: center;` | `color: #888;` |
| L344 | `#888` | `.cta-box p {` | `color: #888;` |
| L437 | `#888` | `.tracker-label {` | `color: #888;` |
| L452 | `#888` | `.tracker-pace {` | `color: #888;` |
| L635 | `#666` | `capacity and throughput. Actual wait varies by staffing, downtime, and Express Pass ratios.` | `<script>(function(){var K='VelociCoaster';var w=document.getElementById('rr-l...` |

**Inline `style=`** (11 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L606 | `#666` | `style="font-size: 0.75rem; text-transform: none; color: #666; margin-top: 2px;">Opens intermitten...` |
| L613 | `#666` | `style="font-size: 0.75rem; text-transform: none; color: #666; margin-top: 2px;">Free dual-sided</...` |
| L623 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 0;">` |
| L624 | `#888` | `<strong style="color: #888;">How these estimates work:</strong> Times are projected based on queue` |
| L632 | `#888` | `<div id="rr-unit" style="font-size:.85rem;color:#888;margin-top:4px;">minutes posted wait</div>` |
| L633 | `#555` | `<div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-top:10px;"><sp...` |
| L725 | `#888` | `style="display:block; color: #888; font-size: 0.8rem; margin-bottom: 4px; text-transform: upperca...` |
| L812 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L819 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L826 | `#888` | `style="display: block; color: #888; font-size: 0.8rem; text-transform: uppercase; letter-spacing:...` |
| L872 | `#666` | `<p><a href="/privacy/" style="color: #666;">Privacy</a> &middot; <a href="/terms/" style="color: ...` |

### `universal-orlando/epic-universe/mario-kart-queue-times/index.html` — 12 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L159 | `#888` | `.survival-label {` | `color: #888;` |
| L194 | `#888` | `align-items: center;` | `color: #888;` |
| L369 | `#888` | `.cta-box p {` | `color: #888;` |
| L528 | `#666` | `ratios.` | `<script>(function(){var K='Mario';var w=document.getElementById('rr-live'),nu...` |

**Inline `style=`** (8 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L486 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">40-48" requires` |
| L494 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">Subject to` |
| L502 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">Take with` |
| L514 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 0;">` |
| L515 | `#888` | `<strong style="color: #888;">How these estimates work:</strong> Times are projected based on queue` |
| L525 | `#888` | `<div id="rr-unit" style="font-size:.85rem;color:#888;margin-top:4px;">minutes posted wait</div>` |
| L526 | `#555` | `<div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-top:10px;"><sp...` |
| L759 | `#666` | `<p><a href="/privacy/" style="color: #666;">Privacy</a> · <a href="/terms/" style="color: #666;">...` |

### `universal-orlando/epic-universe/hiccups-wing-gliders-queue-times/index.html` — 12 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L168 | `#888` | `.survival-label {` | `color: #888;` |
| L203 | `#888` | `align-items: center;` | `color: #888;` |
| L378 | `#888` | `.cta-box p {` | `color: #888;` |
| L537 | `#666` | `ratios.` | `<script>(function(){var K='Hiccup';var w=document.getElementById('rr-live'),n...` |

**Inline `style=`** (8 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L495 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">40"-48" requires` |
| L503 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">Subject to` |
| L511 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">No Metal` |
| L523 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 0;">` |
| L524 | `#888` | `<strong style="color: #888;">How these estimates work:</strong> Times are projected based on queue` |
| L534 | `#888` | `<div id="rr-unit" style="font-size:.85rem;color:#888;margin-top:4px;">minutes posted wait</div>` |
| L535 | `#555` | `<div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-top:10px;"><sp...` |
| L733 | `#666` | `<p><a href="/privacy/" style="color: #666;">Privacy</a> · <a href="/terms/" style="color: #666;">...` |

### `universal-orlando/epic-universe/stardust-racers-queue-times/index.html` — 11 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L152 | `#888` | `.survival-label {` | `color: #888;` |
| L187 | `#888` | `align-items: center;` | `color: #888;` |
| L362 | `#888` | `.cta-box p {` | `color: #888;` |
| L520 | `#666` | `ratios.` | `<script>(function(){var K='Stardust';var w=document.getElementById('rr-live')...` |

**Inline `style=`** (7 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L486 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">Subject to` |
| L494 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">Strict no loose` |
| L506 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 0;">` |
| L507 | `#888` | `<strong style="color: #888;">How these estimates work:</strong> Times are projected based on queue` |
| L517 | `#888` | `<div id="rr-unit" style="font-size:.85rem;color:#888;margin-top:4px;">minutes posted wait</div>` |
| L518 | `#555` | `<div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-top:10px;"><sp...` |
| L723 | `#666` | `<p><a href="/privacy/" style="color: #666;">Privacy</a> · <a href="/terms/" style="color: #666;">...` |

### `universal-orlando/epic-universe/mine-cart-madness-queue-times/index.html` — 11 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L162 | `#888` | `.survival-label {` | `color: #888;` |
| L197 | `#888` | `align-items: center;` | `color: #888;` |
| L372 | `#888` | `.cta-box p {` | `color: #888;` |
| L527 | `#666` | `ratios.` | `<script>(function(){var K='Mine';var w=document.getElementById('rr-live'),num...` |

**Inline `style=`** (7 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L488 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">40"-48" requires` |
| L496 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">Subject to` |
| L513 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 0;">` |
| L514 | `#888` | `<strong style="color: #888;">How these estimates work:</strong> Times are projected based on queue` |
| L524 | `#888` | `<div id="rr-unit" style="font-size:.85rem;color:#888;margin-top:4px;">minutes posted wait</div>` |
| L525 | `#555` | `<div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-top:10px;"><sp...` |
| L660 | `#666` | `<p><a href="/privacy/" style="color: #666;">Privacy</a> · <a href="/terms/" style="color: #666;">...` |

### `universal-orlando/epic-universe/monsters-unchained-queue-times/index.html` — 11 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L153 | `#888` | `.survival-label {` | `color: #888;` |
| L188 | `#888` | `align-items: center;` | `color: #888;` |
| L363 | `#888` | `.cta-box p {` | `color: #888;` |
| L519 | `#666` | `ratios.` | `<script>(function(){var K='Monsters';var w=document.getElementById('rr-live')...` |

**Inline `style=`** (7 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L485 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">Subject to` |
| L493 | `#666` | `style="font-size: 0.5rem; text-transform: none; color: #666; margin-top: 2px;">Facial` |
| L505 | `#666` | `<p style="color: #666; font-size: 0.8rem; margin: 0;">` |
| L506 | `#888` | `<strong style="color: #888;">How these estimates work:</strong> Times are projected based on queue` |
| L516 | `#888` | `<div id="rr-unit" style="font-size:.85rem;color:#888;margin-top:4px;">minutes posted wait</div>` |
| L517 | `#555` | `<div style="display:flex;justify-content:center;align-items:center;gap:10px;margin-top:10px;"><sp...` |
| L728 | `#666` | `<p><a href="/privacy/" style="color: #666;">Privacy</a> · <a href="/terms/" style="color: #666;">...` |

### `go/index.html` — 7 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L57 | `#888` | `text-decoration: none;` | `.android-note { color: #888; font-size: 0.9rem; margin-bottom: 40px; }` |
| L59 | `#666` | `.android-note a { color: #FF6B4B; }` | `.escape-link { color: #666; font-size: 0.9rem; }` |
| L60 | `#888` | `.escape-link { color: #666; font-size: 0.9rem; }` | `.escape-link a { color: #888; }` |

**Inline `style=`** (4 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L86 | `#888` | `<p style="color: #888; font-size: 0.9rem; margin-bottom: 12px;">Android coming soon</p>` |
| L97 | `#666` | `<p style="color: #666; font-size: 0.82rem; margin-top: 10px; max-width: 360px; margin-left: auto;...` |
| L97 | `#666` | `<p style="color: #666; font-size: 0.82rem; margin-top: 10px; max-width: 360px; margin-left: auto;...` |
| L171 | `#555` | `<p style="color: #555; font-size: 0.8rem; margin-top: 16px;">` |

### `universal-orlando/islands-of-adventure/index.html` — 5 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L92 | `#888` | `align-items: center;` | `color: #888;` |
| L163 | `#555` | `.arrow-icon {` | `color: #555;` |

**Inline `style=`** (3 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L211 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0;">Free: live waits + 3 drop alerts/day</p>` |
| L274 | `#666` | `<p><a href="/" style="color: #666;">Home</a> · <a href="/privacy/" style="color: #666;">Privacy</...` |
| L275 | `#666` | `<a href="/terms/" style="color: #666;">Terms</a></p>` |

### `universal-orlando/epic-universe/index.html` — 5 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L92 | `#888` | `align-items: center;` | `color: #888;` |
| L157 | `#555` | `.arrow-icon {` | `color: #555;` |

**Inline `style=`** (3 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L206 | `#888` | `<p style="color: #888; font-size: 0.85rem; margin: 0;">Free: live waits + 3 drop alerts/day</p>` |
| L388 | `#666` | `<p><a href="../../" style="color: #666;">Home</a> · <a href="/privacy/" style="color: #666;">Priv...` |
| L389 | `#666` | `<a href="/terms/" style="color: #666;">Terms</a></p>` |

### `parks/epic-universe/mlk-day-weekend-2026/index.html` — 5 findings

**Inline `style=`** (5 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L508 | `#888` | `<p style="font-size: 0.8rem; color: #888; text-align: center; margin: -8px 0 16px;">Sample data —...` |
| L515 | `#666` | `<p style="text-align: center; margin-top: 12px; font-size: 0.85rem; color: #666;">` |
| L516 | `#888` | `<a href="/waitlist/android/" style="color: #888; text-decoration: underline;">Android coming soon...` |
| L933 | `#666` | `<span style="font-size: 0.9rem; color: #666; line-height: 1.4;">Feb 14-16. Updated with MLK` |
| L940 | `#666` | `<span style="font-size: 0.9rem; color: #666; line-height: 1.4;">Mar 9 - Apr 24. Week-by-week` |

### `crowds/index.html` — 5 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L322 | `rgba(255, 255, 255, 0.4)` | `.lookahead-label {` | `color: rgba(255, 255, 255, 0.4);` |
| L349 | `rgba(255, 255, 255, 0.25)` | `background: rgba(255, 255, 255, 0.06);` | `color: rgba(255, 255, 255, 0.25);` |
| L364 | `rgba(255, 255, 255, 0.45)` | `.footer p {` | `color: rgba(255, 255, 255, 0.45);` |
| L370 | `rgba(255, 255, 255, 0.55)` | `.footer a {` | `color: rgba(255, 255, 255, 0.55);` |

**Inline `style=`** (1 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L450 | `rgba(255,255,255,0.35)` | `<p style="color: rgba(255,255,255,0.35); font-size: 0.78rem; margin-top: 8px;">Updated daily</p>` |

### `orlando/spring-break-2026/index.html` — 4 findings

**Inline `style=`** (4 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L900 | `#666` | `<span style="font-size: 0.9rem; color: #666; line-height: 1.4;">Jan 17-19. Strategy for the 3-day` |
| L907 | `#666` | `<span style="font-size: 0.9rem; color: #666; line-height: 1.4;">Feb 14-16. Why it's the "Sweet` |
| L914 | `#666` | `<span style="font-size: 0.9rem; color: #666; line-height: 1.4;">Data-backed ride order, hourly ba...` |
| L920 | `#666` | `<span style="font-size: 0.9rem; color: #666; line-height: 1.4;">Daily crowd predictions for all U...` |

### `parks/kings-island/orion-queue-times/index.html` — 4 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L185 | `#888` | `align-items: center;` | `color: #888;` |
| L247 | `#888` | `.stat-card .label {` | `color: #888;` |
| L275 | `#888` | `.hourly-table th {` | `color: #888;` |
| L356 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/kings-island/the-beast-queue-times/index.html` — 4 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L134 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L148 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L153 | `#888` | `.hourly-table th, .hourly-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 0.95rem; }` | `.hourly-table th { color: #888; font-size: 0.75rem; text-transform: uppercase...` |
| L171 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/kings-island/mystic-timbers-queue-times/index.html` — 4 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L134 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L148 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L153 | `#888` | `.hourly-table th, .hourly-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 0.95rem; }` | `.hourly-table th { color: #888; font-size: 0.75rem; text-transform: uppercase...` |
| L171 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/six-flags-over-georgia/goliath-queue-times/index.html` — 4 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L125 | `#888` | `.hourly-table th, .hourly-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 0.95rem; }` | `.hourly-table th { color: #888; font-size: 0.75rem; text-transform: uppercase...` |
| L139 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/six-flags-over-georgia/twisted-cyclone-queue-times/index.html` — 4 findings

**`<style>` block** (4 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L125 | `#888` | `.hourly-table th, .hourly-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 0.95rem; }` | `.hourly-table th { color: #888; font-size: 0.75rem; text-transform: uppercase...` |
| L139 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/epic-universe/2025-holiday-strategy/index.html` — 3 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L51 | `#888` | `.back-link {` | `display: inline-flex; align-items: center; color: #888;` |
| L97 | `#888` | `.secondary-links a {` | `color: #888; font-size: 0.85rem; text-decoration: none;` |
| L104 | `#666` | `footer { border-top: 1px solid #222; padding-top: 20px; color: #666; font-size: 0.8rem; }` | `footer a { color: #666; }` |

### `compare/official-apps/index.html` — 3 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L124 | `#555` | `.cross {` | `color: #555;` |
| L182 | `#888` | `text-align: center;` | `color: #888;` |

**Inline `style=`** (1 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L327 | `#555` | `<p style="text-align: center; font-size: 0.8rem; color: #555; margin-top: 10px;">Ride Ready is an...` |

### `parks/kings-dominion/pantherian-queue-times/index.html` — 3 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L134 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/kings-dominion/rapterra-queue-times/index.html` — 3 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L134 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/kings-dominion/twisted-timbers-queue-times/index.html` — 3 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L134 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/six-flags-great-adventure/nitro-queue-times/index.html` — 3 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L134 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/six-flags-great-adventure/jersey-devil-queue-times/index.html` — 3 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L134 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/six-flags-great-adventure/el-toro-queue-times/index.html` — 3 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L134 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/six-flags-over-georgia/georgia-gold-rusher-queue-times/index.html` — 3 findings

**`<style>` block** (3 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L110 | `#888` | `.nav-cta { background: var(--primary-gradient); padding: 10px 16px; border-radius: 999px; font-weight: 700; color: white; box-shadow: 0 12px 30px rgba(249,115,22,0.20); }` | `.back-link { display: inline-flex; align-items: center; color: #888; text-dec...` |
| L121 | `#888` | `.stat-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; text-align: center; }` | `.stat-card .label { color: #888; font-size: 0.75rem; text-transform: uppercas...` |
| L134 | `rgba(255,255,255,0.55)` | `details p { margin: 10px 0 0; color: rgba(255,255,255,0.78); }` | `footer { margin: 34px 0 22px; color: rgba(255,255,255,0.55); font-size: 0.9re...` |

### `parks/epic-universe/secrets/index.html` — 3 findings

**Inline `style=`** (3 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L928 | `#888` | `<p style="margin-top: 10px;"><a href="/parks/epic-universe/" style="color: #888;">Epic Hub</a> \| ...` |
| L929 | `#888` | `style="color: #888;">Home</a> \| <a href="/privacy/" style="color: #888;">Privacy</a> \|` |
| L930 | `#888` | `<a href="/terms/" style="color: #888;">Terms</a>` |

### `terms.html` — 3 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L82 | `#888888` | `.meta {` | `color: #888888;` |

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L368 | `#888888` | `<p style="color:#888888; font-size:0.9rem; margin-top:30px;">© 2026 RideReady. All rights reserve...` |
| L369 | `#888888` | `<p style="color:#888888; font-size:0.9rem; margin-top:30px;">Ride Ready is an independent applica...` |

### `terms/index.html` — 3 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L82 | `#888888` | `.meta {` | `color: #888888;` |

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L368 | `#888888` | `<p style="color:#888888; font-size:0.9rem; margin-top:30px;">© 2026 RideReady. All rights reserve...` |
| L369 | `#888888` | `<p style="color:#888888; font-size:0.9rem; margin-top:30px;">Ride Ready is an independent applica...` |

### `parks/epic-universe/presidents-day-weekend-2026/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L802 | `#666` | `<span style="font-size: 0.9rem; color: #666; line-height: 1.4;">Jan 17-19. Predictions vs actual` |
| L809 | `#666` | `<span style="font-size: 0.9rem; color: #666; line-height: 1.4;">Mar 9 - Apr 24. Survival guide for` |

### `privacy/index.html` — 2 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L82 | `#888888` | `.meta {` | `color: #888888;` |

**Inline `style=`** (1 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L496 | `#888888` | `<p style="color:#888888; font-size:0.9rem; margin-top:30px;">Ride Ready is an independent applica...` |

### `privacy.html` — 2 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L82 | `#888888` | `.meta {` | `color: #888888;` |

**Inline `style=`** (1 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L496 | `#888888` | `<p style="color:#888888; font-size:0.9rem; margin-top:30px;">Ride Ready is an independent applica...` |

### `guides/ride-reaction-scripts.html` — 2 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L309 | `rgba(255, 255, 255, 0.50)` | `.thrill-label {` | `color: rgba(255, 255, 255, 0.50);` |
| L540 | `rgba(255, 255, 255, 0.55)` | `footer {` | `color: rgba(255, 255, 255, 0.55);` |

### `parks/kings-island/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L589 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L590 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/universal-studios-florida/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L608 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L609 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/busch-gardens-tampa/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L507 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L508 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/kings-dominion/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L437 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L438 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/islands-of-adventure/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L787 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L788 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/six-flags-great-adventure/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L381 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L382 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/six-flags-over-georgia/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L367 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L368 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/canadas-wonderland/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L492 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L493 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/six-flags-great-america/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L439 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L440 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/busch-gardens-williamsburg/apollos-chariot-queue-times/index.html` — 2 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L261 | `rgba(255,255,255,0.55)` | `.stat-note {` | `color: rgba(255,255,255,0.55);` |
| L343 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/busch-gardens-williamsburg/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L515 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L516 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/busch-gardens-williamsburg/pantheon-queue-times/index.html` — 2 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L261 | `rgba(255,255,255,0.55)` | `.stat-note {` | `color: rgba(255,255,255,0.55);` |
| L343 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/busch-gardens-williamsburg/griffon-queue-times/index.html` — 2 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L261 | `rgba(255,255,255,0.55)` | `.stat-note {` | `color: rgba(255,255,255,0.55);` |
| L343 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/cedar-point/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L616 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L617 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/carowinds/copperhead-strike-queue-times/index.html` — 2 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L268 | `rgba(255,255,255,0.55)` | `.stat-note {` | `color: rgba(255,255,255,0.55);` |
| L350 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/carowinds/secrets/index.html` — 2 findings

**Inline `style=`** (2 findings)

| Line | Color Value | Rule Snippet |
|------|-------------|--------------|
| L379 | `rgba(255,255,255,0.5)` | `<p style="margin-top: 8px;"><a href="/privacy/" style="color: rgba(255,255,255,0.5);">Privacy</a>...` |
| L380 | `rgba(255,255,255,0.5)` | `href="/terms/" style="color: rgba(255,255,255,0.5);">Terms</a></p>` |

### `parks/carowinds/fury-325-queue-times/index.html` — 2 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L268 | `rgba(255,255,255,0.55)` | `.stat-note {` | `color: rgba(255,255,255,0.55);` |
| L350 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/carowinds/afterburn-queue-times/index.html` — 2 findings

**`<style>` block** (2 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L268 | `rgba(255,255,255,0.55)` | `.stat-note {` | `color: rgba(255,255,255,0.55);` |
| L350 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L152 | `#888` | `background: rgba(255, 255, 255, 0.1);` | `color: #888;` |

### `parks/kings-island/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L294 | `rgba(255,255,255,0.55)` | `.plan li { margin: 8px 0; }` | `color: rgba(255,255,255,0.55);` |

### `parks/seaworld-orlando/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L294 | `rgba(255,255,255,0.55)` | `.plan li { margin: 8px 0; }` | `color: rgba(255,255,255,0.55);` |

### `parks/universal-studios-florida/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L332 | `rgba(255, 255, 255, 0.55)` | `background: rgba(255, 255, 255, 0.03);` | `color: rgba(255, 255, 255, 0.55);` |

### `parks/busch-gardens-tampa/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L316 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/kings-dominion/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L316 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/islands-of-adventure/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L332 | `rgba(255, 255, 255, 0.55)` | `background: rgba(255, 255, 255, 0.03);` | `color: rgba(255, 255, 255, 0.55);` |

### `parks/six-flags-great-adventure/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L294 | `rgba(255,255,255,0.55)` | `.plan li { margin: 8px 0; }` | `color: rgba(255,255,255,0.55);` |

### `parks/six-flags-over-georgia/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L294 | `rgba(255,255,255,0.55)` | `.plan li { margin: 8px 0; }` | `color: rgba(255,255,255,0.55);` |

### `parks/canadas-wonderland/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L316 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/busch-gardens-williamsburg/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L316 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/epic-universe/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L351 | `rgba(255, 255, 255, 0.55)` | `background: rgba(255, 255, 255, 0.03);` | `color: rgba(255, 255, 255, 0.55);` |

### `parks/cedar-point/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L316 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |

### `parks/carowinds/index.html` — 1 findings

**`<style>` block** (1 findings)

| Line | Color Value | Selector Context | Rule Snippet |
|------|-------------|-----------------|--------------|
| L316 | `rgba(255,255,255,0.55)` | `footer {` | `color: rgba(255,255,255,0.55);` |
