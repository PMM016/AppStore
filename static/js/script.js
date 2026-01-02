document.addEventListener("DOMContentLoaded", () => {
  const headers = document.querySelectorAll(".app-header");

  if (!headers.length) return;

  window.addEventListener("scroll", () => {
    headers.forEach(header => {
      if (window.scrollY > 10) {
        header.classList.add("scroll");
      } else {
        header.classList.remove("scroll");
      }
    });
  });
});
