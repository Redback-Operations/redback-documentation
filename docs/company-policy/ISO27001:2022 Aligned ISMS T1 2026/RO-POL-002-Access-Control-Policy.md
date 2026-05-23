# Access Control Policy

## Redback Operations – ISO27001:2022 ISMS

| **Document Code** | RO – POL – 002 |
| --- | --- |
| **Version** | 1.0 |
| **Review Interval** | Start of Each Trimester |
| **Document Owner** | Ethics / GRC Team |
| **ISO Reference** | ISO/IEC 27001:2022 – Annex A Controls 5.15, 5.16, 5.17, 5.18, 8.2, 8.3, 8.5 |

---

## Table of Contents

1. Purpose
2. Scope
3. Policy Statement
4. Roles and their Responsibilities
5. Access Control Principles
   - 5.1 Least Privilege
   - 5.2 Need to Know
   - 5.3 Separation of Duties
   - 5.4 Team-Based Ownership
6. Access Management
   - 6.1 Onboarding
   - 6.2 Access Review
   - 6.3 Offboarding
7. System – Specific Access Controls
   - 7.1 GitHub
   - 7.2 Entra ID
   - 7.3 Security Tooling
   - 7.4 HiveMQ
8. Multi-Factor Authentication (MFA)
9. Credentials and Secrets Management
10. Non-Compliance
11. Policy Review

---

## 1. Purpose

The policy highlights how Redback Operations manages access control to its information assets, systems, repositories and their data. This policy outlines that only authorized individuals can access certain assets that are indicative of their role. The policy also states that access to Redback's resources should be removed when a student enrolment is concluded. Redback Operation's rotation nature calls for this policy to indicate access based on time and withdrawal of access.

## 2. Scope

This policy is applicable to:

- Redback Operations members operating in the 8 active teams for Trimester 1, 2026.
- All assets including GitHub Repositories, cloud environments, authorization platforms, communication platforms, data warehouse systems and documentation relating to.
- All third-party software and services used by Redback Operations project teams.
- Team leads who are responsible for managing access control with their team members.

## 3. Policy Statement

Redback Operations must ensure that all assets are granted on a permitted basis and least privilege principle. All access must be authorized, documented and revoked when the student is offboard or their enrolment within the capstone unit concludes. Individuals should not be granted access to assets beyond their scope of responsibilities and role.

## 4. Roles and their Responsibilities

| **Role** | **Responsibilities** |
| --- | --- |
| **Ethics / GRC** | Reviewing and maintaining this policy each trimester; perform access audits where possible and educate Redback Operations on access control policies |
| **SecDevOps** | Ensure that only certain students have access to code reviews on GitHub. Ensure that only certain students have access to workflow files and automatic scanning implementation. |
| **Blue Team** | Manage access to security platforms such as Microsoft Entra ID and Wazuh. Ensure that only certain members can access configurations for ModSecurity firewall. |
| **Team Leaders** | Manage access control for members in team. |
| **All Members** | Use access that has only been granted for their role. Report unauthorized access where the role should not be able to access. Do not share login credentials. |

## 5. Access Control Principles

### 5.1 Least Privilege

All access must be granted on a least-privilege basis. Members can only be given the minimum level of access and authorization that is required for their role. Access should not be pre-emptively granted for future roles, only when confirmed.

### 5.2 Need to Know

Access to critical information and their systems is only available to those who need it to carry out their responsibilities.

### 5.3 Separation of Duties

Critical functions should ideally be split across individuals to minimize error or misuse. A single student should not have management responsibilities over an entire system.

### 5.4 Team-Based Ownership

All ownership of assets and systems can only be assigned to a team, not an individual. This can help with access management for future trimesters.

## 6. Access Management

### 6.1 Onboarding

When a new student is enrolled and commencing work:

- Access is only given based on their role
- The member is educated on security policies before access is given.
- Ensure that students report any unauthorized access.

### 6.2 Access Review

An access review must be undertaken per the start of each trimester:

- Team leads have to confirm which members are enrolled in their teams and their access levels for their responsibilities.
- If unauthorized permissions or inactive permissions are found, ensure that it is reported and removed immediately.
- Ethics / GRC team have to document each review taken.

### 6.3 Offboarding

When a trimester concludes, these protocols should be enacted:

- Team leads initiate offboarding at the last day of the trimester.
- GitHub membership and team assignments should be revoked.
- All authorization platforms and their members' access should be revoked.
- Microsoft Teams chat for ongoing Redback Operations' communications should be revoked.
- Any Personal Access Tokens (PAT) should be revoked.
- Offboarding is documented by the team leader.

## 7. System – Specific Access Controls

### 7.1 GitHub

- All repositories are under the central Redback Operations GitHub platform
- Repository visibility should default to Private unless permitted as Public.
- Members should only be granted access to their team repository only.
- Members should only be granted the access they need to their repository.
- Admin access is permitted only for SecDevOps, tutors and team leaders.
- Collaborators outside Redback Operations needs to be permitted by Ethics / GRC.
- Branch protection rules should be enabled on all branches in all active repositories.

### 7.2 Entra ID

- Access utilising Entra ID is managed by Blue Team.
- Role assignments should mirror the member's team and their responsibilities.
- Privileged roles should be audited at the start of each trimester.
- MFA is compulsory for all accounts.

### 7.3 Security Tooling

- Access to cyber-security tools should only be restricted to Blue Team.
- No other team members should have access to dashboards or security logs.
- Access is audited at the start of each trimester and withdrawn for concluding Blue Team members.

### 7.4 HiveMQ

- Access utilising HiveMQ is managed by Smartbike VR Team Lead
- No other team members should have access to IoT communication via HiveMQ.
- Access to platform must be audited per trimester.

## 8. Multi-Factor Authentication (MFA)

MFA should be mandatory for every account with access to Redback Operations, the systems include:

- GitHub organisation accounts
- Microsoft Entra ID
- React Native & Expo
- HiveMQ

If student does not have multi-factor authentication enabled, ensure that they do within 5 days of enrolment and/or commencing work, otherwise, suspend responsibilities.

## 9. Credentials and Secrets Management

- Passwords should never be shared via communication channels.
- Passwords should never be present in repositories.
- Personal Access Tokens should be scoped to the minimal requirement and revoked when student is offboarding.
- Any exposed credentials or compromise should be reported to Ethics / GRC Team immediately.

## 10. Non-Compliance

If compliance with this policy cannot be reached then these protocols should be enacted:

- Suspension of access to Redback Operations' programs.
- Escalation to tutor or unit chair.
- Formal report should be made and raised to proper authorities.

If misuse or non-compliance is detected, report to Ethics / GRC Team.

## 11. Policy Review

This policy should be reviewed at the start of the trimester by the commencing Ethics / GRC team. The senior students should oversee the review. Any changes should alter the version of the document, dated and reviewed before commenced. The document version should be incremented per iteration.
