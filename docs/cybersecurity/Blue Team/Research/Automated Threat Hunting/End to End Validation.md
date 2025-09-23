---
sidebar_position: 11
---

:::info
**Document Creation:** 23 September 2025. **Last Edited:** 23 September 2025. **Authors:** Syed Mahmood Aleem Huzaifa.  
**Effective Date:** 23 September 2025. **Expiry Date:** 09 September 2026.
:::

### Overview 
This project aimed to design and validate a Security Orchestration, Automation, and Response (SOAR) pipeline entirely on community editions of open-source tools. The intent was to replicate the core capabilities of a modern SOC (Security Operations Center) — detection, enrichment, case management, and automation — without relying on enterprise licenses.

The chosen stack included:

1. **Wazuh** – SIEM and endpoint monitoring platform.

2. **Suricata** – Network Intrusion Detection System (NIDS).

3. **MISP** – Threat intelligence sharing and enrichment platform.

4. **TheHive** – Security Incident Response Platform (SIRP).

5. **Cortex** – Analyzer engine for automated enrichment.

The project was divided into nine sequential phases (Phases 1–9), each delivering one layer of capability. This page consolidates these phases and validates the pipeline by tracing the journey of a malicious IOC through every stage - from initial detection in Wazuh/Suricata through MISP enrichment, TheHive escalation, Cortex automation, and finally analyst case closure.

### Phase-by-Phase Explanations 

### Phase 1 – Wazuh Core Setup
Link to [Phase 1](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%201%20-%20Core%20Setup%20and%20Wazuh%20Deployment).

**Why this phase matters**:
No SOAR pipeline can function without a central log ingestion and correlation layer. Wazuh was chosen because it combines SIEM capabilities (log analysis, rule correlation, dashboards) with endpoint monitoring (File Integrity Monitoring, rootkit detection).

**What was done**:

1. Installed Wazuh Manager on Ubuntu 22.04.

2. Deployed Wazuh Agents on Debian endpoints to forward system logs.

3. Configured secure manager-agent communication using TLS certificates.

4. Verified integration using the Wazuh Dashboard (Kibana plugin or web UI).

**Validation**:
Triggered simple test events (e.g., failed SSH logins) and confirmed alerts appeared in the Wazuh Dashboard. Agents were listed as active, and rule-based alerts (from Wazuh’s built-in rule set) were generated.

**Link to next phase**:
This established the detection backbone. Suricata logs and threat intelligence feeds would later enrich the data flowing through Wazuh.

### Phase 2 – Suricata + Wazuh (Network Threat Detection)
Link to [Phase 2](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%202%20-Network%20Threat%20Detection%20Integration%20%E2%80%93%20Suricata%20+%20Wazuh).

**Why this phase matters**:
While Wazuh can monitor endpoints, modern threats often exploit network-based vulnerabilities. By integrating Suricata with Wazuh, the project gained visibility into live network traffic.

**What was done**:

Installed Suricata 6.0.8 on Ubuntu.

Configured it to run in AF-PACKET mode to capture live traffic.

Enabled EVE JSON output, directing logs to /var/log/suricata/eve.json.

Configured Wazuh to parse Suricata alerts by editing ossec.conf.

Loaded the Emerging Threats Open ruleset, which includes detection for botnets, C2 servers, and common exploit attempts.

**Validation**:
Simulated malicious network traffic (e.g., connecting to a known blacklisted IP). Suricata generated an alert in eve.json. Wazuh ingested the alert and triggered rule correlation, displaying it in the dashboard.

**Link to next phase**:
This phase provided network-layer detection, which when combined with IOC enrichment from MISP, would allow alerts to be contextualized.

### Phase 3 – MISP Deployment
Link to [Phase 3](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%203%20-%20MISP%20Threat%20Intelligence%20Platform%20Deployment).

