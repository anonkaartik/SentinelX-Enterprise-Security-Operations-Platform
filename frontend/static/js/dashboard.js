let threatChart

async function loadDashboard(){

    const response=await fetch("/api/dashboard")

    const data=await response.json()

    document.getElementById("threatCounter").innerHTML=data.kpis.threats

    document.getElementById("incidentCounter").innerHTML=data.kpis.incidents

    document.getElementById("riskCounter").innerHTML=data.kpis.risk+"%"

    document.getElementById("healthCounter").innerHTML=data.kpis.health+"%"

    loadChart(data.timeline)

    loadEvents(data.events)

    loadAlerts(data.alerts)

    loadAI(data.ai)

}

function loadChart(values){

    const ctx=document.getElementById("threatChart")

    if(threatChart){

        threatChart.destroy()

    }

    threatChart=new Chart(ctx,{
        type:"line",
        data:{
            labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
            datasets:[{
                data:values,
                borderWidth:3,
                tension:.4,
                fill:false
            }]
        },
        options:{
            responsive:true,
            plugins:{
                legend:{
                    display:false
                }
            }
        }
    })

}

function loadEvents(events){

    const tbody=document.getElementById("eventsTable")

    tbody.innerHTML=""

    events.forEach(event=>{

        tbody.innerHTML+=`
        <tr>
            <td>${event.time}</td>
            <td>${event.severity}</td>
            <td>${event.event}</td>
        </tr>
        `

    })

}

function loadAlerts(alerts){

    const tbody=document.getElementById("alertsTable")

    tbody.innerHTML=""

    alerts.forEach(alert=>{

        tbody.innerHTML+=`
        <tr>
            <td>${alert.time}</td>
            <td>${alert.severity}</td>
            <td>${alert.type}</td>
        </tr>
        `

    })

}

function loadAI(ai){

    const list=document.querySelector(".ai-list")

    list.innerHTML=""

    ai.forEach(item=>{

        list.innerHTML+=`<li>${item}</li>`

    })

}

function updateTime(){

    document.getElementById("datetime").innerHTML=

    new Date().toLocaleString("en-IN")

}

setInterval(updateTime,1000)

updateTime()

loadDashboard()