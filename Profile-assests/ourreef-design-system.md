# OurReef Design System
## Style Guide for AI-Assisted HTML Rebuilding

Use this document to rebuild any HTML file in the OurReef visual style. Apply every rule here faithfully — this is a complete design specification.

---

## 1. Design Aesthetic

**Tone:** Clean editorial minimalism with a warm, nature-inspired personality. The design is confident and spacious — like a well-crafted science magazine. White space is generous and intentional. The underwater/coral theme is expressed through illustration and color, never through busy decoration.

**Feel:** Calm, trustworthy, slightly playful. Academic enough to feel credible; approachable enough for children's education.

---

## 2. Color Palette

```css
:root {
  /* Primary backgrounds */
  --color-bg-white: #FFFFFF;
  --color-bg-light: #F5F5F5;      /* Light gray sections, callout boxes */

  /* Underwater hero gradient (top to bottom) */
  --color-ocean-deep: #2B5AA0;    /* Deep blue top */
  --color-ocean-mid: #4A9FD4;     /* Mid ocean blue */
  --color-ocean-light: #7EC8E3;   /* Lighter blue-teal */
  --color-ocean-surface: #A8DCF0; /* Near-surface pale blue */

  /* Coral/accent */
  --color-coral: #F4927A;         /* Salmon-coral pink — illustrations, accents */
  --color-coral-light: #F9B5A0;

  /* Text */
  --color-text-primary: #1A1A1A;  /* Near-black for headings */
  --color-text-body: #2D2D2D;     /* Dark gray for body copy */
  --color-text-secondary: #888888;/* Labels, captions, metadata */
  --color-text-muted: #AAAAAA;    /* De-emphasized text */

  /* Accent / Interactive */
  --color-accent-blue: #3B82F6;   /* Icon strokes, links, bold highlights */
  --color-accent-blue-light: #DBEAFE; /* Light blue icon backgrounds */

  /* Dark sections (data viz, diagrams) */
  --color-dark-bg: #111111;       /* Near-black for diagram panels */
  --color-dark-surface: #1E1E1E;
  --color-dark-card: #2A2A2A;
  --color-highlight-red: #EF4444; /* Error/wrong state in diagrams */
  --color-highlight-blue-outline: #3B82F6; /* Correct state outline */

  /* Dividers */
  --color-divider: #E5E5E5;
}
```

---

## 3. Typography

### Font Families
```css
/* Import these from Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* 
  DISPLAY / HEADINGS: "Sora" — geometric, friendly, modern
  BODY: "Sora" — same family at lighter weights for cohesion
  MONO / DIAGRAMS: "IBM Plex Mono" — used inside dark diagram/data panels
*/

:root {
  --font-display: 'Sora', sans-serif;
  --font-body: 'Sora', sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;
}
```

### Type Scale
```css
/* Hero title (large page title in white on hero image) */
.text-hero {
  font-family: var(--font-display);
  font-size: clamp(56px, 8vw, 96px);
  font-weight: 700;
  color: #FFFFFF;
  letter-spacing: -0.02em;
  line-height: 1.05;
}

/* Section headline */
.text-headline {
  font-family: var(--font-display);
  font-size: clamp(32px, 4vw, 48px);
  font-weight: 700;
  color: var(--color-text-primary);
  letter-spacing: -0.02em;
  line-height: 1.2;
}

/* Sub-headline / section statement */
.text-subheadline {
  font-family: var(--font-display);
  font-size: clamp(22px, 3vw, 32px);
  font-weight: 600;
  color: var(--color-text-primary);
  letter-spacing: -0.01em;
  line-height: 1.3;
}

/* Body copy */
.text-body {
  font-family: var(--font-body);
  font-size: 16px;
  font-weight: 400;
  color: var(--color-text-body);
  line-height: 1.7;
}

/* Eyebrow / label (small all-caps or small regular above a headline) */
.text-eyebrow {
  font-family: var(--font-body);
  font-size: 13px;
  font-weight: 400;
  color: var(--color-text-secondary);
  letter-spacing: 0.01em;
}

/* Caption */
.text-caption {
  font-family: var(--font-body);
  font-size: 12px;
  font-weight: 400;
  color: var(--color-text-muted);
  text-align: center;
}

/* Metadata label (Roles, Timeline, Tools) */
.text-meta-label {
  font-family: var(--font-body);
  font-size: 12px;
  font-weight: 400;
  color: var(--color-text-secondary);
  margin-bottom: 4px;
}

/* Metadata value */
.text-meta-value {
  font-family: var(--font-body);
  font-size: 15px;
  font-weight: 400;
  color: var(--color-text-body);
  line-height: 1.6;
}

/* Inline bold emphasis (used within body copy for key terms) */
strong, .text-emphasis {
  font-weight: 700;
  color: var(--color-text-primary);
}

/* Mono text inside dark panels */
.text-mono {
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 400;
  color: #CCCCCC;
}
```

