document.addEventListener("DOMContentLoaded", function () {
  const config = {
    brand_name: "Dr.CodeMagic",
    hero_title: "طراحی سایت حرفه‌ای با Django&Python",
    hero_subtitle: "فروشگاهی • شرکتی • شخصی",
    services_title: "خدمات من",
    service_1_title: "سایت فروشگاهی",
    service_2_title: "سایت شرکتی",
    service_3_title: "سایت شخصی",
    portfolio_title: "نمونه کارهای من",
    contact_title: "بیایید شروع کنیم",
    github_username: "DrCodeMagic",
    whatsapp_number: "09921609084",
    telegram_number: "09921609084",

    hero_button: "شروع پروژه 🚀"
  };

  // Set text content
  document.getElementById('brand-logo').textContent = config.brand_name;
  document.getElementById('hero-title').textContent = config.hero_title;
  document.getElementById('hero-subtitle').textContent = config.hero_subtitle;
  document.getElementById('services-title').textContent = config.services_title;
  document.getElementById('service-1-title').textContent = config.service_1_title;
  document.getElementById('service-2-title').textContent = config.service_2_title;
  document.getElementById('service-3-title').textContent = config.service_3_title;
  document.getElementById('portfolio-title').textContent = config.portfolio_title;
  document.getElementById('contact-title').textContent = config.contact_title;
  document.getElementById('github-username').textContent = config.github_username;
  document.getElementById('whatsapp-number').textContent = config.whatsapp_number;
  document.getElementById('hero-button').textContent = config.hero_button;

  // Set links
  document.getElementById('github-link').href = `https://github.com/${config.github_username}`;
  const cleanNumber = config.whatsapp_number.replace(/\s/g, '');
  document.getElementById('whatsapp-link').href = `https://wa.me/98${cleanNumber.startsWith('0') ? cleanNumber.substring(1) : cleanNumber}`;

  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.getElementById(this.getAttribute('href').substring(1));
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
});


