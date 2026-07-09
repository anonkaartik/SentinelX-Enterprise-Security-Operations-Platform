import re

IOC_PATTERNS={

"ipv4":r"\b(?:\d{1,3}\.){3}\d{1,3}\b",

"email":r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

"url":r"https?://[^\s]+",

"domain":r"\b(?:[a-zA-Z0-9-]+\.)+[A-Za-z]{2,}\b",

"md5":r"\b[a-fA-F0-9]{32}\b",

"sha1":r"\b[a-fA-F0-9]{40}\b",

"sha256":r"\b[a-fA-F0-9]{64}\b",

"cve":r"CVE-\d{4}-\d{4,7}",

"mitre":r"T\d{4}(?:\.\d{3})?",

"windows_path":r"[A-Za-z]:\\(?:[^\\/:*?\"<>|\r\n]+\\)*[^\\/:*?\"<>|\r\n]*",

"linux_path":r"(?:/[^/\s]+)+",

"hostname":r"\b(?:WS|PC|HR-PC|SRV)-[A-Za-z0-9-]+\b"

}

def extract_iocs(event):

    results={}

    text=event["message"]

    for name,pattern in IOC_PATTERNS.items():

        matches=re.findall(pattern,text)

        results[name]=list(set(matches))

    if event.get("ip"):

        results.setdefault("ipv4",[])

        if event["ip"] not in results["ipv4"]:

            results["ipv4"].append(event["ip"])

    if event.get("host"):

        results.setdefault("hostname",[])

        if event["host"] not in results["hostname"]:

            results["hostname"].append(event["host"])

    if event.get("user"):

        results["username"]=[event["user"]]

    return results