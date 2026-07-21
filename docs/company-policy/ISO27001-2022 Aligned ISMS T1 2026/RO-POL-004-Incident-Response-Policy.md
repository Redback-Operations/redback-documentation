# Incident Response Policy

## Redback Operations

| **Document Code** | RO – POL - 004 |
| --- | --- |
| **Version** | 1.0 |
| **Review interval** | Start of Trimester |
| **Document Owner** | Ethics / GRC Team |
| **ISO27001 Reference** | ISO27001:2022 – Annex A Controls 5.24, 5.25, 5.26, 5.27, 5.28 |

---

## Purpose

This policy is to ensure that a comprehensive and coherent incident response plan is in place for Redback Operations. This includes, detecting, reporting, managing and fixing the information security incident.

Due to Redback Operations' nature of trimester cycles, this document will also assist in ensuring that every incident knowledge is documented.

## Scope

This policy is applicable to:

- All Redback Operations members who are enrolled in Trimester 1, 2026.
- Every asset or system.
- Any event that will breach Redback Operations' systems, expose member or project information or halter active development.

## What defines a Security Incident

A security incident is when there is potentially negative impacts on the confidentiality, integrity or availability of Redback Operations' assets. All developers and staff of Redback Operations should report suspected malicious activity.

## Incident Security Levels

All incidents have to be assigned a level that determines it severity in an incident report.

| **Severity** | Criteria | Time of attendance | Escalation |
| --- | --- | --- | --- |
| **Critical** | Live unauthorised access, PII or credentials are in GitHub repositories, harm from physical assets, malware | Within 1 Hour | Notify tutor and team lead. |
| **High** | Suspected access from malicious actor, offboarded students still have access through old accounts, physical assets are missing | Within 4 hours | Notify Ethics / GRC and your team lead within the same day. |
| **Medium** | Security controls need to be implemented, policy is breached | Within 24 hours | Notify your team or team lead. |
| **Low** | Minor policy breach, automatic scanning tools find vulnerability in code before merging | Within 1 week | Log in Risk Register or notify team. |

## Roles and Responsibilities

### All Members

- Report any suspicious behaviour.
- Document evidence that relate to malicious activity.
- Cooperate with Blue Team and Ethics / GRC team.

### Ethics / GRC Team

- Input all incident reports in Incident Register.
- Coordinate severity level with incident and manage the appropriate response for said incident.
- Escalate to tutor or unit chair if required.
- Log incident, document every process and monitor results to asset compromised.
- Escalate to Blue Team if technical mitigation is needed.

### Blue Team

- Coordinate investigations for information system assets.
- Technical incidents are documented and contained.
- After incident is concluded, forward information to Ethics / GRC team for it to be documented.
- Establish new controls where it is needed to mitigate risks and breaches.

### SecDevOps Team

- Coordinate investigations on source code repositories.
- Ensure that automatic scanning tools are not detecting further vulnerabilities.
- Notify Ethics / GRC team of breaches and documentation.

### Team Leads

- Notify Ethics / GRC team of incidents within team processes.
- Offer logs, communications or documentation relating to incident.
- Educate team members on incident response policies.

## Incident Response Procedure

Any incident report must follow these procedures:

### Phase 1 – Identification

- Any developer who has suspected or recognises an incident must report it to the Ethics / GRC team, preferably the team lead on Microsoft Teams.
- Do not try to resolve or investigate by yourself.
- Document all evidence, do not tamper with digital forensics such as logs and files.
- If PII or credential was exposed, do not delete from repository aside if it is pre-merge.

### Phase 2 – Logging

- Ethics / GRC Team must log the incident in the Incident Register.
- The log entry must include, the date and time, overview of incident, assets affected and severity assessment.
- An incident ID is assigned, defined as INC-001, INC-002, incrementing per incident logged.

### Phase 3 – Containment

- Depending on nature and environment of incident, either Blue Team or SecDevOps has to direct the containment of said incident.
- If credentials are compromised, revoke immediately.
- If account is accessed maliciously, revoke account or suspend immediately.
- If source code contains PII or sensitive information, contact GitHub support and notify SecDevOps immediately.
- If physical harm occurs via physical assets, secure hardware and restrict access to physical environment.

