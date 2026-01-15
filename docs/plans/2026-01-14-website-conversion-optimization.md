# Website Conversion Optimization Plan

**Date:** January 14, 2026 (Updated with 2026 research)
**Goal:** Increase app downloads from website visitors
**Scope:** Moderate updates to existing pages + new landing pages + strategic additions

---

## Executive Summary

Based on Google Analytics data from January 1-14, 2026:
- 407 sessions, 283 users, 16 app store clicks (5.7% conversion)
- Queue time pages have 80-94% engagement but lack strong app CTAs
- Social traffic bounces at 53-83%
- Holiday strategy page lost 96% traffic (outdated content)
- **SEO traffic has 67% engagement but only 11% of visits** - biggest opportunity

### Research Findings (2026 Best Practices)

- iOS Smart App Banners can drive **33% of total installs** when optimized
- Landing pages with single CTA convert **2-3x better** than cluttered pages
- Median landing page conversion: 4.3%, top 10%: 11.5%+
- Reducing bounce: fast load times (✓ we have 0.15s), relevant content, clear CTA hierarchy
- Industry trend: deep linking from social to in-app content increases conversions

---

## Impact Tier Overview

### Tier 1: High Impact / Quick Wins (Sections 1-2)
| # | Change | Why | Effort |
|---|--------|-----|--------|
| 1 | Smart App Banner Optimization | Can drive 33% of installs | Low |
| 2 | Queue page CTAs (improve existing) | 80-94% engagement, warm traffic | Low |

### Tier 2: Medium Impact (Sections 3-6)
| # | Change | Why | Effort |
|---|--------|-----|--------|
| 3 | SEO Content Strategy | 67% engagement, only 11% traffic | High |
| 4 | Holiday → Evergreen guide | Recapture lost traffic | Medium |
| 5 | Homepage comparison section | Clarify value prop | Low |
| 6 | Social landing page `/go/` | Convert 23% of traffic from social | Medium |

### Tier 3: Foundation/Support (Sections 7-9)
| # | Change | Why | Effort |
|---|--------|-----|--------|
| 7 | Vanity redirect system | Clean social sharing | Low |
| 8 | Clean tracking system | Measure what works | Low |
| 9 | A/B Testing Framework | Validate changes | Medium |

### Tier 4: Future Investment (Sections 10-11)
| # | Change | Why | Effort |
|---|--------|-----|--------|
| 10 | Deep Linking Setup | Social → app content | High |
| 11 | Seasonal Content Calendar | Recurring traffic peaks | Ongoing |

---

# TIER 1: HIGH IMPACT / QUICK WINS

---

## 1. Smart App Banner Optimization

**Impact:** Can drive up to 33% of total installs with zero friction
**Current State:** Meta tag exists on 12 pages, but may not be optimized

### Current Implementation
```html
<meta name="apple-itunes-app" content="app-id=6748330847">
```

### Optimized Implementation
Add `app-argument` to pass context to the app and `affiliate-data` for tracking:

```html
<meta name="apple-itunes-app"
      content="app-id=6748330847, app-argument=rideready://page/{page-id}, affiliate-data=ct=smartbanner-{page}">
```

### Page-Specific Arguments

| Page | app-argument | affiliate-data |
|------|--------------|----------------|
| Homepage | `rideready://home` | `ct=smartbanner-home` |
| Queue pages | `rideready://ride/{ride-slug}` | `ct=smartbanner-queue-{ride}` |
| Epic Hub | `rideready://park/epic` | `ct=smartbanner-hub` |
| Strategy Guide | `rideready://park/epic` | `ct=smartbanner-guide` |

### Files to Update
All pages currently have the basic meta tag. Update these 12 files with optimized version:
- `index.html`
- `parks/epic-universe/index.html`
- `parks/epic-universe/strategy/index.html` (new)
- All 6 queue pages
- `parks/epic-universe/mlk-day-weekend-2026/index.html`
- `universal-orlando/epic-universe/index.html`
- `go/index.html` (new)

### Why This Matters
Smart App Banners:
- Only appear to iOS users who don't have the app
- Show when user scrolls (not intrusive)
- Pre-fill the App Store page (one tap install)
- Can track via `affiliate-data` in App Store Connect
- No friction vs manual banner clicks

---

## 2. Queue Time Page CTAs

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

# TIER 2: MEDIUM IMPACT

---

## 3. SEO Content Strategy

**Problem:** SEO traffic has 67% engagement rate but represents only 11% of total traffic. This is your biggest missed opportunity.

### Current SEO State (Jan 1-14, 2026)
- 45 sessions from organic search (11% of total)
- 67% engagement rate (highest of all channels)
- Ranking for: "epic universe queue times", ride-specific searches

