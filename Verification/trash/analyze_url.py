import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://bikiron.in/mysterybox"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract all style blocks
    styles = soup.find_all('style')
    css_content = "\n".join([s.get_text() for s in styles])
    
    # Try finding external CSS if not enough inline
    links = soup.find_all('link', rel='stylesheet')
    for link in links:
        href = link.get('href')
        if href:
            if href.startswith('/'):
                href = "https://bikiron.in" + href
            if href.startswith('http'):
                try:
                    css_text = urllib.request.urlopen(urllib.request.Request(href, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
                    css_content += "\n" + css_text
                except:
                    pass
    
    # We want to look for clues: font-family, border-radius, box-shadow, line-height, padding, margins
    fonts = set(re.findall(r'font-family:\s*([^;}]+)', css_content))
    radii = set(re.findall(r'border-radius:\s*([^;}]+)', css_content))
    shadows = set(re.findall(r'box-shadow:\s*([^;}]+)', css_content))
    
    print("--- DESIGN ANALYSIS ---")
    print(f"Fonts found: {list(fonts)[:10]}")
    print(f"Border radii found: {list(radii)[:10]}")
    print(f"Shadows found: {list(shadows)[:10]}")
    
    # Let's save a bit of the css to inspect classes for layout spacing
    with open('/tmp/bikiron.css', 'w') as f:
        f.write(css_content)
    
except Exception as e:
    print(f"Error fetching: {e}")
