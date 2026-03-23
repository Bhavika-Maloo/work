import re

file_path = "/Users/bhavikamaloo/Desktop/Portfolio-case study/Verification/index-framer.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

html_start = r'<!-- ============================================================\s*SECTION 08 — Industry[\s\S]*?============================================================ -->'
html_end = r'<!-- ============================================================\s*SECTION 09 — Quote[\s\S]*?============================================================ -->'

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
    print("Done html replacement")
else:
    print("NO MATCH FOUND!")
