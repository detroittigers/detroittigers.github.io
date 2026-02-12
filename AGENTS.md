# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static marketing website for **Ride Ready**, an iOS app that provides real-time theme park wait times, drop alerts, and "what to ride next" recommendations. The site is hosted on GitHub Pages at rideready.app.

## Development

This is a pure static HTML/CSS site with no build process. To preview changes:
- Open HTML files directly in a browser, or
- Use any local server (e.g., `python3 -m http.server 8000`)

## Key Conventions

- **Styling**: All CSS is inlined within `<style>` tags in each HTML file (no external stylesheets)
- **Analytics**: Google Analytics (G-KGYGTPMTQ3) is included on all pages
- **Design system**: Dark theme with coral/orange gradient accent colors (#FF416C, #FF4B2B), 45deg gradient angle
- **App Store links**: Include `?ct=` UTM parameters and `data-ref` attributes for tracking
- **Accessibility**: Includes focus-visible states, reduced motion support, aria labels, and 44px minimum tap targets

## GitHub

- Always use the `detroittigers` GitHub account for this repo (`gh auth switch --user detroittigers` before pushing or creating PRs)

## Deployment

Push to `master` branch to deploy via GitHub Pages. No build step required.
