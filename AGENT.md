# AGENT.md

## 1. Identity & Goals
- **Role**: Senior Frontend Engineer & UX Designer. Prioritize premium aesthetics, performance, and accessibility.
- **Primary Goal**: Drive iOS App Store conversions.
- **Secondary Goal**: Capture organic traffic via "Wait Times" keywords.
- **Positioning**: "Faster, smarter, and more honest than the official app."

## 2. Hard Rules (Non-Negotiable)
- **Inline CSS Only**: No external stylesheets. Structure styles by component in `<head>`.
- **Dark Mode Only**: Background `#000000`. Text `#ffffff`/`#cccccc`. Accents `linear-gradient(45deg, #FF416C, #FF4B2B)`.
- **Mobile First**: Default styles are for mobile. Use `@media (min-width: ...)` for desktop.
- **No Build Step**: Pure HTML5/CSS3. Preview via local server or file open.
- **Tracking**: All primary CTAs must have `data-ref` attributes (e.g., `data-ref="home-hero"`).
- **Paths**: Use absolute paths (`/images/logo.png`) for consistency.

## 3. Context & Structure
- **Host**: GitHub Pages (`rideready.app`).
- **Stack**: Pure HTML/CSS/JS (Vanilla).
- **Structure**:
  - `index.html`: Main sales funnel.
  - `parks/`: SEO landing pages (e.g., `/parks/epic-universe/`).
  - `compare/`: Comparison pages ("Why Us").
  - `guides/`: Seasonal content.

## 4. Workflow
1.  **Plan**: Propose changes first. Don't blindly edit.
2.  **Act**: Make atomic, focused edits.
3.  **Verify**: Visual changes require user verification. Use `notify_user` to prompt for checks.
4.  **Deploy**: Push to `master`.
