from modules.log_ingestion.log_processor import process_logs
from modules.threat_detection.threat_detector import detect_threats
from modules.threat_detection.risk_engine import calculate_risk

def get_dashboard_data():

    logs=process_logs()

    alerts=detect_threats()

    critical=0

    warning=0

    high=0

    events=[]

    for log in logs:

        events.append({

            "time":log["timestamp"].split()[1],

            "severity":log["severity"],

            "event":log["message"]

        })

        if log["severity"]=="CRITICAL":

            critical+=1

        elif log["severity"]=="HIGH":

            high+=1

        elif log["severity"]=="WARNING":

            warning+=1

    timeline=[

        warning,

        high,

        critical,

        warning+high,

        high+critical,

        warning+critical,

        len(alerts)

    ]

    return{

        "kpis":{

            "threats":len(alerts),

            "incidents":critical,

            "risk":calculate_risk(),

            "health":max(0,100-calculate_risk()//2)

        },

        "timeline":timeline,

        "events":events,

        "alerts":alerts,

        "ai":[

            f"{len(alerts)} threats detected.",

            f"{critical} critical incidents.",

            f"{high} high severity events.",

            "Continuous monitoring active."

        ]

    }