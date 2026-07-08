css_content = """
/* ==========================================
   PREMIUM ACCORDION SERVICES
   ========================================== */

.premium-accordion {
  border-top: 1px solid var(--border-delicate);
  margin-top: 40px;
}

.accordion-item {
  border-bottom: 1px solid var(--border-delicate);
  overflow: hidden;
  transition: background-color 0.4s ease;
}

.accordion-item:hover {
  background-color: rgba(255, 255, 255, 0.4);
}

.accordion-header {
  padding: 30px 20px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.accordion-header h3 {
  font-family: var(--font-serif);
  font-size: 32px;
  font-weight: 400;
  margin: 0;
  transition: color 0.3s;
}

.accordion-icon {
  width: 24px;
  height: 24px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.accordion-icon::before,
.accordion-icon::after {
  content: '';
  position: absolute;
  background-color: var(--text-main);
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.accordion-icon::before {
  width: 100%;
  height: 1px;
}

.accordion-icon::after {
  height: 100%;
  width: 1px;
}

/* Open State */
.accordion-item.open .accordion-header h3 {
  color: var(--champagne-dark);
}

.accordion-item.open .accordion-icon::after {
  transform: rotate(90deg) scaleY(0);
}

.accordion-body {
  max-height: 0;
  opacity: 0;
  padding: 0 20px;
  transition: max-height 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease, padding 0.4s ease;
}

.accordion-item.open .accordion-body {
  opacity: 1;
  padding: 0 20px 30px;
}

.sub-services-wrapper {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding-top: 20px;
  border-top: 1px dashed var(--border-delicate);
}

/* Custom Premium Checkbox */
.custom-checkbox-container {
  display: flex;
  align-items: center;
  cursor: pointer;
  position: relative;
  padding-left: 35px;
  font-size: 16px;
  user-select: none;
  transition: opacity 0.3s;
}

.custom-checkbox-container:hover {
  opacity: 0.8;
}

.custom-checkbox-container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}

.checkmark {
  position: absolute;
  top: 50%;
  left: 0;
  transform: translateY(-50%);
  height: 22px;
  width: 22px;
  background-color: transparent;
  border: 1px solid var(--border-delicate);
  border-radius: 50%;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.custom-checkbox-container input:checked ~ .checkmark {
  background-color: var(--champagne-dark);
  border-color: var(--champagne-dark);
  box-shadow: 0 0 10px rgba(184, 158, 127, 0.3);
}

.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.custom-checkbox-container input:checked ~ .checkmark:after {
  display: block;
}

.custom-checkbox-container .checkmark:after {
  left: 8px;
  top: 4px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 1.5px 1.5px 0;
  transform: rotate(45deg);
}

.service-name {
  color: var(--text-secondary);
  transition: color 0.3s;
}

.custom-checkbox-container input:checked ~ .service-name {
  color: var(--text-main);
  font-weight: 500;
}

/* Floating Booking Bar */
.floating-booking-bar {
  position: fixed;
  bottom: -100px;
  left: 0;
  width: 100%;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(15px);
  -webkit-backdrop-filter: blur(15px);
  border-top: 1px solid var(--border-delicate);
  box-shadow: 0 -10px 40px rgba(0,0,0,0.05);
  z-index: 1000;
  transition: bottom 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.floating-booking-bar.visible {
  bottom: 0;
}

.floating-bar-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.selection-count {
  font-family: var(--font-serif);
  font-size: 24px;
  color: var(--text-main);
}

@media (max-width: 768px) {
  .sub-services-wrapper {
    grid-template-columns: 1fr;
  }
  .floating-bar-content {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }
}
"""

with open('src/style.css', 'a', encoding='utf-8') as f:
    f.write("\n" + css_content)

print("Updated style.css")
