:::info
**Document Creation:** 17 April, 2025. **Last Edited:** 17 April, 2025. **Authors:** Shreyas Vivek, Kim Brvenik.
<br></br>**Effective Date:** 17 April 2025. **Expiry Date:** 17 April 2026.
:::

# As-Needed Audit Checklist

## Multi-Factor Authentication

### ML1-MF-10 — Lost or stolen MFA tokens/devices are reported and revoked within 24 hours.

- **Audit Procedure:**  
  Review helpdesk tickets and IAM logs for revocation response time.

- **Evidence Required:**  
  Incident reports, audit trail of token disablement.

- **Tools/Methods:**  
  `Helpdesk Portal, IAM Logs`

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

### ML1-PA-05 — Exploitable vulnerabilities on internet-facing services are patched within 48 hours.

- **Audit Procedure:**  
  Map CVE disclosure date to patch application date and analyze lag.

- **Evidence Required:**  
  Patch timeline table, remediation logs, CVE tracker screenshots.

- **Tools/Methods:**  
  `CVE Scanner, Manual review`

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

### ML1-PO-05 — Exploited vulnerabilities on internet-facing OSs are patched or mitigated within 48 hours.

- **Audit Procedure:**  
  Compare known exploit CVE release vs. patch implementation time.

- **Evidence Required:**  
  CVE timelines, patch logs, incident response summary.

- **Tools/Methods:**  
  `CVE Tracker, Patch Management Tools`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

