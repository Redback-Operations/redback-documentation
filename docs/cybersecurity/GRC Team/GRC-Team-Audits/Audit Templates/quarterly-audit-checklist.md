:::info
**Document Creation:** 17 April, 2025. **Last Edited:** 17 April, 2025. **Authors:** Shreyas Vivek, Kim Brvenik.
<br></br>**Effective Date:** 17 April 2025. **Expiry Date:** 17 April 2026.
:::

# Quarterly Audit Checklist

## Application Control

### ML1-AC-01 — Prevent execution of EXE/COM files in user profile directories by standard users.

- **Audit Procedure:**  
  Attempt to run benign EXE/COM file in temp directories or Desktop.

- **Evidence Required:**  
  Execution logs, screenshots of failed attempts.

- **Tools/Methods:**  
  `E8MVT, Manual Execution Test`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-02 — Block software library files (DLL/OCX) from executing in user profile/temp folders.

- **Audit Procedure:**  
  Place DLL/OCX files in user space and attempt to invoke using standard tools.

- **Evidence Required:**  
  System logs, execution attempts, allowlist enforcement logs.

- **Tools/Methods:**  
  `E8MVT`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-03 — Prevent script file (BAT, PS, VBS, JS) execution in restricted paths.

- **Audit Procedure:**  
  Deploy test scripts into temp folders and execute with user permissions.

- **Evidence Required:**  
  Screenshots of blocked script runs, log entries showing prevention.

- **Tools/Methods:**  
  `ACVT, PowerShell`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-04 — Prevent installation via MSI/MST/MSP in non-privileged locations.

- **Audit Procedure:**  
  Attempt to install dummy MSI via user Desktop or Downloads.

- **Evidence Required:**  
  E8MVT reports, MSI install logs, endpoint monitoring logs.

- **Tools/Methods:**  
  `E8MVT`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-05 — Block execution of Compiled HTML (CHM) files from temp/user locations.

- **Audit Procedure:**  
  Run benign CHM files from various folders and log behavior.

- **Evidence Required:**  
  Screenshot and CHM handling logs.

- **Tools/Methods:**  
  `Manual Test, E8MVT`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-06 — Block execution of HTML applications (HTA) from browser cache or download folders.

- **Audit Procedure:**  
  Attempt to run HTA file from Downloads directory.

- **Evidence Required:**  
  Browser logs, application policy evidence, HTA test file logs.

- **Tools/Methods:**  
  `E8MVT, Manual Browser Test`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-07 — Block Control Panel Applet (CPL) execution from non-system folders.

- **Audit Procedure:**  
  Run benign CPL from Downloads and verify execution is blocked.

- **Evidence Required:**  
  ACVT reports, Windows logs, allowlist policies.

- **Tools/Methods:**  
  `ACVT`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-08 — Application allowlisting enforced via policy and managed centrally.

- **Audit Procedure:**  
  Review allowlist management system and policy distribution (e.g., Intune, GPO).

- **Evidence Required:**  
  Allowlist configuration files, policy logs.

- **Tools/Methods:**  
  `Group Policy, Config Audit`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-09 — Execution prevention enforced even when file renamed or copied across locations.

- **Audit Procedure:**  
  Rename known executables (e.g., .txt to .exe) and attempt execution.

- **Evidence Required:**  
  Test logs, screenshots, renamed file handling logs.

- **Tools/Methods:**  
  `Manual Tests, E8MVT`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AC-10 — File execution control verified against known bypass vectors.

- **Audit Procedure:**  
  Attempt to exploit known paths (e.g., 8.3 name format, symbolic links).

- **Evidence Required:**  
  Output of exploit test cases, logs from bypass attempts.

- **Tools/Methods:**  
  `E8MVT, ACVT, Script Toolkit`

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

### ML1-OM-01 — Microsoft Office macros are disabled for all users by default.

- **Audit Procedure:**  
  Run RSOP or review Group Policy settings; test macro behavior.

- **Evidence Required:**  
  GPO config screenshots, test results, approved user list.

- **Tools/Methods:**  
  `RSOP, GPMC, Office`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-OM-02 — A record is maintained of users approved to run macros.

- **Audit Procedure:**  
  Compare macro-enabled group membership to access requests.

- **Evidence Required:**  
  Approval requests, group membership exports.

- **Tools/Methods:**  
  `Active Directory, Confluence`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-OM-03 — Macros embedded in files downloaded from the internet are blocked.

- **Audit Procedure:**  
  Download Office files with macros and verify execution result.

- **Evidence Required:**  
  E8MVT output, file logs, macro execution error logs.

- **Tools/Methods:**  
  `Office, GPO, E8MVT`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

## Restrict Admin Privileges

### ML1-RA-01 — Access to administrative privileges is granted only through formal approval processes.

- **Audit Procedure:**  
  Review access request forms and change control tickets.

- **Evidence Required:**  
  Request logs, approval emails, workflow tickets.

- **Tools/Methods:**  
  `Active Directory, JIRA, Confluence`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-RA-02 — Privileged accounts are restricted from accessing the internet.

- **Audit Procedure:**  
  Attempt to access internet from admin account; review enforcement.

- **Evidence Required:**  
  Access logs, proxy blocks, firewall rules.

- **Tools/Methods:**  
  `Squid Proxy, FW ACLs, AD GPO`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-RA-03 — Privileged accounts are not used for email communication.

- **Audit Procedure:**  
  Test mailbox functionality for admin accounts.

- **Evidence Required:**  
  User directory exports, mail server configs, access logs.

- **Tools/Methods:**  
  `Exchange Admin Center, ADUC`

- **Responsible Team:**  
  `Cybersecurity GRC`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

## User App Hardening

### ML1-AH-01 — Web browsers do not process Java from internet websites.

- **Audit Procedure:**  
  Attempt to load Java content in Edge from known malicious site.

- **Evidence Required:**  
  Screenshot of blocked Java content, registry keys.

- **Tools/Methods:**  
  `Edge browser, RegEdit, test website`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AH-02 — Java content is disabled in Google Chrome.

- **Audit Procedure:**  
  Attempt Java content execution and verify result.

- **Evidence Required:**  
  Chrome plugin settings, screenshots, blocked content.

- **Tools/Methods:**  
  `Chrome, test site, GPO`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._

---

### ML1-AH-03 — Java content is disabled in Mozilla Firefox.

- **Audit Procedure:**  
  Test Java plugin activation and loading behavior.

- **Evidence Required:**  
  Firefox about:config, Java plugin settings.

- **Tools/Methods:**  
  `Firefox browser, plugin audit`

- **Responsible Team:**  
  `DevSecOps`

- **Status:**  
  [ ] Pass  
  [ ] Fail  
  [ ] N/A

- **Notes:**  
  > _Add notes here during audit._


