// Mobile nav toggle
const burger = document.querySelector('.burger')
const nav = document.querySelector('.nav-links')

if (burger && nav) {
  burger.addEventListener('click', () => {
    nav.classList.toggle('active')
  })
}

// Chart (only if present)
const chartCanvas = document.getElementById('taskChart')

if (chartCanvas && window.taskStats) {
  const ctx = chartCanvas.getContext('2d')

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Backlog', 'Pending', 'In-Progress', 'Completed'],
      datasets: [
        {
          data: [
            window.taskStats.backlog,
            window.taskStats.pending,
            window.taskStats['in-progress'],
            window.taskStats.completed,
          ],
          backgroundColor: ['#FFC107', '#FF5722', '#03A9F4', '#4CAF50'],
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' },
        maintainAspectRatio: false,
      },
    },
  })
}

console.log(window.taskStats)
