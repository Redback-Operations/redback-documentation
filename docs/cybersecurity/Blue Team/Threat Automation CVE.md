# CVE Hunter Script Progress Report

**Author:** Muhammad Arsalan Khan  
**Date:** 4 April 2025  
**Project:** Automated CVE Threat Hunter (Docker-based Python Script)

---

## Environment Setup

- **OS:** Ubuntu 18.04 (VirtualBox)
- **Tools Used:**
  - Docker
  - Python 3.10 (slim image)
  - `requests`, `tabulate`, `socket` Python modules
  - CVE Data source: [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0)

---

## Script Setup Steps

1. Created working directory:
   ```bash
   mkdir ~/cve-hunter && cd ~/cve-hunter
   ```
2. Created files:
   - `hunter.py` - Core Python script
   - `requirements.txt` - Python dependencies
   - `Dockerfile` - For containerized execution

3. Built Docker image:
   ```bash
   sudo docker build -t cve-hunter .
   ```

4. Executed script:
   ```bash
   sudo docker run cve-hunter
   ```

![Docker Script Execution](./ThreatAutomationAssets/docker_run_output.png)

---

## Verified CVEs Detected

1. **CVE-2023-38408** – OpenSSH agent forwarding RCE  
2. **CVE-2021-3156** – Sudo buffer overflow  
3. **CVE-2021-4034** – Polkit pkexec privilege escalation  
4. **CVE-2024-8376** – Mosquitto MQTT DoS  

![CVE Detection Output](./ThreatAutomationAssets/cve_detection_output.png)

---

## CVE Log Correlation Script

```python
# Python log correlation snippet here...
```

![Log Correlation Output](./ThreatAutomationAssets/log_scan_output.png)

---

## SIEM Detection Rules (Wazuh)

- **Rule ID:** 100100  
- **Search Query:** `manager.name: wazuh-server AND rule.level: 7 to 11`  
- **Findings:** Medium severity alerts from netstat open ports.

![Wazuh Alert Rule 100100](./ThreatAutomationAssets/wazuh_rule_100100.png)

---

## Threat Intelligence via MISP

- MISP OVA deployed, feeds configured.
- CVE indicator extraction via Python script.
- Exported Suricata rules and CSVs.

![MISP Feed Sync](./ThreatAutomationAssets/misp_feed_sync.png)  
![MISP Python Script Output](./ThreatAutomationAssets/misp_api_script_output.png)  
![MISP Exported Formats](./ThreatAutomationAssets/misp_export_formats.png)

---

## Conclusion

This project automates CVE detection and log correlation using Docker, enhances visibility with MISP, and integrates with Wazuh SIEM. It is production-ready for SOC or Blue Team deployments.