**Why this phase matters**:
Detection without context leads to alert fatigue. Analysts need to know if an IP/domain is just unusual or actively associated with malware or attacks. MISP solves this by storing and sharing structured IOCs.

**What was done**:

1. Deployed MISP on Kali Linux.

2. Configured MySQL, PHP, and Apache services for the web interface.

3. Created an admin user and organization.

4. Added test IOCs: IP (1.2.3.4), domain (malicious.test), and a file hash.

5. Published these as events, making them available to API queries.

**Validation**:
Queried the MISP API directly to confirm that IOCs were retrievable. Ensured that Cortex’s MISP Analyzer could also pull events from MISP.

**Link to next phase**:
With MISP in place, Wazuh could now enrich alerts by checking observables against known IOCs.

### Phase 4 – Wazuh–MISP Enrichment Automation
Link to [Phase 4](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%204%20-%20Wazuh%E2%80%93MISP%20Automation%20and%20Alert%20Enrichment).

**Why this phase matters**:
Without automation, analysts would need to manually query threat intelligence for each alert - a time-consuming process. Integration ensures enrichment happens at detection time.

**What was done**:

1. Installed the custom-misp Python script.

2. Modified local_rules.xml in Wazuh to run this script on matching alerts (e.g., suspicious IPs, hashes).

3. Configured the script to query the MISP API and return enrichment tags.

4. Verified enriched alerts were displayed in Wazuh Dashboard with additional context.

**Validation**:
Generated an alert using a known malicious IP (1.2.3.4). Wazuh triggered the enrichment script, queried MISP, and tagged the alert with IOC context (e.g., “Threat Level: High, Category: C2”).

**Link to next phase**:
Enriched alerts would later be forwarded to TheHive, ensuring that analysts saw intelligence-backed alerts, not raw data.

### Phase 5 – TheHive + Cortex Deployment
Link to [Phase 5](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%205%20-%20SOAR%20Deployment-The%20Hive%20and%20Cortex).

**Why this phase matters**:
SIEMs detect and enrich alerts, but analysts need a platform to manage investigations, assign tasks, and escalate cases. TheHive provides this functionality, while Cortex powers observable enrichment.

**What was done**:

1. Deployed TheHive 5.2.4 and Cortex 3.1.6 via Docker Compose.

2. Connected TheHive to Elasticsearch (for indexing) and Cassandra (for storage).

3. Installed Cortex analyzers: AbuseIPDB, VirusTotal, MISP Analyzer.

4. Configured TheHive to connect to Cortex using API keys.

**Validation**:
Created a test case in TheHive with an IP observable. Ran the AbuseIPDB analyzer through Cortex. The report (abuse confidence score, categories) was attached back to the observable.

**Link to next phase**:
With TheHive + Cortex live, Wazuh alerts could now be escalated into TheHive for case management and automated analysis.

### Phase 6 – Behavioural Detection and Testing
Link to [Phase 6](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%206%20-%20Behavioural%20Rules%20and%20Testing).

**Why this phase matters**:
IOC-based detection is useful but incomplete. Behavioural detection identifies patterns of malicious activity even when no IOC match exists.

**What was done**:

1. Configured Wazuh rules for SSH brute-force (multiple failed logins in short time).

2. Monitored suspicious PowerShell commands on endpoints.

3. Added rules for Suricata to flag malicious IP communication.

4. Tested each by simulating attacks (e.g., brute-force SSH, scripted PowerShell).

**Validation**:
Alerts fired as expected and appeared in TheHive after Wazuh–TheHive integration. Enrichment confirmed whether behaviours were linked to known IOCs.

**Link to next phase**:
Behavioural rules combined with IOC intelligence provided comprehensive coverage for both known and unknown threats.

### Phase 7 – Wazuh–TheHive Integration
Link to [Phase 7](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%207%20-%20Wazuh%20&%20The%20Hive%20Integration).

