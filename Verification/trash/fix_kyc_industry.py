import re

file_path = "/Users/bhavikamaloo/Desktop/Portfolio-case study/Verification/index-framer.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- CSS REPLACEMENT ---
new_css = """      /* =============================================
         Section 08 — Industry (Redesigned)
         ============================================= */
      .cs-industry-section {
        display: flex;
        flex-direction: column;
        width: 100%;
        padding: 40px 0;
      }
      .cs-industry-heading {
        margin-bottom: 32px;
        display: flex;
        flex-direction: column;
        gap: 12px;
      }
      .cs-industry-eyebrow {
        font-size: 11px;
        font-weight: 500;
        color: var(--Color-neutral-text_8, #7D8BA2);
        text-transform: uppercase;
        letter-spacing: 0.12em;
      }
      .cs-industry-h2 {
        font-size: 26px;
        font-weight: 500;
        color: var(--Color-neutral-text_7);
        letter-spacing: -0.01em;
        line-height: 1.2;
      }
      .cs-industry-lede {
        font-size: 14px;
        color: var(--Color-neutral-text_5);
        line-height: 1.5;
      }
      /* Zone A: Context Bar */
      .cs-context-bar-wrapper {
        margin-bottom: 32px;
      }
      .cs-context-bar {
        background: var(--Color-neutral-bg_3, #F0F3F7);
        border-radius: 16px;
        padding: 16px 24px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        margin-bottom: 8px;
      }
      .cs-context-cell {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
        padding-right: 20px;
        padding-left: 20px;
        border-right: 0.5px solid var(--Color-neutral-border_4, #CFD5DE);
      }
      .cs-context-cell:first-child { padding-left: 0; }
      .cs-context-cell:last-child {
        border-right: none;
        padding-right: 0;
      }
      .cs-context-num {
        font-size: 24px;
        font-weight: 500;
        color: var(--Color-neutral-text_7);
        line-height: 1.1;
      }
      .cs-context-lbl {
        font-size: 12px;
        color: var(--Color-neutral-text_5);
        line-height: 1.3;
      }
      .cs-context-caption {
        font-size: 13px;
        color: var(--Color-neutral-text_5);
        line-height: 1.5;
        padding: 0 4px;
      }
      /* Zone B: Constraints */
      .cs-constraint-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 100%;
      }
      .cs-constraint-card {
        background: #FFFFFF;
        border: 1px solid var(--Color-neutral-border_3, #DFE3E8);
        border-radius: 16px;
        overflow: hidden;
        display: flex;
        flex-direction: column;
      }
      .cs-constraint-card.accent-coral {
        border-left: 2px solid #D85A30;
      }
      .cs-constraint-top {
        padding: 10px 16px 0;
      }
      .cs-constraint-body {
        padding: 12px 16px 16px;
        display: flex;
        flex-direction: column;
        gap: 6px;
      }
      .cs-constraint-title {
        font-size: 15px;
        font-weight: 500;
        color: var(--Color-neutral-text_7);
        line-height: 1.3;
      }
      .cs-constraint-desc {
        font-size: 13px;
        color: var(--Color-neutral-text_5);
        line-height: 1.65;
      }
      .cs-constraint-footer {
        border-top: 0.5px solid var(--Color-neutral-border_3, #DFE3E8);
        background: var(--Color-neutral-bg_3, #F0F3F7);
        padding: 10px 16px;
        display: flex;
        flex-direction: column;
        gap: 10px;
      }
      .cs-constraint-impl {
        font-size: 11px;
        color: var(--Color-neutral-text_5);
        line-height: 1.4;
      }
      .cs-proof-chips {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
      }
      .cs-proof-pill {
        font-size: 11px;
        font-weight: 500;
        padding: 3px 10px;
        border-radius: 20px;
        background: #FFFFFF;
        border: 0.5px solid var(--Color-neutral-border_4, #CFD5DE);
        color: var(--Color-neutral-text_7);
      }
      /* Tag System */
      .cs-tag-pill {
        display: inline-flex;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 6px;
        letter-spacing: 0.04em;
        text-transform: uppercase;
      }
      .cs-tag-infrastructure { background: #F3E8FF; color: #6B21A8; }
      .cs-tag-regulatory { background: #FFFBEB; color: #B45309; }
      .cs-tag-timing { background: #FFE4E6; color: #9F1239; }
      .cs-tag-decision { background: #EFF6FF; color: #1E40AF; }
      
      /* Zone C: Regulation Image */
      .cs-reg-evidence {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 6px;
        margin-top: 4px;
      }
      .cs-reg-evidence img {
        width: 100%;
        max-height: 180px;
        border-radius: 8px;
        object-fit: cover;
        display: block;
        border: 1px solid rgba(0,0,0,0.06);
      }
      .cs-reg-caption {
        font-size: 11px;
        color: var(--Color-neutral-text_5);
        line-height: 1.3;
      }
      @media (max-width: 600px) {
        .cs-context-bar {
          grid-template-columns: 1fr;
          gap: 16px;
          padding: 20px;
        }
        .cs-context-cell {
          padding: 0;
          border-right: none;
          border-bottom: 0.5px solid var(--Color-neutral-border_4);
          padding-bottom: 12px;
        }
        .cs-context-cell:last-child {
          border-bottom: none;
          padding-bottom: 0;
        }
      }"""

