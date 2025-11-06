// Example: Highlight expenses over $100
document.addEventListener('DOMContentLoaded', () => {
    const rows = document.querySelectorAll("table tr");
    rows.forEach(row => {
        const amount = parseFloat(row.cells[2]?.innerText);
        if (amount > 100) {
            row.style.backgroundColor = "#ff4d4d";
        }
    });
});
