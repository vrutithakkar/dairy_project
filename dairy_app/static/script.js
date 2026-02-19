// Welcome Alert
window.onload = function() {
    console.log("Smart Dairy Loaded Successfully!");
};

// Card Click Animation
document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll(".dashboard-card");

    cards.forEach(card => {
        card.addEventListener("click", function() {
            card.style.boxShadow = "0 0 25px yellow";
            setTimeout(() => {
                card.style.boxShadow = "0 4px 15px rgba(0,0,0,0.5)";
            }, 500);
        });
    });
});
