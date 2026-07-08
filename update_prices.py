import re

with open('prices.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# Skip title line if present
if 'Rate List' in lines[0]:
    lines = lines[1:]

categories = []
current_cat = None

for line in lines:
    if line in ['Facials', 'Peel', 'Lasers', 'Laser Hair Reduction (LHR)', 'Injectables', 'Hair Care', 'Other Wellness Segment']:
        current_cat = {'name': line, 'services': []}
        categories.append(current_cat)
    elif line in ['S.No', 'Treatment', 'Price (₹)']:
        continue
    elif line.isdigit():
        continue # It's an S.No
    else:
        # Check if line is a price
        if re.match(r'^[\d,]+$', line):
            if current_cat and current_cat['services']:
                current_cat['services'][-1]['price'] = line
        else:
            if current_cat:
                current_cat['services'].append({'name': line, 'price': ''})

def get_filter_cat(cat_name):
    if cat_name in ['Facials', 'Peel']: return 'facial'
    if cat_name in ['Lasers', 'Laser Hair Reduction (LHR)']: return 'laser'
    if cat_name == 'Injectables': return 'inject'
    if cat_name == 'Hair Care': return 'hair'
    if cat_name == 'Other Wellness Segment': return 'wellness'
    return 'all'

html = """
          <!-- Filters -->
          <div class="catalog-filters">
            <button class="filter-btn active hoverable" data-filter="all">All Services</button>
            <button class="filter-btn hoverable" data-filter="facial">Facials & Peels</button>
            <button class="filter-btn hoverable" data-filter="laser">Lasers & LHR</button>
            <button class="filter-btn hoverable" data-filter="inject">Injectables</button>
            <button class="filter-btn hoverable" data-filter="hair">Hair Care</button>
            <button class="filter-btn hoverable" data-filter="wellness">Wellness</button>
          </div>

          <!-- Catalog List (Accordion Style) -->
          <div class="services-catalog-list premium-accordion">
"""

for cat in categories:
    filter_val = get_filter_cat(cat['name'])
    html += f"""
            <div class="accordion-item hoverable" data-category="{filter_val}">
              <div class="accordion-header">
                <h3>{cat['name']}</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">"""
    
    for srv in cat['services']:
        name = srv['name']
        price = srv['price']
        html += f"""
                  <label class="custom-checkbox-container" style="justify-content: space-between; padding-right: 20px;">
                    <div style="display: flex; align-items: center;">
                      <input type="checkbox" class="sub-service-checkbox" value="{name}">
                      <span class="checkmark"></span>
                      <span class="service-name">{name}</span>
                    </div>
                    <span class="service-price" style="color: var(--champagne-dark); font-weight: 500; font-size: 14px;">₹{price}</span>
                  </label>"""
    html += """
                </div>
              </div>
            </div>"""

html += """
          </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace filters and catalog list
pattern = r'<!-- Filters -->\s*<div class="catalog-filters">.*</div>\s*<!-- Catalog List.*?</div>\s*</div>'
# We need a more precise regex. Let's just find the start of <!-- Filters --> and the end of </section>
# Wait, replacing up to </section> is dangerous.
# Let's use string split/replace if possible.

# The block to replace starts with <!-- Filters --> and ends right before </div>\s*</div>\s*</section>
import re
new_content = re.sub(
    r'<!-- Filters -->.*?</div>\s*</div>\s*(?=</div>\s*</section>)', 
    html, 
    content, 
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html with prices.")
