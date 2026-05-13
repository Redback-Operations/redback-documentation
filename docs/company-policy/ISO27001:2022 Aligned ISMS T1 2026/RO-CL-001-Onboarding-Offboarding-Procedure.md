# Onboarding & Offboarding Procedure

## Redback Operations – ISO27001:2022 ISMS

| **Document Code** | RO – CL – 001 |
| --- | --- |
| **Version** | 1.0 |
| **Document Owner** | Ethics / GRC Team |
| **ISO27001 Reference** | Annex A Controls 5.16, 5.17, 5.18, 6.1 , 6.2, 6.4, 6.5 |
| **Review Interval** | Start of each Trimester |

---

## Purpose

This procedure dictates the step-by-step process needed for onboarding new students into Redback Operations and offboarding concluding students at the end of their SIT378 Capstone Team Project (B) enrolment. All access to systems is approved and revoked in a documented and managed manner through this policy. This policy is created due to Redback Operations' nature of trimester-based student rotation.

## Scope

This procedure is applicable to:

- Students who are joining Redback Operations at the start of the trimester.
- Students who are leaving Redback Operations at the end of their enrolment within the unit.
- All systems that the students are given access to.
- Ethics / GRC Team to maintain access records.

## Roles and Responsibilities

| **Role** | **Responsibilities** |
| --- | --- |
| **Ethics / GRC Team** | Maintain the Access Register; document all onboarding and offboarding events; conduct trimester access reviews; ensure this procedure is practiced and followed |
| **Team Leads** | Submit access requests for new members; brief new members on security policies; initiate offboarding for departing members; confirm access revocation is complete |
| **Blue Team** | Manage Microsoft Entra ID provisioning and revocation; confirm Entra ID access is removed on offboarding |
| **SecDevOps Team** | confirm GitHub access is removed on offboarding |
| **All Members** | Notify team lead immediately if they become aware of stale or unauthorised accounts; delete local project data on offboarding; complete security briefing during onboarding |

## Onboarding

The following checklist must be completed for every new student joining Redback Operations. Team leads need to initiate the checklist within 3 business days of when leadership is established and student is confirmed within their team. All completed checklists must be filed with the Ethics / GRC Team.

### Before Access

| **#** | **Task — Before Access Is Granted** | **Responsible** | **Done ✓** |
| --- | --- | --- | --- |
| **1** | Team lead confirms student is enrolled in the current trimester capstone unit | Team Lead |  |
| **2** | Team lead submits access request to Ethics / GRC Team including student name, team, role, and systems required | Team Lead |  |
| **3** | Ethics / GRC Team creates entry in the Access Register for the new member | Ethics / GRC |  |
| **4** | New member is provided with and reads the following policies before access is granted: Information Security Policy (RO-POL-001), Acceptable Use Policy (RO-POL-003), Access Control Policy (RO-POL-002) | Ethics / GRC |  |
| **5** | New member signs the Member Acknowledgement form confirming they have read and understood the policies | New Member |  |

### System Access Provisioning

| **#** | **Task — System Access Provisioning** | **Responsible** | **Done ✓** |
| --- | --- | --- | --- |
| **6** | GitHub: add member to Redback Operations GitHub organisation | SecDevOps / Tutor |  |
| **7** | GitHub: assign member to their team repository with Write access only | SecDevOps / Tutor |  |
| **8** | GitHub: confirm member has MFA enabled on their GitHub account. If not, member has 5 days to enable it before access is suspended | SecDevOps / Ethics GRC |  |
| **9** | Microsoft Teams: confirm member has access to relevant team channels | Tutor |  |
| **10** | Microsoft Entra ID: provision role assignment aligned to team and responsibilities (if applicable) | Blue Team |  |
| **11** | Physical hardware: brief member on safe use and storage procedures if team uses physical assets | Team Lead |  |
| **12** | Data Warehouse systems: provision access to relevant Data Warehouse tools if member is on Data Warehouse team (MinIO, Dremio, Airflow etc.) | Data Warehouse Lead |  |

### Onboarding Completion

| **#** | **Task — Onboarding Completion** | **Responsible** | **Done ✓** |
| --- | --- | --- | --- |
| **13** | Team lead confirms all required access has been provisioned and is appropriate to the member's role | Team Lead |  |
| **14** | Ethics / GRC Team records onboarding completion date in the Access Register | Ethics / GRC |  |
| **15** | New member completes Ethics module on D2L before commencing active work | New Member |  |
| **16** | Team lead briefs new member on team-specific security responsibilities and any active incidents or open risks relevant to their role | Team Lead |  |

## Offboarding

The following checklist must be completed for every departing student leaving Redback Operations. The departure can happen at any point of the trimester. Offboarding must be commenced by the team leader.

The 32 inactive GitHub member accounts in the T1 2026 GitHub Audit is a consequence of an absent offboarding procedure.

### Data and Knowledge Transfer

