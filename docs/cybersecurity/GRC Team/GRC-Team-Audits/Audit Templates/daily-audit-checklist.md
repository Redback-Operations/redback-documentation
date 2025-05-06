:::info
**Document Creation:** 17 April, 2025. **Last Edited:** 17 April, 2025. **Authors:** Shreyas Vivek, Kim Brvenik.
<br></br>**Effective Date:** 17 April 2025. **Expiry Date:** 17 April 2026.
:::

# Daily Audit Checklist

---

## Patch Applications

### ML1-PA-02 — Vulnerability scanner uses an up-to-date vulnerability database.

- **Audit Procedure:**  
  Check database version and last update timestamps in scanner console.

- **Evidence Required:**  
  Scanner config files, version logs.

- **Tools/Methods:**  
  `Qualys, Nessus, Rapid7`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-PA-03 — Vulnerability scans run daily on all internet-facing applications and services.

- **Audit Procedure:**  
  Validate daily scan logs and alerting mechanisms for exposed services.

- **Evidence Required:**  
  Daily reports, alerting logs.

- **Tools/Methods:**  
  `Nessus, Tenable.io`

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

### ML1-PO-02 — Vulnerability scanner used has an up-to-date vulnerability database.

- **Audit Procedure:**  
  Check scanner config and verify update frequency.

- **Evidence Required:**  
  Scanner version info, update logs.

- **Tools/Methods:**  
  `Nessus, OpenVAS, GVM`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-PO-03 — Daily scans are performed on operating systems of internet-facing services.

- **Audit Procedure:**  
  Validate daily scan frequency; review issue triage and response logs.

- **Evidence Required:**  
  Daily scan reports, incident tickets.

- **Tools/Methods:**  
  `Nessus Pro, InsightVM`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

