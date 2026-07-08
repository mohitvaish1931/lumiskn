import re

html_content = """
          <!-- Catalog List (Accordion Style) -->
          <div class="services-catalog-list premium-accordion">
            
            <div class="accordion-item hoverable" data-category="facial">
              <div class="accordion-header">
                <h3>Medi Facial</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Hydra facial">
                    <span class="checkmark"></span>
                    <span class="service-name">Hydra facial</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Oxygeneo">
                    <span class="checkmark"></span>
                    <span class="service-name">Oxygeneo</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Bridal Medi Facial">
                    <span class="checkmark"></span>
                    <span class="service-name">Bridal Medi Facial</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Deep Cleansing">
                    <span class="checkmark"></span>
                    <span class="service-name">Deep Cleansing</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="accordion-item hoverable" data-category="facial">
              <div class="accordion-header">
                <h3>Peels</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Acne Peel">
                    <span class="checkmark"></span>
                    <span class="service-name">Acne Peel</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Party Peel">
                    <span class="checkmark"></span>
                    <span class="service-name">Party Peel</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Pumpkin Peel">
                    <span class="checkmark"></span>
                    <span class="service-name">Pumpkin Peel</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Brightening Peel">
                    <span class="checkmark"></span>
                    <span class="service-name">Brightening Peel</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="accordion-item hoverable" data-category="laser">
              <div class="accordion-header">
                <h3>Laser Treatment</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Laser Hair Reduction">
                    <span class="checkmark"></span>
                    <span class="service-name">Laser Hair Reduction</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Tattoo Removal">
                    <span class="checkmark"></span>
                    <span class="service-name">Tattoo Removal</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Red Carpet Facial">
                    <span class="checkmark"></span>
                    <span class="service-name">Red Carpet Facial (Laser Therapy)</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="accordion-item hoverable" data-category="acne">
              <div class="accordion-header">
                <h3>Acne Treatment</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Active Acne">
                    <span class="checkmark"></span>
                    <span class="service-name">Active Acne</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Acne Scars">
                    <span class="checkmark"></span>
                    <span class="service-name">Acne Scars</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Acne Solution">
                    <span class="checkmark"></span>
                    <span class="service-name">Acne Solution</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Treatment PRP + Microneedling">
                    <span class="checkmark"></span>
                    <span class="service-name">Treatment PRP + Microneedling</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="accordion-item hoverable" data-category="laser">
              <div class="accordion-header">
                <h3>HIFU</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Jawline Contouring">
                    <span class="checkmark"></span>
                    <span class="service-name">Jawline Contouring</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Double Chin Reduction">
                    <span class="checkmark"></span>
                    <span class="service-name">Double Chin Reduction</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Face Lift">
                    <span class="checkmark"></span>
                    <span class="service-name">Face Lift</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Neck Tightening">
                    <span class="checkmark"></span>
                    <span class="service-name">Neck Tightening</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="accordion-item hoverable" data-category="inject">
              <div class="accordion-header">
                <h3>Botox</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Forehead Lines">
                    <span class="checkmark"></span>
                    <span class="service-name">Forehead Lines</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Frown Lines">
                    <span class="checkmark"></span>
                    <span class="service-name">Frown Lines</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Crows Lines">
                    <span class="checkmark"></span>
                    <span class="service-name">Crows Lines</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Bunny Lines">
                    <span class="checkmark"></span>
                    <span class="service-name">Bunny Lines</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Masseter Botox">
                    <span class="checkmark"></span>
                    <span class="service-name">Masseter Botox (Jaw Slimming)</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="accordion-item hoverable" data-category="inject">
              <div class="accordion-header">
                <h3>Fillers</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Lip Fillers">
                    <span class="checkmark"></span>
                    <span class="service-name">Lip Fillers</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Chin Enhancement">
                    <span class="checkmark"></span>
                    <span class="service-name">Chin Enhancement</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Cheek Fillers">
                    <span class="checkmark"></span>
                    <span class="service-name">Cheek Fillers</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Under Eye Fillers">
                    <span class="checkmark"></span>
                    <span class="service-name">Under Eye Fillers</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Jawline Fillers">
                    <span class="checkmark"></span>
                    <span class="service-name">Jawline Fillers</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="accordion-item hoverable" data-category="makeup">
              <div class="accordion-header">
                <h3>Semi Permanent Makeup</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Lip Tinting">
                    <span class="checkmark"></span>
                    <span class="service-name">Lip Tinting</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Eyebrow Microblading">
                    <span class="checkmark"></span>
                    <span class="service-name">Eyebrow Microblading</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="BB Glow">
                    <span class="checkmark"></span>
                    <span class="service-name">BB Glow</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Cheek Blushing">
                    <span class="checkmark"></span>
                    <span class="service-name">Cheek Blushing</span>
                  </label>
                </div>
              </div>
            </div>

            <div class="accordion-item hoverable" data-category="hair">
              <div class="accordion-header">
                <h3>Hair Care</h3>
                <span class="accordion-icon"></span>
              </div>
              <div class="accordion-body">
                <div class="sub-services-wrapper">
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Meso Therapy">
                    <span class="checkmark"></span>
                    <span class="service-name">Meso Therapy</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Hair GFC">
                    <span class="checkmark"></span>
                    <span class="service-name">Hair GFC</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="Hair PRP">
                    <span class="checkmark"></span>
                    <span class="service-name">Hair PRP</span>
                  </label>
                  <label class="custom-checkbox-container">
                    <input type="checkbox" class="sub-service-checkbox" value="QR678">
                    <span class="checkmark"></span>
                    <span class="service-name">QR678</span>
                  </label>
                </div>
              </div>
            </div>

          </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything from <div class="services-catalog-list"> to the end of that div.
# Looking at the file, it goes until the closing </div> of <div class="services-catalog-list">.
pattern = r'<!-- Catalog List -->\s*<div class="services-catalog-list">.*?</div>\s*(?=</div>\s*</section>)'
new_content = re.sub(pattern, html_content, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated index.html")
