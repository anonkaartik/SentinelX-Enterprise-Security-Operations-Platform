from modules.log_ingestion.log_processor import process_logs

RULES={

"Failed login":"Brute Force Attempt",

"Port scan":"Network Reconnaissance",

"Malware":"Malware Infection",

"Ransomware":"Ransomware Activity",

"PowerShell":"Suspicious PowerShell Execution",

"USB":"USB Device Connected"

}

def detect_threats():

    logs=process_logs()

    alerts=[]

    for log in logs:

        message=log["message"]

        for keyword,threat in RULES.items():

            if keyword.lower() in message.lower():

                alerts.append({

                    "time":log["time"],

                    "severity":log["severity"],

                    "type":threat,

                    "message":message

                })

    return alerts