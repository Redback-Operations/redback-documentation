---
sidebar_position : 1
---

**Last updated by:** shreyas-vivek, **Last updated on:** 18/05/2025


**Last updated by:** shreyas-vivek, **Last updated on:** 18/05/2025


# Redback Operations Audit Policy

## Table of Contents

1. [Introduction](#1-introduction)  
2. [Purpose](#2-purpose)  
3. [Scope](#3-scope)  
4. [Roles and Responsibilities](#4-roles-and-responsibilities)  
   - Cybersecurity GRC Team  
   - DevSecOps & Platform Teams  
   - Software & Hardware Teams  
   - Project Leads & Academic Coordinators  
   - External Auditors (if engaged)  
5. [Audit Types and Frequency](#5-audit-types-and-frequency)  
   - Quarterly Audit  
   - Post-Incident Audit  
   - Ad Hoc Audit  
   - Annual Review Audit  
6. [Audit Lifecycle Methodology](#6-audit-lifecycle-methodology)  
   - Planning  
   - Execution  
   - Reporting  
   - Remediation and Follow-Up  
7. [Essential Eight Implementation and Testing](#7-essential-eight-implementation-and-testing)  
   - Application Control (ML1-AC)  
   - Patch Management (ML1-PA/PO)  
   - Multi-Factor Authentication (ML1-MF)  
   - Restrict Administrative Privileges (ML1-RA)  
   - Configure Microsoft Office Macros (ML1-OM)  
   - User Application Hardening (ML1-AH)  
   - Regular Backups (ML1-RB)  
   - Patch Operating Systems (ML1-PO)  
8. [Enforcement and Sanctions](#8-enforcement-and-sanctions)  
9. [Policy Maintenance and Review](#9-policy-maintenance-and-review)  
10. [References](#10-references)  
11. [Contact](#contact)

---

## 1. Introduction

This Cybersecurity Audit Policy defines Redback Operations’ commitment to comprehensive, systematic auditing practices. It ensures a proactive and disciplined approach to managing cyber risks across critical systems such as virtual machines (VMs), cloud environments, code repositories, and embedded systems like the SmartBike. This policy is informed by the Australian Cyber Security Centre’s (ACSC) Essential Eight (E8) Maturity Model – Maturity Level One (ML1), ISO/IEC 27001, and relevant data protection legislation. It aims to validate the effectiveness of implemented cybersecurity controls and guide the continuous improvement of Redback’s security posture.

---

## 2. Purpose

This policy serves the following objectives:

- Establish a transparent and standardised audit framework.  
- Assess the maturity and effectiveness of cybersecurity controls.  
- Identify weaknesses and reduce risk exposure through structured remediation.  
- Ensure compliance with applicable internal standards, ACSC E8 guidelines, ISO/IEC 27001, and university governance requirements.  
- Maintain a culture of accountability and security awareness.  

---

## 3. Scope

This policy covers all digital infrastructure and personnel involved in Redback Operations, including but not limited to:

- Virtualised environments (e.g., Linux and Windows VMs)  
- SmartBike embedded systems (hardware, firmware, runtime execution)  
- Cloud platforms (e.g., GCP, AWS) and deployment pipelines  
- Source code repositories (e.g., GitHub, GitLab)  
- Developer endpoints, admin tools, and software assets  
- Third-party services processing Redback data  

All students, staff, and contributors with access to Redback environments are subject to this policy.

---

## 4. Roles and Responsibilities

### Cybersecurity GRC Team

- Design and lead cybersecurity audits.  
- Define scope and audit criteria.  
- Maintain audit logs, findings registry, and maturity assessments.  
- Recommend remediation actions and track closure.  

### DevSecOps & Platform Teams

- Implement controls aligned with audit outcomes.  
- Provide patch management, configuration control, and access provisioning.  
- Support enforcement of multi-factor authentication (MFA) and endpoint hardening.  

### Software & Hardware Teams

- Cooperate with audit inquiries relating to firmware, CI/CD workflows, and source control.  
- Implement audit-based changes for application whitelisting, permissions, or runtime policies.  

### Project Leads & Academic Coordinators

- Review audit findings with team members.  
- Validate resolution of assigned remediation items.  
- Ensure contributors understand and apply secure development standards.  

### External Auditors (if engaged)

- Provide independent assurance and verification of policy adherence.  
- Report to academic and operational stakeholders.  

---

## 5. Audit Types and Frequency

| Audit Type           | Description                                                | Frequency / Trigger                   |
|----------------------|------------------------------------------------------------|----------------------------------------|
| **Quarterly Audit**  | Internal audit to assess VM configs, GitHub, whitelisting | Every trimester                        |
| **Post-Incident Audit** | Triggered after breach, misconfiguration, anomaly       | Within 7 days of incident detection    |
| **Ad Hoc Audit**     | Based on GRC, leadership, or academic supervisor request  | As needed                              |
| **Annual Review Audit** | Comprehensive policy and control validation             | Once per academic calendar year        |

### Quarterly Audit

**Purpose:** Assess baseline enforcement of critical security controls.  
**Scope & Activities:**

- **VM Hardening:** Patch validation, config integrity, unauthorised software checks  
- **GitHub Control:** User access, admin role checks, MFA enforcement  
- **E8 Testing:** Use E8MVT/ACVT to test controls, firmware whitelisting  
- **Reporting:** Categorise and flag recurring issues  

### Post-Incident Audit

**Purpose:** Root cause analysis and recovery validation  
**Scope & Activities:**

- **Timeline:** Log review and event reconstruction  
- **Root Cause:** Identify failures and gaps  
- **Validation:** Backup restore testing, config verification  
- **Docs:** Incident report, ISMS/risk register update  

### Ad Hoc Audit

**Purpose:** Address risks or compliance checks outside regular cycle  
**Scope & Activities:**

- Targeted MFA & access testing  
- Config reviews on high-risk systems  
- Re-check previously deferred controls  

### Annual Review Audit

**Purpose:** Review cybersecurity posture for compliance and maturity  
**Scope & Activities:**

- E8 maturity assessment across environments  
- ISO/IEC 27001 Annex A validation  
- Disaster recovery drills  
- Update recommendations  

---

## 6. Audit Lifecycle Methodology

### 6.1 Planning

- Define audit scope and tools  
- Assign roles and notify stakeholders  

### 6.2 Execution

- Use tools like E8MVT, ACVT, GitHub API  
- Collect screenshots, logs, command outputs  

### 6.3 Reporting

- Classify findings (Critical, High, Medium, Low)  
- Provide actionable recommendations  

### 6.4 Remediation and Follow-Up

- Track implementation  
- Verify and close in audit register  

---

## 7. Essential Eight Implementation and Testing

### 7.1 Application Control (ML1-AC)

- Allowlisting on VMs and SmartBike  
- Block unauthorized executables and scripts  
- Validate via E8MVT test payloads  

### 7.2 Patch Management (ML1-PA/PO)

- Daily scans on internet-facing apps  
- Fortnightly internal updates  
- Log patches and decommission unsupported software  

### 7.3 Multi-Factor Authentication (ML1-MF)

- Enforce MFA on GitHub, GCP, SSH  
- Monthly report checks  

### 7.4 Restrict Administrative Privileges (ML1-RA)

- Require documented justification  
- Quarterly privilege review  
- Separate admin and user accounts  

### 7.5 Configure Microsoft Office Macros (ML1-OM)

- Currently not enforced  
- Monitor for future macro usage  

### 7.6 User Application Hardening (ML1-AH)

- Not actively enforced currently  
- Future web apps to disable Java/Flash/ads  

### 7.7 Regular Backups (ML1-RB)

- Weekly encrypted VM snapshots  
- Offsite GitHub syncing  
- Quarterly restore drills  

### 7.8 Patch Operating Systems (ML1-PO)

- Weekly patch cycle  
- Kernel and update validation  
- Rebuild outdated systems  

---

## 8. Enforcement and Sanctions

Noncompliance may lead to:

- Suspension of access  
- Incident escalation  
- Mandatory re-training  
- Role reassignment or privilege loss  

All sanctions are logged in the Audit Register.

---

## 9. Policy Maintenance and Review

- Reviewed annually by the GRC Team  
- Updated per regulation, incidents, or architectural changes  
- Communicated via Teams and GitHub  

---

## 10. References

- Redback Operations ISMS  
- ACSC Essential Eight – Maturity Level One  
- ISO/IEC 27001:2013  
- GitHub Security Best Practices  
- Deakin University Cybersecurity Policy  

---

## Contact

**Cybersecurity GRC Team**  
📄 [Redback Documentation](https://redback-operations.github.io/redback-documentation/)

