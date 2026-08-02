import os
import re

treatments = [
    {"folder": "medi-facials", "title": "Signature Medi Facials", "hero": "Experience luxury and glowing skin with our Signature Medi Facials.", "value": "Medi Facial"},
    {"folder": "anti-ageing", "title": "Anti-Ageing Solutions", "hero": "Turn back time with our premium Botox & Fillers.", "value": "Botox"},
    {"folder": "pigmentation", "title": "Advanced Pigmentation Control", "hero": "Achieve a flawless, even skin tone with our advanced pigmentation treatments.", "value": "Pigmentation"},
    {"folder": "acne-management", "title": "Acne & Scar Management", "hero": "Clear, smooth skin is just an appointment away with our acne and scar treatments.", "value": "Acne Treatment"},
    {"folder": "laser-hair-reduction", "title": "Laser Hair Reduction", "hero": "Enjoy smooth, hair-free skin permanently with our advanced laser technology.", "value": "Laser Hair Reduction"}
]

base_dir = "treatments"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

with open("index.html", "r", encoding="utf-8") as f:
    base_html = f.read()

# Fix relative paths for CSS and JS to absolute from root
base_html = base_html.replace('href="./src/style.css"', 'href="/src/style.css"')

for t in treatments:
    t_dir = os.path.join(base_dir, t["folder"])
    os.makedirs(t_dir, exist_ok=True)
    
    # Customize Hero Title and Subtitle
    html = re.sub(r'<h1 class="hero-title">.*?</h1>', f'<h1 class="hero-title">{t["title"]}</h1>', base_html, flags=re.DOTALL)
    html = re.sub(r'<p class="hero-subtitle">.*?</p>', f'<p class="hero-subtitle">{t["hero"]}</p>', html, flags=re.DOTALL)
    
    # Remove the massive services accordion since they are already on a service page
    html = re.sub(r'<!-- Services Section \(Premium Accordion\) -->.*?<!-- End Services Section -->', '', html, flags=re.DOTALL)
    
    # Add a hidden input to the form to specify the treatment
    html = html.replace('<form id="booking-form" class="glass-form">', f'<form id="booking-form" class="glass-form">\n            <input type="hidden" id="specific-treatment" value="{t["value"]}">')
    
    # Change title
    html = html.replace('<title>Lumi SKN | Aesthetic & Laser Clinic</title>', f'<title>{t["title"]} | Lumi SKN</title>')

    with open(os.path.join(t_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

print("Landing pages generated successfully!")
