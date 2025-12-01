// Timeline interactive
document.addEventListener('DOMContentLoaded', function() {
    // Animation au scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observer tous les événements de la timeline
    document.querySelectorAll('.timeline-event, .schema-box').forEach(el => {
        observer.observe(el);
    });

    // Effet hover sur les événements
    document.querySelectorAll('.timeline-event').forEach(event => {
        event.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        event.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observer tous les événements de la timeline et les boîtes
    document.querySelectorAll('.timeline-event, .schema-box, .info-card').forEach(el => {
        observer.observe(el);
    });

    // Smooth scroll pour les liens internes
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Animation spéciale pour les info-cards au survol
    document.querySelectorAll('.info-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});


// ============================================
// FONCTIONNALITÉS POUR PAGE LONGUE
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ========================================
    // 1. BARRE DE PROGRESSION DE LECTURE
    // ========================================
    const progressBar = document.createElement('div');
    progressBar.className = 'reading-progress';
    document.body.prepend(progressBar);
    
    window.addEventListener('scroll', function() {
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight - windowHeight;
        const scrolled = window.scrollY;
        const progress = (scrolled / documentHeight) * 100;
        progressBar.style.width = progress + '%';
    });
    
    // ========================================
    // 2. BOUTON RETOUR EN HAUT
    // ========================================
    const backToTop = document.createElement('button');
    backToTop.className = 'back-to-top';
    backToTop.innerHTML = '↑';
    backToTop.setAttribute('aria-label', 'Retour en haut');
    document.body.appendChild(backToTop);
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });
    
    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    // ========================================
    // 3. HIGHLIGHT SECTION ACTIVE DANS SOMMAIRE
    // ========================================
    const sections = document.querySelectorAll('.cours-content section[id]');
    const navLinks = document.querySelectorAll('.table-of-contents a');
    
    function highlightActiveSection() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= (sectionTop - 150)) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    }
    
    window.addEventListener('scroll', highlightActiveSection);
    highlightActiveSection(); // Initial call
    
    // ========================================
    // 4. SMOOTH SCROLL AMÉLIORÉ
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 100;
                const elementPosition = target.offsetTop;
                const offsetPosition = elementPosition - headerOffset;
                
                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // ========================================
    // 5. SAUVEGARDE POSITION DE LECTURE (LocalStorage)
    // ========================================
    const pageKey = 'scroll_' + window.location.pathname;
    
    // Restaurer la position au chargement
    const savedPosition = localStorage.getItem(pageKey);
    if (savedPosition) {
        setTimeout(() => {
            window.scrollTo(0, parseInt(savedPosition));
        }, 100);
    }
    
    // Sauvegarder la position toutes les secondes
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
            localStorage.setItem(pageKey, window.scrollY);
        }, 1000);
    });
});