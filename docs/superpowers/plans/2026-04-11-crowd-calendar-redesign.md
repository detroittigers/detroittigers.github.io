# Crowd Calendar Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the per-park crowd calendar cell layout, color palette, labels, drawer, and authority block across all 14 parks, add YoY delta badges, and redirect the old Universal Orlando calendar page.

**Architecture:** All 15 per-park calendar pages share the same 1706-line HTML template with only park-specific strings differing. We'll build and validate all changes on the Epic Universe page first, then propagate to the other 14 pages using a diff-and-apply script. The old `/universal-orlando/crowd-calendar/` page gets replaced with a meta-refresh redirect.

**Tech Stack:** Static HTML/CSS/JS (no build process), GitHub Pages deployment

**Spec:** `docs/superpowers/specs/2026-04-11-crowd-calendar-redesign.md`
**Mockup:** `.superpowers/brainstorm/18553-1775956550/content/final-v4.html`

---

### Task 1: Update Color Palette and Label System

**Files:**
- Modify: `parks/epic-universe/crowd-calendar/index.html`

This task changes the `levelToHsl()` function to use the new more-saturated palette, and adds a `getDisplayLabel()` function that maps old crowdLabel values to the new 5-tier system.

- [ ] **Step 1: Replace the `levelToHsl` function**

In `parks/epic-universe/crowd-calendar/index.html`, find the existing function (around line 1143):

```javascript
function levelToHsl(level) {
  const t = (level - 1) / 9;
  const hue = 120 * (1 - t);
  return `hsl(${hue.toFixed(0)}, 70%, 28%)`;
}
```

Replace with:

```javascript
function levelToHsl(level) {
  const palette = [
    'hsl(132,72%,27%)', // 1
    'hsl(118,72%,25%)', // 2
    'hsl(100,68%,25%)', // 3
    'hsl(82,68%,26%)',  // 4
    'hsl(63,70%,27%)',  // 5
    'hsl(44,72%,28%)',  // 6
    'hsl(26,72%,28%)',  // 7
    'hsl(13,72%,27%)',  // 8
    'hsl(4,74%,26%)',   // 9
    'hsl(0,78%,22%)',   // 10
  ];
  return palette[Math.min(Math.max(level, 1), 10) - 1];
}
```

- [ ] **Step 2: Replace the `getMobileLabel` function with `getDisplayLabel`**

Find `getMobileLabel` (around line 1149) and replace the entire function:

```javascript
function getDisplayLabel(level) {
  if (level <= 2) return 'Dead';
  if (level <= 4) return 'Light';
  if (level <= 6) return 'Moderate';
  if (level <= 8) return 'Busy';
  return 'Packed';
}
```

- [ ] **Step 3: Update all references from `getMobileLabel(record.crowdLabel)` to `getDisplayLabel(record.crowdLevel)`**

In `buildCell` (around line 1236), change:

```javascript
let miniHtml = `<div><strong>${getMobileLabel(record.crowdLabel)}</strong></div>`;
```

to:

```javascript
let miniHtml = `<div><strong>${getDisplayLabel(record.crowdLevel)}</strong></div>`;
```

In `buildBestDays` function, find any reference to `crowdLabel` used in display text and replace with `getDisplayLabel(record.crowdLevel)`.

In `openDrawer` (around line 1379), change the drawer subtitle:

```javascript
sub.textContent = `Crowd Level ${record.crowdLevel}/10 (${record.crowdLabel})`;
```

to:

```javascript
sub.textContent = `Crowd Level ${record.crowdLevel}/10 (${getDisplayLabel(record.crowdLevel)})`;
```

- [ ] **Step 4: Update the legend HTML**

Find the legend section (around line 932):

```html
<div class="legend" aria-label="Legend">
  <div class="chip"><span class="swatch" style="background: hsl(120, 70%, 30%)"></span><span>Low (1-3)</span></div>
  <div class="chip"><span class="swatch" style="background: hsl(70, 70%, 30%)"></span><span>Moderate (4-6)</span></div>
  <div class="chip"><span class="swatch" style="background: hsl(25, 70%, 32%)"></span><span>Busy (7-8)</span></div>
  <div class="chip"><span class="swatch" style="background: hsl(0, 70%, 32%)"></span><span>Very Busy (9-10)</span></div>
</div>
```

Replace with:

