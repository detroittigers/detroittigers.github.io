# Crowd Calendar Redesign — Design Spec

**Date:** 2026-04-11
**Status:** Approved via brainstorm session

## Goal

Redesign the per-park crowd calendar pages across all 14 parks to improve scannability, add year-over-year context, fix the color palette, add authority messaging, redesign the day-detail drawer, and retire the old Universal Orlando crowd calendar page.

## Scope

### In scope
1. Calendar cell redesign (number-hero layout)
2. New color palette (more saturated, wider hue spread)
3. New label system (Dead/Light/Moderate/Busy/Packed)
4. YoY delta badges from `lastYearLevel` field (desktop only)
5. Weather visibility fix (bump opacity/size)
6. Legend split into 5 tiers
7. Drawer redesign (hero band, info grid, authority strip, CTA)
8. Authority block replacing "how crowd levels are calculated"
9. SEO redirect for old `/universal-orlando/crowd-calendar/` page
10. Mobile breakpoints (YoY and weather hidden, cells simplified)

### Out of scope
- Crowd arc / hourly data (no hourly data in pipeline yet)
- Week-level summary (future iteration)
- Colorblind mode toggle (arrows provide adequate fallback)

## Design Decisions

### Cell Layout (Option B — Number Hero)
- Day number: top-left, 12px, 0.5 opacity
- Crowd level number: centered, 30px, bold 900, white
- Label: below number, 10px uppercase (Dead/Light/Moderate/Busy/Packed)
- Event badge: dark pill, 7px uppercase, below label
- Weather: bottom-right absolute, 11px, 0.58 opacity, past dates only
- YoY badge: top-right absolute, 9px pill, green ↓ or red ↑, desktop only. Hidden when delta is 0.
- Background: full-cell hsl color from new palette

### Color Palette (new)
| Level | HSL | Label |
|-------|-----|-------|
| 1 | hsl(132, 72%, 27%) | Dead |
| 2 | hsl(118, 72%, 25%) | Dead |
| 3 | hsl(100, 68%, 25%) | Light |
| 4 | hsl(82, 68%, 26%) | Light |
| 5 | hsl(63, 70%, 27%) | Moderate |
| 6 | hsl(44, 72%, 28%) | Moderate |
| 7 | hsl(26, 72%, 28%) | Busy |
| 8 | hsl(13, 72%, 27%) | Busy |
| 9 | hsl(4, 74%, 26%) | Packed |
| 10 | hsl(0, 78%, 22%) | Packed |

### Label System
Old: Ghost Town / Very Low / Low / Below Average / Average / Above Average / Busy / Very Busy / Packed / Extreme
New: Dead (1-2) / Light (3-4) / Moderate (5-6) / Busy (7-8) / Packed (9-10)

The `crowdLabel` field in actuals.json keeps the old labels. The JS maps them to the new display labels client-side.

### YoY Delta Badge
- Source: `lastYearLevel` field in actuals.json
- Delta = `crowdLevel - lastYearLevel`
- Show only when delta != 0 and `lastYearLevel` exists
- Green `↓N` badge when delta < 0 (quieter than last year, good for visitors)
- Red `↑N` badge when delta > 0 (busier than last year)
- Desktop only — hidden via `display: none` at 768px breakpoint
- Shown in drawer hero band for mobile users

### Legend
5 entries: Dead (1-2), Light (3-4), Moderate (5-6), Busy (7-8), Packed (9-10)

### Drawer
Sections top to bottom:
1. **Hero band** — colored by crowd level, shows: park+date, big number, /10, label, confidence range pill ("We're calling 4-6 for this day"), YoY drawer pill ("↓1 vs last year")
2. **Info grid** — Hours card, Weather card, Event card (full-width, accent-colored). Order: Hours → Weather → Event.
3. **Authority strip** — shield icon + "We've tested this: 82% of our predictions land within 2 crowd levels of reality. Tested on Islands of Adventure, all 365 days of 2025."
4. **CTA section** — crowd-level-specific copy, "Get free drop alerts" button, "View ride-by-ride breakdown →" secondary link

CTA copy varies by level:
- 1-4: "Level N is a great pick. Drop alerts help you nail the ride order."
- 5-6: "Level N is workable if you time it right. Drop alerts tell you the moment a line dips. That's when you go."
- 7-8: "Level N means long lines all day. Drop alerts catch the dips everyone else misses. That's your window."
- 9-10: "Level N is a tough day. Drop alerts are the difference between 3 rides and 8."

### Authority Block
Replaces the "How crowd levels are calculated" section. Contains:
- Header: "We actually test this. Here's what we found."
- Stats row: 82% within 2 levels, 59% within 1 level (vs 45%), 10k+ park-days
- Bar chart: Ride Ready 59% vs Leading alternative 45%
- Footnote: methodology explanation
- 4 differentiator cards: event-aware, daily updates, closed-day detection, YoY adjustment

### UO Redirect
Replace `/universal-orlando/crowd-calendar/index.html` with an HTML meta-refresh redirect to `/parks/universal-orlando/crowd-calendar/`. Include canonical tag and JS fallback for SEO preservation.

## Files Affected

All 15 calendar pages share the same template (1706 lines, only park-specific strings differ):
- `parks/epic-universe/crowd-calendar/index.html`
- `parks/islands-of-adventure/crowd-calendar/index.html`
- `parks/universal-studios-florida/crowd-calendar/index.html`
- `parks/cedar-point/crowd-calendar/index.html`
- `parks/kings-island/crowd-calendar/index.html`
- `parks/canadas-wonderland/crowd-calendar/index.html`
- `parks/seaworld-orlando/crowd-calendar/index.html`
- `parks/busch-gardens-tampa/crowd-calendar/index.html`
- `parks/busch-gardens-williamsburg/crowd-calendar/index.html`
- `parks/carowinds/crowd-calendar/index.html`
- `parks/kings-dominion/crowd-calendar/index.html`
- `parks/six-flags-great-adventure/crowd-calendar/index.html`
- `parks/six-flags-great-america/crowd-calendar/index.html`
- `parks/six-flags-over-georgia/crowd-calendar/index.html`
- `parks/universal-orlando/crowd-calendar/index.html` (already exists, unrelated to the old UO page)

Plus the redirect page:
- `universal-orlando/crowd-calendar/index.html` (old page → redirect)

## Mockup Reference

Final approved mockup: `.superpowers/brainstorm/18553-1775956550/content/final-v4.html`
