document.addEventListener("DOMContentLoaded", () => {
  const topBtn = document.getElementById("topBtn");
  const navLinks = document.querySelectorAll(".nav-links a");
  const sections = document.querySelectorAll("main .section");

  function toggleTopButton() {
    if (!topBtn) return;
    if (window.scrollY > 300) {
      topBtn.classList.remove("hidden");
    } else {
      topBtn.classList.add("hidden");
    }
  }

  function activateCurrentSection() {
    let currentSectionId = "";

    sections.forEach((section) => {
      const sectionTop = section.offsetTop - 140;
      const sectionHeight = section.offsetHeight;

      if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
        currentSectionId = section.getAttribute("id");
      }
    });

    navLinks.forEach((link) => {
      link.classList.remove("active");
      const href = link.getAttribute("href");
      if (href === `#${currentSectionId}`) {
        link.classList.add("active");
      }
    });
  }

  function revealSections() {
    const triggerPoint = window.innerHeight * 0.9;

    sections.forEach((section) => {
      const sectionTop = section.getBoundingClientRect().top;
      if (sectionTop < triggerPoint) {
        section.classList.add("visible");
      }
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      navLinks.forEach((item) => item.classList.remove("active"));
      link.classList.add("active");
    });
  });

  if (topBtn) {
    topBtn.classList.add("hidden");
    topBtn.addEventListener("click", () => {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }

  window.addEventListener("scroll", () => {
    toggleTopButton();
    activateCurrentSection();
    revealSections();
  });

  revealSections();
  activateCurrentSection();
  toggleTopButton();
});