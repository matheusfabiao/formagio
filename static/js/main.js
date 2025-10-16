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
        const headerOffset = document.querySelector('header').offsetHeight || 100; // Fallback para 100px

        // Verifica se é um link para uma âncora na página atual
        if (href.startsWith('#')) {
            e.preventDefault();
            const targetId = href.substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                lenis.scrollTo(targetElement, { offset: -headerOffset });
            }
        } else {
            // É um link para outra página com uma âncora
            const urlParts = href.split('#');
            const pageUrl = urlParts[0];
            const targetId = urlParts[1];

            // Se o link for para a página atual, apenas role
            if (pageUrl === window.location.pathname || pageUrl === '') {
                e.preventDefault();
                const targetElement = document.getElementById(targetId);
                if (targetElement) {
                    lenis.scrollTo(targetElement, { offset: -headerOffset });
                }
            }
            // Se for um link para outra página, deixe o navegador lidar com isso,
            // mas podemos armazenar o targetId para rolar após o carregamento da página.
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
            const headerOffset = document.querySelector('header').offsetHeight || 100;
            setTimeout(() => {
                lenis.scrollTo(targetElement, { offset: -headerOffset });
            }, 100); // Um pequeno atraso para garantir que a página esteja totalmente renderizada
        }
    }
});

// Read More Functionality
document.addEventListener('DOMContentLoaded', function() {
    const guestGrids = document.querySelectorAll('.guest-grid');

    guestGrids.forEach(grid => {
        grid.addEventListener('click', function(e) {
            if (e.target.classList.contains('read-more')) {
                e.preventDefault();
                const card = e.target.closest('.card');
                const shortMessage = card.querySelector('.short-message');
                const fullMessage = card.querySelector('.full-message');

                if (card.classList.contains('expanded')) {
                    card.classList.remove('expanded');
                    e.target.textContent = 'Leia Mais';
                    fullMessage.style.display = 'none';
                    shortMessage.style.display = 'block';
                } else {
                    card.classList.add('expanded');
                    e.target.textContent = 'Leia Menos';
                    shortMessage.style.display = 'none';
                    fullMessage.style.display = 'block';
                }
            }
        });
    });
});
