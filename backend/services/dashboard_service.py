from modules.log_ingestion.log_processor import process_logs

def get_dashboard_data():

    logs=process_logs()

    threats=0
    incidents=0

    events=[]

    for log in logs:

        if log["severity"] in ["WARNING","HIGH","CRITICAL"]:

            threats+=1

        if log["severity"]=="CRITICAL":

            incidents+=1

        events.append({

            "time":log["time"],

            "severity":log["severity"],

            "event":log["message"]

        })

    return{

        "kpis":{

            "threats":threats,

            "incidents":incidents,

            "risk":78,

            "health":96

        },

        "timeline":[5,8,6,9,7,10,threats],

        "events":events,

        "ai":[

            "Critical threats require immediate attention.",

            "Multiple authentication failures detected.",

            "Review PowerShell activity.",

            "Investigate ransomware indicators."

        ]

    }