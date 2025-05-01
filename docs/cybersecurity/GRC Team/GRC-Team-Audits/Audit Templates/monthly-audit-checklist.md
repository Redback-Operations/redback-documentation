:::info
**Document Creation:** 17 April, 2025. **Last Edited:** 17 April, 2025. **Authors:** Shreyas Vivek, Kim Brvenik.
<br></br>**Effective Date:** 17 April 2025. **Expiry Date:** 17 April 2026.
:::

# Monthly Audit Checklist

## Multi-Factor Authentication

### ML1-MF-01 — MFA is enforced on all internet-facing Redback services (e.g., GitHub, GCP).

- **Audit Procedure:**  
  Attempt user authentication and verify MFA challenge on login.

- **Evidence Required:**  
  Access attempt logs, screenshots of MFA prompts, enforcement settings.

- **Tools/Methods:**  
  `GitHub, GCP IAM, Azure Console`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-MF-02 — MFA challenge is triggered for remote desktop access to internal systems.

- **Audit Procedure:**  
  Perform test RDP session and check for MFA prompt.

- **Evidence Required:**  
  VPN/RDP access logs, security group enforcement evidence.

- **Tools/Methods:**  
  `Azure AD, Duo, RDP Config`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-MF-03 — All other internet-facing systems require MFA on login.

- **Audit Procedure:**  
  Enumerate services; attempt user login; confirm MFA challenge.

- **Evidence Required:**  
  MFA logs, system login records, user directory screenshots.

- **Tools/Methods:**  
  `Okta, PingID, Azure MFA`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-MF-07 — MFA bypass policies are reviewed monthly and exceptions require formal approval.

- **Audit Procedure:**  
  Review all policy exceptions and approvals for validity.

- **Evidence Required:**  
  Exception tracking sheets, approval forms.

- **Tools/Methods:**  
  `IAM Dashboard, Jira, Confluence`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

## Office Macros

### ML1-OM-10 — Microsoft Office macro usage logs are retained for audit trail and incident investigation.

- **Audit Procedure:**  
  Verify log retention settings; ensure logs are centralized.

- **Evidence Required:**  
  Sysmon logs, GPO logging configuration, centralized log exports.

- **Tools/Methods:**  
  `SIEM, Event Viewer, Syslog Server`

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

### ML1-PA-08 — Patches for internal apps (Office, PDF, browsers) applied within one month.

- **Audit Procedure:**  
  Review patch cycles and correlate version info with vendor dates.

- **Evidence Required:**  
  Patch audit reports, software version matrix.

- **Tools/Methods:**  
  `E8MVT, Software Inventory`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-PA-09 — Internal applications contain no vulnerabilities older than one month.

- **Audit Procedure:**  
  Use scanner to verify version compliance.

- **Evidence Required:**  
  List of vulnerable versions, patch timestamps.

- **Tools/Methods:**  
  `Qualys, Nessus, E8MVT`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

## Patch Operating Systems

### ML1-PO-08 — Workstation and server OS patches are applied within one month of release.

- **Audit Procedure:**  
  Match scan output with patch application dates; check backlog or exceptions.

- **Evidence Required:**  
  Patch cycle report, dashboard exports.

- **Tools/Methods:**  
  `WSUS, Linux YUM/APT Logs`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-PO-09 — No OS vulnerabilities older than one month exist in any production environment.

- **Audit Procedure:**  
  Run full authenticated vulnerability scan and compare to patch registry.

- **Evidence Required:**  
  Vulnerability scan logs, remediation reports.

- **Tools/Methods:**  
  `Qualys, Nessus`

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

### ML1-RB-09 — Backup systems are regularly patched and updated to prevent exploitation of backup infrastructure.

- **Audit Procedure:**  
  Check patch levels, CVEs, and update history of backup systems.

- **Evidence Required:**  
  Patch management reports, CVE summaries.

- **Tools/Methods:**  
  `Nessus, GVM, Patch Logs`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-RB-10 — Backup logs and access events are centrally stored and retained for investigation and forensics.

- **Audit Procedure:**  
  Verify central logging for backup infrastructure and access.

- **Evidence Required:**  
  SIEM logs, syslog records, retention policy evidence.

- **Tools/Methods:**  
  `Splunk, CloudWatch Logs, Graylog`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

