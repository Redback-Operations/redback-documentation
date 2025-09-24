---
sidebar_position: 1
---
# Automated Threat Hunting System 

:::info
**Document Creation:** 17 May 2025. **Last Edited:** 23 May 2025. **Authors:** Syed Mahmood Aleem Huzaifa.  
**Effective Date:** 23 May 2025. **Expiry Date:** 23 May 2026.
:::

## Introduction

The aim of this project was to build a fully integrated Automated Threat Hunting System using open-source security tools. The objective was to detect, enrich, and automatically triage security threats by leveraging real-time logs, behavioural analytics, threat intelligence, and SOAR capabilities.

## Tools and Technologies Used

- **Wazuh Manager** (Host-based SIEM and endpoint detection)  
- **Wazuh Agent** (Deployed on monitored machines)  
- **Suricata** (Network Intrusion Detection System)  
- **MISP** (Malware Information Sharing Platform for Threat Intelligence)  
- **The Hive** (Incident Response Platform for case management)  
- **Cortex** (Automated observable analysis engine)  
- **Docker & Docker Compose** (For containerised deployments)  
- **Python** (Custom scripting for Wazuh-MISP integration)  
- **Linux Systems** (Ubuntu, Debian, Kali VMs)  
- **VirtualBox Networking** (Bridged/NAT IP setups)

## Project Phases and Milestones

### Phase 1: Core Setup and Wazuh Deployment

- Installed Wazuh Manager on an Ubuntu VM for centralised security monitoring.  
- Deployed Wazuh Agent on a Debian VM to collect logs (system, authentication, file monitoring).  
- Used the Wazuh built-in dashboard (not external ELK) to visualise agent events and alerts.  
- Verified agent registration, health monitoring, and event flow.  

### Phase 2: Network Threat Detection Integration

- Installed Suricata IDS on the same Ubuntu VM hosting Wazuh Manager.  
- Configured Suricata to output EVE JSON logs for network-based event detection.  
- Integrated Suricata logs into Wazuh by configuring local log collection rules.  
- Verified detection of network events like port scans, brute-force attempts, and suspicious traffic.  

### Phase 3: Threat Intelligence Platform Deployment (MISP)

- Deployed MISP on a Kali Linux VM using Docker for easier management.  
- Populated MISP with custom and public threat indicators (IP addresses, hashes, domains).  
- Developed a custom Python script (`custom-misp.py`) to enable Wazuh alerts to query MISP indicators in real-time.  
- Created a shell wrapper (`custom-misp`) to trigger MISP lookups from Wazuh based on alert rules.  

### Phase 4: Wazuh–MISP Integration and Automation

- Configured custom Wazuh rules to trigger MISP lookups on specific alerts (e.g., new file detections, network connections).  
- Modified Wazuh decoders and ruleset to tag alerts enriched with MISP intelligence.  
- Monitored MISP-correlated events through Wazuh Dashboard (e.g., tagged with threat categories, risk scores).  

### Phase 5: Security Orchestration (SOAR) — TheHive and Cortex

- Deployed TheHive (case management platform) and Cortex (observable analyser) via Docker Compose.  
- Installed and configured Cortex analyzers.   
- Validated the full pipeline:  
  - Wazuh triggers alert  
  - MISP enriches alert  
  - Alert forwarded to TheHive (Future Work) 
  - Cortex enriches observables (Future Work)  
  - Analyst triages case  (Future Work) 

### Phase 6: Behavioural Detection and Automated Threat Hunting

- Designed and deployed custom Wazuh behavioural rules for detecting:
  - SSH brute-force attacks (multiple login failures from the same IP)
  - Suspicious PowerShell commands that may indicate lateral movement or privilege escalation
  - Communication with known malicious IPs using Suricata with enrichment from MISP

- Simulated realistic attacks to validate detection accuracy, including:
  - Repeated failed login attempts over SSH
  - Execution of encoded PowerShell commands
  - Test network connections to blacklisted IPs

- Created advanced Wazuh correlation rules that:
  - Link related suspicious events using shared indicators (e.g., IP address, file path)
  - Combine failed authentication attempts with malicious outbound traffic into a single high-priority alert

- Developed an automated IOC hunting mechanism by scheduling MISP indicator lookups using a cron-based script.  
- Tuned rule thresholds and suppression criteria to reduce alert fatigue and eliminate low-fidelity noise.

## Architecture Overview

| **Component**    | **Purpose**                                             |
|------------------|----------------------------------------------------------|
| Wazuh Manager     | Collects and analyses endpoint and Suricata network logs |
| Wazuh Agent       | Sends local system events to Wazuh Manager               |
| Suricata          | Captures and analyses network traffic                    |
| MISP              | Provides real-time threat intelligence for enrichment    |
| TheHive           | Manages incidents and alert triage                       |
| Cortex            | Performs automatic analysis of observables attached to incidents |

## Key Outcomes

- Real-time security event collection and monitoring using Wazuh and Suricata.  
- Automated IOC enrichment from MISP with Wazuh rule correlation.  
- End-to-end SOAR capabilities with TheHive and Cortex for automated case handling.  
- Custom behavioural detection rules tailored to common attack techniques.  
- Full automation of threat detection, enrichment, and triage.