**Why this phase matters**:
Analysts shouldn’t have to monitor both Wazuh and TheHive. Centralizing alerts in TheHive streamlines workflows.

**What was done**:

1. Configured Wazuh to forward alerts via TheHive API.

2. Mapped Wazuh fields to TheHive alert schema (title, description, severity, source, observables).

3. Verified alerts enriched in Wazuh (from MISP) were fully visible in TheHive.

**Validation**:
Triggered alerts appeared in TheHive’s Alerts section with metadata intact. Analysts could promote alerts directly to cases.

**Link to next phase**:
Now that alerts were centralized, Cortex analyzers could be run directly from TheHive.

### Phase 8 – Cortex Observables
Link to [Phase 8](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%208%20-%20Cortex%20Observables).

**Why this phase matters**:
Analysts often need to validate observables (IP, hash, domain) in external sources. Cortex enables automated checks without leaving TheHive.

**What was done**:

1. Configured Cortex analyzers (AbuseIPDB, MISP Analyzer, VirusTotal).

2. Attached observables to cases in TheHive.

3. Ran analyzers and confirmed reports were attached back to the case.

**Validation**:
When running AbuseIPDB on a malicious IP, the report showed abuse categories (e.g., SSH brute-force) and confidence score.

**Link to next phase**:
While Phase 8 required manual analyzer execution, Phase 9 introduced automation to remove analyst effort.

### Phase 9 – Cortex Automation
Link to [Phase 9](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Blue%20Team/Research/Automated%20Threat%20Hunting/Phase%209%20-%20Cortex%20Automation).

**Why this phase matters**:
Manual enrichment wastes analyst time. Automation ensures observables are enriched immediately upon alert creation.

**What was done**:

1. Configured TheHive notification rules (e.g., trigger on ArtifactCreated).

2. Linked the rule to Cortex analyzers (AbuseIPDB, VirusTotal).

3. Tested by injecting a malicious IP observable from Wazuh.

**Validation**:
AbuseIPDB ran automatically, returning a report without analyst intervention. The report was attached to the observable in TheHive.

**Link to final validation**:
This completed the SOAR loop, ensuring that alerts arriving in TheHive were already enriched and ready for analyst action.

### Example of a validation scenario

 A malicious IP (1.2.3.4) published in MISP was used to validate the full workflow:

1. *Detection*: Suricata flagged communication → Wazuh alert created.

2. *Enrichment*: Wazuh triggered custom script → MISP tags added.

3. *Escalation*: Alert forwarded into TheHive.

4. *Automation*: Cortex ran AbuseIPDB automatically → report attached.

5. *Case Handling*: Analyst promoted alert to case, added notes, and closed as True Positive.

This confirms the pipeline can detect, enrich, escalate, automate, and resolve incidents in real time.

### Future Scope
This project demonstrates the feasibility of building a SOAR pipeline entirely with community tools. Each phase contributed incrementally:

*Phases 1–2*: Core detection layer (host + network).

*Phases 3–4*: Intelligence enrichment (MISP).

*Phases 5–7*: Orchestration and centralized case management (TheHive).

*Phases 8–9*: Automated enrichment and analysis (Cortex).

**Strengths**:

1. Real-time enrichment reduced manual triage time.

2. TheHive centralized alert and case management.

3. Cortex automation provided instant IOC validation.

**Limitations**:

1. Community editions lack enterprise scalability.

2. Manual configuration (scripts, custom rules) required maintenance.

3. Advanced case workflows (SLA, dashboards) limited compared to paid SOAR.

### Conclusion

The project successfully validated an end-to-end SOAR workflow across detection, enrichment, orchestration, automation, and response. Despite using only free/community editions, the stack demonstrated the capabilities required for modern SOCs.

This marks the closure of the project - proving that a functioning SOAR pipeline can be achieved with open-source tools, and providing a foundation for future enhancements (e.g., scaling, machine learning-based correlation, or additional analyzers).