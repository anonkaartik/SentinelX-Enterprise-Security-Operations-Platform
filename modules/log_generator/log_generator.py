import random
import time
from datetime import datetime
from pathlib import Path

LOG_FILE=Path("data/logs/security_logs.log")

EVENTS=[

("INFO","User admin logged in successfully"),

("WARNING","Failed login attempt for user root"),

("HIGH","Port scan detected"),

("CRITICAL","Malware signature detected"),

("INFO","Scheduled backup completed"),

("WARNING","Multiple failed SSH logins detected"),

("HIGH","Suspicious PowerShell execution detected"),

("INFO","User analyst logged out"),

("CRITICAL","Ransomware behavior detected"),

("WARNING","USB storage device connected"),

("HIGH","DNS tunneling detected"),

("CRITICAL","Privilege escalation detected"),

("WARNING","Firewall policy modified"),

("HIGH","Brute force attack detected"),

("INFO","VPN connection established")

]

IPS=[

"192.168.1.15",

"10.0.0.25",

"172.16.0.12",

"203.0.113.45",

"198.51.100.22",

"185.22.67.88",

"91.240.118.120"

]

def generate_log():

    severity,message=random.choice(EVENTS)

    ip=random.choice(IPS)

    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line=f"{timestamp} {severity} {message} from {ip}"

    with open(LOG_FILE,"a",encoding="utf-8") as file:

        file.write(line+"\n")

def start_generator():

    while True:

        generate_log()

        time.sleep(random.randint(2,5))

if __name__=="__main__":

    start_generator()  