### High-Value Content Opportunities

Based on search volume and your competitive advantage (real wait time data):

| Topic | Search Intent | Content Type |
|-------|---------------|--------------|
| "Epic Universe wait times" | Real-time info | Interactive page (have it) |
| "Best time to visit Epic Universe" | Planning | Strategy guide (converting) |
| "Epic Universe crowd calendar 2026" | Planning | **New content needed** |
| "Epic Universe tips" | Planning | Roundup of existing content |
| "Spring break crowd predictions" | Seasonal | **Seasonal content** |

### Priority Content to Create

**1. Crowd Calendar Page** `/parks/epic-universe/crowd-calendar/`
- Use your wait time data to show historical patterns
- Include: best days, worst days, seasonal patterns
- Update monthly with fresh data
- This is your unique competitive advantage

**2. "Tips" Aggregation Page** `/parks/epic-universe/tips/`
- Link to queue guides, strategy, seasonal content
- Optimize for "Epic Universe tips" searches
- Acts as internal linking hub for SEO

### Why SEO Matters
- Organic traffic is **free** (vs paid)
- Users actively searching have **high intent**
- 67% engagement proves content quality
- Each ranking page is a permanent traffic source
- Compounds over time

### Effort vs Impact
This is marked "High effort" because good SEO content takes time. But the ROI is excellent:
- Crowd calendar: 2-3 hours to build, ranks for years
- Tips page: 1 hour, improves internal linking
- Strategy guide (already planned): helps all SEO

---

## 4. Holiday → Evergreen Guide Conversion

**Problem:** `/parks/epic-universe/2025-holiday-strategy/` traffic dropped 96% after Jan 3, and the URL looks dated.

**Solution:** Create evergreen guide at new clean URL, redirect old URL to preserve SEO.

### 2a. URL Structure

```
OLD (redirect):  /parks/epic-universe/2025-holiday-strategy/  →  301 to new URL
NEW (content):   /parks/epic-universe/strategy/
VANITY:          /epic-guide  →  /parks/epic-universe/strategy/
```

This sets up for future guides: `/usf-guide`, `/ioa-guide`, `/cedar-point-guide`, etc.

### 2b. Meta Tags (New Page)

```html
<title>Epic Universe Strategy Guide: Data-Driven Tips | Ride Ready</title>
<meta name="description"
      content="Beat the crowds at Epic Universe. Based on 400,000+ wait time samples - see the best days, times, and ride order strategies.">
<link rel="canonical" href="https://rideready.app/parks/epic-universe/strategy/">
```

### 2c. Content Changes

| Current | New |
|---------|-----|
| "2025 Holiday Strategy" | "Epic Universe Strategy Guide" |
| Holiday-specific dates | "Best Days to Visit" (patterns) |
| "Christmas crowds" | "Peak vs Off-Peak patterns" |
| Snowflake animations | Remove |

### 2d. Add App CTA Section

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

### 2e. Update Internal Links

**Homepage "Trending Strategies" chip:**
```html
<!-- Change from -->
<a class="chip" href="/parks/epic-universe/2025-holiday-strategy/">
  🎄 2025 Holiday Recap
</a>

<!-- To -->
<a class="chip" href="/parks/epic-universe/strategy/">
  📊 Epic Strategy Guide
</a>
```

**FAQ link:** Update href to `/parks/epic-universe/strategy/` and text to "Epic Universe Strategy Guide"

### 2f. Redirect Old URL

Convert `/parks/epic-universe/2025-holiday-strategy/index.html` to a redirect:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Redirecting... | Ride Ready</title>
  <link rel="canonical" href="https://rideready.app/parks/epic-universe/strategy/">
  <meta http-equiv="refresh" content="0;url=/parks/epic-universe/strategy/">
  <script>
    window.location.replace("/parks/epic-universe/strategy/" + window.location.search);
  </script>
</head>
<body>
  <p>Moved to <a href="/parks/epic-universe/strategy/">Epic Universe Strategy Guide</a></p>
</body>
</html>
```

---

## 5. Homepage "App vs Website" Section

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

## 6. Social Landing Page (`/go/`)

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

---

# TIER 3: FOUNDATION / SUPPORT

---

## 7. Vanity Redirect System

**Purpose:** Clean, memorable URLs for social sharing. No platform variants needed - GA4 automatically captures referrer source.

### URL Structure

```
/epic-guide    → /parks/epic-universe/strategy/
/mlk           → /parks/epic-universe/mlk-day-weekend-2026/
/pres          → /parks/epic-universe/presidents-day-weekend-2026/
/spring        → /orlando/spring-break-2026/
/queues        → /universal-orlando/epic-universe/
/app           → App Store
```

Future-proof for more guides: `/usf-guide`, `/ioa-guide`, `/cedar-point-guide`, etc.

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

1. Create folder: `mkdir {shortname}`
2. Copy template to `{shortname}/index.html`
3. Change 3 things:
   - `ref: '{shortname}'`
   - `url=/actual/page/path/`
   - `href` in canonical and body

### Cheat Sheet for Social Team

```
STRATEGY GUIDES:
  rideready.app/epic-guide   - Epic Universe Strategy
  rideready.app/queues       - All Queue Guides

