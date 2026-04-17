const menuToggle = document.querySelector('.menu-toggle');
const siteNav = document.querySelector('.site-nav');
const navLinks = document.querySelectorAll('.site-nav a');

if (menuToggle && siteNav) {
  menuToggle.addEventListener('click', () => {
    const expanded = menuToggle.getAttribute('aria-expanded') === 'true';
    menuToggle.setAttribute('aria-expanded', String(!expanded));
    menuToggle.classList.toggle('active');
    siteNav.classList.toggle('open');
  });
}

navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    if (siteNav && menuToggle && siteNav.classList.contains('open')) {
      siteNav.classList.remove('open');
      menuToggle.classList.remove('active');
      menuToggle.setAttribute('aria-expanded', 'false');
    }
  });
});

const sections = document.querySelectorAll('main section[id]');

const setActiveNav = () => {
  const scrollPos = window.scrollY + 120;
  sections.forEach((section) => {
    const top = section.offsetTop;
    const height = section.offsetHeight;
    const id = section.getAttribute('id');
    const currentLink = document.querySelector(`.site-nav a[href="#${id}"]`);

    if (currentLink) {
      const isActive = scrollPos >= top && scrollPos < top + height;
      currentLink.classList.toggle('active', isActive);
    }
  });
};

setActiveNav();
window.addEventListener('scroll', setActiveNav);

// Sticky header with scroll effect
const siteHeader = document.querySelector('.site-header');
let lastScroll = 0;

const handleHeaderScroll = () => {
  const currentScroll = window.scrollY;

  if (currentScroll > 100) {
    siteHeader.classList.add('scrolled');
  } else {
    siteHeader.classList.remove('scrolled');
  }

  lastScroll = currentScroll;
};

window.addEventListener('scroll', handleHeaderScroll);

// Back to top button
const backToTopButton = document.createElement('button');
backToTopButton.className = 'back-to-top';
backToTopButton.setAttribute('aria-label', 'Вернуться наверх');
backToTopButton.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>';
document.body.appendChild(backToTopButton);

const toggleBackToTop = () => {
  if (window.scrollY > 400) {
    backToTopButton.classList.add('visible');
  } else {
    backToTopButton.classList.remove('visible');
  }
};

backToTopButton.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

window.addEventListener('scroll', toggleBackToTop);

const revealItems = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.16,
    rootMargin: '0px 0px -40px 0px',
  }
);

revealItems.forEach((item) => revealObserver.observe(item));

const parallaxItems = document.querySelectorAll('.parallax');
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReducedMotion && parallaxItems.length > 0) {
  let ticking = false;

  const handleParallax = () => {
    const scrollTop = window.scrollY;

    parallaxItems.forEach((item) => {
      const speed = Number(item.dataset.speed || 0.06);
      const offset = scrollTop * speed;
      item.style.setProperty('--parallax-offset', `${offset}px`);
    });

    ticking = false;
  };

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(handleParallax);
      ticking = true;
    }
  });
}

const gallerySlides = Array.from(document.querySelectorAll('.gallery-slide'));
const galleryDotsContainer = document.querySelector('.gallery-dots');
const galleryPrevButton = document.querySelector('.gallery-prev');
const galleryNextButton = document.querySelector('.gallery-next');
let galleryIndex = 0;
let galleryAutoSlide;

if (gallerySlides.length > 0 && galleryDotsContainer) {
  const galleryDots = gallerySlides.map((_, i) => {
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.setAttribute('aria-label', `Показать фото ${i + 1}`);
    dot.addEventListener('click', () => {
      galleryIndex = i;
      renderGallery();
      restartGalleryAutoSlide();
    });
    galleryDotsContainer.append(dot);
    return dot;
  });

  const renderGallery = () => {
    gallerySlides.forEach((slide, i) => {
      const isActive = i === galleryIndex;
      slide.classList.toggle('active', isActive);
      slide.setAttribute('aria-hidden', String(!isActive));
    });

    galleryDots.forEach((dot, i) => {
      dot.classList.toggle('active', i === galleryIndex);
    });
  };

  const nextGallerySlide = () => {
    galleryIndex = (galleryIndex + 1) % gallerySlides.length;
    renderGallery();
  };

  const prevGallerySlide = () => {
    galleryIndex = (galleryIndex - 1 + gallerySlides.length) % gallerySlides.length;
    renderGallery();
  };

  const startGalleryAutoSlide = () => {
    galleryAutoSlide = setInterval(nextGallerySlide, 5200);
  };

  const restartGalleryAutoSlide = () => {
    clearInterval(galleryAutoSlide);
    startGalleryAutoSlide();
  };

  if (galleryNextButton) {
    galleryNextButton.addEventListener('click', () => {
      nextGallerySlide();
      restartGalleryAutoSlide();
    });
  }

  if (galleryPrevButton) {
    galleryPrevButton.addEventListener('click', () => {
      prevGallerySlide();
      restartGalleryAutoSlide();
    });
  }

  renderGallery();
  startGalleryAutoSlide();
}

