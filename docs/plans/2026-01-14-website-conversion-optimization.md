# Website Conversion Optimization Plan

**Date:** January 14, 2026
**Goal:** Increase app downloads from website visitors
**Scope:** Moderate updates to existing pages + new landing pages

---

## Executive Summary

Based on Google Analytics data from January 1-14, 2026:
- 407 sessions, 283 users, 16 app store clicks (5.7% conversion)
- Queue time pages have 80-94% engagement but lack app CTAs
- Social traffic bounces at 53-83%
- Holiday strategy page lost 96% traffic (outdated content)

This plan addresses these issues with targeted changes to convert engaged visitors into app downloads.

---

## Changes Overview

| Change | Impact | Effort |
|--------|--------|--------|
| Queue page CTAs | High | Low |
| Holiday → Evergreen guide | Medium | Medium |
| Homepage comparison section | Medium | Low |
| Social landing page `/go/` | High | Medium |
| Vanity redirect system | Medium | Low |
| Clean tracking system | Low | Low |

---

## 1. Queue Time Page CTAs

**Problem:** Queue pages have 80-94% engagement but no clear path to app download.

**Pages affected:**
- `/universal-orlando/epic-universe/ministry-queue-times/`
- `/universal-orlando/epic-universe/mario-kart-queue-times/`
- `/universal-orlando/epic-universe/mine-cart-madness-queue-times/`
- `/universal-orlando/epic-universe/stardust-racers-queue-times/`
- `/universal-orlando/epic-universe/monsters-unchained-queue-times/`
- `/universal-orlando/epic-universe/hiccups-wing-gliders-queue-times/`

### 1a. Sticky Bottom Bar

Fixed bar at bottom, appears after 25% scroll:

```html
<div class="sticky-bottom-cta">
  <span>📲 Track this queue live</span>
  <a href="https://apps.apple.com/us/app/ride-ready/id6748330847?ct=queue-{ridename}"
     data-ref="queue-{ridename}">Download Free</a>
</div>
```

CSS:
```css
.sticky-bottom-cta {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #fff;
  color: #000;
  padding: 12px 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.15);
  transform: translateY(100%);
  transition: transform 0.3s ease;
  z-index: 1000;
}

.sticky-bottom-cta.visible {
  transform: translateY(0);
}

.sticky-bottom-cta a {
  background: #000;
  color: #fff;
  padding: 8px 18px;
  border-radius: 99px;
  font-weight: 700;
  text-decoration: none;
}
```

JavaScript:
```javascript
window.addEventListener('scroll', function() {
  const cta = document.querySelector('.sticky-bottom-cta');
  const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;

  if (scrollPercent > 25 && !localStorage.getItem('dismissedQueueCTA')) {
    cta.classList.add('visible');
  }
});
```

### 1b. Inline CTA Block

Insert after main queue content, before footer:

```html
<div class="app-cta-block">
  <h3>🎯 Want Real-Time Updates?</h3>
  <p class="cta-subtitle">This guide shows where you are in line.<br>
  <strong>The app tells you when to GO.</strong></p>
  <ul class="cta-features">
    <li>Live wait times updated realtime</li>
    <li>Drop alerts when lines get short</li>
    <li>"What to ride next" recommendations</li>
  </ul>
  <a href="https://apps.apple.com/us/app/ride-ready/id6748330847?ct=queue-{ridename}"
     class="cta-button" data-ref="queue-{ridename}">
    Download Ride Ready - Free
  </a>
</div>
```

---

## 2. Holiday → Evergreen Guide Conversion

**Problem:** `/parks/epic-universe/2025-holiday-strategy/` traffic dropped 96% after Jan 3.

**Solution:** Convert to evergreen "Epic Universe Strategy Guide" while preserving URL for SEO.

### 2a. Meta Changes

```html
<title>Epic Universe Strategy Guide: Data-Driven Tips | Ride Ready</title>
<meta name="description"
      content="Beat the crowds at Epic Universe. Based on 400,000+ wait time samples - see the best days, times, and ride order strategies.">
```

### 2b. Content Changes

| Current | New |
|---------|-----|
| "2025 Holiday Strategy" | "Epic Universe Strategy Guide" |
| Holiday-specific dates | "Best Days to Visit" (patterns) |
| "Christmas crowds" | "Peak vs Off-Peak patterns" |
| Snowflake animations | Remove |

### 2c. Add App CTA Section

Insert after strategy content:

```html
<div class="app-promo-section">
  <h2>📊 Put This Strategy on Autopilot</h2>
  <p>This guide gives you the patterns.<br>
  <strong>Ride Ready gives you the live intel.</strong></p>
  <ul>
    <li>See today's crowd level vs predictions</li>
    <li>Get alerts when your target rides drop</li>
    <li>Know what's actually short RIGHT NOW</li>
  </ul>
  <a href="https://apps.apple.com/us/app/ride-ready/id6748330847?ct=guide"
     class="cta-button" data-ref="guide">
    Get Ride Ready - Free
  </a>
</div>
```

### 2d. Update Internal Links