---

## 4. Layout & Spacing

### Grid
```css
/* All content is centered in a max-width container */
.container {
  max-width: 1040px;
  margin: 0 auto;
  padding: 0 48px;
}

/* Narrow text container (for prose sections) */
.container-text {
  max-width: 680px;
  margin: 0 auto;
  padding: 0 48px;
}
```

### Section Spacing
```css
/* Between major sections */
--spacing-section: 96px;

/* Between subsections within a section */
--spacing-block: 64px;

/* Between a label and its content */
--spacing-label-gap: 12px;

/* Standard paragraph gap */
--spacing-para: 20px;
```

### Two-Column Layout (Research/Design sections)
```css
/* Left: statement/question | Right: explanation/content */
.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: start;
}

/* Slightly unequal split variant (image | text) */
.two-col-media {
  display: grid;
  grid-template-columns: 45% 55%;
  gap: 48px;
  align-items: start;
}
```

### Metadata Row (Project info strip)
```css
/* Horizontal row with 5 columns: Roles | Timeline | Type | Teammates | Tools */
.meta-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 24px;
  padding: 40px 0;
  border-top: 1px solid var(--color-divider);
}
```

---

## 5. Navigation Bar

```css
/* Fixed or sticky pill-shaped navbar, centered at top */
.navbar {
  position: fixed;
  top: 16px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 0;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(12px);
  border-radius: 999px;
  padding: 8px 24px 8px 8px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.10);
  z-index: 1000;
}

/* Home icon button (square-ish, slightly rounded) */
.navbar-home {
  width: 36px;
  height: 36px;
  background: #F0F0F0;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 16px;
  color: #555555;
}

/* Nav divider */
.navbar::before-divider {
  width: 1px;
  height: 20px;
  background: var(--color-divider);
  margin-right: 16px;
}

/* Nav links */
.navbar a {
  font-family: var(--font-body);
  font-size: 14px;
  font-weight: 400;
  color: var(--color-text-body);
  text-decoration: none;
  padding: 6px 14px;
  border-radius: 999px;
  transition: background 0.2s;
}

.navbar a:hover {
  background: #F0F0F0;
}
```

---

## 6. Hero Section

```css
.hero {
  width: 100%;
  height: 100vh; /* or min 600px */
  background: linear-gradient(
    180deg,
    var(--color-ocean-deep) 0%,
    var(--color-ocean-mid) 50%,
    var(--color-ocean-light) 85%,
    #FFFFFF 100%
  );
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

/* The white curved section break at the bottom of the hero */
.hero-curve {
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 100%;
  height: 120px;
  background: #FFFFFF;
  border-radius: 50% 50% 0 0 / 80px 80px 0 0;
}

/* Geometric rock shapes in hero — flat polygon shapes in layered blues */
/* Rendered as SVG or CSS clip-path polygons in varying shades of blue */
.hero-rocks {
  position: absolute;
  bottom: 100px;
  width: 100%;
  /* Colors: #4A7FBF, #5B9FD4, #72B5E0 — staggered layers */
}

/* Floating glowing orbs (subtle radial blur spots) */
.hero-glow {
  position: absolute;
  width: 80px;
  height: 80px;
  background: radial-gradient(circle, rgba(255,255,255,0.5) 0%, transparent 70%);
  border-radius: 50%;
  filter: blur(12px);
}
```

