// Set current year in footer
document.getElementById('current-year').textContent = new Date().getFullYear();

// Menu 
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const mobileMenu = document.querySelector('.mobile-menu');

mobileMenuBtn.addEventListener('click', () => {
  mobileMenu.classList.toggle('show');
});

// Chiude il menu
const mobileLinks = document.querySelectorAll('.mobile-link');
mobileLinks.forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('show');
  });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    if (this.getAttribute('href') !== "#") {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        const navbarHeight = document.querySelector('.navbar').offsetHeight;
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
        
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    }
  });
});

//Scrollamento quando clicco il pulsante
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('.nav-link');
  
  let current = '';
  
  sections.forEach(section => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;
    if (pageYOffset >= sectionTop - 200) {
      current = section.getAttribute('id');
    }
  });
  
  navLinks.forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
});

// Counter Animati
function animateCounters() {
  const counters = document.querySelectorAll('.stat-count');
  
  counters.forEach(counter => {
    const target = +counter.getAttribute('data-target');
    const duration = 2000; // Duration in milliseconds
    const increment = target / (duration / 16); // 60fps
    
    let count = 0;
    
    const updateCount = () => {
      count += increment;
      
      if (count < target) {
        counter.textContent = Math.floor(count);
        requestAnimationFrame(updateCount);
      } else {
        counter.textContent = target;
      }
    };
    
    updateCount();
  });
}

const fadeElements = document.querySelectorAll('.fade-in');

const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      fadeObserver.unobserve(entry.target);
      
      // Animate counters if this is the about section
      if (entry.target.closest('.about')) {
        setTimeout(animateCounters, 500);
      }
    }
  });
}, {
  threshold: 0.1
});

fadeElements.forEach(element => {
  fadeObserver.observe(element);
});