**Homepage "Trending Strategies" chip:**
```html
<!-- Change from -->
<a class="chip" href="/parks/epic-universe/2025-holiday-strategy/">
  🎄 2025 Holiday Recap
</a>

<!-- To -->
<a class="chip" href="/parks/epic-universe/2025-holiday-strategy/">
  📊 Epic Strategy Guide
</a>
```

**FAQ link:** Update "Epic Universe Holiday Strategy Guide" → "Epic Universe Strategy Guide"

---

## 3. Homepage "App vs Website" Section

**Problem:** Visitors may not understand why to download app when website has guides.

**Placement:** Between "Features" grid and "Premium" section.

```html
<section class="comparison-section">
  <h2>Website vs App: What You Get</h2>
  <div class="comparison-grid">
    <div class="comparison-col website">
      <h3>📖 Website</h3>
      <p class="col-subtitle">You're here now</p>
      <ul>
        <li>✓ Queue guides</li>
        <li>✓ Strategy articles</li>
        <li>✓ Planning tips</li>
      </ul>
      <p class="col-note">Static content<br>Plan before you go</p>
    </div>
    <div class="comparison-col app">
      <h3>📱 App</h3>
      <p class="col-subtitle">Free download</p>
      <ul>
        <li>✓ Everything here, plus:</li>
        <li>✓ LIVE wait times</li>
        <li>✓ Drop alerts</li>
        <li>✓ "Ride next" picks</li>
      </ul>
      <p class="col-note">Updates realtime<br>Use IN the park</p>
    </div>
  </div>
  <a href="https://apps.apple.com/us/app/ride-ready/id6748330847?ct=compare"
     class="cta-button" data-ref="compare">
    Get the App - It's Free
  </a>
</section>
```

---

## 4. Social Landing Page (`/go/`)

**Problem:** Social traffic bounces at 53-83%. Different intent than organic search.

**Solution:** Dedicated landing page optimized for app download.

