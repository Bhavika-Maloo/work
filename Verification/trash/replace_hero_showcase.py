import re

file_path = "/Users/bhavikamaloo/Desktop/Portfolio-case study/Verification/index-framer.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Hero Section
hero_start = '<section id="hero"'
hero_end = '<!-- ============================================================\n           SECTION 2 — Project Meta'

hero_match = re.search(f'({hero_start}[\s\S]*?){hero_end}', content)
if hero_match:
    old_hero = hero_match.group(1)
    new_hero = """<section id="hero" class="cs-new-hero" aria-label="KYC Redesign Case Study">
        <h1 class="cs-hero-title">Verification<br/>Revamp</h1>
        
        <div class="cs-hero-icon-container">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="cs-hero-icon" aria-hidden="true">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
            <path d="M12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"></path>
            <path d="M10 16v-1a2 2 0 0 1 4 0v1"></path>
          </svg>
        </div>

        <div class="cs-hero-logo">
          Dream11
        </div>

        <p class="cs-hero-subtitle">
          Redesigning verification for 200M+ users at Dream11<br/>
          Transforming fragmented KYC touch points into a unified, compliant experience.
        </p>

        <ul class="cs-hero-tags" aria-label="Key attributes">
          <li>secure</li>
          <li>compliant</li>
          <li>frictionless</li>
        </ul>
      </section>

      """
    content = content.replace(old_hero, new_hero)
else:
    print("Could not find hero boundaries!")

# 2. Replace Showcase Section
showcase_start = '<section id="showcase"'
showcase_end = '<!-- ============================================================\n           SECTION 04 — Key Contributions'

showcase_match = re.search(f'({showcase_start}[\s\S]*?){showcase_end}', content)
if showcase_match:
    old_showcase = showcase_match.group(1)
    new_showcase = """<section id="showcase">
        <div class="cs-prototype-container">
          <!-- Placeholder for working prototype -->
          <div class="cs-prototype-placeholder">
            <span class="cs-prototype-text">Drop your Figma / Framer prototype here</span>
          </div>
        </div>
      </section>

      """
    content = content.replace(old_showcase, new_showcase)
else:
    print("Could not find showcase boundaries!")

# 3. Inject CSS overrides for the new Hero & Showcase
new_css = """
      /* ----------------------------------------------------
         HERO & SHOWCASE AESTHETICS (Purple Gradient Mockups)
         ---------------------------------------------------- */
      .cs-new-hero {
        background: linear-gradient(180deg, #A48BBE 0%, #403250 100%);
        border-radius: 48px;
        padding: 80px 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        color: #FFFFFF;
        box-shadow: 0 40px 80px rgba(0,0,0,0.1);
      }
      .cs-hero-title {
        font-family: 'Editorial New', 'DM Sans', serif; /* Or matching font */
        font-size: 64px !important;
        font-weight: 500 !important;
        letter-spacing: -0.02em !important;
        line-height: 1.1 !important;
        margin-bottom: 48px;
        text-shadow: 0 4px 20px rgba(0,0,0,0.2);
      }
      .cs-hero-icon-container {
        background: linear-gradient(135deg, #E6E1F0, #A48BBE);
        border: 4px solid rgba(255,255,255,0.2);
        border-radius: 24px;
        padding: 24px;
        margin-bottom: 48px;
        box-shadow: 0 16px 32px rgba(0,0,0,0.3);
      }
      .cs-hero-icon {
        color: #302640;
        transform: scale(1.5);
      }
      .cs-hero-logo {
        font-size: 36px;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-bottom: 24px;
        color: #FFFFFF;
      }
      .cs-hero-subtitle {
        font-size: 18px !important;
        line-height: 1.6 !important;
        font-weight: 400 !important;
        color: rgba(255,255,255,0.85) !important;
        max-width: 800px;
        margin-bottom: 40px;
      }
      .cs-hero-tags {
        display: flex;
        gap: 16px;
        list-style: none;
        padding: 0;
      }
      .cs-hero-tags li {
        background: #F0EEFF;
        color: #6B21A8;
        padding: 8px 24px;
        border-radius: 100px;
        font-size: 14px;
        font-weight: 600;
        text-transform: lowercase;
        letter-spacing: 0.02em;
      }

      /* Showcase / Prototype Holder */
      .cs-prototype-container {
        /* User asked to "remove the background and keep a placeholder image" */
        background: transparent;
        border: 2px dashed rgba(0,0,0,0.1);
        border-radius: 48px;
        padding: 24px;
        min-height: 600px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
      }
      .cs-prototype-placeholder {
        background: #F8F9FA;
        border-radius: 32px;
        width: 100%;
        height: 100%;
        min-height: 600px;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .cs-prototype-text {
        font-size: 16px;
        color: var(--Color-neutral-text_3);
        font-weight: 500;
      }

      /* Clean out old .page-wrapper top padding if any to fit the new massive hero */
      .page-wrapper {
        padding-top: 40px !important;
      }
"""

if "HERO & SHOWCASE AESTHETICS" not in content:
    content = content.replace("</style>", new_css + "\n</style>")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero and Showcase replacement complete.")