```html
<div class="legend" aria-label="Legend">
  <div class="chip"><span class="swatch" style="background: hsl(125, 72%, 26%)"></span><span>Dead (1-2)</span></div>
  <div class="chip"><span class="swatch" style="background: hsl(90, 68%, 25%)"></span><span>Light (3-4)</span></div>
  <div class="chip"><span class="swatch" style="background: hsl(55, 70%, 27%)"></span><span>Moderate (5-6)</span></div>
  <div class="chip"><span class="swatch" style="background: hsl(26, 72%, 28%)"></span><span>Busy (7-8)</span></div>
  <div class="chip"><span class="swatch" style="background: hsl(0, 78%, 22%)"></span><span>Packed (9-10)</span></div>
</div>
```

- [ ] **Step 5: Test in browser**

Open `parks/epic-universe/crowd-calendar/index.html` in a browser. Verify:
- Color gradient spans green through olive through orange through red with distinct steps
- Labels show Dead/Light/Moderate/Busy/Packed instead of old verbose labels
- Legend shows 5 tiers with correct colors

- [ ] **Step 6: Commit**

```bash
git add parks/epic-universe/crowd-calendar/index.html
git commit -m "feat: new color palette and 5-tier label system for crowd calendar"
```

---

### Task 2: Redesign Cell Layout (Number Hero)

**Files:**
- Modify: `parks/epic-universe/crowd-calendar/index.html` (CSS + JS)

This task replaces the current cell layout (day-num + corner badge + verbose label + park hours + weather) with the number-hero design (centered big number, small day number top-left, one-word label below, YoY badge top-right, weather bottom-right).

- [ ] **Step 1: Replace cell CSS**

Find and replace the following CSS blocks. Remove the old `.day-top`, `.day-num`, `.lvl`, `.mini`, `.wx`, `.wx .wx-temp`, `.event-tag` styles and replace with:

```css
.cell {
  min-height: 96px;
  border-right: 1px solid rgba(0,0,0,0.25);
  border-bottom: 1px solid rgba(0,0,0,0.25);
  padding: 8px 6px;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3px;
  transition: filter 0.12s;
}

.cell:hover { filter: brightness(1.12); }

.cell:nth-child(7n) { border-right: none; }

.cell.empty {
  background: rgba(255, 255, 255, 0.015);
  cursor: default;
}
.cell.empty:hover { filter: none; }

.day-num {
  position: absolute;
  top: 7px;
  left: 9px;
  font-size: 12px;
  font-weight: 800;
  color: rgba(255,255,255,0.5);
  line-height: 1;
}

.crowd-num {
  font-size: 30px;
  font-weight: 900;
  letter-spacing: -0.04em;
  line-height: 1;
  color: rgba(255,255,255,0.95);
  margin-top: 4px;
}

.crowd-label {
  font-size: 10px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: rgba(255,255,255,0.65);
}

.event-tag {
  display: inline-flex;
  align-items: center;
  background: rgba(0,0,0,0.35);
  border: 1px solid rgba(255,255,255,0.22);
  border-radius: 999px;
  font-size: 7px;
  font-weight: 800;
  padding: 2px 6px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(255,255,255,0.9);
  margin-top: 1px;
}

.wx {
  position: absolute;
  bottom: 5px;
  right: 7px;
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.58);
  line-height: 1;
  pointer-events: none;
}

.yoy {
  position: absolute;
  top: 6px;
  right: 7px;
  font-size: 9px;
  font-weight: 800;
  border-radius: 999px;
  padding: 2px 5px;
  line-height: 1;
  display: flex;
  align-items: center;
  gap: 1px;
}

.yoy-down {
  background: rgba(34,197,94,0.15);
  color: #4ade80;
  border: 1px solid rgba(34,197,94,0.3);
}

.yoy-up {
  background: rgba(239,68,68,0.12);
  color: #f87171;
  border: 1px solid rgba(239,68,68,0.25);
}
```

- [ ] **Step 2: Update the `is-today` styles**

Replace the old today styles with:

```css
.cell.is-today {
  box-shadow: inset 0 0 0 2px rgba(255,255,255,0.85);
  z-index: 1;
}
```

Remove the `.cell.is-today .day-num::before` rule (the "TODAY" prefix text).

- [ ] **Step 3: Update mobile breakpoints**

Replace the `@media (max-width: 768px)` and `@media (max-width: 480px)` blocks with:

