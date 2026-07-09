from modules.log_ingestion.log_parser import read_logs
from modules.log_normalization.normalizer import normalize_log

def process_logs():

    normalized=[]

    logs=read_logs()

    for line in logs:

        parts=line.split()

        raw={

            "date":parts[0],

            "time":parts[1],

            "severity":parts[2],

            "message":" ".join(parts[3:])

        }

        normalized.append(

            normalize_log(raw)

        )

    return normalized