| **#** | **Task — Data and Knowledge Transfer** | **Responsible** | **Done ✓** |
| --- | --- | --- | --- |
| **1** | Departing member transfers all active work, documentation, and project files to the team repository before their final day | Departing Member |  |
| **2** | Team lead confirms all work-in-progress is documented and accessible to remaining or incoming team members | Team Lead |  |
| **3** | Departing member deletes all Redback Operations Confidential data from personal devices | Departing Member |  |
| **4** | Departing member confirms deletion of local data in writing to the Ethics / GRC Team | Departing Member |  |
| **5** | Team lead documents any outstanding tasks or responsibilities the departing member held, outlined in the handover document, to the next cohort | Team Lead |  |

### System Access Revocation

| **#** | **Task — System Access Revocation** | **Responsible** | **Done ✓** |
| --- | --- | --- | --- |
| **6** | GitHub: remove member from Redback Operations GitHub organisation | Tutor |  |
| **7** | GitHub: remove member from all team assignments within the organisation | Tutor |  |
| **8** | Microsoft Entra ID: remove all role assignments and disable or delete the account | Blue Team |  |
| **9** | Shared credentials: rotate any shared passwords or secrets the member had access to | Team Lead / Blue Team |  |
| **10** | Data Warehouse systems: revoke access to MinIO, Dremio, MongoDB, Airflow, and any other Data Warehouse tools (if applicable) | Data Warehouse Lead |  |
| **11** | Physical hardware: confirm all physical assets are returned and in acceptable condition | Team Lead |  |
| **12** | HiveMQ / MQTT: revoke broker credentials if member had access (Smartbike VR and Data Warehouse teams) | Blue Team / Team Lead |  |

### Offboarding Completion

| **#** | **Task — Offboarding Completion** | **Responsible** | **Done ✓** |
| --- | --- | --- | --- |
| **13** | Team lead confirms all access has been revoked across all systems and signs off the offboarding checklist | Team Lead |  |
| **14** | Ethics / GRC Team records offboarding completion date in the Access Register | Ethics / GRC |  |
| **15** | Ethics / GRC Team verifies the member no longer appears as active in GitHub, Entra ID, or any other system | Ethics / GRC |  |
| **16** | If any access could not be confirmed as revoked, raise as an Open incident in the Incident Register under RO-POL-004 | Ethics / GRC |  |

## Access Register

The Ethics / GRC Team is responsible for maintain the Access Register which documents all active members, their access levels, and the dates they are enrolled for, per trimester. This register is to be reviewed at the start of each trimester. The access review process is defined in the Access Control Policy (RO-POL-002).

| **#** | **Student Name** | **Team** | **Role** | **Systems Access Granted** | **Date Onboarded** | **Date Offboarded** | **Completed By** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *001* | *[Name]* | *[Team]* | *[Role]* | *[Systems]* | *[Date]* | *[Date]* | *[GRC Lead]* |
| *002* | *[Name]* | *[Team]* | *[Role]* | *[Systems]* | *[Date]* | *[Date]* | *[GRC Lead]* |
| *003* | *[Name]* | *[Team]* | *[Role]* | *[Systems]* | *[Date]* | *[Date]* | *[GRC Lead]* |
| *004* | *[Name]* | *[Team]* | *[Role]* | *[Systems]* | *[Date]* | *[Date]* | *[GRC Lead]* |
| *005* | *[Name]* | *[Team]* | *[Role]* | *[Systems]* | *[Date]* | *[Date]* | *[GRC Lead]* |

## Mid-Trimester Offboarding

If a student withdraws before the trimester concludes, it is to be treated as a normal offboarding procedure. The checklists must be completed immediately to ensure that the student does not have access to Redback Operations' systems. The Ethics / GRC team must be notified immediately to maintain the Access Register.

## Trimester Start Review

At the start of each trimester, the Ethics / GRC team must conduct a full access review to identify and remove stale accounts from the previous trimester. This review must be completed once all students are placed into their corresponding teams, no longer than one week of that placement.

| **#** | **Task — Trimester Start Access Review** | **Responsible** | **Done ✓** |
| --- | --- | --- | --- |
| **1** | Export full GitHub organisation member list and cross-reference against current trimester enrolment | Ethics / GRC / SecDevOps |  |
| **2** | Identify any members not enrolled in the current trimester and flag for removal | Ethics / GRC |  |
| **3** | Confirm with tutors whether flagged accounts are legitimate (tutors, coordinators, service accounts) before removing | Ethics / GRC |  |
| **4** | Remove all confirmed stale accounts from GitHub organisation and document in Access Register | SecDevOps / Tutor |  |
| **5** | Review Microsoft Entra ID role assignments and remove stale accounts | Blue Team |  |
| **6** | Confirm all active members have MFA enabled across all platforms | Ethics / GRC |  |
| **7** | Document review outcome and any findings in the Access Register | Ethics / GRC |  |

## Non-Compliance

Failure to complete the onboarding and offboarding procedures and checklists may lead to consequences such as:

- A formal incident registered in the Incident Register
- Escalation to tutor or unit chair
- Stale account is counted as unmitigated in Risk Register.

Team leaders are responsible for their member's onboarding and offboarding. If a team leader is not yet established, delegate to Ethics / GRC team.

## Procedure Review

This procedure must be reviewed at the start of each trimester by the Ethics / GRC team. Any changes must be version-controlled, dated, and approved before taking effect.
