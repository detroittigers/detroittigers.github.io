# UTM Links for Social Media

## Good News: UTM Parameters Are Hidden!

When you share a link on Facebook, Instagram, or Twitter/X, the **preview card only shows the clean domain** (rideready.app). Users don't see the ugly `?utm_source=...` stuff - that's only in the actual URL they click.

**What users see:**
```
rideready.app
Epic Universe Holiday Strategy Guide
Our family saved 5+ hours...
[Preview Image]
```

**What's actually in the link:**
```
https://rideready.app/epic-universe/2025-holiday-strategy/?utm_source=facebook&utm_medium=organic-social&utm_campaign=holiday-guide
```

---

## Ready-to-Use Links

### Homepage

**Facebook Post:**
```
https://rideready.app/?utm_source=facebook&utm_medium=organic-social&utm_campaign=general
```

**Instagram Bio / Link in Bio:**
```
https://rideready.app/?utm_source=instagram&utm_medium=organic-social&utm_campaign=bio-link
```

**X (Twitter) Post:**
```
https://rideready.app/?utm_source=x&utm_medium=organic-social&utm_campaign=general
```

**Reddit Post:**
```
https://rideready.app/?utm_source=reddit&utm_medium=referral&utm_campaign=theme-parks
```

---

### Epic Universe Holiday Strategy Guide

**Facebook Post:**
```
https://rideready.app/epic-universe/2025-holiday-strategy/?utm_source=facebook&utm_medium=organic-social&utm_campaign=holiday-guide
```

**Instagram Story:**
```
https://rideready.app/epic-universe/2025-holiday-strategy/?utm_source=instagram&utm_medium=organic-social&utm_campaign=holiday-guide&utm_content=story
```

**X (Twitter):**
```
https://rideready.app/epic-universe/2025-holiday-strategy/?utm_source=x&utm_medium=organic-social&utm_campaign=holiday-guide
```

**Reddit (r/UniversalOrlando, r/themeparks, etc.):**
```
https://rideready.app/epic-universe/2025-holiday-strategy/?utm_source=reddit&utm_medium=referral&utm_campaign=holiday-guide&utm_content=r-universalorlando
```

---

### Queue Guide Pages

**Ministry Queue Guide - Facebook:**
```
https://rideready.app/universal-orlando/epic-universe/ministry-queue-times/?utm_source=facebook&utm_medium=organic-social&utm_campaign=queue-guides&utm_content=ministry
```

**Mario Kart Queue Guide - Facebook:**
```
https://rideready.app/universal-orlando/epic-universe/mario-kart-queue-times/?utm_source=facebook&utm_medium=organic-social&utm_campaign=queue-guides&utm_content=mario-kart
```

**Stardust Racers Queue Guide - Facebook:**
```
https://rideready.app/universal-orlando/epic-universe/stardust-racers-queue-times/?utm_source=facebook&utm_medium=organic-social&utm_campaign=queue-guides&utm_content=stardust-racers
```

---

## URL Shorteners (Optional)

If you want even cleaner links for places where the full URL is visible (like printed materials), use a URL shortener that preserves UTM parameters:

- **Bitly** (free tier available): bit.ly
- **TinyURL**: tinyurl.com
- **Rebrandly**: rebrandly.com (custom short domains)

Example: `bit.ly/rideready-holiday` could redirect to the full UTM-tagged URL.

---

## UTM Parameter Reference

| Parameter | Purpose | Your Standard Values |
|-----------|---------|---------------------|
| `utm_source` | Where traffic comes from | `facebook`, `instagram`, `x`, `reddit`, `newsletter`, `tiktok` |
| `utm_medium` | Type of marketing channel | `organic-social`, `paid-social`, `referral`, `email` |
| `utm_campaign` | Campaign name | `holiday-guide`, `queue-guides`, `general`, `app-launch` |
| `utm_content` | Differentiates similar links | `story`, `feed-post`, `bio-link`, `ministry`, `mario-kart` |

---

## Pro Tips

1. **Always lowercase** - GA4 is case-sensitive (`Facebook` ≠ `facebook`)

2. **Be consistent** - Use the same source name every time (always `facebook`, never `fb` or `Facebook`)

3. **Track campaigns** - Create a new `utm_campaign` value for each major promotion

4. **Use utm_content for A/B testing** - e.g., `utm_content=version-a` vs `utm_content=version-b`

5. **Test your links** - Visit with UTMs, then check GA4 Real-time report to confirm they show up correctly

---

## Quick Copy Templates

### Facebook Post Template
```
[Your post text here]

https://rideready.app/epic-universe/2025-holiday-strategy/?utm_source=facebook&utm_medium=organic-social&utm_campaign=holiday-guide
```

### Instagram Story Template (via link sticker)
```
https://rideready.app/?utm_source=instagram&utm_medium=organic-social&utm_campaign=general&utm_content=story
```

### Reddit Comment Template
```
[Your comment text here]

Full guide: https://rideready.app/epic-universe/2025-holiday-strategy/?utm_source=reddit&utm_medium=referral&utm_campaign=holiday-guide&utm_content=comment
```