EVENT GUIDES:
  rideready.app/mlk          - MLK Weekend
  rideready.app/pres         - Presidents Day
  rideready.app/spring       - Spring Break

APP:
  rideready.app/app          - Download page
  rideready.app/go           - Social landing page
```

**Note:** No need for /mlk/fb or /mlk/x variants. GA4 automatically tracks the referrer source (facebook.com, t.co, etc.) so you'll still see where traffic came from.

**Future guides:** Follow the pattern `/[park]-guide` (e.g., `/usf-guide`, `/ioa-guide`)

---

## 8. Tracking System

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
| Vanity links | `shortname` | `mlk`, `pres`, `spring` |

---

## 9. A/B Testing Framework

**Purpose:** Validate that changes actually improve conversions before rolling out everywhere.

### Recommended Tool
Use Google Optimize (free) or simple manual A/B via GA4 events.

### Manual A/B Testing Approach
Since this is a static site, use URL parameters to test variations:

```javascript
// Check for variant parameter
const urlParams = new URLSearchParams(window.location.search);
const variant = urlParams.get('v') || 'a'; // default to variant A

// Show different CTAs based on variant
if (variant === 'b') {
  document.querySelector('.cta-button').innerHTML = 'Download Free App';
} else {
  document.querySelector('.cta-button').innerHTML = 'Get Ride Ready - Free';
}

