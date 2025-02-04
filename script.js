// Collapsible content functionality
const collapseButtons = document.getElementsByClassName('collapse-btn');
for (let i = 0; i < collapseButtons.length; i++) {
    collapseButtons[i].addEventListener('click', function () {
        const content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}

// Collapsible Info
document.querySelectorAll('.collapse-btn').forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        content.style.display = content.style.display === 'block' ? 'none' : 'block';
    });
});

// Dashboard Charts
const ctxProduction = document.getElementById('productionChart').getContext('2d');
new Chart(ctxProduction, {
    type: 'line',
    data: {
        labels: ['2020', '2021', '2022', '2023'],
        datasets: [{
            label: 'Sugarcane Production (tons)',
            data: [450000, 470000, 480000, 500000],
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: true,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: true },
        }
    }
});

const ctxGlobalProduction = document.getElementById('globalProductionChart').getContext('2d');
new Chart(ctxGlobalProduction, {
    type: 'doughnut',
    data: {
        labels: ['Brazil', 'India', 'Thailand', 'Others'],
        datasets: [{
            label: 'Global Sugarcane Production',
            data: [39, 20, 10, 31],
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#A2EB36'],
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: true },
        }
    }
});
