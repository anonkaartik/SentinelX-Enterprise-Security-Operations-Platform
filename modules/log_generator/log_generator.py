import random
import time
from datetime import datetime

from backend.config.settings import LOG_FILE
from modules.log_generator.log_rotation import rotate_logs

EVENTS=[

("INFO","User admin logged in successfully"),

("WARNING","Failed login attempt for user root"),

("HIGH","Port scan detected"),

("CRITICAL","Malware signature detected"),

("WARNING","Multiple failed SSH logins detected"),

("HIGH","Suspicious PowerShell execution detected"),

("CRITICAL","Ransomware behavior detected"),

("WARNING","Firewall policy modified"),

("HIGH","DNS tunneling detected"),

("CRITICAL","Privilege escalation detected")

]

IPS=[

"192.168.1.12",

"10.0.0.15",

"172.16.5.22",

"203.0.113.45",

"198.51.100.78"

]

def generate_log():

    severity,message=random.choice(EVENTS)

    ip=random.choice(IPS)

    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log=f"{timestamp} {severity} {message} from {ip}"

    with open(LOG_FILE,"a",encoding="utf-8") as file:

        file.write(log+"\n")

    rotate_logs()

def start_generator():

    while True:

        generate_log()

        time.sleep(random.randint(2,5))

if __name__=="__main__":

    start_generator()