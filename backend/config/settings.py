from pathlib import Path

BASE_DIR=Path(__file__).resolve().parents[2]

LOG_DIRECTORY=BASE_DIR/"data"/"logs"

LOG_FILE=LOG_DIRECTORY/"security_logs.log"

MAX_LOG_LINES=1000

MAX_DASHBOARD_EVENTS=50

MAX_ALERTS=20

REFRESH_INTERVAL=3000