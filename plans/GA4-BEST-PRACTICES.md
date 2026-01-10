# GA4 Best Practices for Ride Ready App Marketing Website

**Property:** Ride Ready (G-KGYGTPMTQ3)
**Traffic:** ~900 sessions/month, ~750 users
**Date:** January 2026

---

## Executive Summary

This document provides actionable Google Analytics 4 (GA4) recommendations specifically tailored for rideready.app—a mobile app marketing site with content-driven strategy guides. With ~900 sessions/month from Direct, Facebook, and Google Organic traffic, the focus is on **high-impact, low-effort wins** that track app download intent, optimize content performance, and improve conversion attribution.

Key priorities:
1. **Track app download funnel** (App Store clicks, scroll depth, content engagement)
2. **Fix low-traffic data issues** (thresholding, reporting identity)
3. **Implement UTM standards** for Facebook shares and marketing links
4. **Create conversion events** for key user actions
5. **Build custom audiences** for remarketing and analysis
6. **Set up essential integrations** (Search Console)

This guide prioritizes practical implementation over theoretical best practices, with code examples ready to deploy.

---

## 1. Event Tracking Strategy

### Current State
Your site already tracks one custom event:
- `app_store_click` - Fires when users click App Store buttons (hero-cta, footer-cta)

### Recommended Custom Events (Priority Order)

#### **Priority 1: Core Conversion Events**

**1.1 App Store Click (Already Implemented ✓)**
```javascript
gtag('event', 'app_store_click', {
  event_category: 'engagement',
  event_label: locationLabel,  // 'hero-cta', 'footer-cta'
  transport_type: 'beacon'
});
```
**Action:** Already working. Consider adding `value: 1` to calculate potential conversion value.

**1.2 Queue Guide Navigation**
Track clicks on your Epic Universe queue guides (Ministry, Mario Kart, Stardust Racers, etc.)

```javascript
// Add to each queue guide link click
gtag('event', 'queue_guide_view', {
  event_category: 'content_engagement',
  guide_name: 'Battle at the Ministry',  // or Mario Kart, Stardust Racers, etc.
  guide_position: 1,  // Position in carousel
  source_page: 'homepage'
});
```

**1.3 Epic Universe Strategy Guide Click**
Track the highlighted Epic Universe chip link:

```javascript
gtag('event', 'strategy_guide_click', {
  event_category: 'content_engagement',
  guide_type: 'epic_universe_holiday',
  link_location: 'supported_parks_section'
});
```

**1.4 Park Request Submission**
Track mailto clicks for park requests:

```javascript
gtag('event', 'park_request_click', {
  event_category: 'engagement',
  request_method: 'email',
  value: 5  // Qualitative value of user interest
});
```

#### **Priority 2: Engagement Events**

**2.1 Scroll Depth Tracking**
GA4 only tracks 90% scroll by default. For your content-heavy guides, track milestone depths:

```javascript
// Using GTM or custom script
gtag('event', 'scroll', {
  percent_scrolled: 25,  // or 50, 75, 90
  page_location: window.location.pathname
});
```

**Implementation via GTM (Recommended):**
1. Create Scroll Depth trigger in GTM (25%, 50%, 75%, 90%)
2. Fire GA4 Event tag with `scroll_depth` event
3. Pass `{{Scroll Depth Threshold}}` as parameter

**2.2 Screenshot Gallery Engagement**
Track which screenshots users view:

```javascript
document.querySelectorAll('.screenshot-item').forEach(function(item) {
  item.addEventListener('click', function() {
    gtag('event', 'screenshot_view', {
      event_category: 'engagement',
      screenshot_label: item.getAttribute('data-label'),
      interaction_type: 'click'
    });
  });
});
```

**2.3 Social Media Clicks**
Track X (Twitter) and Instagram clicks:

```javascript
document.querySelectorAll('.social-links a').forEach(function(link) {
  link.addEventListener('click', function() {
    gtag('event', 'social_click', {
      event_category: 'engagement',
      social_network: link.getAttribute('aria-label'),
      link_url: link.href
    });
  });
});
```

**2.4 Premium Section Visibility**
Track users who scroll to the Premium section (indicates high engagement):

```javascript
// Using Intersection Observer
const premiumSection = document.querySelector('.premium-section');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      gtag('event', 'premium_section_view', {
        event_category: 'engagement',
        section: 'premium_pricing',
        visibility_threshold: 0.5
      });
      observer.unobserve(entry.target);  // Fire once
    }
  });
}, { threshold: 0.5 });
observer.observe(premiumSection);
```

#### **Priority 3: Content Performance Events**

**3.1 Time on Page (Enhanced Engagement Time)**
GA4 tracks `user_engagement` automatically, but you can enhance it:

```javascript
// Track 30-second engaged sessions
setTimeout(function() {
  gtag('event', 'engaged_session', {
    event_category: 'engagement',
    engagement_duration: '30_seconds',
    page_title: document.title
  });
}, 30000);
```

**3.2 Outbound Link Tracking**
Track external links (especially important for understanding where users go after leaving):

```javascript
document.querySelectorAll('a[href^="http"]:not([href*="rideready.app"])').forEach(function(link) {
  link.addEventListener('click', function() {
    gtag('event', 'outbound_click', {
      event_category: 'engagement',
      link_url: link.href,
      link_text: link.textContent.trim().substring(0, 50)
    });
  });
});
```

### Event Implementation Priority Matrix

| Event | Impact | Effort | Priority | Status |
|-------|--------|--------|----------|--------|
| App Store Click | High | None | ✓ Done | Already implemented |
| Queue Guide Click | High | Low | 1 | Implement immediately |
| Strategy Guide Click | High | Low | 1 | Implement immediately |
| Scroll Depth (25/50/75%) | High | Medium | 2 | Requires GTM or custom code |
| Premium Section View | Medium | Low | 2 | Quick win |
| Screenshot Gallery | Medium | Low | 3 | Nice to have |
| Social Media Clicks | Medium | Low | 3 | Quick win |
| Outbound Links | Low | Low | 4 | Future enhancement |

---

## 2. Conversion Events (Key Events)

GA4 renamed "Conversions" to "Key Events" in 2024. Here's what to mark as conversions:

### Recommended Key Events

**2.1 Primary Conversion: `app_store_click`**
- **Action:** Mark your existing `app_store_click` event as a Key Event
- **Steps:**
  1. Admin → Data display → Events
  2. Find `app_store_click` → Toggle "Mark as key event"
