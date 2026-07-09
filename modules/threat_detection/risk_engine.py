from modules.threat_detection.threat_detector import detect_threats

def calculate_risk():

    alerts=detect_threats()

    score=0

    for alert in alerts:

        if alert["severity"]=="WARNING":
            score+=5

        elif alert["severity"]=="HIGH":
            score+=12

        elif alert["severity"]=="CRITICAL":
            score+=20

    if score>100:
        score=100

    return score