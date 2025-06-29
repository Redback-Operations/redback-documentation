---
sidebar_position : 1
---

**Last updated by:** shreyas-vivek, **Last updated on:** 18/05/2025


**Last updated by:** shreyas-vivek, **Last updated on:** 18/05/2025


# Cybersecurity Assessment Report  
**Essential Eight Maturity Model – Restrict Administrative Privileges (ML1-RA)**

**Assessment Scope:** Redback Data Warehousing  
**Assessed by:** Cybersecurity GRC Team, Redback Operations  
**Assessment Date:** 17 May 2025  

---

## 1. Introduction

This report presents the outcomes of the Essential Eight Maturity Level 1 (ML1) assessment focused on the “Restrict Administrative Privileges” control category (ML1-RA) for the Redback Data Warehousing environment. The Australian Cyber Security Centre’s (ACSC) Essential Eight is a set of prioritized strategies to mitigate cybersecurity incidents, and ML1 establishes the foundational baseline for organizations to defend against common threats.

The objective of this assessment is to determine the extent to which administrative privilege management practices are implemented in the Redback data warehousing infrastructure and to identify opportunities to improve alignment with best practices in secure system administration.

---

## 2. System Overview and Scope

The target system is the Redback Data Warehousing Virtual Machine (VM), which serves as the core platform for storing and processing structured and semi-structured data across multiple internal Redback projects. The data warehouse:

- Hosts file upload services, MinIO object storage, and MongoDB for project-specific ingestion pipelines.  
- Is used by different student project teams for data aggregation, visualization, and downstream analysis using Dremio, Streamlit dashboards, and Jupyter notebooks.  
- Is a Deakin University-managed on-premises system, accessible only via VPN and internal network.  
- Has no direct internet exposure and is provisioned and patched by Deakin IT Services, not Redback students.  

While Redback students and mentors manage application-level services within the VM, the base operating system, patching, and privileged access controls fall partially within their administrative responsibility, particularly when creating new users, accessing Docker containers, and segmenting project environments.

---

## 3. Assessment Methodology

The audit followed Redback’s internal compliance testing workflow aligned to the ACSC Essential Eight Assessment Guide. For each ML1-RA test case, the following process was applied:

- Review of Active Directory (AD) roles and user groups  
- Analysis of Group Policy Objects (GPOs) applied to privileged and unprivileged environments  
- Interviews with mentors and infrastructure stakeholders (e.g., Ben Dang, Daezel Goyal)  
- Inspection of logs from administrative sessions, credential provisioning, and container activity  
- Manual validation of privilege escalation attempts using tools like `runas`, RDP, PowerShell Remoting (PSRemote)  
- Examination of shared and segregated VM environments, credential reuse, and exception handling  

---

## 4. Summary of Results

| Test ID     | Control Objective                                                   | Compliance Status     |
|-------------|---------------------------------------------------------------------|------------------------|
| ML1-RA01    | Admin access granted only via approved requests                    | Implemented            |
| ML1-RA02    | Admin accounts cannot access internet/web services                 | Implemented            |
| ML1-RA03    | Admin accounts do not have email capabilities                      | Implemented            |
| ML1-RA04    | Admin activities isolated from unprivileged environments           | Implemented            |
| ML1-RA05    | Standard users cannot access privileged environments               | Implemented            |
| ML1-RA06    | Standard users cannot elevate via PSRemote/RDP                     | Implemented            |
| ML1-RA07    | Admin accounts restricted from unprivileged workstations          | Partially Implemented  |
| ML1-RA08    | Privilege elevation via tools like runas or remote management blocked | Implemented          |
| ML1-RA09    | Quarterly review of administrative accounts                        | Partially Implemented  |
| ML1-RA10    | Separate identities used for admin and user roles                 | Partially Implemented  |

---

## 5. Detailed Findings and Analysis

### ML1-RA-01: Approved Justification for Admin Access  
Admin access is provisioned via internal request workflows managed through JIRA. Each access instance uses credentials issued per session, documented in Confluence. **Fully implemented.**

### ML1-RA-02: Restricted Internet Access for Admin Accounts  
Firewall rules and Squid proxy logs confirm admin accounts cannot access the internet. All privileged operations occur on internal networks or bastion hosts. **Fully implemented.**

### ML1-RA-03: No Mail Capability for Admin Accounts  
SMTP and IMAP are disabled for admin accounts. No active mailboxes are found for admin users. **Fully implemented.**

### ML1-RA-04: Segregated Administrative Environments  
Privileged tasks occur in isolated container environments. VLANs and container runtime segmentation ensure logical separation. **Fully implemented.**

### ML1-RA-05: Blocking Unprivileged Access to Admin Systems  
AD policies block standard user login to privileged systems. Logs confirm enforcement of role separation. **Fully implemented.**

### ML1-RA-06: Blocking Remote Elevation (PSRemote, RDP)  
Attempts from standard users to use PSRemote or RDP are denied and logged. **Fully implemented.**

### ML1-RA-07: Restriction of Admin Logins on Unprivileged Systems  
GPOs restrict admin logins to user environments, but shared containers undermine strict isolation. **Partially implemented.**

### ML1-RA-08: Blocking Privilege Elevation via Tools  
Privilege escalation attempts using `runas`, RDP, and others are denied. Event logs confirm technical enforcement. **Fully implemented.**

### ML1-RA-09: Quarterly Admin Account Review  
Reviews are performed manually, with no automation for stale credential alerts. **Partially implemented.**

### ML1-RA-10: Separate Identities for Admin and User Roles  
Admins use +admin suffixed accounts, but shared credentials are used for services like Dremio. **Partially implemented.**

---

## 6. Key Risks Identified

- Shared user environments expose risk of config leakage or accidental privilege overlap.  
- Use of shared admin credentials reduces accountability.  
- Manual admin tracking may delay deactivation or revocation of privileges.  

---

## 7. Recommendations

1. Strengthen isolation between user environments or containers.
2. Eliminate shared service credentials; adopt secrets management (e.g., AWS Secrets Manager, Vault).
3. Automate admin account reviews with AD monitoring scripts and audit tools.
4. Introduce a formal exception register to manage deviations from RBAC.

---

## 8. Conclusion

The Redback Data Warehousing team demonstrates strong foundational compliance with the **Restrict Administrative Privileges** strategy under **ACSC Essential Eight Maturity Level One**. Controls are in place to manage, monitor, and restrict elevated access. Improvements in credential hygiene, process automation, and environment segmentation will enhance overall resilience and reduce risks of unauthorized administrative activity.

---

## Acknowledgment

We acknowledge the support and contributions of the following entities and communities in the completion of this cybersecurity assessment:

- **Deakin University** – For providing infrastructure, guidance, and a robust cybersecurity learning environment.  
- **OpenAI and ChatGPT** – For assistance in drafting and refining audit documentation with clarity and professionalism.  
- **Traditional Owners of the Land** – We pay our respects to the Wadawurrung people, the Traditional Custodians of the land on which we study and work, and honour their enduring connection to land, waters, and culture.

---
