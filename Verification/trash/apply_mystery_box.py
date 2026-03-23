import re

file_path = "/Users/bhavikamaloo/Desktop/Portfolio-case study/Verification/index-framer.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new CSS overrides for the Mystery Box aesthetic
mystery_box_styles = """
      /* ==========================================================
         MYSTERY BOX AESTHETIC OVERRIDES (bikiron.in/mysterybox)
         ========================================================== */
      
      /* Base Typography & Spacing */
      html, body {
        font-family: 'DM Sans', sans-serif;
      }
      .page-wrapper {
        gap: 160px !important;
      }
      .page-wrapper > section:not(#hero) {
        gap: 160px !important;
      }
      
      /* Global Body Text Upgrade */
      .cs-constraint-desc,
      .cs-industry-lede,
      .ch-i-text,
      .ch-sol-desc,
      .cs-meta-value,
      .sol-section-desc,
      .sol-step-desc,
      .cs-phase-body,
      p {
        font-size: 18px !important;
        line-height: 1.6 !important;
        font-weight: 400 !important;
      }

      /* Section Headings */
      .sol-section-title,
      .cs-industry-h2,
      .cs-why-title,
      .cs-hero-title,
      .sol-hero-title {
        font-size: 48px !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
        line-height: 1.1 !important;
      }

      /* Card Titles */
      .cs-constraint-title,
      .ch-i-title,
      .cs-goal-title,
      .cs-phase-title,
      .sol-step-title {
        font-size: 24px !important;
        font-weight: 600 !important;
        line-height: 1.2 !important;
      }

      /* Eyebrows, Labels, Numbers */
      .cs-industry-eyebrow,
      .sol-section-num,
      .cs-meta-label,
      .cs-goal-eyebrow {
        font-size: 13px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.2em !important;
        color: #6B7280 !important;
        font-weight: 500 !important;
        margin-bottom: 8px;
        opacity: 1 !important; /* fixing ghost numbers if any remain */
      }

      /* Cards & Surfaces (Massive border radius & soft shadows) */
      .cs-constraint-card,
      .cs-meta,
      .ch-i-card,
      .cs-goal-card,
      .cs-phase-card,
      .sol-ps-card,
      .cs-why-matters,
      .cs-future-callout {
        border-radius: 48px !important;
        padding: 48px !important;
        box-shadow: 0 24px 48px rgba(0,0,0,0.03) !important;
        border: 1px solid rgba(0,0,0,0.04) !important;
        background: #FFFFFF;
      }
      
      /* Remove inner padding if we just blasted padding recursively on flex wrappers */
      .cs-constraint-body, .cs-constraint-top, .cs-constraint-footer {
        padding-left: 0 !important;
        padding-right: 0 !important;
      }
      .cs-constraint-card {
        padding: 40px !important;
      }
      .cs-constraint-footer {
        border-top: 1px solid rgba(0,0,0,0.04) !important;
        margin-top: 24px !important;
        padding-top: 24px !important;
        background: transparent !important;
      }

      /* Tags & Pills */
      .cs-tag-pill,
      .cs-proof-pill,
      .sol-tag,
      .ch-i-flag,
      .cs-phase-badge {
        border-radius: 100px !important;
        padding: 8px 16px !important;
        font-size: 12px !important;
        font-weight: 600 !important;
      }

      /* Context bar matching the aesthetic */
      .cs-context-bar {
        border-radius: 32px !important;
        padding: 32px 48px !important;
        box-shadow: 0 24px 48px rgba(0,0,0,0.02) !important;
        border: 1px solid rgba(0,0,0,0.04) !important;
      }
      .cs-context-num {
        font-size: 32px !important;
      }

      /* Mobile Adjustments */
      @media (max-width: 768px) {
        .page-wrapper { gap: 120px !important; }
        .page-wrapper > section:not(#hero) { gap: 120px !important; }
        
        .cs-constraint-card,
        .cs-meta,
        .ch-i-card,
        .cs-goal-card,
        .cs-phase-card,
        .sol-ps-card,
        .cs-why-matters,
        .cs-future-callout {
          border-radius: 32px !important;
          padding: 32px !important;
        }

        .sol-section-title,
        .cs-industry-h2,
        .cs-why-title,
        .cs-hero-title,
        .sol-hero-title {
          font-size: 36px !important;
        }
      }
"""

if "MYSTERY BOX AESTHETIC OVERRIDES" not in content:
    content = content.replace("</style>", mystery_box_styles + "\n</style>")
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Injected Mystery Box aesthetic CSS overrides.")
else:
    print("CSS overrides already exist.")
