let threatChart = null

async function loadDashboard() {

    try {

        const response = await fetch("/api/dashboard")

        const data = await response.json()

        updateKPIs(data.kpis)

        updateChart(data.timeline)

        updateEvents(data.events)

        updateAlerts(data.alerts)

        updateAI(data.ai)

    }

    catch (error) {

        console.error("Dashboard Error:", error)

    }

}

function updateKPIs(kpis) {

    document.getElementById("threatCounter").textContent = kpis.threats

    document.getElementById("incidentCounter").textContent = kpis.incidents

    document.getElementById("riskCounter").textContent = kpis.risk + "%"

    document.getElementById("healthCounter").textContent = kpis.health + "%"

}

function updateChart(values) {

    const ctx = document.getElementById("threatChart")

    const labels = values.map((_, index) => index + 1)

    if (threatChart) {

        threatChart.data.labels = labels

        threatChart.data.datasets[0].data = values

        threatChart.update()

        return

    }

    threatChart = new Chart(ctx, {

        type: "line",

        data: {

            labels: labels,

            datasets: [

                {

                    label: "Threat Activity",

                    data: values,

                    borderWidth: 3,

                    tension: 0.4,

                    fill: false

                }

            ]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            animation: {

                duration: 600

            },

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                x: {

                    title: {

                        display: true,

                        text: "Recent Events"

                    }

                },

                y: {

                    beginAtZero: true,

                    title: {

                        display: true,

                        text: "Severity"

                    }

                }

            }

        }

    })

}

function updateEvents(events) {

    const table = document.getElementById("eventsTable")

    table.innerHTML = ""

    events.slice().reverse().forEach(event => {

        table.innerHTML += `

        <tr>

            <td>${event.time}</td>

            <td>${event.severity}</td>

            <td>${event.event}</td>

        </tr>

        `

    })

}

function updateAlerts(alerts) {

    const table = document.getElementById("alertsTable")

    table.innerHTML = ""

    alerts.slice().reverse().forEach(alert => {

        table.innerHTML += `

        <tr>

            <td>${alert.time || alert.timestamp}</td>

            <td>${alert.severity}</td>

            <td>${alert.type}</td>

        </tr>

        `

    })

}

function updateAI(ai) {

    const list = document.querySelector(".ai-list")

    list.innerHTML = ""

    ai.forEach(item => {

        list.innerHTML += `<li>${item}</li>`

    })

}

function updateClock() {

    const clock = document.getElementById("datetime")

    if (clock) {

        clock.textContent = new Date().toLocaleString("en-IN")

    }

}

updateClock()

loadDashboard()

setInterval(updateClock, 1000)

setInterval(loadDashboard, 3000)