document.addEventListener('DOMContentLoaded', () => {
    // Check for stored theme preference and apply it
    const storedTheme = localStorage.getItem('theme');
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    if (storedTheme) {
        document.body.classList.add(storedTheme);
        if (storedTheme === 'dark-mode') {
            themeIcon.classList.remove('bi-sun-fill');
            themeIcon.classList.add('bi-moon-fill');
            themeToggle.title = "Dark Mode";
        } else {
            themeToggle.title = "Light Mode";
        }
    } else {
        themeToggle.title = "Light Mode";
    }
    
    // Add event listener to the theme toggle button
    themeToggle.addEventListener('click', toggleTheme);
});

function toggleTheme() {
    // Toggle between light and dark mode
    const isDarkMode = document.body.classList.toggle('dark-mode');
    
    // Update the icon and title based on the theme
    const themeIcon = document.getElementById('theme-icon');
    const themeToggle = document.getElementById('theme-toggle');

    if (isDarkMode) {
        themeIcon.classList.remove('bi-sun-fill');
        themeIcon.classList.add('bi-moon-fill');
        themeToggle.title = "Dark Mode";
        localStorage.setItem('theme', 'dark-mode');
    } else {
        themeIcon.classList.remove('bi-moon-fill');
        themeIcon.classList.add('bi-sun-fill');
        themeToggle.title = "Light Mode";
        localStorage.setItem('theme', 'light-mode');
    }
}
