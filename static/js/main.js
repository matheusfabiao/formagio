// Navbar Background Change
const navbar = document.getElementById('navbar');
let lastScrollY = window.scrollY;

window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;
    
    if (currentScrollY > 1) {
        // Se estiver rolando para baixo e não tiver a classe, adiciona
        if (!navbar.classList.contains('scrolled', 'box-shadow-bottom')) {
            navbar.classList.add('scrolled', 'box-shadow-bottom');
        }
    } else {
        // Se estiver no topo e tiver a classe, remove
        if (navbar.classList.contains('scrolled', 'box-shadow-bottom')) {
            navbar.classList.remove('scrolled', 'box-shadow-bottom');
        }
    }
    
    lastScrollY = currentScrollY;
});

// Initialize Lenis
const lenis = new Lenis({
  autoRaf: true,
});

// Listen for the scroll event and log the event data
lenis.on('scroll', (e) => {
  console.log(e);
});

// Initialize AOS
AOS.init({
  once: true, 
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"], a[href*="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        
        // Check if it's a link to an anchor on the current page
        if (href.startsWith('#')) {
            e.preventDefault();
            const targetId = href.substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                lenis.scrollTo(targetElement);
            }
        } else {
            // It's a link to another page with an anchor
            const urlParts = href.split('#');
            const pageUrl = urlParts[0];
            const targetId = urlParts[1];

            // If the link is to the current page, just scroll
            if (pageUrl === window.location.pathname || pageUrl === '') {
                e.preventDefault();
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    lenis.scrollTo(targetElement);
                }
            }
            // If it's a link to another page, let the browser handle it,
            // but we can store the targetId to scroll after page load.
            else {
                sessionStorage.setItem('scrollTo', '#' + targetId);
            }
        }
    });
});

// On page load, check if we need to scroll to a section
window.addEventListener('load', () => {
    const scrollTo = sessionStorage.getItem('scrollTo');
    if (scrollTo) {
        sessionStorage.removeItem('scrollTo');
        const targetElement = document.querySelector(scrollTo);
        if (targetElement) {
            setTimeout(() => {
                lenis.scrollTo(targetElement);
            }, 100); // A small delay to ensure the page is fully rendered
        }
    }
});