- **Why:** This is your ultimate conversion—users clicking to download the app
- **Value:** Consider adding `value: 10` to each event to calculate conversion value

**2.2 Secondary Conversions to Create:**

**Queue Guide View** (Micro-conversion)
```javascript
gtag('event', 'queue_guide_view', {
  guide_name: 'Battle at the Ministry',
  value: 2  // Qualitative value
});
```
Mark as Key Event to track content that leads to app downloads.

**Engaged Session** (30+ seconds on site)
```javascript
gtag('event', 'engaged_session', {
  engagement_duration: '30_seconds',
  value: 1
});
```
Mark as Key Event to identify quality traffic sources.

**Premium Section View** (High Intent Signal)
```javascript
gtag('event', 'premium_section_view', {
  section: 'premium_pricing',
  value: 3
});
```
Mark as Key Event—users who read about Premium are highly engaged.

### Key Event Hierarchy

```
Primary Conversion (Highest Value)
└── app_store_click (Direct download intent)

Secondary Conversions (Engagement Indicators)
├── queue_guide_view (Content engagement)
├── engaged_session (Quality traffic)
└── premium_section_view (Feature interest)

Micro-conversions (Future Analysis)
├── scroll_depth_90
└── strategy_guide_click
```

### Adding Conversion Values

Why add values? It enables ROAS calculations and better optimization.

**Suggested Values:**
- `app_store_click`: $10 (estimated lifetime value per download)
- `queue_guide_view`: $2 (content engagement value)
- `engaged_session`: $1 (qualified visitor)
- `premium_section_view`: $3 (feature interest)

```javascript
gtag('event', 'app_store_click', {
  event_category: 'engagement',
  event_label: locationLabel,
  value: 10,  // Add this
  currency: 'USD'  // Add this
});
```

---

## 3. Custom Audiences

Audiences in GA4 are **forward-looking only** (they start collecting data from creation date). With ~900 sessions/month, focus on high-value segments.

### Recommended Audiences (Priority Order)

#### **Priority 1: Remarketing Audiences**