---

## 7. Section Divider (labeled)

```css
/* "Research", "Ideation" etc. — centered label with horizontal rules either side */
.section-divider {
  display: flex;
  align-items: center;
  gap: 24px;
  margin: 80px 0 48px;
}

.section-divider hr {
  flex: 1;
  border: none;
  border-top: 1px solid var(--color-divider);
}

.section-divider span {
  font-family: var(--font-body);
  font-size: 14px;
  font-weight: 400;
  color: var(--color-text-secondary);
  white-space: nowrap;
}
```

---

## 8. Cards & Callout Boxes

### HMW (How Might We) Callout
```css
/* Large centered callout box with light gray background */
.callout-hmw {
  background: #F5F5F5;
  border-radius: 12px;
  padding: 48px 64px;
  text-align: center;
}

.callout-hmw .label {
  font-size: 13px;
  color: var(--color-text-secondary);
  margin-bottom: 16px;
}

.callout-hmw .statement {
  font-size: clamp(20px, 2.5vw, 26px);
  font-weight: 600;
  color: var(--color-text-primary);
  line-height: 1.4;
}
```

### Feature / Reason Cards (icon + text)
```css
/* White cards with thin border, rounded corners, horizontal icon+text layout */
.feature-card {
  border: 1px solid var(--color-divider);
  border-radius: 10px;
  padding: 16px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 12px;
}

.feature-card .icon-wrap {
  width: 40px;
  height: 40px;
  background: var(--color-accent-blue-light);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.feature-card .icon-wrap svg {
  color: var(--color-accent-blue);
  width: 20px;
  height: 20px;
}

.feature-card .card-text {
  font-size: 15px;
  color: var(--color-text-body);
  line-height: 1.4;
}
```

### Dark Diagram Panel
```css
/* Dark background panel used for data flow visualizations */
.diagram-panel {
  background: var(--color-dark-bg);
  border-radius: 16px;
  padding: 48px;
  width: 100%;
  color: #FFFFFF;
  font-family: var(--font-mono);
}
```

---

## 9. Images

```css
/* Inline editorial images (research section, etc.) */
.editorial-image {
  width: 100%;
  border-radius: 8px;
  object-fit: cover;
  display: block;
}

/* Full-bleed image in a bordered container */
.image-container {
  border-radius: 16px;
  overflow: hidden;
  width: 100%;
}

/* App mockup image */
.mockup-container {
  background: #000000;
  border-radius: 16px;
  padding: 24px;
  display: flex;
  gap: 16px;
}
```

---

## 10. Result / Outcome Section

```css
/* Light gray card with centered content — used for "We won first place!" */
.result-card {
  background: #F5F5F5;
  border-radius: 16px;
  padding: 64px 48px;
  text-align: center;
}

.result-card h2 {
  font-size: clamp(28px, 4vw, 40px);
  font-weight: 700;
  color: var(--color-text-primary);
  margin-bottom: 20px;
}

.result-card p {
  font-size: 16px;
  color: var(--color-text-secondary);
  line-height: 1.7;
  max-width: 560px;
  margin: 0 auto;
}
```

---

## 11. Toggle / Interactive Controls

```css
/* "Show Discovery" pill toggle */
.toggle-row {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  margin-bottom: 16px;
}

.toggle-label {
  font-size: 13px;
  color: var(--color-text-secondary);
}

.toggle-switch {
  width: 44px;
  height: 24px;
  background: #DDDDDD;
  border-radius: 999px;
  position: relative;
  cursor: pointer;
  transition: background 0.2s;
}

.toggle-switch.active {
  background: var(--color-accent-blue);
}

.toggle-switch .knob {
  width: 18px;
  height: 18px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 3px;
  left: 3px;
  transition: transform 0.2s;
  box-shadow: 0 1px 4px rgba(0,0,0,0.2);
}

.toggle-switch.active .knob {
  transform: translateX(20px);
}
```