// Track which variant was shown
gtag('event', 'variant_shown', {
  variant: variant,
  page: window.location.pathname
});
```

### What to Test First
Priority tests based on impact:

1. **CTA Copy** - "Download Free" vs "Get the App" vs "Skip the Lines"
2. **CTA Color** - Gradient vs Solid vs White
3. **Sticky Bar Timing** - 25% scroll vs 50% scroll vs exit intent
4. **Social Landing** - Features list vs Social proof vs Minimal

### How to Run Tests
1. Send 50% of traffic to `?v=a`, 50% to `?v=b`
2. Track clicks per variant in GA4
3. Run for 100+ sessions per variant minimum
4. Winner becomes the default

### Success Criteria
A variant wins if it has:
- 20%+ better conversion rate
- Statistical significance (100+ sessions)
- No negative impact on engagement

---

# TIER 4: FUTURE INVESTMENT

---

## 10. Deep Linking Setup

**Purpose:** Let social posts link directly to relevant content *inside* the app, not just the App Store.

### How Deep Linking Works
1. User clicks social link → Landing page
2. If app installed → Opens specific screen in app
3. If not installed → App Store, then opens specific screen after install (deferred deep linking)

### URL Scheme (Already Defined in App?)
```
rideready://home
rideready://park/epic
rideready://ride/ministry-of-magic
rideready://alerts
```

### Implementation Options

**Option A: Smart App Banner + Universal Links (Recommended)**
- Uses your existing `apple-itunes-app` meta tags
- Add `app-argument` with deep link URL
- Apple handles the rest

**Option B: Branch.io / Firebase Dynamic Links**
- More control but requires SDK integration
- Better analytics
- Handles deferred deep links
- **Consider for future**

### When to Implement
This is Tier 4 because:
- Requires app-side work (Universal Links entitlement)
- Smart App Banners already provide 80% of the benefit
- ROI increases as app install base grows

**Recommendation:** Start with optimized Smart App Banners (Tier 1). Add full deep linking when app has 1,000+ installs and deferred deep link value is higher.

---

## 11. Seasonal Content Calendar

**Purpose:** Capture recurring traffic peaks instead of scrambling to create content.

### Identified Opportunities

| Event | Content Needed | Create By |
|-------|----------------|-----------|
| MLK Weekend | Guide | Done ✓ |
| Presidents Day | Guide | Feb 1 |
| Spring Break | Guide + Predictions | March 1 |
| Summer Peak | Strategy update | May 15 |
| Halloween | Horror Nights guide | Sept 1 |
| Thanksgiving | Crowd predictions | Nov 1 |
| Christmas/New Year | Strategy update | Nov 15 |

### Template Structure
Each seasonal guide should include:
1. Crowd prediction (using your data)
2. Ride strategy for that period
3. App CTA section
4. Smart App Banner with context

### Why This Matters
Your holiday strategy page got traffic because it was **timely**. But it died because it was **dated**.

Solution: Create evergreen templates, update dates/specifics each year.

---

## Implementation Checklist

### Phase 1: Quick Wins (Tier 1) - Do First
- [ ] Optimize Smart App Banner meta tags on all 12 pages
- [ ] Add tracking code to all pages
- [ ] Add sticky bottom CTA to 6 queue pages
- [ ] Add inline CTA block to 6 queue pages

### Phase 2: Social Optimization (Tier 2)
- [ ] Create `/go/` landing page
- [ ] Create `/parks/epic-universe/strategy/` page (evergreen guide)
- [ ] Convert old `/parks/epic-universe/2025-holiday-strategy/` to redirect
- [ ] Add "App vs Website" section to homepage
- [ ] Update homepage "Trending Strategies" chip to new URL
- [ ] Update FAQ link text and href

### Phase 3: Infrastructure (Tier 3)
- [ ] Create `/epic-guide/` redirect
- [ ] Create `/mlk/` redirect
- [ ] Create `/pres/` redirect
- [ ] Create `/spring/` redirect
- [ ] Create `/queues/` redirect
- [ ] Create `/app/` redirect

### Phase 4: Verification
- [ ] Test all new pages on mobile
- [ ] Verify GA4 events firing correctly
- [ ] Check App Store Connect for `ct` parameter tracking
- [ ] Update social bios with new vanity URLs

### Phase 5: SEO Investment (Tier 2 - High Effort)
- [ ] Create `/parks/epic-universe/crowd-calendar/` page
- [ ] Create `/parks/epic-universe/tips/` aggregation page
- [ ] Add internal links between all content pages

### Phase 6: Future (Tier 4 - When Ready)
- [ ] Research Universal Links implementation for deep linking
- [ ] Create Presidents Day weekend guide
- [ ] Create Spring Break guide

---

## Success Metrics

Track these weekly after implementation:

| Metric | Current (Jan 1-14) | 30-Day Target | 90-Day Target |
|--------|-------------------|---------------|---------------|
| App Store clicks | 16 | 30+ | 75+ |
| Conversion rate | 5.7% | 8%+ | 12%+ |
| Queue page → App clicks | ~0 | 5+ per page | 10+ per page |
| Social bounce rate | 53-83% | <50% | <40% |
| SEO traffic share | 11% | 15% | 25% |
| Smart Banner installs | Unknown | Track | 33% of installs |

### How to Measure
- **App Store clicks:** GA4 > Events > `app_store_click`
- **Conversion rate:** App Store clicks ÷ Sessions
- **Social bounce:** GA4 > Acquisition > filter by Social
- **SEO share:** GA4 > Acquisition > Organic Search %
- **Smart Banner installs:** App Store Connect > Analytics > by Campaign Token

---

## Files to Create

### Core (Phases 1-3)
```
/parks/epic-universe/strategy/index.html   ← New evergreen strategy guide
/go/index.html                             ← Social landing page
/epic-guide/index.html                     ← Strategy Guide redirect
/mlk/index.html                            ← MLK Weekend redirect
/pres/index.html                           ← Presidents Day redirect
/spring/index.html                         ← Spring Break redirect
/queues/index.html                         ← Queue Guides redirect
/app/index.html                            ← App Store redirect
```
**Core files: 8**

### SEO Content (Phase 5)
```
/parks/epic-universe/crowd-calendar/index.html  ← Crowd calendar with data
/parks/epic-universe/tips/index.html            ← Tips aggregation/hub page
```
**SEO files: 2**

**Total new files: 10**

## Files to Modify

### Smart App Banner Updates (12 files)
```
/index.html (add optimized meta tag)
/parks/epic-universe/index.html (add optimized meta tag)
/parks/epic-universe/mlk-day-weekend-2026/index.html (add optimized meta tag)
/universal-orlando/epic-universe/index.html (add optimized meta tag)
+ All 6 queue pages below (add optimized meta tag)
```

### Content/CTA Updates (8 files)
```
/index.html (add comparison section, update chip link)
/parks/epic-universe/2025-holiday-strategy/index.html (convert to redirect)
/universal-orlando/epic-universe/ministry-queue-times/index.html (add CTAs)
/universal-orlando/epic-universe/mario-kart-queue-times/index.html (add CTAs)
/universal-orlando/epic-universe/mine-cart-madness-queue-times/index.html (add CTAs)
/universal-orlando/epic-universe/stardust-racers-queue-times/index.html (add CTAs)
/universal-orlando/epic-universe/monsters-unchained-queue-times/index.html (add CTAs)
/universal-orlando/epic-universe/hiccups-wing-gliders-queue-times/index.html (add CTAs)
```

**Total files to modify: 12 unique files** (some overlap between lists)
