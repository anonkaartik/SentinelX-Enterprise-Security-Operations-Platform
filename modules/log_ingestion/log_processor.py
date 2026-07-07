from modules.log_ingestion.log_parser import read_logs

def process_logs():

    parsed=[]

    logs=read_logs()

    for log in logs:

        parts=log.split()

        parsed.append({

            "date":parts[0],

            "time":parts[1],

            "severity":parts[2],

            "message":" ".join(parts[3:])

        })

    return parsed