// Form validation
const contactForm = document.getElementById('contact-form');

if (contactForm) {
  const fullNameInput = contactForm.querySelector('#id_full_name');
  const phoneInput = contactForm.querySelector('#id_phone');
  const submitButton = contactForm.querySelector('button[type="submit"]');

  // Validation functions
  const validateName = (value) => {
    if (!value || value.trim().length < 2) {
      return 'Введите имя (минимум 2 символа)';
    }
    if (!/^[а-яА-ЯёЁa-zA-Z\s-]+$/.test(value)) {
      return 'Имя может содержать только буквы';
    }
    return null;
  };

  const validatePhone = (value) => {
    if (!value || value.trim().length === 0) {
      return 'Введите номер телефона';
    }
    const cleaned = value.replace(/\D/g, '');
    if (cleaned.length < 10) {
      return 'Номер телефона слишком короткий';
    }
    return null;
  };

  const showError = (input, message) => {
    const errorId = 'error-' + input.name;
    const errorElement = document.getElementById(errorId);

    input.classList.add('error');
    input.classList.remove('success');

    if (errorElement) {
      errorElement.textContent = message;
      errorElement.classList.add('visible');
    }
  };

  const showSuccess = (input) => {
    const errorId = 'error-' + input.name;
    const errorElement = document.getElementById(errorId);

    input.classList.remove('error');
    input.classList.add('success');

    if (errorElement) {
      errorElement.textContent = '';
      errorElement.classList.remove('visible');
    }
  };

  const clearValidation = (input) => {
    const errorId = 'error-' + input.name;
    const errorElement = document.getElementById(errorId);

    input.classList.remove('error', 'success');

    if (errorElement) {
      errorElement.textContent = '';
      errorElement.classList.remove('visible');
    }
  };

  // Real-time validation
  if (fullNameInput) {
    fullNameInput.addEventListener('blur', () => {
      const error = validateName(fullNameInput.value);
      if (error) {
        showError(fullNameInput, error);
      } else if (fullNameInput.value.trim()) {
        showSuccess(fullNameInput);
      }
    });

    fullNameInput.addEventListener('input', () => {
      if (fullNameInput.classList.contains('error')) {
        const error = validateName(fullNameInput.value);
        if (!error) {
          showSuccess(fullNameInput);
        }
      }
    });
  }

  if (phoneInput) {
    phoneInput.addEventListener('blur', () => {
      const error = validatePhone(phoneInput.value);
      if (error) {
        showError(phoneInput, error);
      } else if (phoneInput.value.trim()) {
        showSuccess(phoneInput);
      }
    });

    phoneInput.addEventListener('input', () => {
      if (phoneInput.classList.contains('error')) {
        const error = validatePhone(phoneInput.value);
        if (!error) {
          showSuccess(phoneInput);
        }
      }
    });
  }

  // Form submission
  contactForm.addEventListener('submit', (e) => {
    let hasErrors = false;

    // Validate name
    if (fullNameInput) {
      const nameError = validateName(fullNameInput.value);
      if (nameError) {
        showError(fullNameInput, nameError);
        hasErrors = true;
      } else {
        showSuccess(fullNameInput);
      }
    }

    // Validate phone
    if (phoneInput) {
      const phoneError = validatePhone(phoneInput.value);
      if (phoneError) {
        showError(phoneInput, phoneError);
        hasErrors = true;
      } else {
        showSuccess(phoneInput);
      }
    }

    if (hasErrors) {
      e.preventDefault();
      return;
    }

    // Show loading state
    submitButton.classList.add('loading');
    submitButton.disabled = true;
  });
}