**3.1 App Store Clickers (But Didn't Download)**
- **Condition:** `app_store_click` event fired
- **Membership duration:** 30 days
- **Use case:** Retarget users who showed download intent but may not have completed
- **GA4 Setup:**
  - Admin → Audiences → New Audience → Create Custom
  - Include: Users who triggered `app_store_click`
  - Membership: 30 days

**3.2 Queue Guide Readers**
- **Condition:** `queue_guide_view` event fired
- **Membership duration:** 30 days
- **Use case:** Highly engaged content readers—ideal for remarketing
- **GA4 Setup:**
  - Include: Users who triggered `queue_guide_view`
  - Membership: 30 days
  - Export to Google Ads for remarketing

**3.3 Premium Feature Viewers**
- **Condition:** `premium_section_view` event fired
- **Membership duration:** 14 days
- **Use case:** Users interested in premium features—target with app benefits
- **GA4 Setup:**
  - Include: Users who triggered `premium_section_view`
  - Membership: 14 days

**3.4 Engaged Visitors (30+ Seconds)**
- **Condition:** Engaged sessions > 30 seconds
- **Membership duration:** 30 days
- **Use case:** Quality traffic for lookalike audiences
- **GA4 Setup:**
  - Include: `session_engaged` = true AND `engagement_time_msec` > 30000
  - Membership: 30 days
  - Export to Google Ads for Similar Audiences

#### **Priority 2: Analysis Audiences**

**3.5 Epic Universe Strategy Guide Visitors**
- **Condition:** Page path contains `/epic-universe`
- **Membership duration:** 30 days
- **Use case:** Segment traffic to understand content performance
- **GA4 Setup:**
  - Include: `page_location` contains `/epic-universe`
  - Membership: 30 days

**3.6 Facebook Referrals**
- **Condition:** Source = `facebook` or `fb` or `m.facebook`
- **Membership duration:** 30 days
- **Use case:** Analyze Facebook traffic separately from other sources
- **GA4 Setup:**
  - Include: `source` = `facebook` OR `fb` OR `m.facebook`
  - Membership: 30 days

**3.7 Repeat Visitors**
- **Condition:** Session count ≥ 2
- **Membership duration:** 90 days
- **Use case:** Identify users returning to the site (strong interest signal)
- **GA4 Setup:**
  - Include: `session_count` ≥ 2
  - Membership: 90 days

**3.8 Mobile vs. Desktop Users**
- **Condition A:** Device category = mobile
- **Condition B:** Device category = desktop
- **Membership duration:** 30 days
- **Use case:** Optimize messaging by platform
- **GA4 Setup:**
  - Create two audiences
  - Include A: `device_category` = `mobile`
  - Include B: `device_category` = `desktop`

### Audience Export to Google Ads

Once audiences are created:
1. Admin → Product Links → Google Ads Links
2. Link your Google Ads account
3. Enable "Personalized Advertising" features
4. Audiences automatically appear in Google Ads Shared Library
5. Use for remarketing campaigns and Similar Audiences

### Audience Limits

- **Max audiences:** 100 per property (you're well under this)
- **Retroactivity:** Audiences are NOT retroactive—create them ASAP
- **Low traffic warning:** With 900 sessions/month, some audiences may have limited size for ads

---

## 4. Custom Dimensions & Metrics

Currently, your property has **0 custom dimensions** and **0 custom metrics**. For low-traffic sites, focus on high-value custom dimensions only.

### Recommended Custom Dimensions

#### **Priority 1: User-Scoped Dimensions**

**4.1 First Traffic Source (User-Scoped)**
- **Purpose:** Track the very first source that brought a user to your site
- **Use case:** Understand first-touch attribution for app downloads
- **Limit:** 25 user-scoped dimensions available
- **Implementation:**
  1. Set a cookie on first visit with `utm_source` or `source`
  2. Send to GA4 as `first_traffic_source` user property
  3. Register in GA4: Admin → Custom Definitions → Create Custom Dimension
     - Dimension name: `First Traffic Source`
     - Scope: User
     - User property: `first_traffic_source`

**Code Example:**
```javascript
// On page load
if (!localStorage.getItem('first_source')) {
  const params = new URLSearchParams(window.location.search);
  const source = params.get('utm_source') || document.referrer || 'direct';
  localStorage.setItem('first_source', source);
  gtag('set', 'user_properties', {
    first_traffic_source: source
  });
}
```

**4.2 Returning User Status (User-Scoped)**
- **Purpose:** Segment new vs. returning visitors
- **Use case:** Analyze behavior differences
- **Implementation:**
  ```javascript
  const isReturning = localStorage.getItem('visited') ? 'returning' : 'new';
  localStorage.setItem('visited', 'true');
  gtag('set', 'user_properties', {
    user_type: isReturning
  });
  ```
  Register in GA4 as user-scoped dimension: `user_type`

#### **Priority 2: Event-Scoped Dimensions**

**4.3 Link Position/Location (Event-Scoped)**
- **Purpose:** Track where on the page users clicked (already doing this with `event_label`)
- **Note:** You're already capturing this in `event_label` for `app_store_click`
- **Action:** No additional dimension needed—use existing event parameters

**4.4 Content Category (Event-Scoped)**
- **Purpose:** Tag queue guides by ride/park category
- **Use case:** Understand which content types drive conversions
- **Implementation:**
  ```javascript
  gtag('event', 'queue_guide_view', {
    content_category: 'epic_universe',  // or 'universal_studios', 'cedar_point'
    guide_name: 'Battle at the Ministry'
  });
  ```
  Register as event-scoped dimension: `content_category`

### Recommended Custom Metrics

#### **Priority 1: Event-Scoped Metrics**

**4.5 Scroll Percentage (Event-Scoped Metric)**
- **Purpose:** Track exact scroll depth as a numeric value
- **Use case:** Calculate average scroll depth per page
- **Implementation:**
  ```javascript
  gtag('event', 'scroll_depth', {
    scroll_percent: 75,  // Numeric value
    page_path: window.location.pathname
  });
  ```
  Register as custom metric:
  - Metric name: `Scroll Percentage`
  - Scope: Event
  - Event parameter: `scroll_percent`
  - Unit: Standard

**4.6 Engagement Duration (Event-Scoped Metric)**
- **Purpose:** Track time spent on specific sections
- **Use case:** Measure premium section engagement time
- **Implementation:**
  ```javascript
  // When user leaves premium section
  gtag('event', 'section_engagement', {
    section_name: 'premium',
    time_spent_seconds: 45  // Numeric value
  });
  ```
  Register as custom metric: `time_spent_seconds`

### Custom Dimension/Metric Limits

- **Event-scoped dimensions:** 50 max (you have 50 available)
- **User-scoped dimensions:** 25 max (you have 25 available)
- **Event-scoped metrics:** 50 max (you have 50 available)
- **User-scoped metrics:** 25 max (you have 25 available)

**Recommendation:** Start with 2-3 custom dimensions maximum. With low traffic, fewer dimensions = cleaner data.

---

## 5. UTM Parameter Best Practices

### Current Issue

Your App Store links use UTM parameters:
```
https://apps.apple.com/us/app/ride-ready/id6748330847?ch=website&ct=homepage
```

But they use **Apple's campaign attribution format** (`ch`, `ct`) instead of standard UTM parameters. This is fine for Apple attribution but won't show up in GA4.

### UTM Parameter Standards

#### **5.1 UTM Naming Conventions**

**Critical Rules:**
- Always use **lowercase** (GA4 is case-sensitive: `Facebook` ≠ `facebook`)
- Use **hyphens** not underscores (`paid-social`, not `paid_social`)
- Be **consistent** across all campaigns
- Keep parameters **short but descriptive**

#### **5.2 Standard UTM Structure**

```
https://rideready.app/?utm_source=facebook&utm_medium=paid-social&utm_campaign=epic-universe-holiday&utm_content=carousel-ad-1&utm_term=theme-park-app
```

**Parameter Definitions:**
- `utm_source` - Where the traffic came from (facebook, google, newsletter, x, instagram)
- `utm_medium` - Marketing medium (paid-social, organic-social, email, cpc, display, referral)
- `utm_campaign` - Campaign name (epic-universe-holiday, q1-2025, app-launch)
- `utm_content` - Ad variation (carousel-ad-1, video-ad, story-ad) [Optional]
- `utm_term` - Keyword (for paid search) [Optional]

#### **5.3 Recommended UTM Values for Ride Ready**

**Facebook Organic Posts:**
```
utm_source=facebook
utm_medium=organic-social
utm_campaign=epic-universe-strategy-guide
utm_content=link-post
```

**Facebook Paid Ads:**
```
utm_source=facebook
utm_medium=paid-social
utm_campaign=q1-app-downloads
utm_content=carousel-ad-1
```

**Instagram Stories:**
```
utm_source=instagram
utm_medium=organic-social
utm_campaign=queue-guide-series
utm_content=story-link
```

**Email Newsletter:**
```
utm_source=newsletter
utm_medium=email
utm_campaign=weekly-digest
utm_content=app-download-cta
```

**Reddit/Forum Posts:**
```
utm_source=reddit
utm_medium=referral
utm_campaign=theme-park-subreddit
utm_content=comment-link
```

#### **5.4 Facebook Dynamic Parameters**

For Facebook Ads, use **dynamic tokens** that auto-populate:

```
https://rideready.app/?utm_source=facebook&utm_medium=paid-social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{placement}}
```

**Available Tokens:**
- `{{campaign.id}}` - Campaign ID
- `{{campaign.name}}` - Campaign name
- `{{adset.id}}` - Ad set ID
- `{{adset.name}}` - Ad set name
- `{{ad.id}}` - Ad ID
- `{{ad.name}}` - Ad name
- `{{placement}}` - Placement (feed, story, etc.)

**Example:**
```
https://rideready.app/?utm_source=facebook&utm_medium=paid-social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&fbclid={{ad.id}}
```

#### **5.5 Common UTM Mistakes to Avoid**

1. **Inconsistent Capitalization**
   - ❌ `utm_source=Facebook` (one campaign)
   - ❌ `utm_source=facebook` (another campaign)
   - ✅ Always use: `utm_source=facebook`

2. **Wrong Medium for Channel**
   - ❌ `utm_medium=cpc` (for Facebook ads—makes GA think it's paid search)
   - ✅ `utm_medium=paid-social`

3. **Changing UTMs Mid-Campaign**
   - ❌ Editing UTM parameters on a running ad splits data
   - ✅ Create new ad with new UTMs

4. **Forgetting to Tag Boosted Posts**
   - ❌ Boosting a post without adding UTM parameters
   - ✅ Always add URL parameters field when boosting

5. **Relying on fbclid**
   - ❌ Facebook's `fbclid` parameter doesn't populate GA4 campaign reports
   - ✅ Always add UTM parameters manually

#### **5.6 UTM Spreadsheet Template**

Create a Google Sheet to track all UTM links:

| Link Purpose | Source | Medium | Campaign | Content | Full URL |
|-------------|--------|--------|----------|---------|----------|
| Facebook Ad - Epic Universe | facebook | paid-social | epic-universe-q1 | carousel-ad-1 | https://rideready.app/?utm_source=... |
| Instagram Story - Queue Guide | instagram | organic-social | queue-guide-series | story-link | https://rideready.app/?utm_source=... |
| Email Newsletter | newsletter | email | weekly-digest | app-download-cta | https://rideready.app/?utm_source=... |

**Tool:** Use [Google's Campaign URL Builder](https://ga-dev-tools.google/ga4/campaign-url-builder/) to generate links.

#### **5.7 Implementing UTM Tracking on Your Site**

Your site already captures UTM parameters through GA4's automatic tracking. No additional code needed.

**Verification:**
1. Visit: `https://rideready.app/?utm_source=facebook&utm_medium=paid-social&utm_campaign=test`
2. Check GA4 Real-time report
3. Look for "Traffic acquisition" → Source/Medium should show: `facebook / paid-social`

---

## 6. GA4 Explorations & Reports

Standard reports are limited. Use **Explorations** for deeper insights.

### Priority Explorations to Build

#### **6.1 Landing Page Performance Report**

**Purpose:** Understand which pages drive app downloads

**How to Create:**
1. Navigate to **Explore** in GA4
2. Select **Free Form** template
3. Add Dimensions:
   - `Landing page + query string`
   - `Session source/medium`
4. Add Metrics:
   - `Sessions`
   - `Engaged sessions`
   - `Average engagement time`
   - `Key events` (app_store_click)
   - `Key event conversion rate`
5. Drag `Landing page` to Rows
6. Drag metrics to Values
7. Save as "Landing Page to App Download Report"

**What to Look For:**
- Which queue guides have highest app download conversion rate?
- Do Epic Universe pages convert better than other content?
- Are Facebook visitors converting at same rate as Google visitors?

#### **6.2 User Journey (Path Exploration)**

**Purpose:** Visualize the path users take before clicking App Store button

**How to Create:**
1. Go to **Explore** → **Path exploration**
2. Set Starting Point:
   - Node type: `Page path and screen class`
   - Select your homepage `/` or queue guide pages
3. Set Ending Point:
   - Event name: `app_store_click`
4. Add Breakdown: `Session source/medium`
5. Save as "Journey to App Download"

**What to Look For:**
- Do users visit multiple pages before downloading?
- Which content sequence leads to highest conversion?
- Are users bouncing from homepage or exploring guides first?

#### **6.3 Cohort Analysis (User Retention)**

**Purpose:** See if users return after first visit

**How to Create:**
1. Go to **Explore** → **Cohort exploration**
2. Set Cohort inclusion:
   - `First visit` (default)
3. Set Return criteria:
   - `Any event` (to track returns)
4. Set Cohort granularity: `Daily` or `Weekly`
5. Save as "User Retention Analysis"

**What to Look For:**
- What % of users return within 7 days?
- Which traffic sources have highest retention?
- Does content drive repeat visits?

#### **6.4 Funnel Analysis**

**Purpose:** Track drop-off in conversion funnel

**How to Create:**
1. Go to **Explore** → **Funnel exploration**
2. Define Funnel Steps:
   - Step 1: `page_view` (Homepage)
   - Step 2: `queue_guide_view` or `scroll` > 50%
   - Step 3: `premium_section_view`
   - Step 4: `app_store_click`
3. Set "Next step within": `Same session`
4. Add Breakdown: `Session source/medium`
5. Save as "Homepage to App Download Funnel"

**What to Look For:**
- Where are users dropping off?
- What % of users scroll down to Premium section?
- Which traffic sources have best funnel completion?

#### **6.5 Segment Overlap**

**Purpose:** Understand audience overlap (e.g., Facebook visitors who also read queue guides)

**How to Create:**
1. Go to **Explore** → **Segment overlap**
2. Create Segments:
   - Segment 1: `Session source` = `facebook`
   - Segment 2: `Event name` = `queue_guide_view`
   - Segment 3: `Event name` = `app_store_click`
3. Save as "Traffic Source & Content Engagement Overlap"

**What to Look For:**
- Do Facebook visitors engage with queue guides?
- What overlap exists between content readers and app downloaders?

### Quick Report Template Downloads

**Access Prebuilt Templates:**
- GA4 Explore Gallery: **Admin → Property → Template Gallery**
- Import templates directly into your property

---

## 7. Integration Opportunities

### Priority 1: Google Search Console (MUST DO)

**Why:** Your site gets Google Organic traffic—see which keywords drive visits.

**How to Link:**
1. GA4: Admin → Product Links → Search Console Links
2. Click "Link" → Choose Search Console property
3. Select "rideready.app" property
4. Click "Confirm"
5. Wait 24-48 hours for data

**Benefits:**
- See exact search queries that bring users to your site
- Understand which queue guides rank in Google
- Track click-through rate (CTR) from search results
- Identify SEO opportunities

**Reports After Linking:**
- Reports → Acquisition → **Google Organic Search Queries**
- Reports → Acquisition → **Google Organic Search Traffic**

### Priority 2: Google Ads (If Running Ads)

**Why:** Import Key Events to Google Ads for conversion tracking and Smart Bidding.

**How to Link:**
1. GA4: Admin → Product Links → Google Ads Links
2. Click "Link" → Choose Google Ads account
3. Enable "Auto-tagging" (required)
4. Enable "Personalized advertising"
5. Import Key Events:
   - Go to Google Ads → Goals → Summary
   - Click "Import" → Select GA4 Key Events
   - Import: `app_store_click`, `queue_guide_view`, `engaged_session`

**Benefits:**
- Track app download conversions from ads
- Use Smart Bidding (Target CPA, Target ROAS)
- Export audiences for remarketing
- Sync conversion data bidirectionally

### Priority 3: BigQuery (Advanced - Not Recommended Yet)

**Why:** Export raw, unsampled GA4 data for custom analysis.

**When to Use:**
- If you need to analyze data without thresholding limits
- If you want to combine GA4 data with other sources (CRM, app analytics)
- If you need historical data beyond GA4's 14-month limit

**Cost:**
- Free tier: 1TB queries/month, 10GB storage/month
- Your site (~900 sessions/month) = ~100MB/month = **Free**

**How to Link:**
1. GA4: Admin → Product Links → BigQuery Links
2. Enable **"Daily"** export (not streaming—overkill for your traffic)
3. Link to Google Cloud project
4. Wait 24 hours for first export

**Warning:** Requires SQL knowledge to query. Not needed unless you hit thresholding issues frequently.

### Priority 4: Firebase (If Building Native App Features)

**Why:** If you're tracking in-app events for the Ride Ready iOS app, link Firebase to GA4.

**Status:** Your property is already a standard GA4 property (not Firebase-based).

**Action:** If you want to track iOS app installs and in-app events in the same GA4 property:
1. Integrate Firebase SDK into iOS app
2. Link Firebase project to GA4
3. Use same Measurement ID (G-KGYGTPMTQ3)

**Benefit:** Unified web + app analytics in one property.

---

## 8. Content Insights & Optimization

### Current Top Content

Based on your setup, you have strong content assets:
- Epic Universe holiday strategy guide
- Queue time pages (Ministry, Mario Kart, Stardust Racers, etc.)
- Homepage

### How to Measure Content Effectiveness

#### **8.1 Set Up Content Grouping**

**Purpose:** Group queue guides by park/category for easier analysis.

**Implementation:**
1. Use `content_group` event parameter on all page views:
   ```javascript
   gtag('event', 'page_view', {
     content_group: 'Queue Guides',  // or 'Strategy Guides', 'Homepage'
     content_category: 'Epic Universe'  // or 'Universal Studios', 'Cedar Point'
   });
   ```

2. Create custom dimension in GA4:
   - Admin → Custom Definitions → Create Custom Dimension
   - Dimension name: `Content Group`
   - Scope: Event
   - Event parameter: `content_group`

**Analysis:**
- Reports → Engagement → Pages and screens
- Add secondary dimension: `Content Group`
- See which content types drive most engagement

#### **8.2 Track Content → App Download Attribution**

**Goal:** Understand which content leads to app downloads.

**Method 1: Path Exploration (Already Covered)**
- Use Path Exploration to see user journey from queue guide → homepage → app_store_click

**Method 2: Last-Click Content Attribution**
```javascript
// Store last content page visited
if (window.location.pathname.includes('/queue-times/')) {
  localStorage.setItem('last_content', document.title);
}

// On app_store_click, send last content
document.querySelectorAll('[data-app-store-link]').forEach(function(link) {
  link.addEventListener('click', function() {
    gtag('event', 'app_store_click', {
      event_category: 'engagement',
      event_label: link.getAttribute('data-app-store-link'),
      last_content_viewed: localStorage.getItem('last_content') || 'none'
    });
  });
});
```

Then create custom dimension: `last_content_viewed` (event-scoped)

**Analysis:**
- Explorations → Free Form
- Rows: `Last Content Viewed`
- Values: `app_store_click` (Key event)
- See which queue guides lead to most downloads

#### **8.3 Scroll Depth by Content Type**

**Goal:** Understand which content is most engaging.

**Implementation:**
```javascript
gtag('event', 'scroll', {
  percent_scrolled: 90,
  content_type: 'queue_guide',  // or 'strategy_guide', 'homepage'
  page_title: document.title
});
```

**Analysis:**
- Explorations → Free Form
- Rows: `Page title`, `Content type`
- Values: Average `scroll_percent`
- Filter: `scroll_percent` > 0
- See which pages have highest average scroll depth

#### **8.4 Content Engagement Score**

**Create a Calculated Metric:**

In Explorations, create calculated metric:
```
Engagement Score = (Engaged Sessions / Sessions) * 100 + (Key Events / Sessions) * 1000
```

**What It Measures:**
- Combines engagement rate + conversion rate
- Higher score = more valuable content

**Analysis:**
- Free Form Exploration
- Rows: `Landing page`
- Values: `Engagement Score` (calculated), `Sessions`, `Key events`
- Sort by Engagement Score descending
- Top pages = highest quality content

### Content Optimization Workflow

1. **Weekly Review (5 min):**
   - Check "Landing Page Performance Report" (Exploration 6.1)
   - Identify top 3 pages by `app_store_click` conversions
   - Note: Which content drives downloads?

2. **Monthly Deep Dive (30 min):**
   - Run "Journey to App Download" (Path Exploration 6.2)
   - Identify: What content sequence converts best?
   - Action: Cross-link related queue guides to guide users down high-converting paths

3. **Content Gap Analysis:**
   - Check Google Search Console (after linking)
   - Find: Which keywords bring traffic but have low CTR?
   - Action: Create queue guides for high-impression, low-CTR keywords

4. **Promotion Strategy:**
   - Identify: Queue guides with high engagement but low traffic
   - Action: Promote on Facebook/Instagram with UTM-tagged links
   - Measure: `utm_campaign` performance in Traffic Acquisition report

---

## 9. Low-Traffic Optimizations

Your site has ~900 sessions/month. This creates specific challenges in GA4.

### Critical Low-Traffic Fixes

#### **9.1 Fix Reporting Identity (CRITICAL)**

**Problem:** GA4's default "Blended" reporting identity requires 1,000 daily users for 7+ days to work effectively. Your site has ~30 users/day.

**Result:** You're seeing **data thresholding**—GA4 hides data to protect privacy.

**Fix (5 minutes):**
1. Admin → Data Settings → **Reporting Identity**
2. Change from "Blended" to **"Device-Based"**
3. Click "Show all" if Device-Based is hidden
4. Save

**Impact:**
- ✅ Removes most data thresholding
- ✅ Shows more accurate low-volume data
- ✅ Improves report accuracy
- ❌ Loses cross-device tracking (acceptable trade-off for low traffic)

**Verification:**
After changing, check your reports for "(thresholded)" labels—should be fewer/gone.

#### **9.2 Extend Data Retention (CRITICAL)**

**Problem:** GA4 defaults to 2-month data retention. For low-traffic sites, this limits historical analysis.

**Fix (2 minutes):**
1. Admin → Data Settings → **Data Retention**
2. Change from "2 months" to **"14 months"** (maximum)
3. Save

**Impact:**
- ✅ Can analyze historical trends in Explorations
- ✅ Better year-over-year comparisons
- ✅ More data for cohort analysis
- ❌ Standard reports unaffected (always unlimited)

#### **9.3 Disable Google Signals (If Thresholding Persists)**

**Problem:** Google Signals enables cross-device tracking but triggers thresholding on low-traffic sites.

**Trade-off:**
- Keep enabled: Better remarketing audiences, but more thresholding
- Disable: Less thresholding, but lose cross-device insights

**Recommendation:** Try Device-Based reporting first. Only disable Google Signals if thresholding remains severe.

**How to Disable:**
1. Admin → Data Settings → **Data Collection**
2. Toggle OFF: "Google signals data collection"
3. Save

**Warning:** This disables demographics/interests reporting and remarketing audiences.

#### **9.4 Avoid High-Cardinality Custom Dimensions**

**What is High-Cardinality?**
- Dimensions with too many unique values
- Examples: User ID, Timestamp, Full URL with query strings

**Problem:** With low traffic, high-cardinality dimensions trigger "(other)" row in reports.

**Bad Examples (Avoid):**
```javascript
// ❌ DON'T: User ID as dimension (1 unique value per user)
gtag('set', 'user_properties', {
  user_id: '12345'  // Too many unique values
});

// ❌ DON'T: Full page URL with random query params
gtag('event', 'page_view', {
  full_url: window.location.href  // Too many variations
});
```

**Good Examples (Use These):**
```javascript
// ✅ DO: Content category (limited values)
gtag('event', 'page_view', {
  content_group: 'Queue Guides'  // Only 3-4 unique values
});

// ✅ DO: Traffic source (limited values)
gtag('set', 'user_properties', {
  first_source: 'facebook'  // Only 5-10 unique values
});
```

**Rule:** Keep custom dimensions to <20 unique values for low-traffic sites.

#### **9.5 Focus on Ratios, Not Absolutes**

**Problem:** With low session counts, small changes in absolute numbers look dramatic.

**Example:**
- Week 1: 5 app_store_clicks out of 200 sessions = 2.5% conversion rate
- Week 2: 8 app_store_clicks out of 220 sessions = 3.6% conversion rate

**Bad Analysis:** "Conversions increased 60%!" (8/5 - 1)
**Good Analysis:** "Conversion rate improved 1.1 percentage points" (3.6% - 2.5%)

**Use These Metrics:**
- Conversion rate (not absolute conversions)
- Engagement rate (not absolute engaged sessions)
- Bounce rate (not absolute bounces)

#### **9.6 Aggregate Time Periods**

**Problem:** Daily reports are too noisy with low traffic.

**Solution:** Analyze **weekly or monthly** periods instead of daily.

**In Reports:**
- Change date range to "Last 30 days" or "Last 90 days"
- Compare "This month vs. Last month" instead of "Today vs. Yesterday"

**In Explorations:**
- Use "Week" or "Month" granularity
- Avoid "Day" or "Hour" breakdowns

---

## 10. Privacy & Compliance Considerations

### Current Status

Your site:
- ✅ Uses GA4 (privacy-focused compared to Universal Analytics)
- ✅ Doesn't collect PII (personally identifiable information)
- ❌ No visible cookie consent banner (may be required depending on audience location)

### Privacy Best Practices

#### **10.1 Add Cookie Consent (If EU Traffic)**

**Question:** Do you have EU visitors?

- If **Yes:** You need cookie consent under GDPR
- If **No:** Recommended but not legally required

**Simple Implementation (Google Consent Mode v2):**

```html
<!-- Add BEFORE GA4 script -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}

  // Default consent to denied
  gtag('consent', 'default', {
    'analytics_storage': 'denied',
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied'
  });
</script>

<!-- Then your existing GA4 script -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-KGYGTPMTQ3"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-KGYGTPMTQ3');
</script>
```

**When User Accepts Cookies:**
```javascript
gtag('consent', 'update', {
  'analytics_storage': 'granted',
  'ad_storage': 'granted'
});
```

**Free Consent Tools:**
- [Cookiebot](https://www.cookiebot.com/) (free for small sites)
- [Osano](https://www.osano.com/)
- [Cookie Consent by Insites](https://www.cookieconsent.com/)

#### **10.2 Exclude PII from Events**

**Never send to GA4:**
- ❌ Email addresses
- ❌ Names
- ❌ Phone numbers
- ❌ IP addresses (GA4 anonymizes by default)

**Review Your Events:**
Your current implementation is clean—no PII detected.

**Example of BAD Implementation (DON'T DO THIS):**
```javascript
// ❌ DON'T SEND PII
gtag('event', 'park_request_click', {
  user_email: 'user@example.com'  // VIOLATION
});
```

#### **10.3 Update Privacy Policy**

Your privacy policy (`privacy.html`) should mention:
- You use Google Analytics 4
- What data is collected (page views, clicks, device info)
- How users can opt out ([Google Analytics Opt-out Browser Add-on](https://tools.google.com/dlpage/gaoptout))
- Link to [Google's Privacy Policy](https://policies.google.com/privacy)

---

## 11. Quick Win Implementation Checklist

Use this checklist to prioritize implementation.

### Week 1: Critical Foundations (2 hours)

- [ ] **Fix Reporting Identity** (5 min)
  - Admin → Reporting Identity → Change to "Device-Based"

- [ ] **Extend Data Retention** (2 min)
  - Admin → Data Retention → Change to "14 months"

- [ ] **Mark app_store_click as Key Event** (2 min)
  - Admin → Events → Toggle "Mark as key event" for `app_store_click`

- [ ] **Link Google Search Console** (10 min)
  - Admin → Product Links → Search Console → Link

- [ ] **Add Queue Guide Click Tracking** (30 min)
  - Implement `queue_guide_view` event on queue guide links
  - Test in GA4 DebugView

- [ ] **Add Strategy Guide Click Tracking** (15 min)
  - Implement `strategy_guide_click` event on Epic Universe chip link

- [ ] **Create UTM Spreadsheet** (30 min)
  - Document all existing links with UTM parameters
  - Create standards for future campaigns

- [ ] **Create First Audience: App Store Clickers** (5 min)
  - Admin → Audiences → New → Include `app_store_click` event

### Week 2: Enhanced Tracking (3 hours)

- [ ] **Add Premium Section View Tracking** (30 min)
  - Implement Intersection Observer for `premium_section_view` event

- [ ] **Add Social Media Click Tracking** (20 min)
  - Track X and Instagram link clicks

- [ ] **Mark Additional Key Events** (5 min)
  - Mark `queue_guide_view` as Key Event

- [ ] **Create Audiences** (30 min)
  - Queue Guide Readers
  - Engaged Visitors
  - Repeat Visitors

- [ ] **Build Landing Page Performance Exploration** (20 min)
  - Follow instructions in Section 6.1

- [ ] **Build Journey to App Download Path Exploration** (20 min)
  - Follow instructions in Section 6.2

- [ ] **Tag All Facebook Links with UTM Parameters** (30 min)
  - Update all Facebook posts/ads with consistent UTM structure

### Week 3: Advanced Features (2 hours)

- [ ] **Add Scroll Depth Tracking** (45 min via GTM)
  - Requires Google Tag Manager setup
  - Configure 25%, 50%, 75%, 90% triggers

- [ ] **Create Custom Dimension: First Traffic Source** (30 min)
  - Implement localStorage tracking
  - Register dimension in GA4

- [ ] **Build Funnel Exploration** (20 min)
  - Follow instructions in Section 6.4

- [ ] **Set Up Weekly Reporting Routine** (15 min)
  - Bookmark key reports
  - Schedule calendar reminder for weekly review

### Month 2: Optimization & Iteration

- [ ] **Analyze First Month's Data**
  - Which queue guides drive most app downloads?
  - Which traffic sources have highest conversion rate?
  - What's the typical user journey?

- [ ] **Optimize Content Based on Data**
  - Promote high-converting queue guides
  - Improve low-performing pages

- [ ] **Refine UTM Strategy**
  - Review Traffic Acquisition report
  - Fix any inconsistent UTM parameters

- [ ] **Export Audiences to Google Ads** (if running ads)
  - Set up remarketing campaigns

---

## 12. Measurement Plan Summary

### Primary Business Goals

| Goal | Key Metric | How to Track | Target |
|------|-----------|--------------|--------|
| App Downloads | `app_store_click` (Key Event) | Already tracked | Increase by 20% MoM |
| Content Engagement | `queue_guide_view` (Key Event) | Implement Week 1 | 40% of sessions |
| Quality Traffic | Engaged sessions | GA4 default metric | >60% engagement rate |
| Audience Growth | New users | GA4 default metric | Increase by 15% MoM |

### Traffic Source Goals

| Source | Current Share | Key Metric | Target |
|--------|--------------|-----------|--------|
| Facebook | ~35% | Conversion rate | >3% |
| Google Organic | ~30% | CTR from search | >5% |
| Direct | ~25% | Returning users | Decrease share (indicates brand awareness growing) |
| Other | ~10% | New sources | Diversify traffic |

### Content Goals

| Content Type | Key Metric | Target |
|-------------|-----------|--------|
| Queue Guides (Ministry, Mario Kart, etc.) | `queue_guide_view` → `app_store_click` rate | >5% |
| Epic Universe Strategy Guide | Average engagement time | >2 minutes |
| Homepage | Scroll to Premium section | >30% |
| All Pages | Average scroll depth | >60% |

### Event Tracking Hierarchy

```
Pageviews (Automatic)
│
├── Engagement Events (Priority 1)
│   ├── app_store_click ★ KEY EVENT
│   ├── queue_guide_view ★ KEY EVENT
│   ├── strategy_guide_click
│   └── premium_section_view
│
├── Content Interaction (Priority 2)
│   ├── scroll_depth (25%, 50%, 75%, 90%)
│   ├── screenshot_view
│   └── social_click
│
└── Micro-conversions (Priority 3)
    ├── engaged_session (30+ seconds)
    ├── park_request_click
    └── outbound_click
```

---

## 13. Troubleshooting & FAQ

### Q: Why don't I see my custom events in reports yet?

**A:** Events can take 24-48 hours to appear in standard reports. Use **DebugView** for real-time testing:
1. Admin → DebugView
2. Add `?debug_mode=true` to your URL
3. Trigger events
4. See them appear instantly in DebugView

### Q: Why does my data say "(thresholded)"?

**A:** GA4 hides data when:
- Google Signals is enabled AND
- Your site has <50 users in the date range

**Fix:** Change Reporting Identity to "Device-Based" (Section 9.1).

### Q: How do I test my UTM parameters?

**A:** Use **Real-time Report**:
1. Visit your site with UTM parameters: `https://rideready.app/?utm_source=facebook&utm_medium=paid-social&utm_campaign=test`
2. Go to GA4: Reports → Real-time
3. Look at "Traffic source" card
4. Should show: `facebook / paid-social`

### Q: My audiences have 0 users. Why?

**A:** Audiences are **not retroactive**. They only collect users from the moment you create them.
- Wait 24-48 hours after creation
- Check: Admin → Audiences → Click audience name → See user count

### Q: Should I use Google Tag Manager (GTM)?

**A:**
- **No (Current):** Your site is simple—inline GA4 script is fine
- **Yes (Future):** If you want advanced tracking (scroll depth, video plays, form tracking), GTM makes it easier

**When to Upgrade:**
- If you're implementing >5 custom events
- If you need scroll depth tracking
- If multiple people need to manage tracking (GTM has better permissions)

### Q: How often should I check GA4?

**A:**
- **Daily:** Real-time report (2 min) - Check if tracking is working
- **Weekly:** Landing Page Performance report (5 min) - Identify trends
- **Monthly:** Full review of Explorations (30 min) - Deep analysis

### Q: Can I track iOS app installs in this GA4 property?

**A:** Yes, but requires Firebase integration:
1. Add Firebase SDK to your iOS app
2. Link Firebase project to this GA4 property
3. Use same Measurement ID (G-KGYGTPMTQ3)
4. You'll see web + app data in one property

**Benefit:** Unified cross-platform analytics.

---

## 14. Resources & Tools

### Official Documentation

- [GA4 Help Center](https://support.google.com/analytics/answer/10089681)
- [GA4 Event Reference](https://developers.google.com/analytics/devguides/collection/ga4/reference/events)
- [GA4 Dimensions & Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema)

### UTM Tools

- [Google Campaign URL Builder](https://ga-dev-tools.google/ga4/campaign-url-builder/) - Generate UTM links
- [UTM.io](https://utm.io/) - UTM link management (free tier available)

### GA4 Learning Resources

- [Analytics Mania](https://www.analyticsmania.com/post/google-analytics-4-explorations/) - GA4 Explorations guide
- [Measure School YouTube](https://www.youtube.com/c/MeasureSchool) - GA4 tutorials
- [Analytics Mania DebugView Guide](https://www.analyticsmania.com/post/google-tag-assistant-ga4/)

### Testing & Debugging

- **GA4 DebugView** - Admin → DebugView (real-time event testing)
- [Google Tag Assistant](https://tagassistant.google.com/) - Chrome extension for debugging
- [GA4 Event Builder](https://ga-dev-tools.google/ga4/event-builder/) - Test event syntax

### Community & Support

- [GA4 Reddit](https://www.reddit.com/r/GoogleAnalytics/) - Community support
- [Google Analytics Help Community](https://support.google.com/analytics/community) - Official forum
- [Measure Slack](https://www.measure.chat/) - Analytics professionals community

---

## 15. Next Steps

### Immediate Actions (This Week)

1. **Fix Reporting Identity** - Change to Device-Based (5 min)
2. **Extend Data Retention** - Change to 14 months (2 min)
3. **Mark app_store_click as Key Event** (2 min)
4. **Link Google Search Console** (10 min)

### Short-Term (Next 2 Weeks)

1. **Implement queue guide click tracking**
2. **Create UTM parameter spreadsheet**
3. **Build 2-3 key Explorations**
4. **Create remarketing audiences**

### Long-Term (Next 30 Days)

1. **Analyze first month's data**
2. **Optimize content based on insights**
3. **Refine UTM strategy based on performance**
4. **Consider Google Tag Manager for advanced tracking**

### Ongoing Maintenance

- **Weekly:** Review Landing Page Performance (5 min)
- **Monthly:** Deep dive into Explorations (30 min)
- **Quarterly:** Audit custom events and audiences (1 hour)
- **Annually:** Review overall measurement strategy

---

## Sources & References

This document was compiled from the following authoritative sources on GA4 best practices for 2025-2026:

### Event Tracking
- [Track Events with Google Analytics 4 (GA4 event tracking tutorial)](https://www.analyticsmania.com/post/how-to-track-events-with-google-analytics-4-and-google-tag-manager/)
- [Google Analytics 4 Event Tracking Checklist (2025)](https://measureschool.com/google-analytics-4-event-tracking/)
- [GA4 Recommended Events (Ultimate Guide 2025)](https://analytify.io/ga4-recommended-events/)

### Conversion Tracking
- [GA4 Conversion Tracking Setup (2025): Event-Based Guide](https://www.conversios.io/blog/event-based-conversion-tracking-ga4-setup/)
- [Track Key Events with Google Analytics 4 (GA4 Conversions)](https://www.analyticsmania.com/post/track-key-events-with-google-analytics-4/)
- [How to Set Up Key Events (Conversions) in GA4 and Avoid Costly Mistakes](https://www.analyticsmates.com/post/how-to-set-up-key-events-conversions-in-ga4-and-avoid-costly-mistakes)

### Audiences
- [Google Analytics 4 Audiences (GA4 Audiences) - How to use them?](https://www.analyticsmania.com/post/google-analytics-4-audiences/)
- [Google Analytics 4 Audiences (Definitive Guide) 2025](https://measureschool.com/google-analytics-4-audiences/)
- [GA4 Audience Guide | How to Create & Use Audiences in GA4](https://seotesting.com/blog/ga4-audience-guide/)

### UTM Parameters
- [UTM Best Practices: Complete Guide for 2025](https://linkutm.com/blog/utm-best-practices)
- [UTM Parameters for Facebook Ads: The Complete Guide (2025)](https://admanage.ai/blog/utm-parameters-for-facebook-ads)
- [Track Facebook Ads with UTM Parameters in 2025](https://sierrasocialmarketing.com/utm-facebook-ads/)

### Custom Dimensions & Metrics
- [About custom dimensions and metrics - Analytics Help](https://support.google.com/analytics/answer/14240153?hl=en)
- [Google Analytics 4 Custom Metrics Guide (2025)](https://measureschool.com/google-analytics-4-custom-metrics/)
- [A Guide to Custom Dimensions in Google Analytics 4](https://www.analyticsmania.com/post/a-guide-to-custom-dimensions-in-google-analytics-4/)

### Explorations
- [Google Analytics 4 Explorations: a Complete Guide](https://www.analyticsmania.com/post/google-analytics-4-explorations/)
- [How to Use GA4 Path Exploration Report (2025)](https://analytify.io/ga4-path-exploration-report/)
- [How to Create a GA4 Landing Page Report (2025)](https://analytify.io/ga4-landing-page-report/)

### Search Console Integration
- [How to Link Google Search Console to Google Analytics 4 (2025)](https://analytify.io/link-google-search-console-to-google-analytics/)
- [Google Updates Guidance on GA4 & Search Console Integration](https://www.digitalmarketinginc.net/google-updates-guidance-on-ga4-search-console-integration)
- [Complete Google Analytics 4 Guide: Setup, Reports & SEO Tips for 2025](https://almcorp.com/blog/complete-google-analytics-4-guide-2025/)

### App Install Attribution
- [App Install Attribution in Google Analytics 4: What You Need to Know](https://infotrust.com/articles/app-install-attribution-in-google-analytics-4/)
- [Unlocking App Growth: A Guide to Google Analytics Install Tracking](https://upfront-operations.webflow.io/blog/how-to-track-app-installs-in-google-analytics)

### Content Engagement
- [How to Track Scroll Depth in GA4: The Complete Implementation Guide for 2025](https://www.heatmap.com/blog/ga4-scroll-depth)
- [7 Best Website User Engagement Metrics in Google Analytics 4 (GA4)](https://analytify.io/user-engagement-metrics-in-google-analytics-4/)
- [Scroll Depth Tracking in Google Analytics 4: Improve Engagement Insights](https://aokmarketing.com/scroll-depth-tracking-in-google-analytics-4-improve-engagement-insights/)

### Low-Traffic Optimizations
- [The Hidden GA4 Issue for Low-Traffic Websites](https://www.optimizesmart.com/the-hidden-ga4-issue-for-low-traffic-websites/)
- [GA4 Thresholding Solutions for Smaller Websites](https://fscinteractive.com/blog/ga4-thresholding-solutions/)
- [GA4 in 2025: Top Lesser-Known Features to Boost Analytics](https://nucleoanalytics.com/ga4-in-2025-lesser-known-features-you-should-be-using/)

---

**Document Version:** 1.0
**Last Updated:** January 9, 2026
**Author:** Claude Code Research
**For:** Ride Ready (rideready.app)
