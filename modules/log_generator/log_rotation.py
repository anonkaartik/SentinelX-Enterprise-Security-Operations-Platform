from backend.config.settings import LOG_FILE,MAX_LOG_LINES

def rotate_logs():

    if not LOG_FILE.exists():

        return

    with open(LOG_FILE,"r",encoding="utf-8") as file:

        lines=file.readlines()

    if len(lines)<=MAX_LOG_LINES:

        return

    lines=lines[-MAX_LOG_LINES:]

    with open(LOG_FILE,"w",encoding="utf-8") as file:

        file.writelines(lines)