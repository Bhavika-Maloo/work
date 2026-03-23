import re

file_path = "/Users/bhavikamaloo/Desktop/Portfolio-case study/Verification/index-framer.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up typography duplication
# Move font to body in the base CSS block
content = re.sub(
    r'(html, body \{\n\s*height: 100%;\n\s*overflow-x: hidden;\n\s*line-height: 1\.5;\n\s*\})',
    r'html, body {\n        height: 100%;\n        overflow-x: hidden;\n        line-height: 1.5;\n        font-family: \'DM Sans\', sans-serif;\n      }',
    content
)

# Remove all redundant `font-family: 'DM Sans', sans-serif;` lines
content = re.sub(r'^\s*font-family:\s*[\'"]DM Sans[\'"],\s*sans-serif;\s*\n', '', content, flags=re.MULTILINE)

# Remove unused font-face IBM Plex Sans KR-SemiBold
ibm_plex_pattern = r'\s*/\* =============================================\n\s*Font Faces\n\s*============================================= \*/\n\s*/\* DM Sans.*?\n\s*@font-face \{\n\s*font-family: "IBM Plex Sans KR-SemiBold";\n\s*src: .*?;\n\s*font-weight: 600;\n\s*\}\n'
content = re.sub(ibm_plex_pattern, '', content)


# 2. Extract inline styles in Project Meta
inline_style = r'style="background:#FFFFFF;border:1px solid #E8ECF2;border-radius:16px;padding:24px 28px;box-shadow:0 2px 16px rgba\(32,44,61,0\.07\);"'

class_insert = r'''      .cs-meta-col {
        display: flex;
        flex-direction: column;
        gap: 10px;
        background: #FFFFFF;
        border: 1px solid #E8ECF2;
        border-radius: 16px;
        padding: 24px 28px;
        box-shadow: 0 2px 16px rgba(32,44,61,0.07);
      }'''
content = content.replace('      .cs-meta-col {\n        display: flex;\n        flex-direction: column;\n        gap: 10px;\n      }', class_insert)

content = content.replace(f' {inline_style}', '')


# 3. Clean up generic dark colors to use CSS variables
# 1A1A2E -> var(--Color-neutral-text_7)  [except if it's explicitly needed differently, but they are all just dark text]
# Let's target specific classes for this safe replacement.
content = content.replace('color: #1A1A2E;', 'color: var(--Color-neutral-text_7);')
content = content.replace('color: #202C3D;', 'color: var(--Color-neutral-text_7);')
content = content.replace('color: #3D4A5C;', 'color: var(--Color-neutral-text_5);')
content = content.replace('color: #64748B;', 'color: var(--Color-neutral-text_5);')
content = content.replace('color: #98A2B3;', 'color: var(--Color-neutral-text_3);')

# 4. Fix primary greens in steps to use variables
content = content.replace('background: #109E38;', 'background: var(--Color-accent1-bg_5);')
content = content.replace('color: #109E38;', 'color: var(--Color-accent1-bg_5);')
content = content.replace('border-top: 3px solid #00A348;', 'border-top: 3px solid var(--Color-accent1-bg_4);')

# 5. Fix structural numbering and section IDs
# The sections in the HTML are numbered as 01 (Contributions), 02 (Problem-Space), 03 (Background), 04 (Goals), 05 (Design-Principles), 07 (Research). We should make nav 01..06.
content = content.replace('<div class="sol-section-num">07</div>', '<div class="sol-section-num">06</div>')

# 6. Extract media queries. We'll do this via simple regex to find them, but actually they are quite intertwined.
# Let's just remove the first redundant 1024px and 767px blocks from around line 1089 and put them at the end.
# Actually, the media queries are scattered.
mq_767_1 = """      @media (max-width: 767px) {
        .cs-platform-grid { grid-template-columns: 1fr; max-width: 360px; margin: 0 auto; }
      }"""
content = content.replace(mq_767_1, "")

mq_1024_1 = """      @media (max-width: 1024px) and (min-width: 768px) {
        .cs-platform-grid { grid-template-columns: repeat(3, 1fr); gap: 14px; }
        .cs-platform-name { font-size: 18px; }
      }"""
content = content.replace(mq_1024_1, "")

mq_1024_2 = """      @media (max-width: 1024px) {
        .cs-industry-layout { grid-template-columns: 1fr; }
        .cs-industry-right { display: none; }
      }"""