```css
@media (max-width: 768px) {
  .cell { min-height: 75px; padding: 7px 4px; }
  .crowd-num { font-size: 24px; }
  .crowd-label { font-size: 8px; }
  .day-num { font-size: 11px; }
  .yoy { display: none; }
  .wx { display: none; }
  .event-tag { font-size: 6px; padding: 1px 4px; }
}

@media (max-width: 480px) {
  .cell { min-height: 65px; padding: 5px 3px; }
  .crowd-num { font-size: 22px; margin-top: 8px; }
  .day-num { font-size: 10px; top: 4px; left: 5px; }
  .crowd-label { font-size: 7px; letter-spacing: 0.04em; }
  .event-tag { font-size: 6px; }
  .dow div { font-size: 9px; padding: 8px 1px; }
}
```

- [ ] **Step 4: Rewrite the `buildCell` function**

Replace the entire `buildCell` function with:

```javascript
function buildCell(record) {
  const bg = levelToHsl(record.crowdLevel);
  const nowEt = new Date().toLocaleDateString('en-CA', { timeZone: 'America/New_York' });
  const isToday = record.date === nowEt;
  const past = isPastDate(record.date);
  const hasWeather = record.weatherEmoji || record.tempHigh != null;

  const cell = document.createElement("div");
  cell.className = "cell" + (isToday ? " is-today" : "");
  cell.style.background = bg;

  let clickable;
  if (past) {
    clickable = document.createElement("a");
    clickable.className = "day-btn has-detail";
    clickable.href = `/parks/${PARK_SLUG}/crowd-calendar/${record.date}/`;
    clickable.style.textDecoration = "none";
    clickable.style.color = "inherit";
    clickable.setAttribute("aria-label",
      `${record.date}, crowd level ${record.crowdLevel}/10 ${getDisplayLabel(record.crowdLevel)}. View full report.`);
    clickable.addEventListener("click", () => {
      if (typeof gtag === 'function') {
        gtag('event', 'crowd_calendar_open_report', {
          date: record.date, crowdLevel: record.crowdLevel, park: PARK_SLUG,
        });
      }
    });
  } else {
    clickable = document.createElement("button");
    clickable.className = "day-btn";
    clickable.type = "button";
    clickable.setAttribute("aria-label",
      `${record.date}, crowd level ${record.crowdLevel}/10 ${getDisplayLabel(record.crowdLevel)}. View details.`);
    clickable.addEventListener("click", () => openDrawer(record, clickable));
  }

  const day = parseInt(record.date.split('-')[2], 10);

  // Day number (top-left)
  const dayNum = document.createElement("div");
  dayNum.className = "day-num";
  dayNum.textContent = day;
  clickable.appendChild(dayNum);

  // YoY delta badge (top-right, desktop only)
  if (record.lastYearLevel != null) {
    const delta = record.crowdLevel - record.lastYearLevel;
    if (delta !== 0) {
      const yoy = document.createElement("div");
      yoy.className = "yoy " + (delta < 0 ? "yoy-down" : "yoy-up");
      yoy.textContent = (delta < 0 ? "↓" : "↑") + Math.abs(delta);
      clickable.appendChild(yoy);
    }
  }

  // Big crowd number (centered)
  const num = document.createElement("div");
  num.className = "crowd-num";
  num.textContent = record.crowdLevel;
  clickable.appendChild(num);

  // Label
  const lbl = document.createElement("div");
  lbl.className = "crowd-label";
  lbl.textContent = getDisplayLabel(record.crowdLevel);
  clickable.appendChild(lbl);

  // Event tag
  if (record.eventTag) {
    const evt = document.createElement("div");
    evt.className = "event-tag";
    evt.textContent = record.eventTag;
    clickable.appendChild(evt);
  }

  cell.appendChild(clickable);

  // Weather (past days only)
  if (past && hasWeather) {
    const wx = document.createElement("div");
    wx.className = "wx";
    let wxContent = "";
    if (record.tempHigh != null) {
      wxContent += record.tempHigh + "°";
    }
    if (record.weatherEmoji) {
      wxContent += record.weatherEmoji;
    }
    wx.textContent = "";
    wx.innerHTML = wxContent;
    cell.appendChild(wx);
  }

  return cell;
}
```

- [ ] **Step 5: Remove old unused CSS**