### 4a. File: `/go/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ride Ready - Skip the Lines</title>
  <meta name="description" content="Live wait times, drop alerts, and ride recommendations for Epic Universe and Universal Orlando.">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-KGYGTPMTQ3"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-KGYGTPMTQ3');
  </script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #000;
      color: #fff;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px 24px;
      text-align: center;
    }
    .logo { width: 80px; height: 80px; margin-bottom: 24px; }
    h1 { font-size: 1.8rem; margin-bottom: 12px; }
    .subtitle { color: #aaa; font-size: 1.1rem; margin-bottom: 32px; }
    .features {
      list-style: none;
      text-align: left;
      margin-bottom: 32px;
      background: rgba(255,255,255,0.05);
      padding: 20px 28px;
      border-radius: 12px;
    }
    .features li {
      padding: 8px 0;
      font-size: 1rem;
    }
    .cta-button {
      display: inline-block;
      background: linear-gradient(100deg, #FF416C, #FF4B2B);
      color: #fff;
      padding: 16px 40px;
      border-radius: 12px;
      text-decoration: none;
      font-weight: 600;
      font-size: 1.1rem;
      margin-bottom: 16px;
    }
    .android-note { color: #888; font-size: 0.9rem; margin-bottom: 40px; }
    .android-note a { color: #FF6B4B; }
    .escape-link { color: #666; font-size: 0.9rem; }
    .escape-link a { color: #888; }
  </style>
</head>
<body>
  <img src="/images/logo.png" alt="Ride Ready" class="logo">
  <h1>Skip the lines at Epic Universe</h1>
  <p class="subtitle">Free app for Universal Orlando</p>

  <ul class="features">
    <li>📍 Live wait times</li>
    <li>🔔 Alerts when lines drop</li>
    <li>🎯 "What to ride next" picks</li>
  </ul>

  <a href="https://apps.apple.com/us/app/ride-ready/id6748330847?ct=social"
     class="cta-button" data-ref="social"
     onclick="gtag('event', 'app_store_click', {source: 'social'});">
    Download Free on iPhone
  </a>

  <p class="android-note">
    Android coming 2026 · <a href="mailto:support@rideready.app?subject=Android%20Waitlist">Join waitlist</a>
  </p>

  <p class="escape-link">
    Want to plan first? <a href="/">Browse our guides →</a>
  </p>
</body>
</html>
```

### 4b. Platform-Specific Variants

Create these with same template, different tracking:

| File | Tracks as |
|------|-----------|
| `/go/index.html` | `ct=social` |
| `/go/fb/index.html` | `ct=fb` |
| `/go/x/index.html` | `ct=x` |
| `/go/ig/index.html` | `ct=ig` |

---

## 5. Vanity Redirect System

**Purpose:** Clean, memorable URLs for social sharing.

### URL Structure

```
/mlk           → /parks/epic-universe/mlk-day-weekend-2026/
/mlk/fb        → same, tracks as mlk-fb
/mlk/x         → same, tracks as mlk-x

/pres          → /parks/epic-universe/presidents-day-weekend-2026/
/spring        → /orlando/spring-break-2026/
/guide         → /parks/epic-universe/2025-holiday-strategy/
/queues        → /universal-orlando/epic-universe/
/app           → App Store
```

### Redirect Template

**`/mlk/index.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Redirecting... | Ride Ready</title>
  <link rel="canonical" href="https://rideready.app/parks/epic-universe/mlk-day-weekend-2026/">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-KGYGTPMTQ3"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-KGYGTPMTQ3');
    gtag('event', 'shortlink', { ref: 'mlk' });
  </script>
  <meta http-equiv="refresh" content="0;url=/parks/epic-universe/mlk-day-weekend-2026/">
</head>
<body>
  <p>Redirecting to <a href="/parks/epic-universe/mlk-day-weekend-2026/">MLK Weekend Guide</a>...</p>
</body>
</html>
```

### Adding New Redirects

1. Create folder: `mkdir -p {shortname}/fb {shortname}/x`
2. Copy template to `{shortname}/index.html`
3. Change 3 things:
   - `ref: '{shortname}'`
   - `url=/actual/page/path/`
   - `href` in canonical and body

### Cheat Sheet for Social Team

```
GUIDES:
  rideready.app/mlk       - MLK Weekend
  rideready.app/pres      - Presidents Day
  rideready.app/spring    - Spring Break
  rideready.app/guide     - Epic Strategy Guide
  rideready.app/queues    - All Queue Guides

APP:
  rideready.app/app       - Download page

ADD PLATFORM (optional):
  /mlk/fb    - posting on Facebook
  /mlk/x     - posting on X
  /mlk/ig    - posting on Instagram
```

---

## 6. Tracking System

### Parameter Convention

**Website (GA4):**
- Single `data-ref` attribute on links
- Values: `home`, `sticky`, `queue-ministry`, `guide`, `social`, `compare`

**App Store (`ct` parameter):**
- Same values as `data-ref`
- Shows in App Store Connect Analytics

### Event Tracking Code

Add to all pages (in main script block):

```javascript
document.querySelectorAll('[data-ref]').forEach(link => {
  link.addEventListener('click', function() {
    const ref = this.dataset.ref;
    gtag('event', 'app_store_click', {
      source: ref,
      page: window.location.pathname
    });
  });
});
```

### Naming Convention

| Type | Format | Examples |
|------|--------|----------|
| Pages | `page-name` | `home`, `guide`, `social` |
| Queue pages | `queue-ridename` | `queue-ministry`, `queue-mario` |
| Sections | `section` | `sticky`, `premium`, `footer`, `compare` |
| Vanity links | `shortname` or `shortname-platform` | `mlk`, `mlk-fb`, `spring-x` |

---

## Implementation Checklist

### Phase 1: Foundation
- [ ] Add tracking code to all pages
- [ ] Create `/go/` landing page
- [ ] Create `/go/fb/`, `/go/x/`, `/go/ig/` variants

### Phase 2: Content Updates
- [ ] Convert holiday strategy to evergreen guide
- [ ] Update homepage "Trending Strategies" chip
- [ ] Update FAQ link text

### Phase 3: CTA Additions
- [ ] Add sticky bottom CTA to 6 queue pages
- [ ] Add inline CTA block to 6 queue pages
- [ ] Add "App vs Website" section to homepage

### Phase 4: Vanity Redirects
- [ ] Create `/mlk/` redirect (+ fb, x, ig variants)
- [ ] Create `/pres/` redirect (+ variants)
- [ ] Create `/spring/` redirect (+ variants)
- [ ] Create `/guide/` redirect (+ variants)
- [ ] Create `/queues/` redirect (+ variants)
- [ ] Create `/app/` redirect

### Phase 5: Verification
- [ ] Test all new pages on mobile
- [ ] Verify GA4 events firing correctly
- [ ] Check App Store Connect for `ct` parameter tracking
- [ ] Update social bios with new vanity URLs

---

## Success Metrics

Track these weekly after implementation:

| Metric | Current (Jan 1-14) | Target |
|--------|-------------------|--------|
| App Store clicks | 16 | 30+ |
| Conversion rate | 5.7% | 10%+ |
| Queue page → App clicks | ~0 | 5+ per page |
| Social bounce rate | 53-83% | <50% |

---

## Files to Create

```
/go/index.html
/go/fb/index.html
/go/x/index.html
/go/ig/index.html
/mlk/index.html
/mlk/fb/index.html
/mlk/x/index.html
/pres/index.html
/pres/fb/index.html
/pres/x/index.html
/spring/index.html
/spring/fb/index.html
/spring/x/index.html
/guide/index.html
/queues/index.html
/app/index.html
```

## Files to Modify

```
/index.html (homepage)
/parks/epic-universe/2025-holiday-strategy/index.html
/universal-orlando/epic-universe/ministry-queue-times/index.html
/universal-orlando/epic-universe/mario-kart-queue-times/index.html
/universal-orlando/epic-universe/mine-cart-madness-queue-times/index.html
/universal-orlando/epic-universe/stardust-racers-queue-times/index.html
/universal-orlando/epic-universe/monsters-unchained-queue-times/index.html
/universal-orlando/epic-universe/hiccups-wing-gliders-queue-times/index.html
```
