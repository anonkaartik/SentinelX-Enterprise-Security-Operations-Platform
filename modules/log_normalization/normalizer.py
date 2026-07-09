import re

def normalize_log(log):

    event={

        "timestamp":f"{log['date']} {log['time']}",

        "severity":log["severity"],

        "source":"Unknown",

        "event_type":"General",

        "host":None,

        "user":None,

        "ip":None,

        "message":log["message"]

    }

    ip=re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b",log["message"])

    if ip:

        event["ip"]=ip.group()

    user=re.search(r"user\s+([A-Za-z0-9_-]+)",log["message"],re.IGNORECASE)

    if user:

        event["user"]=user.group(1)

    host=re.search(r"(WS-\d+|HR-PC-\d+)",log["message"])

    if host:

        event["host"]=host.group()

    message=log["message"].lower()

    if "login" in message:

        event["event_type"]="Authentication"

    elif "malware" in message:

        event["event_type"]="Malware"

    elif "ransomware" in message:

        event["event_type"]="Ransomware"

    elif "port scan" in message:

        event["event_type"]="Reconnaissance"

    elif "powershell" in message:

        event["event_type"]="PowerShell"

    elif "usb" in message:

        event["event_type"]="USB Activity"

    return event