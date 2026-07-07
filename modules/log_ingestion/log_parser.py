from pathlib import Path

LOG_FILE=Path("data/logs/security_logs.log")

def read_logs():

    if not LOG_FILE.exists():
        return []

    logs=[]

    with open(LOG_FILE,"r",encoding="utf-8") as file:

        for line in file:

            line=line.strip()

            if line:

                logs.append(line)

    return logs