Delete these CSS classes that are no longer used: `.day-top`, `.lvl`, `.mini`, `.mini .muted`, `.wx .wx-temp`, `.price-row`, `.price-row span`. Also remove the old `.cell .has-detail::after` arrow indicator.

- [ ] **Step 6: Test in browser**

Open the page. Verify:
- Big centered numbers are visible and readable
- Day number is small in top-left
- Labels show one-word tier names
- Event tags appear as dark pills
- Weather shows bottom-right on past dates only at readable opacity
- YoY badges appear top-right in green/red (where data exists)
- Today has white border ring
- Hover brightens the cell
- Past dates link to per-date report pages
- Future dates open the drawer

- [ ] **Step 7: Test mobile**

Resize browser to 375px width. Verify:
- YoY badges are hidden
- Weather is hidden
- Cells are compact (65px min-height at 480px)
- Numbers are still readable at 22px

- [ ] **Step 8: Commit**

```bash
git add parks/epic-universe/crowd-calendar/index.html
git commit -m "feat: number-hero cell layout with YoY badges and improved weather"
```

---

### Task 3: Redesign the Drawer

**Files:**
- Modify: `parks/epic-universe/crowd-calendar/index.html` (CSS + JS)

- [ ] **Step 1: Add drawer CSS**

Replace the existing `.drawer`, `.drawer-inner`, `.drawer-head`, `.drawer-title`, `.close`, `.drawer-body`, `.metric` CSS with the new drawer styles. Add these styles:

```css
.drawer { position: fixed; inset: 0; z-index: 9999; background: rgba(0,0,0,0.85); display: none; align-items: flex-end; justify-content: center; padding: 16px; }
.drawer.open { display: flex; }
.drawer-inner { width: min(440px, 100%); background: #0d0d0d; border: 1px solid rgba(255,255,255,0.09); border-radius: 20px; overflow: hidden; box-shadow: 0 24px 60px rgba(0,0,0,0.7); max-height: 85vh; overflow-y: auto; }

.hero-band { position: relative; padding: 18px 20px 16px; overflow: hidden; }
.hero-band::before { content: ""; position: absolute; inset: 0; background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 55%); pointer-events: none; }
.hero-band .park-date { font-size: 11px; font-weight: 700; color: rgba(255,255,255,0.6); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }
.hero-band .level-row { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
.hero-band .big-level { font-size: 56px; font-weight: 900; letter-spacing: -0.05em; line-height: 1; }
.hero-band .denom { font-size: 22px; font-weight: 700; opacity: 0.5; }
.hero-band .level-label { font-size: 22px; font-weight: 800; opacity: 0.9; margin-left: 2px; }
.hero-band .pill-row { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }
.hero-band .conf-pill { display: inline-flex; align-items: center; gap: 5px; background: rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.15); border-radius: 999px; font-size: 11px; font-weight: 700; padding: 4px 10px; color: rgba(255,255,255,0.65); }
.hero-band .conf-pill .range { color: rgba(255,255,255,0.9); }
.hero-band .yoy-pill { display: inline-flex; align-items: center; gap: 5px; background: rgba(0,0,0,0.25); border-radius: 999px; font-size: 11px; font-weight: 700; padding: 4px 10px; }
.hero-band .yoy-pill.is-down { color: #4ade80; border: 1px solid rgba(34,197,94,0.3); }
.hero-band .yoy-pill.is-up { color: #f87171; border: 1px solid rgba(239,68,68,0.25); }

.drawer-close { position: absolute; top: 12px; right: 14px; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.15); border-radius: 999px; color: rgba(255,255,255,0.75); font-size: 12px; font-weight: 700; padding: 5px 11px; cursor: pointer; }

.drawer-info { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 14px 20px; border-bottom: 1px solid rgba(255,255,255,0.06); }
.info-card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.07); border-radius: 14px; padding: 11px 12px; }
.info-card .ic-label { font-size: 9px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.07em; color: rgba(255,255,255,0.3); margin-bottom: 5px; }
.info-card .ic-value { font-size: 16px; font-weight: 800; line-height: 1.2; }
.info-card .ic-sub { font-size: 11px; color: rgba(255,255,255,0.35); margin-top: 3px; }
.info-card.event-card { background: rgba(249,115,22,0.07); border-color: rgba(249,115,22,0.2); grid-column: span 2; display: flex; align-items: center; gap: 12px; }
.info-card.event-card .evt-icon { font-size: 26px; flex-shrink: 0; }
.info-card.event-card .ic-label { color: rgba(249,115,22,0.6); }
.info-card.event-card .ic-value { font-size: 14px; color: #F97316; }

.authority-strip { padding: 12px 20px; border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(255,255,255,0.01); display: flex; align-items: flex-start; gap: 10px; }
.authority-strip .a-text { font-size: 11px; color: rgba(255,255,255,0.4); line-height: 1.5; }
.authority-strip .a-text strong { color: rgba(255,255,255,0.7); }
.authority-strip .a-stat { display: inline-block; background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.25); border-radius: 4px; color: #4ade80; font-size: 10px; font-weight: 800; padding: 1px 5px; }

.drawer-cta { padding: 14px 20px 18px; }
.drawer-cta .cta-msg { font-size: 13px; color: rgba(255,255,255,0.45); line-height: 1.5; margin-bottom: 12px; }
.drawer-cta .cta-msg strong { color: rgba(255,255,255,0.85); }
.drawer-cta-btn { display: flex; align-items: center; justify-content: center; padding: 14px 20px; background: linear-gradient(45deg, #FF416C, #FF4B2B); border-radius: 14px; font-weight: 800; font-size: 15px; color: white; text-decoration: none; box-shadow: 0 8px 24px rgba(255,65,108,0.28); }
.drawer-view-link { display: flex; align-items: center; justify-content: center; margin-top: 10px; font-size: 12px; font-weight: 600; color: rgba(255,255,255,0.35); text-decoration: none; }

@media (max-width: 700px) {
  .drawer-info { grid-template-columns: 1fr; }
}
```