### Phase 4 – Investigation

- Blue Team or SecDevOps must conduct an investigation to figure out cause, scope and result of the incident.
- Evidence collected during this investigation has to be retained and logged.
- The Ethics / GRC team has to coordinate the investigation and communicate with all parties relevant.
- Supervising tutor has to be notified if the incident is critical within the same day.

### Phase 5 – Remediation

- Implement fixes to ensure that the cause is solved.
- Ensure that fix is effective before concluding the incident.
- Update relevant documentation such as policies, procedures or controls if the incident has identified a gap.
- Add newly identified risks to Risk Register.

### Phase 6 – Lessons Learned

- Within a week of the conclusion of the incident, conduct a review on lessons learned.
- Document what had happened, what the cause was, how it was solved and what will be utilised to mitigate future incidents similar.
- Share findings with teams.
- Update Incident Register for next cohort to know of incidents.

## Escalation

The following table provides the contact information for escalation if an incident requires escalation and/or reaches Critical level of severity assessment:

| **Role** | **Name** | **Contact Method** | **Hours available** |
| --- | --- | --- | --- |
| **Ethics / GRC Team Lead** |  | Microsoft Teams | Full availability, no hours set. |
| **Blue Team Lead** |  | Microsoft Teams | Full availability, no hours set. |
| **SecDevOps Team Lead** |  | Microsoft Teams | Full availability, no hours set. |
| **Cybersecurity Team Tutor** |  | Microsoft Teams / Email | Full availability, no hours set. |
| **Unit Chair** |  | Microsoft Teams / Email | Full availability, no hours set. |

## Specific Incident Scenarios

### Credentials or PII exposed in Repository

- Severity Level: Critical
- Immediate action: rotate the exposed credential, do not delete the commit.
- Enable push protection on the repository that the exposure is on.
- Investigate commit history to check how long the exposure had existed.
- Notify SecDevOps immediately.

### Stale or Unauthorised Account Access

- Severity Level: High
- Immediate Action: suspend account until further verification is conducted.
- Ensure that account is not registered with those enrolled in this trimester.
- If account belongs to a former student, remove access and document in incident register.
- Review offboarding checklist as to how the account remained on Redback Operations.

### Critical Dependabot or Trivy Vulnerability Alert

- Severity Level: High
- SecDevOps team reviews alert and evaluates exploitability within 24 hours of alert.
- If source code is exploitable on GitHub, classify as High and update dependencies for project.
- If not, add to Risk Register.

### Physical Hardware Lost or Stolen

- Severity Level: High
- Report to team lead.
- Determine if any sensitive information or credentials were on the device.
- If credentials were on device, rotate credentials.

### ROS or IoT Safety Incident

- Severity: Critical
- Power down systems related to incident.
- Restrict access to physical environment until cause is recognised.
- Notify tutor as physical safety is concerned.

### Private AI Platform Data Exposure

- Severity: Critical
- Immediate Action: Document the information that is exposed.
- Take A.I offline until security risk is solved and trialled that mistake will not be repeated.
- Notify Data Warehouse Leader and Blue Team immediately.
- Review AI security.

## Evidence Preservation

Evidence needs to be preserved when an incident is occurring and its response process. This information should not be deleted or modification or overwritten during an incident:

- GitHub commit history, access logs and security alert messages.
- Communication messages related to incident
- Wazuh security logs and alert records.
- Any screenshots at the time of incident identification.

## Incident Register

Every incident must be logged into the Incident Register. This register should be maintained by the Ethics / GRC Team and reviewed at the start of each trimester.

| **Incident ID** | **Date Reported** | **Reported By** | **Description** | **Severity** | **Status** |
| --- | --- | --- | --- | --- | --- |
| Example | 6.4.26 | Rick M | In GitHub repository, Ethics, found hardcoded PII from the report.json file. | Critical | Closed. SecDevOps removed hardcoded PII by deleting commit and finding solution to ignore scans from PII scanner. |
| INC-001 |  |  |  |  |  |
| INC-002 |  |  |  |  |  |
| INC-003 |  |  |  |  |  |

## Policy Review

This policy must be reviewed at the start of every trimester by the incoming Ethics / GRC Team. Any changes must be version-controlled, dated and approved.
