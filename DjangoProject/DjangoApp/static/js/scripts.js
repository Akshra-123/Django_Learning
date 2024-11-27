// Toggle navigation for mobile devices
document.addEventListener("DOMContentLoaded", function () {
    const toggleMenu = document.querySelector("#menu-toggle");
    const navMenu = document.querySelector("nav ul");

    if (toggleMenu) {
        toggleMenu.addEventListener("click", function () {
            navMenu.classList.toggle("show");
        });
    }
});
