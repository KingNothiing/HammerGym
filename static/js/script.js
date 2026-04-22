const addScrollListener = (callback) => {
  window.addEventListener('scroll', callback, { passive: true });
};

const initNavigation = () => {
  const menuToggle = document.querySelector('.menu-toggle');
  const siteNav = document.querySelector('.site-nav');
  const navLinks = document.querySelectorAll('.site-nav a');
  const sections = document.querySelectorAll('main section[id]');

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

  const setActiveNav = () => {
    const scrollPos = window.scrollY + 120;
    sections.forEach((section) => {
      const id = section.getAttribute('id');
      const currentLink = document.querySelector(`.site-nav a[href="#${id}"]`);

      if (!currentLink) {
        return;
      }

      const top = section.offsetTop;
      const height = section.offsetHeight;
      const isActive = scrollPos >= top && scrollPos < top + height;
      currentLink.classList.toggle('active', isActive);
    });
  };

  setActiveNav();
  addScrollListener(setActiveNav);
};

const initHeader = () => {
  const siteHeader = document.querySelector('.site-header');
  if (!siteHeader) {
    return;
  }

  const handleHeaderScroll = () => {
    siteHeader.classList.toggle('scrolled', window.scrollY > 100);
  };

  handleHeaderScroll();
  addScrollListener(handleHeaderScroll);
};

const initBackToTopButton = () => {
  const backToTopButton = document.createElement('button');
  backToTopButton.className = 'back-to-top';
  backToTopButton.type = 'button';
  backToTopButton.setAttribute('aria-label', 'Вернуться наверх');
  backToTopButton.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>';
  document.body.append(backToTopButton);

  const toggleBackToTop = () => {
    backToTopButton.classList.toggle('visible', window.scrollY > 400);
  };

  backToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  toggleBackToTop();
  addScrollListener(toggleBackToTop);
};

const initRevealAnimations = () => {
  const revealItems = document.querySelectorAll('.reveal');
  if (revealItems.length === 0) {
    return;
  }

  if (!('IntersectionObserver' in window)) {
    revealItems.forEach((item) => item.classList.add('visible'));
    return;
  }

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
};

const initParallax = () => {
  const parallaxItems = document.querySelectorAll('.parallax');
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReducedMotion || parallaxItems.length === 0) {
    return;
  }

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

  handleParallax();
  addScrollListener(() => {
    if (!ticking) {
      requestAnimationFrame(handleParallax);
      ticking = true;
    }
  });
};

const initGallery = () => {
  const gallerySlides = Array.from(document.querySelectorAll('.gallery-slide'));
  const galleryDotsContainer = document.querySelector('.gallery-dots');
  const galleryPrevButton = document.querySelector('.gallery-prev');
  const galleryNextButton = document.querySelector('.gallery-next');

  if (gallerySlides.length === 0 || !galleryDotsContainer) {
    return;
  }

  let galleryIndex = 0;
  let galleryAutoSlide = null;

  const galleryDots = gallerySlides.map((_, index) => {
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.setAttribute('aria-label', `Показать фото ${index + 1}`);
    dot.addEventListener('click', () => {
      galleryIndex = index;
      renderGallery();
      restartGalleryAutoSlide();
    });
    galleryDotsContainer.append(dot);
    return dot;
  });

  const renderGallery = () => {
    gallerySlides.forEach((slide, index) => {
      const isActive = index === galleryIndex;
      slide.classList.toggle('active', isActive);
      slide.setAttribute('aria-hidden', String(!isActive));
    });

    galleryDots.forEach((dot, index) => {
      dot.classList.toggle('active', index === galleryIndex);
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
    galleryAutoSlide = window.setInterval(nextGallerySlide, 5200);
  };

  const stopGalleryAutoSlide = () => {
    if (galleryAutoSlide) {
      window.clearInterval(galleryAutoSlide);
      galleryAutoSlide = null;
    }
  };

  const restartGalleryAutoSlide = () => {
    stopGalleryAutoSlide();
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

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
      stopGalleryAutoSlide();
    } else {
      startGalleryAutoSlide();
    }
  });

  renderGallery();
  startGalleryAutoSlide();
};

const initContactForm = () => {
  const contactForm = document.getElementById('contact-form');
  if (!contactForm) {
    return;
  }

  const fullNameInput = contactForm.querySelector('#id_full_name');
  const phoneInput = contactForm.querySelector('#id_phone');
  const submitButton = contactForm.querySelector('button[type="submit"]');

  const validateName = (value) => {
    const normalised = value.trim().replace(/\s+/g, ' ');
    if (!normalised || normalised.length < 2) {
      return 'Введите имя минимум из 2 символов';
    }
    if (!/^[а-яА-ЯёЁa-zA-ZіІїЇєЄґҐ' -]+$/.test(normalised)) {
      return 'Имя может содержать только буквы, пробел, апостроф или дефис';
    }
    return null;
  };

  const validatePhone = (value) => {
    if (!value || value.trim().length === 0) {
      return 'Введите номер телефона';
    }
    const cleaned = value.replace(/\D/g, '');
    if (cleaned.length < 5) {
      return 'Укажите телефон в понятном формате';
    }
    return null;
  };

  const setFieldState = (input, message) => {
    const errorElement = document.getElementById(`error-${input.name}`);
    const hasError = Boolean(message);

    input.classList.toggle('error', hasError);
    input.classList.toggle('success', !hasError && input.value.trim().length > 0);
    input.setAttribute('aria-invalid', String(hasError));

    if (errorElement) {
      errorElement.textContent = message || '';
      errorElement.classList.toggle('visible', hasError);
    }
  };

  const attachValidation = (input, validator) => {
    if (!input) {
      return;
    }

    input.addEventListener('blur', () => {
      setFieldState(input, validator(input.value));
    });

    input.addEventListener('input', () => {
      if (!input.value.trim()) {
        setFieldState(input, '');
        return;
      }

      if (input.classList.contains('error') || input.classList.contains('success')) {
        setFieldState(input, validator(input.value));
      }
    });
  };

  attachValidation(fullNameInput, validateName);
  attachValidation(phoneInput, validatePhone);

  contactForm.addEventListener('submit', (event) => {
    const fieldChecks = [
      [fullNameInput, validateName],
      [phoneInput, validatePhone],
    ].filter(([input]) => Boolean(input));

    const invalidFields = [];
    fieldChecks.forEach(([input, validator]) => {
      const message = validator(input.value);
      setFieldState(input, message);
      if (message) {
        invalidFields.push(input);
      }
    });

    if (invalidFields.length > 0) {
      event.preventDefault();
      invalidFields[0].focus();
      return;
    }

    if (submitButton) {
      submitButton.classList.add('loading');
      submitButton.disabled = true;
    }
  });
};

const initPage = () => {
  initNavigation();
  initHeader();
  initBackToTopButton();
  initRevealAnimations();
  initParallax();
  initGallery();
  initContactForm();
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPage);
} else {
  initPage();
}
