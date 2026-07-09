from modules.log_ingestion.log_processor import process_logs
from modules.ioc_extractor.extractor import extract_iocs

def generate_ioc_report():

    logs=process_logs()

    report=[]

    for event in logs:

        report.append({

            "timestamp":event["timestamp"],

            "severity":event["severity"],

            "iocs":extract_iocs(event)

        })

    return report