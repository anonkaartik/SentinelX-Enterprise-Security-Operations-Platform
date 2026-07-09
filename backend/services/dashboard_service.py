from modules.log_ingestion.log_processor import process_logs
from modules.threat_detection.threat_detector import detect_threats
from modules.threat_detection.risk_engine import calculate_risk

def get_dashboard_data():

    logs=process_logs()

    alerts=detect_threats()

    critical=0

    events=[]

    for log in logs:

        events.append({

            "time":log["time"],

            "severity":log["severity"],

            "event":log["message"]

        })

        if log["severity"]=="CRITICAL":

            critical+=1

    return{

        "kpis":{

            "threats":len(alerts),

            "incidents":critical,

            "risk":calculate_risk(),

            "health":100-calculate_risk()//2

        },

        "timeline":[

            len(alerts),

            len(alerts)-1,

            len(alerts),

            len(alerts)+1,

            len(alerts),

            len(alerts)+2,

            len(alerts)

        ],

        "events":events,

        "alerts":alerts,

        "ai":[

            "SOC analysis completed successfully.",

            f"{len(alerts)} threats detected.",

            f"{critical} critical incidents require investigation.",

            "Threat intelligence correlation pending."

        ]

    }