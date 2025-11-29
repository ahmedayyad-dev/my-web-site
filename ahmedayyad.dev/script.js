// ========== Utility Functions ==========
const animateCounter = (element, targetValue, duration = 50) => {
    let current = 0;
    const interval = setInterval(() => {
        if (current < targetValue) {
            element.textContent = ++current;
        } else {
            clearInterval(interval);
        }
    }, duration);
};

const calculateYearsDiff = (startDate) => {
    const today = new Date();
    let years = today.getFullYear() - startDate.getFullYear();
    const monthDiff = today.getMonth() - startDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < startDate.getDate())) years--;
    return years;
};

// ========== Age & Experience ==========
const calculateAge = () => {
    const age = calculateYearsDiff(new Date('2005-05-21'));
    const el = document.getElementById('age');
    if (el) animateCounter(el, age);
};

const updateExperience = () => {
    const years = Math.max(1, calculateYearsDiff(new Date('2021-02-05')));
    const el = document.getElementById('experience');
    if (el) animateCounter(el, years);
};

// ========== Language Toggle ==========
let currentLang = 'ar';

const toggleLanguage = () => {
    const html = document.documentElement;
    const langButton = document.getElementById('lang-toggle');

    currentLang = currentLang === 'ar' ? 'en' : 'ar';
    const isArabic = currentLang === 'ar';

    html.setAttribute('lang', currentLang);
    html.setAttribute('dir', isArabic ? 'rtl' : 'ltr');
    langButton.querySelector('.lang-text').textContent = isArabic ? 'English' : 'العربية';

    document.querySelectorAll('[data-ar][data-en]').forEach(el => {
        el.textContent = el.getAttribute(`data-${currentLang}`);
    });

    localStorage.setItem('preferred-language', currentLang);
};

// ========== Theme Toggle ==========
let currentTheme = 'dark';

const toggleTheme = () => {
    const html = document.documentElement;
    const sunIcon = document.querySelector('.sun-icon');
    const moonIcon = document.querySelector('.moon-icon');

    currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
    const isLight = currentTheme === 'light';

    html[isLight ? 'setAttribute' : 'removeAttribute']('data-theme', 'light');
    sunIcon.style.display = isLight ? 'none' : 'block';
    moonIcon.style.display = isLight ? 'block' : 'none';
    localStorage.setItem('preferred-theme', currentTheme);
};

const loadPreferredTheme = () => {
    if (localStorage.getItem('preferred-theme') === 'light') toggleTheme();
};

// ========== Skills Animation ==========
const animateSkills = () => {
    document.querySelectorAll('.skill-item').forEach((skill, i) => {
        skill.style.cssText = 'opacity:0;transform:translateY(20px)';
        setTimeout(() => {
            skill.style.cssText = 'transition:all 0.5s ease;opacity:1;transform:translateY(0)';
        }, i * 100);
    });
};

// ========== Load Preferences ==========
const loadPreferredLanguage = () => {
    const preferred = localStorage.getItem('preferred-language');
    if (preferred && preferred !== currentLang) toggleLanguage();
};

// ========== Initialize ==========
document.addEventListener('DOMContentLoaded', () => {
    document.body.classList.remove('loading');

    // Initialize
    calculateAge();
    updateExperience();
    loadPreferredLanguage();
    loadPreferredTheme();
    animateSkills();

    // Event Listeners
    document.getElementById('lang-toggle')?.addEventListener('click', toggleLanguage);
    document.getElementById('theme-toggle')?.addEventListener('click', toggleTheme);

    // Keyboard shortcuts
    document.addEventListener('keydown', e => {
        if (e.target.matches('input, textarea')) return;
        if (['l', 'L', 'ل'].includes(e.key)) toggleLanguage();
        if (['t', 'T'].includes(e.key)) toggleTheme();
    });
});

// ========== About Modal ==========
const aboutBtn = document.getElementById('about-btn');
const aboutModal = document.getElementById('about-modal');
const modalClose = document.querySelector('.modal-close');

if (aboutBtn && aboutModal) {
    aboutBtn.addEventListener('click', () => {
        aboutModal.style.display = 'block';
    });
}

if (modalClose && aboutModal) {
    modalClose.addEventListener('click', () => {
        aboutModal.style.display = 'none';
    });
}

if (aboutModal) {
    window.addEventListener('click', (e) => {
        if (e.target === aboutModal) {
            aboutModal.style.display = 'none';
        }
    });
}
