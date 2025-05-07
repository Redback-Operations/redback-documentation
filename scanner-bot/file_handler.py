import json

def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def save_report(data):
    with open("reports/scan_report.json", "w") as f:
        json.dump(data, f, indent=4)