---

## 12. Scroll Indicator

```css
/* Small rounded pill / line at bottom-center of each section */
.scroll-indicator {
  width: 36px;
  height: 4px;
  background: #CCCCCC;
  border-radius: 999px;
  margin: 48px auto 0;
}
```

---

## 13. Global Defaults

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-body);
  background: var(--color-bg-white);
  color: var(--color-text-body);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

/* Section wrapper */
section {
  padding: 80px 0;
}

/* Horizontal rule */
hr {
  border: none;
  border-top: 1px solid var(--color-divider);
}

/* Links */
a {
  color: var(--color-accent-blue);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
```

---

## 14. Page Structure Template

When rebuilding any HTML file in this style, use this section order and structure:

```html
<body>

  <!-- 1. Fixed pill navbar -->
  <nav class="navbar">
    <div class="navbar-home">🏠</div>
    <!-- vertical divider -->
    <a href="#overview">Overview</a>
    <a href="#research">Research</a>
    <a href="#ideation">Ideation</a>
    <a href="#design">Design</a>
    <a href="#results">Results</a>
  </nav>

  <!-- 2. Full-screen hero with ocean gradient + title -->
  <section class="hero">
    <!-- SVG rock shapes, glowing orbs, coral illustrations -->
    <h1 class="text-hero">Page Title</h1>
    <div class="hero-curve"></div>
  </section>

  <!-- 3. Overview section (white bg) -->
  <section id="overview">
    <div class="container">
      <p class="text-eyebrow">Project Name</p>
      <h2 class="text-headline">Tagline headline here.</h2>
      <br/>
      <h3>Overview</h3>
      <p class="text-body">Description paragraph...</p>
      <!-- Meta row: Roles | Timeline | Type | Teammates | Tools -->
      <div class="meta-row">...</div>
      <!-- App mockup image -->
    </div>
  </section>

  <!-- 4. Labeled section divider -->
  <div class="section-divider container">
    <hr/><span>Research</span><hr/>
  </div>

  <!-- 5. Research / Content sections -->
  <section id="research">
    <div class="container">
      <!-- Two-column layout: image | headline+body -->
      <!-- HMW callout box -->
      <!-- Feature cards -->
      <!-- Dark diagram panel -->
    </div>
  </section>

  <!-- 6. Results section -->
  <section id="results">
    <div class="container">
      <div class="result-card">
        <img .../>
        <h2>We won first place!</h2>
        <p>Reflection text...</p>
      </div>
    </div>
  </section>

  <!-- 7. Scroll indicator -->
  <div class="scroll-indicator"></div>

</body>
```

---

## 15. Illustration Style Notes

- **Coral creatures**: Simple flat rounded blobs in `#F4927A` coral pink with two small dark oval eyes. No outlines. Used as mascots/decorations.
- **Rock formations**: Flat polygon shapes (CSS `clip-path` or inline SVG) in layered blues — `#4A7FBF`, `#5B9FD4`, `#7EC8E3` — stacked to create underwater depth.
- **Glow spots**: Soft `radial-gradient` white blobs with heavy `filter: blur()` to simulate underwater light rays.
- **Icons**: Thin 2px stroke style, `var(--color-accent-blue)` color, on `var(--color-accent-blue-light)` rounded square backgrounds.

---

## 16. Responsive Breakpoints

```css
/* Tablet */
@media (max-width: 768px) {
  .two-col, .two-col-media {
    grid-template-columns: 1fr;
  }
  .meta-row {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
  .container {
    padding: 0 24px;
  }
}

/* Mobile */
@media (max-width: 480px) {
  .navbar {
    display: none; /* or collapse to hamburger */
  }
  .meta-row {
    grid-template-columns: 1fr;
  }
  .callout-hmw {
    padding: 32px 24px;
  }
}
```

---

*End of OurReef Design System. Provide this entire document to your AI agent along with your original HTML file and instruct it to restyle every element using these tokens, components, and layout patterns.*