content = content.replace(mq_1024_2, "")

mq_767_2 = """      @media (max-width: 767px) {
        .ch-insight-grid { grid-template-columns: 1fr; }
        .ch-impact-row { grid-template-columns: 1fr; }
      }"""
content = content.replace(mq_767_2, "")

mq_767_3 = """      @media (max-width: 767px) {
        .sol-framework-nav { gap: 8px; }
        .sol-screen-grid.three { grid-template-columns: 1fr 1fr; }
        .sol-ps-row { grid-template-columns: 1fr; }
        .sol-arrow { display: none; }
        .sol-stat-row { grid-template-columns: 1fr; }
      }"""
content = content.replace(mq_767_3, "")

mq_1024_3 = """      @media (max-width: 1024px) {
        .cs-phase-cards { grid-template-columns: 1fr 1fr; }
        .cs-final-solution-banner { padding: 56px 40px; }
      }"""
content = content.replace(mq_1024_3, "")

mq_767_4 = """      @media (max-width: 767px) {
        .cs-phase-cards { grid-template-columns: 1fr; }
        .cs-two-col-phone { flex-direction: column; align-items: center; }
        .cs-final-solution-banner { padding: 40px 24px; border-radius: 24px; }
        .cs-principle-slides { flex-direction: column; }
        .cs-principle-slide { min-height: 100px; }
        .cs-why-matters { padding: 40px 24px; border-radius: 20px; }
        .cs-regulatory-callout { padding: 40px 24px; border-radius: 20px; }
      }"""
content = content.replace(mq_767_4, "")

# Now we find the main Part 1 media queries and append the rules to them.
consolidated_1024 = """      @media (max-width: 1024px) {
        .page-wrapper { padding: 48px 32px; gap: 80px; }
        .page-wrapper > section:not(#hero) { gap: 56px; }

        /* Hero */
        .frame { gap: 48px; }
        .frame .div { max-width: calc(100% - 320px); }
        .hero-placeholder { flex: 0 0 300px; width: 300px; height: 260px; }

        .cs-meta { grid-template-columns: repeat(3, 1fr); }
        .cs-contributions { flex-direction: column; }
        .cs-problem-grid { grid-template-columns: repeat(2, 1fr); }
        .cs-goals-grid { grid-template-columns: 1fr 1fr; }
        .cs-platforms { flex-direction: column; }
        
        .cs-industry-layout { grid-template-columns: 1fr; }
        .cs-industry-right { display: none; }
        .cs-phase-cards { grid-template-columns: 1fr 1fr; }
        .cs-final-solution-banner { padding: 56px 40px; }
      }
      @media (max-width: 1024px) and (min-width: 768px) {
        .cs-platform-grid { grid-template-columns: repeat(3, 1fr); gap: 14px; }
        .cs-platform-name { font-size: 18px; }
      }"""

consolidated_767 = """      @media (max-width: 767px) {
        .page-wrapper { padding: 40px 20px; gap: 64px; }
        .page-wrapper > section:not(#hero) { gap: 40px; }

        /* Hero */
        .frame { flex-direction: column; align-items: center; gap: 32px; }
        .frame .div { width: 100%; max-width: 100%; }
        .frame .div-3, .frame .div-2 { width: 100%; }
        .frame .transforming { width: 100%; }
        .frame .div-4 { gap: 12px; }
        .hero-placeholder { flex: none; width: 100%; height: 220px; }

        .cs-meta { grid-template-columns: 1fr; gap: 20px; }
        .cs-contributions { padding: 32px 24px; flex-direction: column; }
        .cs-problem-grid { grid-template-columns: 1fr; }
        .cs-problem-grid-2 { grid-template-columns: 1fr; }
        .cs-goals-grid { grid-template-columns: 1fr; }
        .cs-numbered-card { flex-direction: column; gap: 16px; }
        .cs-observations { flex-direction: column; gap: 32px; }
        .cs-slide { padding: 40px 24px; border-radius: 24px; }
        .cs-stats-row { gap: 16px; }
        .cs-platforms { flex-direction: column; }
        .cs-platform-card { padding: 20px; }
        .cs-future-callout { padding: 40px 24px; }
        
        .cs-platform-grid { grid-template-columns: 1fr; max-width: 360px; margin: 0 auto; }
        .ch-insight-grid { grid-template-columns: 1fr; }
        .ch-impact-row { grid-template-columns: 1fr; }
        .sol-framework-nav { gap: 8px; }
        .sol-screen-grid.three { grid-template-columns: 1fr 1fr; }
        .sol-ps-row { grid-template-columns: 1fr; }
        .sol-arrow { display: none; }
        .sol-stat-row { grid-template-columns: 1fr; }
        .cs-phase-cards { grid-template-columns: 1fr; }
        .cs-two-col-phone { flex-direction: column; align-items: center; }
        .cs-final-solution-banner { padding: 40px 24px; border-radius: 24px; }
        .cs-principle-slides { flex-direction: column; }
        .cs-principle-slide { min-height: 100px; }
        .cs-why-matters { padding: 40px 24px; border-radius: 20px; }
        .cs-regulatory-callout { padding: 40px 24px; border-radius: 20px; }
      }"""

