from modules.log_ingestion.log_processor import process_logs

RULES={

"failed login":"Brute Force",

"port scan":"Port Scan",

"malware":"Malware",

"ransomware":"Ransomware",

"powershell":"PowerShell Abuse",

"usb":"USB Device",

"dns tunneling":"DNS Tunneling",

"privilege escalation":"Privilege Escalation",

"firewall":"Firewall Modification",

"brute force":"Brute Force"

}

def detect_threats():

    logs=process_logs()

    alerts=[]

    for event in logs:

        message=event["message"].lower()

        for keyword,threat in RULES.items():

            if keyword in message:

                alerts.append({

                    "timestamp":event["timestamp"],

                    "severity":event["severity"],

                    "type":threat,

                    "source":event["source"],

                    "host":event["host"],

                    "ip":event["ip"],

                    "message":event["message"]

                })

                break

    return alerts