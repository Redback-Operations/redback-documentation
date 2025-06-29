:::info
**Document Creation:** 17 April, 2025. **Last Edited:** 17 April, 2025. **Authors:** Shreyas Vivek, Kim Brvenik.
<br></br>**Effective Date:** 17 April 2025. **Expiry Date:** 17 April 2026.
:::

# Weekly Audit Checklist

## Multi-Factor Authentication

### ML1-MF-08 — MFA logs are collected and reviewed for suspicious login attempts.

- **Audit Procedure:**  
  Inspect SIEM logs and MFA monitoring dashboards.

- **Evidence Required:**  
  SIEM alerts, login pattern reports.

- **Tools/Methods:**  
  `Splunk, Microsoft Sentinel`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

## Patch Applications

### ML1-PA-06 — Confirm all known exploitable vulnerabilities older than 48 hours are patched or mitigated.

- **Audit Procedure:**  
  Run patch verification and determine lag beyond allowed window.

- **Evidence Required:**  
  Remediation evidence, exception logs.

- **Tools/Methods:**  
  `Qualys, Sysmon`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-PA-07 — All internet-facing apps patched within 2 weeks of patch availability.

- **Audit Procedure:**  
  Compare software patch date with original vendor release.

- **Evidence Required:**  
  System patch logs, vendor release notes.

- **Tools/Methods:**  
  `Patch management dashboard`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

## Regular Backups

### ML1-RB-02 — Important data and configuration settings are backed up weekly.

- **Audit Procedure:**  
  Inspect backup logs and compare to policy schedule.

- **Evidence Required:**  
  Backup job reports, retention policy, storage logs.

- **Tools/Methods:**  
  `Veeam, GCP Snapshot, AWS Backup`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-RB-03 — Backups are performed in a synchronised manner across systems and environments.

- **Audit Procedure:**  
  Confirm snapshot coordination across systems.

- **Evidence Required:**  
  Timestamps of snapshots, recovery point reports.

- **Tools/Methods:**  
  `ZFS, RAID Logs, Cloud Sync Reports`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