old_1024 = """      @media (max-width: 1024px) {
        .page-wrapper { padding: 48px 32px; gap: 80px; }
        .page-wrapper > section:not(#hero) { gap: 56px; }

        /* Hero */
        .frame { gap: 48px; }
        .frame .div { max-width: calc(100% - 320px); }
        .hero-placeholder { flex: 0 0 300px; width: 300px; height: 260px; }

        .cs-meta { grid-template-columns: repeat(3, 1fr); }
        .cs-contributions { flex-direction: column; }
        .cs-problem-grid { grid-template-columns: repeat(2, 1fr); }
        .cs-goals-grid { grid-template-columns: 1fr 1fr; }
        .cs-platforms { flex-direction: column; }
      }"""

old_767 = """      @media (max-width: 767px) {
        .page-wrapper { padding: 40px 20px; gap: 64px; }
        .page-wrapper > section:not(#hero) { gap: 40px; }

        /* Hero */
        .frame { flex-direction: column; align-items: center; gap: 32px; }
        .frame .div { width: 100%; max-width: 100%; }
        .frame .div-3, .frame .div-2 { width: 100%; }
        .frame .transforming { width: 100%; }
        .frame .div-4 { gap: 12px; }
        .hero-placeholder { flex: none; width: 100%; height: 220px; }

        .cs-meta { grid-template-columns: 1fr; gap: 20px; }
        .cs-contributions { padding: 32px 24px; flex-direction: column; }
        .cs-problem-grid { grid-template-columns: 1fr; }
        .cs-problem-grid-2 { grid-template-columns: 1fr; }
        .cs-goals-grid { grid-template-columns: 1fr; }
        .cs-numbered-card { flex-direction: column; gap: 16px; }
        .cs-observations { flex-direction: column; gap: 32px; }
        .cs-slide { padding: 40px 24px; border-radius: 24px; }
        .cs-stats-row { gap: 16px; }
        .cs-platforms { flex-direction: column; }
        .cs-platform-card { padding: 20px; }
        .cs-future-callout { padding: 40px 24px; }
      }"""

content = content.replace(old_1024, consolidated_1024)
content = content.replace(old_767, consolidated_767)

# Final step: clean up the section nav to be consistent with HTML IDs
# Replace non-sequential section comments too to make the file more readable.
content = content.replace('SECTION 10 — Problem Space', 'SECTION 05 — Problem Space')
content = content.replace('SECTION 4 — Key Contributions', 'SECTION 04 — Key Contributions')
content = content.replace('SECTION 5 — Background', 'SECTION 06 — Background')
content = content.replace('SECTION 6 — Future Callout', 'SECTION 07 — Future Callout')
content = content.replace('SECTION 7 — Industry', 'SECTION 08 — Industry')
content = content.replace('SECTION 8 — Quote', 'SECTION 09 — Quote')
content = content.replace('SECTION 9 — Why This Matters', 'SECTION 10 — Why This Matters')
content = content.replace('SECTION 11 — Goals', 'SECTION 11 — Goals')
content = content.replace('SECTION 17 — Design Strategy', 'SECTION 12 — Design Strategy')
content = content.replace('SECTION 13 — Final Solution', 'SECTION 13 — Final Solution')
content = content.replace('SECTION 12 — Navigating Uncertainty', 'SECTION 14 — Navigating Uncertainty')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("done editing html")