# Remove old CSS blocks
css_to_remove = [
    r'\.cs-industry-header \{[\s\S]*?\}',
    r'\.cs-stats-row \{[\s\S]*?\}',
    r'\.cs-stat-item \{[\s\S]*?\}',
    r'\.cs-stat-item img \{[\s\S]*?\}',
    r'\.cs-stat-text \{[\s\S]*?\}',
    r'\.cs-numbered-cards \{[\s\S]*?\}',
    r'\.cs-numbered-card \{[\s\S]*?\}',
    r'\.cs-industry-layout \{[\s\S]*?\}',
    r'\.cs-industry-left \{[\s\S]*?\}',
    r'\.cs-industry-right \{[\s\S]*?\}',
    r'\.cs-doc-stack \{[\s\S]*?\}',
    r'\.cs-doc-layer \{[\s\S]*?\}',
    r'\.cs-doc-layer img \{[\s\S]*?\}',
    r'\.cs-doc-layer:nth-child\(1\) \{[\s\S]*?\}',
    r'\.cs-doc-layer:nth-child\(2\) \{[\s\S]*?\}',
    r'\.cs-doc-layer:nth-child\(3\) \{[\s\S]*?\}',
    r'\.cs-numbered-card-row \{[\s\S]*?\}',
    r'\.cs-number-lg \{[\s\S]*?\}'
]

for pat in css_to_remove:
    content = re.sub(pat, '', content)

# Inject new CSS right where we removed the old css (or at bottom of style)
content = content.replace('      /* Phase cards — Navigating Uncertainty */', new_css + '\n      /* Phase cards — Navigating Uncertainty */')

# --- HTML REPLACEMENT ---
# We need to extract the entire blocks from "SECTION 08 — Industry" to "SECTION 09 — Quote"
html_start = r'<!-- ============================================================\s*SECTION 08 — Industry\s*============================================================ -->'
html_end = r'<!-- ============================================================\s*SECTION 09 — Quote\s*============================================================ -->'

match = re.search(f'({html_start}[\s\S]*?){html_end}', content)

if match:
    old_html = match.group(1)
    new_html = """<!-- ============================================================
           SECTION 08 — Industry
           ============================================================ -->
      <section id="industry" class="cs-industry-section">
        
        <header class="cs-industry-heading">
          <span class="cs-industry-eyebrow">INDUSTRY</span>
          <h2 class="cs-industry-h2">Why KYC is hard across digital India</h2>
          <p class="cs-industry-lede">These numbers define the constraints — scale, identity fragmentation, and moment-sensitivity.</p>
        </header>

        <!-- ZONE A: CONTEXT BAR -->
        <div class="cs-context-bar-wrapper">
          <div class="cs-context-bar">
            <div class="cs-context-cell">
              <span class="cs-context-num">1.4B</span>
              <span class="cs-context-lbl">population</span>
            </div>
            <div class="cs-context-cell">
              <span class="cs-context-num">1.2B</span>
              <span class="cs-context-lbl">Aadhaar registrations</span>
            </div>
            <div class="cs-context-cell">
              <span class="cs-context-num">700M+</span>
              <span class="cs-context-lbl">internet users</span>
            </div>
          </div>
        </div>

        <!-- ZONE B & C: CONSTRAINTS & EVIDENCE -->
        <div class="cs-constraint-list">
          
          <!-- Constraint 01 -->
          <div class="cs-constraint-card">
            <div class="cs-constraint-top">
              <span class="cs-tag-pill cs-tag-infrastructure">Infrastructure</span>
            </div>
            <div class="cs-constraint-body">
              <h3 class="cs-constraint-title">Low Aadhaar-mobile linkage</h3>
              <p class="cs-constraint-desc">A significant portion of users had not linked their mobile number to Aadhaar, ruling out the fastest OTP path.</p>
            </div>
            <div class="cs-constraint-footer">
              <span class="cs-constraint-impl">Users requires alternative document processing pathways natively.</span>
            </div>
          </div>

          <!-- Constraint 02 (+ Zone C) -->
          <div class="cs-constraint-card">
            <div class="cs-constraint-top">
              <span class="cs-tag-pill cs-tag-regulatory">Regulatory</span>
            </div>
            <div class="cs-constraint-body">
              <h3 class="cs-constraint-title">Restricted state compliance</h3>
              <p class="cs-constraint-desc">Andhra Pradesh, Telangana, Assam and others required geo-gating at contest entry, adding dynamic logic per user depending on their location.</p>
            </div>
            <div class="cs-constraint-footer">
              <div class="cs-reg-evidence">
                <img src="https://placehold.co/800x240/EEF2FF/8B9EC7?text=Statewise+PMLA+Regulations" alt="KYC regulations document with Indian flag" />
                <span class="cs-reg-caption">Regulatory framework governing cash contests by state</span>
              </div>
            </div>
          </div>

          <!-- Constraint 03 -->
          <div class="cs-constraint-card accent-coral">
            <div class="cs-constraint-top">
              <span class="cs-tag-pill cs-tag-timing">Timing</span>
            </div>
            <div class="cs-constraint-body">
              <h3 class="cs-constraint-title">High-stakes match moments</h3>
              <p class="cs-constraint-desc">KYC drop-off peaks during IPL and major matches when user intent is highest but patience is lowest.</p>
            </div>
            <div class="cs-constraint-footer">
              <div class="cs-proof-chips">
                <span class="cs-proof-pill">10X Traffic</span>
                <span class="cs-proof-pill">Real Money</span>
              </div>
            </div>
          </div>

          <!-- Constraint 04 -->
          <div class="cs-constraint-card">
            <div class="cs-constraint-top">
              <span class="cs-tag-pill cs-tag-decision">Decision complexity</span>
            </div>
            <div class="cs-constraint-body">
              <h3 class="cs-constraint-title">Document variety</h3>
              <p class="cs-constraint-desc">Users needed to choose from Aadhaar, PAN, Passport, Voter ID, or Driving License — each with different validation paths.</p>
            </div>
          </div>

        </div>

      </section>

      """
    content = content.replace(old_html, new_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done processing industry section")
