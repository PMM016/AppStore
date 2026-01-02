// Sticky header shadow
  const header = document.getElementById('appsHeader');
  window.addEventListener('scroll', () => {
      if (window.scrollY > 5) {
          header.classList.add('scrolled');
      } else {
          header.classList.remove('scrolled');
      }
  });

  // Mobile toggle
  const toggleBtn = document.getElementById('mobileToggle');
  const headerRight = document.getElementById('headerRight');
  const overlay = document.getElementById('mobileOverlay');

  toggleBtn.addEventListener('click', () => {
      const show = !headerRight.classList.contains('show');
      headerRight.classList.toggle('show', show);
      overlay.classList.toggle('show', show);
      document.body.classList.toggle('open', show);
  });

  overlay.addEventListener('click', () => {
      headerRight.classList.remove('show');
      overlay.classList.remove('show');
      document.body.classList.remove('open');
  });

  document.querySelectorAll(".categories").forEach(cat => {
  cat.addEventListener("keydown", e => {
    if (e.key === "ArrowRight") {
      cat.scrollLeft += 80;
    }
    if (e.key === "ArrowLeft") {
      cat.scrollLeft -= 80;
    }
  });
});