- [ ] **Step 2: Update drawer HTML structure**

Replace the `<div class="drawer" id="drawer">` block with:

```html
<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer-inner" role="dialog" aria-modal="true" aria-label="Day details">
    <div class="hero-band" id="drawerHero">
      <button class="drawer-close" id="drawerClose">✕</button>
      <div class="park-date" id="drawerParkDate"></div>
      <div class="level-row">
        <div class="big-level" id="drawerLevel"></div>
        <div class="denom">/10</div>
        <div class="level-label" id="drawerLabel"></div>
      </div>
      <div class="pill-row" id="drawerPills"></div>
    </div>
    <div class="drawer-info" id="drawerInfo"></div>
    <div class="authority-strip">
      <div style="font-size:16px;flex-shrink:0;margin-top:2px;">🛡️</div>
      <div class="a-text">We've tested this: <span class="a-stat">82%</span> of our predictions land within 2 crowd levels of reality. Tested on Islands of Adventure, all 365 days of 2025.</div>
    </div>
    <div class="drawer-cta" id="drawerCta"></div>
  </div>
</div>
```

- [ ] **Step 3: Rewrite the `openDrawer` function**

Replace the entire `openDrawer` function:

```javascript
function openDrawer(record, btn) {
  const drawer = document.getElementById("drawer");
  focusReturnTarget = btn;

  const dateObj = new Date(record.date + 'T12:00:00');
  const dateLabel = dateObj.toLocaleDateString('en-US', { weekday: 'short', month: 'long', day: 'numeric' });
  const displayLabel = getDisplayLabel(record.crowdLevel);

  // Hero band
  document.getElementById("drawerHero").style.background = levelToHsl(record.crowdLevel);
  document.getElementById("drawerParkDate").textContent = `${PARK_NAME} · ${dateLabel}`;
  document.getElementById("drawerLevel").textContent = record.crowdLevel;
  document.getElementById("drawerLabel").textContent = displayLabel;

  // Pills
  const pillRow = document.getElementById("drawerPills");
  pillRow.innerHTML = "";
  const confPill = document.createElement("div");
  confPill.className = "conf-pill";
  const lo = Math.max(1, record.crowdLevel - 1);
  const hi = Math.min(10, record.crowdLevel + 1);
  confPill.innerHTML = `We're calling <span class="range">${lo}–${hi}</span> for this day`;
  pillRow.appendChild(confPill);

  if (record.lastYearLevel != null) {
    const delta = record.crowdLevel - record.lastYearLevel;
    if (delta !== 0) {
      const yoyPill = document.createElement("div");
      yoyPill.className = "yoy-pill " + (delta < 0 ? "is-down" : "is-up");
      yoyPill.textContent = (delta < 0 ? "↓" : "↑") + Math.abs(delta) + " vs last year";
      pillRow.appendChild(yoyPill);
    }
  }

  // Info grid
  const info = document.getElementById("drawerInfo");
  info.innerHTML = "";

  // Park hours
  if (record.parkHours) {
    info.innerHTML += `<div class="info-card"><div class="ic-label">Park Hours</div><div class="ic-value">${record.parkHours}</div></div>`;
  }

  // Weather
  if (record.tempHigh != null || record.weatherEmoji) {
    const tempText = record.tempHigh != null ? `${record.weatherEmoji || ""} ${record.tempHigh}°F` : (record.weatherEmoji || "");
    const subParts = [];
    if (record.tempLow != null) subParts.push(`Low ${record.tempLow}°`);
    if (record.rainHours) subParts.push(`${record.rainHours}h rain`);
    else subParts.push("no rain");
    info.innerHTML += `<div class="info-card"><div class="ic-label">Weather</div><div class="ic-value">${tempText}</div><div class="ic-sub">${subParts.join(" · ")}</div></div>`;
  }

  // Event
  if (record.eventTag || record.eventName) {
    const eventEmojis = { HHN: "🎃", HAUNT: "🎃", FRIGHT: "🎃", WFST: "🎄", XMAS: "🎄", MARDI: "🎭", NYE: "🎆", JULY4TH: "🎆" };
    const emoji = eventEmojis[record.eventTag] || "🎪";
    info.innerHTML += `<div class="info-card event-card"><div class="evt-icon">${emoji}</div><div><div class="ic-label">Event</div><div class="ic-value">${record.eventName || record.eventTag}</div><div class="ic-sub">Adds to crowds</div></div></div>`;
  }

  // CTA
  const cta = document.getElementById("drawerCta");
  const lvl = record.crowdLevel;
  let ctaMsg;
  if (lvl <= 4) ctaMsg = `<strong>Level ${lvl} is a great pick.</strong> Drop alerts help you nail the ride order.`;
  else if (lvl <= 6) ctaMsg = `<strong>Level ${lvl} is workable if you time it right.</strong> Drop alerts tell you the moment a line dips. That's when you go.`;
  else if (lvl <= 8) ctaMsg = `<strong>Level ${lvl} means long lines all day.</strong> Drop alerts catch the dips everyone else misses. That's your window.`;
  else ctaMsg = `<strong>Level ${lvl} is a tough day.</strong> Drop alerts are the difference between 3 rides and 8.`;

  cta.innerHTML = `
    <div class="cta-msg">${ctaMsg}</div>
    <a class="drawer-cta-btn" href="https://apps.apple.com/us/app/ride-ready/id6748330847?ct=crowd-cal-${PARK_SLUG}-drawer" data-ref="crowd-cal-${PARK_SLUG}-drawer" target="_blank" rel="noopener noreferrer">Get free drop alerts</a>
    ${isPastDate(record.date) ? `<a class="drawer-view-link" href="/parks/${PARK_SLUG}/crowd-calendar/${record.date}/">View ride-by-ride breakdown →</a>` : ""}
  `;

  if (typeof gtag === 'function') {
    gtag('event', 'crowd_calendar_open_day', {
      date: record.date, crowdLevel: record.crowdLevel, park: PARK_NAME, parkSlug: PARK_SLUG
    });
  }

  drawer.classList.add("open");
  drawer.setAttribute("aria-hidden", "false");
  document.getElementById("drawerClose").focus();
}
```

- [ ] **Step 4: Test drawer**

Click a future date. Verify:
- Hero band is colored correctly
- Big number + label display
- Confidence pill shows range
- YoY pill shows if data exists
- Park hours, weather, event cards show
- Authority strip shows 82% stat with IOA callout
- CTA copy adjusts based on crowd level
- Close button works, escape key works, backdrop click works

- [ ] **Step 5: Commit**

```bash
git add parks/epic-universe/crowd-calendar/index.html
git commit -m "feat: redesigned drawer with hero band, authority strip, and level-specific CTA"
```

---

### Task 4: Add Authority Block

**Files:**
- Modify: `parks/epic-universe/crowd-calendar/index.html`

- [ ] **Step 1: Replace the "How crowd levels are calculated" section**

Find the `<section class="panel">` containing "How crowd levels are calculated" (around line 967). Replace the entire `<div class="card">` containing that content with the authority block HTML from the spec. Keep the CTA card next to it.

The authority block HTML is the full block from the final-v4 mockup: header ("We actually test this"), 3 stat blocks (82%, 59%, 10k+), bar chart, methodology note, and 4 differentiator cards.

- [ ] **Step 2: Add authority block CSS**

Add the authority block styles (`.authority-block`, `.ab-header`, `.stats-row`, `.stat-block`, `.accuracy-bar`, `.bar-track`, `.bar-fill`, `.diff-grid`, `.diff-card`, etc.) from the final-v4 mockup.

- [ ] **Step 3: Test**

Scroll below the calendar. Verify:
- Authority block renders with stats, bar chart, and differentiator cards
- Mobile responsive (stats stack vertically below 700px)
- Bar chart shows Ride Ready 59% vs Leading alternative 45%
- No competitor names anywhere

- [ ] **Step 4: Commit**

```bash
git add parks/epic-universe/crowd-calendar/index.html
git commit -m "feat: authority block with accuracy stats and methodology"
```

---

### Task 5: Propagate Changes to All 14 Parks

**Files:**
- Modify: all 14 other `parks/*/crowd-calendar/index.html` files

All pages share the same template. The changes from Tasks 1-4 need to be applied to each. The differences between pages are only park-specific strings (park name, slug, meta tags, descriptions, CTAs with tracking params).

- [ ] **Step 1: Create a diff of the shared sections**

Generate the diff between the original and modified Epic Universe page. Identify which line ranges contain the shared CSS, JS functions, and HTML structure that are identical across all pages.

- [ ] **Step 2: Apply changes to each park page**

For each of the 14 other parks, apply the same changes to: `levelToHsl`, `getDisplayLabel` (replacing `getMobileLabel`), `buildCell`, `openDrawer`, legend HTML, cell CSS, drawer CSS+HTML, authority block CSS+HTML, and mobile breakpoints.

Key: do NOT change any park-specific strings (PARK_NAME, PARK_SLUG, meta tags, tracking params, breadcrumbs, disclaimers).

- [ ] **Step 3: Spot-check 3 parks in browser**

Open Cedar Point, Kings Island, and Busch Gardens Tampa in a browser. Verify:
- Correct park name in header, breadcrumbs, drawer
- Calendar loads data from correct actuals.json
- New cell design renders correctly
- Drawer shows correct park name and CTA tracking params

- [ ] **Step 4: Commit**

```bash
git add parks/*/crowd-calendar/index.html
git commit -m "feat: propagate crowd calendar redesign to all 14 parks"
```

---

### Task 6: Redirect Old Universal Orlando Calendar

**Files:**
- Modify: `universal-orlando/crowd-calendar/index.html`

- [ ] **Step 1: Replace the entire file content with a redirect page**

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Universal Orlando Crowd Calendar | Ride Ready</title>
  <link rel="canonical" href="https://rideready.app/parks/universal-orlando/crowd-calendar/">
  <meta http-equiv="refresh" content="0; url=/parks/universal-orlando/crowd-calendar/">
  <meta name="robots" content="noindex">
  <script>window.location.replace('/parks/universal-orlando/crowd-calendar/');</script>
</head>
<body>
  <p>This page has moved. <a href="/parks/universal-orlando/crowd-calendar/">View the Universal Orlando crowd calendar</a>.</p>
</body>
</html>
```

- [ ] **Step 2: Test the redirect**

Open `http://localhost:8000/universal-orlando/crowd-calendar/` (or however you serve locally). Verify it immediately redirects to `/parks/universal-orlando/crowd-calendar/`.

- [ ] **Step 3: Commit**

```bash
git add universal-orlando/crowd-calendar/index.html
git commit -m "feat: redirect old UO crowd calendar to per-park pages (SEO-preserving)"
```

---

### Task 7: Final Review and Deploy

- [ ] **Step 1: Full visual review**

Open Epic Universe calendar at desktop and mobile widths. Walk through:
- Calendar grid: colors, numbers, labels, YoY badges, weather, events
- Drawer: hero band, info cards, authority strip, CTA
- Authority block below calendar
- All links work (per-date reports, app store links)

- [ ] **Step 2: Check 3 other parks**

Quick scan of IOA, Cedar Point, and Kings Island to confirm propagation worked.

- [ ] **Step 3: Switch to detroittigers account and push**

```bash
gh auth switch --user detroittigers
git push origin master
```

GitHub Pages auto-deploys. Verify on rideready.app.
