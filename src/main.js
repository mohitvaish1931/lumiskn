import './style.css'

document.addEventListener('DOMContentLoaded', () => {
  /* ==========================================
     1. CUSTOM CURSOR TRACKING
     ========================================== */
  const cursor = document.querySelector('.custom-cursor');
  const cursorDot = document.querySelector('.custom-cursor-dot');

  if (cursor && cursorDot) {
    document.addEventListener('mousemove', (e) => {
      cursor.style.left = `${e.clientX}px`;
      cursor.style.top = `${e.clientY}px`;
      
      cursorDot.style.left = `${e.clientX}px`;
      cursorDot.style.top = `${e.clientY}px`;
    });

    document.addEventListener('mouseleave', () => {
      cursor.style.opacity = '0';
      cursorDot.style.opacity = '0';
    });

    document.addEventListener('mouseenter', () => {
      cursor.style.opacity = '1';
      cursorDot.style.opacity = '1';
    });

    // Add scale class on hoverable elements
    const hoverables = document.querySelectorAll('.hoverable, a, button, select, input, textarea');
    hoverables.forEach(item => {
      item.addEventListener('mouseenter', () => {
        cursor.classList.add('hovered');
      });
      item.addEventListener('mouseleave', () => {
        cursor.classList.remove('hovered');
      });
    });
  }

  /* ==========================================
     2. SPA ROUTING & VIEW SWITCHING
     ========================================== */
  const pageViews = document.querySelectorAll('.page-view');
  
  function navigateToPage(targetPageId) {
    if (!targetPageId) targetPageId = 'home';
    
    // Hide mobile menu if open
    const navMenu = document.getElementById('nav-menu');
    if (navMenu) navMenu.classList.remove('open');

    // Switch active view
    pageViews.forEach(view => {
      if (view.id === `view-${targetPageId}`) {
        view.classList.add('active');
      } else {
        view.classList.remove('active');
      }
    });

    // Update nav links active class
    const mainNavLinks = document.querySelectorAll('.nav-menu .nav-link');
    mainNavLinks.forEach(link => {
      if (link.getAttribute('data-target') === targetPageId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });

    // Scroll back to top smoothly
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
    
    // Check if we are on inverse header page (like home with dark hero)
    checkHeaderInverse(targetPageId);
  }

  function checkHeaderInverse(pageId) {
    const header = document.getElementById('main-header');
    if (pageId === 'home') {
      header.classList.add('inverse-mode');
    } else {
      header.classList.remove('inverse-mode');
    }
  }

  // Monitor navigation clicks
  document.addEventListener('click', (e) => {
    const navClick = e.target.closest('[data-target]');
    if (navClick) {
      e.preventDefault(); // Prevent default hash jump
      const pageId = navClick.getAttribute('data-target');
      window.location.hash = pageId;
      navigateToPage(pageId);
    }
  });

  // Handle URL hash changes directly
  window.addEventListener('hashchange', () => {
    const hash = window.location.hash.substring(1);
    if (hash && ['home', 'services', 'contact'].includes(hash)) {
      navigateToPage(hash);
    }
  });

  // Trigger initial route load
  const initialHash = window.location.hash.substring(1);
  if (initialHash && ['home', 'services', 'contact'].includes(initialHash)) {
    navigateToPage(initialHash);
  } else {
    navigateToPage('home');
  }

  /* ==========================================
     3. HEADER SCROLL & MOBILE MENU TOGGLE
     ========================================== */
  const header = document.getElementById('main-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  const mobileToggle = document.getElementById('mobile-nav-toggle');
  const navMenu = document.getElementById('nav-menu');
  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('open');
    });
  }

  /* ==========================================
     4. CLIENT TESTIMONIALS SLIDER
     ========================================== */
  const slides = document.querySelectorAll('.testimonial-slide');
  const dots = document.querySelectorAll('.slider-dots .dot');
  let currentSlideIndex = 0;
  let testimonialInterval = null;

  function showSlide(index) {
    if (!slides.length) return;
    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));

    slides[index].classList.add('active');
    dots[index].classList.add('active');
    currentSlideIndex = index;
  }

  function nextSlide() {
    if (!slides.length) return;
    let nextIdx = (currentSlideIndex + 1) % slides.length;
    showSlide(nextIdx);
  }

  function prevSlide() {
    if (!slides.length) return;
    let prevIdx = (currentSlideIndex - 1 + slides.length) % slides.length;
    showSlide(prevIdx);
  }

  const prevTestiBtn = document.getElementById('prev-slide');
  const nextTestiBtn = document.getElementById('next-slide');

  if (prevTestiBtn && nextTestiBtn) {
    prevTestiBtn.addEventListener('click', () => {
      prevSlide();
      resetInterval();
    });

    nextTestiBtn.addEventListener('click', () => {
      nextSlide();
      resetInterval();
    });
  }

  dots.forEach(dot => {
    dot.addEventListener('click', () => {
      const index = parseInt(dot.getAttribute('data-slide'));
      showSlide(index);
      resetInterval();
    });
  });

  function startInterval() {
    testimonialInterval = setInterval(nextSlide, 6000);
  }

  function resetInterval() {
    clearInterval(testimonialInterval);
    if(slides.length) startInterval();
  }

  if (slides.length > 0) {
    startInterval();
  }

  /* ==========================================
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
  });

  /* ==========================================
     6. CINEMATIC MODAL TOGGLE
     ========================================== */
  const bookingModal = document.getElementById('booking-modal');
  const openModalBtns = document.querySelectorAll('[data-action="open-booking"]');
  const closeModalBtn = document.getElementById('close-modal');

  openModalBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (bookingModal) bookingModal.classList.add('open');
    });
  });

  if (closeModalBtn && bookingModal) {
    closeModalBtn.addEventListener('click', () => {
      bookingModal.classList.remove('open');
    });
  }

  /* ==========================================
     7. BOOKING FORM & WHATSAPP LEAD GEN
     ========================================== */
  const bookingForm = document.getElementById('booking-form');

  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      let isFormValid = true;

      const fields = [
        { id: 'name', valFn: val => val.trim().length > 0 },
        { id: 'email', valFn: val => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val) },
        { id: 'interest', valFn: val => val !== '' }
      ];

      fields.forEach(field => {
        const elem = document.getElementById(field.id);
        if (elem) {
          const isValid = field.valFn(elem.value);
          const formGroup = elem.closest('.form-group');
          
          if (!isValid) {
            formGroup.classList.add('has-error');
            isFormValid = false;
          } else {
            formGroup.classList.remove('has-error');
          }
        }
      });

      if (isFormValid) {
        // Construct WhatsApp Message
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const interest = document.getElementById('interest').value;
        
        const message = `Hello Lumi SKN Concierge!\n\nI would like to request a bespoke consultation.\n\n*Name:* ${name}\n*Email:* ${email}\n*Focus Area:* ${interest}\n\nPlease let me know your earliest availability.`;
        
        // Clinic Phone Number (Include country code without '+')
        const phoneNumber = '916377335341'; 
        
        const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;
        
        // Open WhatsApp in new tab
        window.open(whatsappUrl, '_blank');
        
        // Reset and close modal
        bookingForm.reset();
        if (bookingModal) bookingModal.classList.remove('open');
      }
    });

    const inputs = bookingForm.querySelectorAll('input, select');
    inputs.forEach(input => {
      input.addEventListener('input', () => {
        const formGroup = input.closest('.form-group');
        if (formGroup) formGroup.classList.remove('has-error');
      });
      input.addEventListener('change', () => {
        const formGroup = input.closest('.form-group');
        if (formGroup) formGroup.classList.remove('has-error');
      });
    });
  }

  /* ==========================================
     7. FAQ ACCORDION TRANSITIONS
     ========================================== */
  const faqTriggers = document.querySelectorAll('.faq-trigger');

  faqTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const faqItem = trigger.closest('.faq-item');
      const faqContent = faqItem.querySelector('.faq-content');
      const isOpen = faqItem.classList.contains('open');

      document.querySelectorAll('.faq-item').forEach(item => {
        item.classList.remove('open');
        item.querySelector('.faq-content').style.maxHeight = '0px';
      });

      if (!isOpen) {
        faqItem.classList.add('open');
        faqContent.style.maxHeight = `${faqContent.scrollHeight}px`;
      }
    });
  });
  
  // Set copyright year
  const yearElem = document.getElementById('current-year');
  if(yearElem) yearElem.textContent = new Date().getFullYear();
});
