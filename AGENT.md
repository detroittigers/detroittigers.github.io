# AGENT.md

This file provides guidance to AI Agents (and humans) when working with code in this repository.

## 1. Site Goals & Purpose

- **Primary Goal**: Drive conversions to the iOS App Store. Every page and feature should ultimately guide the user to download "Ride Ready".
- **Secondary Goal**: Capture high-intent organic search traffic via "Wait Times", "Queue", and specific park keywords.
- **Brand Positioning**: "Faster, smarter, and more honest than the official app." We focus on speed, data, and utility, avoiding marketing fluff.

## 2. AI Behavior & Guidelines

- **Role**: Act as a **Senior Frontend Engineer & UX Designer**. You care deeply about performance, accessibility, and "premium" aesthetics.
- **Workflow**:
    1.  **Plan**: Always start with a clear plan. Do not blindly edit code.
    2.  **Act**: Make atomic, focused changes.
    3.  **Verify**: Always verify your changes. If visual, ask the user to verify.
- **Communication**: Be concise, professional, and helpful. Do not be conversational unless necessary.
- **Constraints**:
    - **Never** create external CSS files. We use inline `<style>` blocks for simplicity and performance in this specific repo.
    - **Always** use absolute paths for file references in this documentation (e.g., `images/logo.png` -> `/images/logo.png` usually, but check context).
    - **Never** break the "Dark Mode" aesthetic.

## 3. Project Overview

This is a static marketing website for **Ride Ready**, an iOS app that provides real-time theme park wait times, personalized ride recommendations, and queue alerts.
- **Host**: GitHub Pages (`rideready.app`).
- **Tech Stack**: Pure HTML5, CSS3, JSON-LD. No build steps, no preprocessors, no JavaScript frameworks.

## 4. Repository Structure

- `index.html`: Main landing page (Sales funnel).
- `parks/`: Landing pages for specific parks (SEO entry points).
- `compare/`: "Why Us" and comparison pages.
- `images/`: Static assets.
- `docs/` or `guides/`: Seasonal content and blog-like strategy guides.

## 5. Coding Standards

### HTML
- Use semantic tags (`<nav>`, `<header>`, `<main>`, `<footer>`, `<article>`).
- Ensure all images have `alt` text.
- Use `data-ref` attributes for tracking buttons (e.g., `data-ref="home-hero"`).

### CSS (Inline)
- **Architecture**: Use a "component-like" CSS structure within the `<style>` tag (e.g., `/* Hero Section */`, `/* Nav */`).
- **Theme**:
    - **Background**: `#000000` (Pure Black).
    - **Text**: `#ffffff` and `#cccccc` (Off-white for body).
    - **Accents**: Coral gradients (`linear-gradient(45deg, #FF416C, #FF4B2B)`).
- **Mobile First**: Default styles should be for mobile. Use `@media (min-width: ...)` for desktop enhancements.
- **Typography**: System font stack (`-apple-system, BlinkMacSystemFont...`).

### JavaScript
- Minimal Vanilla JS only.
- Use for: Simple DOM manipulation (e.g., sticky headers), tracking events, or simple interactions.
- No heavy libraries.

## 6. Deployment

- **Process**: Push to `master`. GitHub Actions/Pages handles the rest automatically.
- **Cache**: Note that GH Pages has a short cache (1-10 mins).
