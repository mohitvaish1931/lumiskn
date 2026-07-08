import re

with open('src/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace catalog filters logic
catalog_filters_old = """  /* ==========================================
     5. CATALOG FILTERS (SERVICES PAGE)
     ========================================== */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const catalogRows = document.querySelectorAll('.service-row-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterVal = btn.getAttribute('data-filter');

      catalogRows.forEach(row => {
        const rowCat = row.getAttribute('data-category');
        if (filterVal === 'all' || rowCat === filterVal) {
          row.style.display = 'grid';
          row.style.animation = 'smoothReveal 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards';
        } else {
          row.style.display = 'none';
        }
      });
    });
  });"""

catalog_filters_new = """  /* ==========================================
     5. CATALOG FILTERS (SERVICES PAGE)
     ========================================== */
  const filterBtns = document.querySelectorAll('.filter-btn');
  const catalogRows = document.querySelectorAll('.accordion-item');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterVal = btn.getAttribute('data-filter');

      catalogRows.forEach(row => {
        const rowCat = row.getAttribute('data-category');
        if (filterVal === 'all' || rowCat === filterVal) {
          row.style.display = 'block';
          row.style.animation = 'smoothReveal 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards';
        } else {
          row.style.display = 'none';
        }
      });
    });
  });

  /* ==========================================
     5.5 PREMIUM ACCORDION TOGGLE
     ========================================== */
  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const accordionItem = header.parentElement;
      const accordionBody = accordionItem.querySelector('.accordion-body');
      const isOpen = accordionItem.classList.contains('open');

      // Close all others
      document.querySelectorAll('.accordion-item').forEach(item => {
        item.classList.remove('open');
        const body = item.querySelector('.accordion-body');
        if(body) body.style.maxHeight = '0px';
      });

      // Toggle current
      if (!isOpen) {
        accordionItem.classList.add('open');
        accordionBody.style.maxHeight = accordionBody.scrollHeight + 'px';
      }
    });
  });

  /* ==========================================
     5.6 SUB-SERVICE SELECTION & FLOATING BAR
     ========================================== */
  const subServiceCheckboxes = document.querySelectorAll('.sub-service-checkbox');
  const floatingBar = document.getElementById('floating-bar');
  const selectionCountEl = document.querySelector('.selection-count');
  const floatingBookBtn = document.getElementById('floating-book-btn');
  let selectedServices = [];

  function updateSelectionState() {
    selectedServices = Array.from(subServiceCheckboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.value);

    if (selectedServices.length > 0) {
      selectionCountEl.textContent = `${selectedServices.length} Service${selectedServices.length > 1 ? 's' : ''} Selected`;
      floatingBar.classList.add('visible');
    } else {
      floatingBar.classList.remove('visible');
    }
  }

  subServiceCheckboxes.forEach(cb => {
    cb.addEventListener('change', updateSelectionState);
  });
"""
content = content.replace(catalog_filters_old, catalog_filters_new)

# Update form validation and whatsapp message logic
form_old = """      const fields = [
        { id: 'name', valFn: val => val.trim().length > 0 },
        { id: 'email', valFn: val => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val) },
        { id: 'interest', valFn: val => val !== '' }
      ];"""

form_new = """      const fields = [
        { id: 'name', valFn: val => val.trim().length > 0 },
        { id: 'email', valFn: val => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val) }
      ];
      // Note: we removed interest validation since we inject selectedServices dynamically."""

content = content.replace(form_old, form_new)

message_old = """        const message = `Hello Lumi SKN Concierge!\\n\\nI would like to request a bespoke consultation.\\n\\n*Name:* ${name}\\n*Email:* ${email}\\n*Focus Area:* ${interest}\\n\\nPlease let me know your earliest availability.`;"""

message_new = """        let interestText = interest;
        if (typeof selectedServices !== 'undefined' && selectedServices.length > 0) {
          interestText = selectedServices.join(', ');
        }
        
        const message = `Hello Lumi SKN Concierge!\\n\\nI would like to request a bespoke consultation.\\n\\n*Name:* ${name}\\n*Email:* ${email}\\n*Selected Services:* ${interestText}\\n\\nPlease let me know your earliest availability.`;"""

content = content.replace(message_old, message_new)

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated main.js")
