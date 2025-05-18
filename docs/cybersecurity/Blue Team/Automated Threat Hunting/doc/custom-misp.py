#!/usr/bin/env python3
import sys
import os
import json
import requests
import ipaddress
import re
from socket import socket, AF_UNIX, SOCK_DGRAM

print("=== custom-misp.py START ===")
print("Arguments received:", sys.argv)

pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
socket_addr = f"{pwd}/queue/sockets/queue"

# MISP Configuration
misp_base_url = "https://192.168.0.211/attributes/restSearch/"
misp_api_auth_key = "<API Key>"
misp_apicall_headers = {
    "Content-Type": "application/json",
    "Authorization": misp_api_auth_key,
    "Accept": "application/json"
}

# Helper to send enriched output back to Wazuh queue
def send_event(msg, agent=None):
    string = f"1:[{agent.get('id', '000')}] ({agent.get('name', 'unknown')}) {agent.get('ip', 'any')}->misp:{json.dumps(msg)}" \
        if agent else f"1:misp:{json.dumps(msg)}"
    sock = socket(AF_UNIX, SOCK_DGRAM)
    sock.connect(socket_addr)
    sock.send(string.encode())
    sock.close()

# Read and process alerts line-by-line
try:
    with open(sys.argv[1], 'r') as alert_file:
        for line in alert_file:
            try:
                alert = json.loads(line)
                print("[*] Loaded alert:")
                print(json.dumps(alert, indent=2))
            except json.JSONDecodeError as e:
                print(f"[!] JSON decode error: {e}")
                continue

            alert_output = {}

            # Extract and validate IP address
            try:
                data = alert.get("data", {})
                ip = data.get("srcip") or data.get("src_ip")
                if not ip:
                    print("[-] No srcip or src_ip field found. Skipping.")
                    continue
                if not ipaddress.ip_address(ip).is_global:
                    print(f"[-] Skipping non-public IP: {ip}")
                    continue
                misp_search_value = f"value:{ip}"
            except Exception as e:
                print(f"[-] Error extracting IP: {e}")
                continue

            # Prepare MISP search
            misp_search_url = f"{misp_base_url}{misp_search_value}"
            print(f"[*] Querying MISP for: {misp_search_url}")

            try:
                misp_api_response = requests.get(misp_search_url, headers=misp_apicall_headers, verify=False).json()
                print("[*] MISP response:")
                print(json.dumps(misp_api_response, indent=2))
            except Exception as e:
                print(f"[-] MISP API error: {e}")
                alert_output["integration"] = "misp"
                alert_output["misp"] = {"error": "Connection Error to MISP API"}
                send_event(alert_output, alert.get("agent", {}))
                continue

            # MISP match handling
            if misp_api_response.get("response", {}).get("Attribute"):
                print("[+] MISP HIT: IOC match found!")
                attr = misp_api_response["response"]["Attribute"][0]
                alert_output["integration"] = "misp"
                alert_output["misp"] = {
                    "event_id": attr.get("event_id"),
                    "category": attr.get("category"),
                    "value": attr.get("value"),
                    "type": attr.get("type")
                }

                print("[*] Sending enriched alert:")
                print(json.dumps(alert_output, indent=2))
                send_event(alert_output, alert.get("agent", {}))
                print("[*] Sent to Wazuh.")
            else:
                print("[-] No MISP match found.")

except Exception as e:
    print(f"[!] Fatal error processing alerts: {e}")
    sys.exit(1)

