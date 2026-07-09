from backend.config.settings import LOG_FILE

def read_logs():

    if not LOG_FILE.exists():

        return []

    with open(LOG_FILE,"r",encoding="utf-8") as file:

        return [

            line.strip()

            for line in file

            if line.strip()

        ]