# Statement of Applicability

## Redback Operations – ISO27001:2022 ISMS

| Document Code | RO – SOA – 001 |
| --- | --- |
| Version | 1.0 |
| Document Owner | Ethics / GRC Team |
| ISO Reference | ISO/IEC 27001:2022 – Annex A |
| Prepared By | Ramon Garcia – Ethics / GRC Team Lead |

---

## Purpose

This Statement of Applicability documents the 93 controls that are from Annex A, ISO: IEC27001:2022. It declares whether each control is applicable, partially applicable or not applicable to Redback Operations. It also provides a justification as to why that control is relevant / not relevant to the company. This is a mandatory document as per the ISO:IEC27001:2022 ISMS.

## Scope

This SoA is applicable to all assets, systems and members of Redback Operations that is defined within the scope statement document (RO-ISMS-001).

## ISMS Document Suite Relevance

The applicability decisions in this SoA are informed by the following Redback Operations ISMS documents:

- RO-POL-001 – Information Security Policy
- RO-POL-002 – Access Control Policy
- RO-POL-003 – Acceptable Use Policy
- RO-POL-004 – Incident Response Policy
- RO-POL-005 – Secure Development Policy
- RO-POL-006 – Data Handling Policy
- RO-ISMS-001 – ISMS Scope Statement
- RO-REG-001 – Asset Register
- RO-REG-002 – Risk Register
- RO-AUDIT-GIT-001 – GitHub Audit Report
- RO-CL-001 – Onboarding & Offboarding Procedure

## Applicability Summary

| **Applicable** | **55** |
| --- | --- |
| **Partial** | **11** |
| **Not Applicable** | **27** |
| **Total Controls** | **93** |

## Status Legend

| **Applicable** | Control is applicable and implemented or planned within this trimester. |
| --- | --- |
| **Partial** | Control is applicable but only partially implemented; noted in Gap Analysis. |
| **Not Applicable** | Control does not apply to Redback Operations. Justification provided. |

## Annex A Controls

| **Control ID** | **Control Name** | **Status** | **Justification & Implementation Evidence** |
| --- | --- | --- | --- |
| **5 – Organisational Controls** | | | |
| **5.1** | Policies for information security | **Applicable** | Redback Operations operates on a rotational basis every trimester, continuity is necessity for Redback Operations' security posture, therefore policies are established and maintained. Information Security Policy is present and available to all Redback Operations Members. The Acceptable Use Policy, Secure Development Policy, Access Control Policy and Data Handling Policy is present in the ISMS suite as well. |
| **5.2** | Information security roles and responsibilities | **Applicable** | Students' roles change per trimester, therefore, the role they are assigned needs to have established responsibilities. Roles are defined across the ISMS suite. Ethics / GRC, Blue Team, SecDevOps, Team Leads and their corresponding team members are defined. Their responsibilities are documented in the Access Control Policy and Incident Response Policy. |
| **5.3** | Segregation of duties | **Applicable** | Different students have different responsibilities as per their role in Redback Operations. Separation of duties is documented in the Access Control Policy. No single student controls an entire system. |
| **5.4** | Management responsibilities | **Applicable** | Deakin staff are the leading figures in Redback Operations due to it being a student-driven company needing supervision whilst the Ethics / GRC team holds ISMS ownership. The tutor and unit chair are established as individuals for escalation. Defined in the Incident Response Policy. |
| **5.5** | Contact with authorities | **Partial** | Deakin staff such as the tutor or unit chair are the escalation points. There is no formal external authority contact procedure. |
| **5.6** | Contact with special interest groups | **Not Applicable** | Redback Operations is a student capstone company; they do not engage with external groups. |
| **5.7** | Threat intelligence | **Not Applicable** | No formal threat intelligence system is defined. Not applicable to Redback Operations it is out of scope and not at that maturity level. |
| **5.8** | Information security in project management | **Applicable** | This control applies to Redback Operations specifically as we have publicly facing repositories and a rotational nature with students. Policies include principles such as Secure by design and Need to Know, policies are established since there are no 'long-time' developers in the company. |
| **5.9** | Inventory of information and other associated assets | **Applicable** | Asset Register is established with classification, ownerships, risks and controls across all of Redback Operations. Control is applicable to Redback Operations as the company handles physical and digital assets and also important to track assets that are handled by Deakin but utilised by Redback. |
| **5.10** | Acceptable use of information and other assets | **Applicable** | Redback Operations handles sensitive information and controls publicly facing repositories. Utilisation of an Acceptable Use Policy (RO – POL – 001) is present in the ISMS suite in order to state appropriate use of Redback's systems and assets. |
| **5.11** | Return of assets | **Applicable** | Offboarding Procedure ( RO – CL – 001) requires handover and deletion of local data from personal devices. Applicable to Redback due to their rotational nature, emphasising the necessity for offboarding. |
| **5.12** | Classification of information | **Applicable** | In Data Handling Policy and Asset Register, information is categorised into Confidential, Internal and Public and what each criteria means. Applicable to Redback due to handling sensitive information and having to maintain security awareness of data across all students, across all trimesters. |
| **5.13** | Labelling of information | **Partial** | Classifications levels are defined and applied in Asset Register however there are no formal labelling conventions on systems, assets and repositories. Suggestion for next cohort. |
| **5.14** | Information transfer | **Applicable** | Data Handling Policy establishes the restrictions for transferring sensitive data via communication channels. Acceptable Use Policy restricts sharing of credentials and confidential information. Applicable to Redback as we primarily use Microsoft Teams or email secondarily, under Deakin student accounts. |
| **5.15** | Access control | **Applicable** | Access Control Policy covers least privilege, need-to-know, MFA and system specific controls. Team-based ownership is also present in policies. Applicable to Redback as the company does not have a centralised access control management system but is instead delegating responsibilities to Team leaders. Established in ROCII as implementing streamlined process for next cohort. |
| **5.16** | Identity management | **Applicable** | GitHub is managed per trimester. Onboarding and Offboarding Procedure establishes standards for access and revocation of systems. Applicable to Redback due to its rotational nature, leaving potential for shadow identities and accounts maintaining access. |
| **5.17** | Authentication information | **Applicable** | MFA is mandatory in Access Control Policy. Credentials are not to be shared or hardcoded, Personal Access Tokens are managed in Access Control Policy and Secure Development Policy. |
| **5.18** | Access rights | **Applicable** | Access onboarding and offboarding management in RO-CL-001. Access review is established as having to be done at the start of each trimester, present in Access Control Policy. Applicable to Redback specifically as rotational nature leaves potential for unnecessary stale access. |
| **5.19** | Information security in supplier relationships | **Not Applicable** | Redback Operations does not engage with formal suppliers. Tools are open-source or licensed through Deakin. |
| **5.20** | Addressing security within supplier agreements | **Not Applicable** | Redback Operations does not engage with formal suppliers and thus does not need to evaluate security within agreements as there are none. |
| **5.21** | Managing security in the ICT supply chain | **Not Applicable** | No ICT supply chain is managed by Redback. No formal third-party suppliers to assess security risks and mitigations. |
| **5.22** | Monitoring, review and change management of supplier services | **Not Applicable** | Supplier services are out of scope for Redback Operations, therefore no necessity for this control. |
| **5.23** | Information security for use of cloud services | **Partial** | Personal cloud storage is prohibited for confidential data as defined in the Data Handling Policy. Cloud storage classifications are defined in the DHP. No formal baseline for cloud services and its security. |
| **5.24** | Information security incident management planning and preparation | **Applicable** | Incident Response Policy defines severity levels, roles, escalation paths and a response procedure. Incident Register template is included. |
| **5.25** | Assessment and decision on information security events | **Applicable** | In Incident Response Policy, classification framework is defined. Critical /High /Medium and Low. |
| **5.26** | Response to information security incidents | **Applicable** | Six-phase incident response procedure (Identification, Logging, Containment, Investigation, Remediation, Lessons Learned) is defined in the Incident Response Policy. |
| **5.27** | Learning from information security incidents | **Applicable** | Lessons Learned Phase is mandated in the IRP as Phase 6. Findings are shared with teams and Incident Register is updated for continuity. |
| **5.28** | Collection of evidence | **Applicable** | Evidence preservation is required as documented in the Incident Response Policy. Commit History, access logs, Wazuh Logs, Screenshots and communications must be preserved during incidents as per the IRP. |
| **5.29** | Information security during disruption | **Not Applicable** | Business continuity / disaster recovery planning is outside the scope for Redback Operations. No production systems operated. |
| **5.30** | ICT readiness for business continuity | **Not Applicable** | No business continuity programme maintained. Redback Operations does not operate critical production infrastructure. |
| **5.31** | Legal, statutory, regulatory and contractual requirements | **Applicable** | Information Security Policy commits to adherence to Victorian Law and Deakin University policies. Acceptable Use Policy references licensing compliance for software. Applicable to Redback due handling information and under Deakin University as a capstone company. |
| **5.32** | Intellectual property rights | **Applicable** | Acceptable Use Policy prohibits sharing of confidential source code and documentation externally. Repositories default to private as per the Access Control Policy. AUP mandates the use of only open-source or licensed software. D2L Modules outline education on IP. |
| **5.33** | Protection of records | **Applicable** | ISMS Documents are shared in GitHub Repository or Docusaurus wiki. Incident and Asset Registers are maintained by Ethics / GRC Team. Data Handling Policy defines retention requirements. Applicable to Redback as ISMS suite covers registers that the company has sensitive information on. |
| **5.34** | Privacy and protection of PII | **Applicable** | PII is classified as confidential in Asset Register and Data Handling Policy. IRP includes specific scenarios for PII exposure in repositories. Secure Development Policy prohibits hardcoded PII. Applicable to Redback Operations due to its presence of PII from individuals who participate in the testing of Redback's projects. |
| **5.35** | Independent review of information security | **Partial** | GitHub audit was conducted (RO – AUDIT – GIT – 001). Internal audit checklist is planned for next cohort. Independent external audit is not feasible for Redback Operations. |
| **5.36** | Compliance with policies, rules and standards | **Applicable** | Non-compliance consequences defined in all policies. Escalation to unit chair and tutors are documented. Applicable to Redback specifically as Deakin Staff are supervising students, ensuring no harm is done to Redback Operations' systems and assets. |
| **5.37** | Documented operating procedures | **Applicable** | Onboarding and Offboarding Procedure provides step-by-step checklist. Applicable to Redback specifically due to its trimester-based rotation. |
| **6 – People Controls** | | | |
| **6.1** | Screening | **Not Applicable** | Student enrolment and background screening is managed by Deakin University, Redback Operations does not handle or have the authority to conduct student screening. |
| **6.2** | Terms and conditions of employment | **Applicable** | Member acknowledgement form required at onboarding as per the Acceptable Use Policy. Members acknowledge and accept ISMS policies before access is granted. |
| **6.3** | Information security awareness, education and training | **Applicable** | Policy briefing is mandated at onboarding. Security awareness / Ethics modules referenced on D2L. Applicable to Redback due to not all students having a security background. |
| **6.4** | Disciplinary process | **Applicable** | Non-compliance repercussions are defined across all policies. Formal disciplinary authority is held by Deakin University. |
| **6.5** | Responsibilities after termination or change of employment | **Applicable** | Offboarding Procedure dictates deletion of local data and revocation of all access during conclusion of enrolment. AUP prohibits retention of data after enrolment. |
| **6.6** | Confidentiality or non-disclosure agreements | **Partial** | Member acknowledgment form covers policy acceptance. There are no formal NDA in place. |
| **6.7** | Remote working | **Applicable** | Acceptable Use Policy governs personal device use for remote work for Redback Operations. Members required to use updated devices with anti-virus whilst not having local storage of sensitive information. Applicable to Redback Operations since there is no on-site premises to utilise company computers, students utilise their own devices. |
| **6.8** | Information security event reporting | **Applicable** | All members are required to report incidents to the Ethics / GRC team via Microsoft Teams. Reporting obligations are defined in the Incident Response Policy. Applicable to Redback Operations since a clear policy on how to report incidents is needed to ensure that the same procedure is followed per trimester. |
| **7 – Physical Controls** | | | |
| **7.1** | Physical security perimeters | **Not Applicable** | Physical environment is out of scope per the Scope Statement. Redback Operations is not responsible for the control or management of the physical premises used by members. |
| **7.2** | Physical entry | **Not Applicable** | Physical entry controls are managed by Deakin University, outside of scope of Redback operations. |
| **7.3** | Securing offices, rooms and facilities | **Not Applicable** | Redback Operations does not manage or own facilities. |
| **7.4** | Physical security monitoring | **Not Applicable** | Redback Operations does not have any physical security monitoring devices or controls. If accessing VM stored at Deakin University, Deakin University is responsible for physical monitoring. |
| **7.5** | Protecting against physical and environmental threats | **Not Applicable** | Environmental controls are managed by Deakin University. |
| **7.6** | Working in secure areas | **Not Applicable** | No dedicated secure areas operated by Redback Operations. |
| **7.7** | Clear desk and clear screen | **Applicable** | Acceptable Use Policy requires members to operate personal devices in a secure manner. This entails sharing screens when working on Redback Operations and leaving your device locked whilst unattended. |
| **7.8** | Equipment siting and protection | **Applicable** | Physical hardware handling guidelines are established in the AUP. Safe use, storage and reporting of loss or damage. Applicable to Redback Operations as projects have physical hardware such as bikes and Wahoo equipment. |
| **7.9** | Security of assets off-premises | **Applicable** | Acceptable Use Policy addresses personal device security for off-campus access. Applicable to Redback as every student has their own personal device. |
| **7.10** | Storage media | **Applicable** | Data Handling Policy defines storage requirements aligned with classification. Storage of sensitive information on the cloud or local is prohibited. Physical media containing sensitive information must not be retained after offboarding. |
| **7.11** | Supporting utilities | **Not Applicable** | Power and utility infrastructure is managed by Deakin University. Outside Redback Operations' scope. |
| **7.12** | Cabling security | **Not Applicable** | Network cabling infrastructure is managed by Deakin University. Outside Redback Operations' scope. |
| **7.13** | Equipment maintenance | **Applicable** | Acceptable Use Policy requires hardware to be utilised safely. Loss or damage must be reported to the Ethics / GRC team. Incident Response Policy also defines what to do when physical hardware loss or theft is an incident. Applicable to Redback Operations as multiple teams have physical assets such as Metaverse VR headset and Raspberry PI modules. |
| **7.14** | Secure disposal or re-use of equipment | **Partial** | E-Waste Battery Extraction team handles hardware disposal as a project focus. Formal secure disposal procedure for Redback-managed equipment is not documented. |
| **8 – Technological Controls** | | | |
| **8.1** | User end point devices | **Applicable** | Acceptable Use Policy requires end point devices to be installed with anti-virus and updated regularly. Any misuse is reported to the Ethics / GRC team. Confidential data cannot be stored locally. Applicable to Redback Operations as personal devices are the only form of devices used to access Redback systems. |
| **8.2** | Privileged access rights | **Applicable** | Admin access and tutors are the only ones with admin rights on GitHub. Privileged access is audited each trimester as per the access control policy. Applicable to Redback Operations as students belonging to certain sub-teams are the only ones responsible for GitHub management and Entra ID access management. |
| **8.3** | Information access restriction | **Applicable** | Members are restricted to team repository only for editing as per the Access Control Policy. Need-to-know principle is enforced. Applicable to Redback Operations as students in Project Orion does not need access to Wazuh Logs. |
| **8.4** | Access to source code | **Applicable** | Repository access is only restricted to team members. However public viewing is available. Branch protection is active with PRs needing reviews before merge. No student can approve their own request. Applicable to Redback Operations due to its reliance on GitHub and SecDevOps team reviewing pull requests. |
| **8.5** | Secure authentication | **Applicable** | MFA is compulsory across GitHub, Entra ID and HiveMQ as per the Access Control Policy. MFA has to be enabled within 5 days of enrolment as per the enrolment as per the policy. Applicable to Redback Operations due to its trimester based rotation, findings of stale accounts mandate MFA. |
| **8.6** | Capacity management | **Not Applicable** | Infrastructure capacity is not managed by Redback Operations. It is managed by Deakin University IT. |
| **8.7** | Protection against malware | **Applicable** | Acceptable Use Policy requires anti-virus on personal devices. The policy also restricts installation of malware. Malware is treated as critical as per the IRP. |
| **8.8** | Management of technical vulnerabilities | **Applicable** | Dependabot mandatory across all repositories as per the Secure Development policy. Trivy scanner required as well. GitHub Audit document found open vulnerabilities. OWASP TOP 10 is in code review checklist. |
| **8.9** | Configuration management | **Partial** | Secure-by-default principle is documented in Secure Development Policy. GitHub repository defaults defined in Access Control Policy. Formal configuration baseline is not present within Redback Operations yet. Applicable to Redback Operations as there Orion utilises FastAPI and security management tools. |
| **8.10** | Information deletion | **Applicable** | Offboarding procedures mandates the deletion of local data derived from Redback Operations on personal devices. |
| **8.11** | Data masking | **Not Applicable** | No publicly facing production systems with live personal data is present. Data masking is not required. |
| **8.12** | Data leakage prevention | **Partial** | Push protection is necessary in Incident Response Policy for credential exposure incidents. However, there are no formal DLP tools utilised. Applicable to the company as we utilise publicly facing repositories. |
| **8.13** | Information backup | **Partial** | ISMS is stored in GitHub or Docusaurus. Data Warehouse team utilises Restic for backups of their lakehouse architecture. No formal back up policy. |
| **8.14** | Redundancy of information processing facilities | **Not Applicable** | Redback Operations does not have any information processing facilities. |
| **8.15** | Logging | **Applicable** | GitHub activity logs and Wazuh security logs are established as evidence in the Incident Response Policy. Evidence preservation requirements are established in the IRP as well. |
| **8.16** | Monitoring activities | **Applicable** | Acceptable Use Policy defines reviewing GitHub activity logs and security scanning results whilst Blue Team manages Wazuh monitoring. |
| **8.17** | Clock synchronisation | **Not Applicable** | Clock synchronisation is per personal device and Deakin IT manages university supervised hardware. |
| **8.18** | Use of privileged utility programs | **Applicable** | Access to security tooling is only to Blue Team as per the Acceptable Use Policy. Workflow file changes are reviewed by SecDevOp through PRs as per the Acceptable Use Policy. |
| **8.19** | Installation of software on operational systems | **Applicable** | Acceptable Use Policy mandates only open-source or licensed software must be utilised for Redback operations systems. Dependency sources need to be official as per the Secure Development Policy. |
| **8.20** | Networks security | **Not Applicable** | Network security is handled by the Deakin IT team for VMs and Deakin managed software. Network is managed by ISPs for personal devices. |
| **8.21** | Security of network services | **Not Applicable** | Network services are managed by Deakin University IT for devices on network premises. Redback Operations does not manage security of network services. |
| **8.22** | Segregation of networks | **Not Applicable** | Network segregation is managed by Deakin University IT Team for devices on university premises and ISPs for personal devices. |
| **8.23** | Web filtering | **Not Applicable** | Web filtering is managed by ISPs and by Deakin University IT staff for devices on university premises. |
| **8.24** | Use of cryptography | **Applicable** | The Data Handling Policy mandates encryption at rest and in transit for data that is given the Confidential classification. |
| **8.25** | Secure development lifecycle | **Applicable** | The SDP lists security by design, secure by default, defense in depth and least privilege to be practiced in Redback Operations. The OWASP 10 and a PR checklist is also in the review process. |
| **8.26** | Application security requirements | **Applicable** | Input validation, error handling and OWASP Top 10 are checked in code reviews as per the Secure Development Policy. This is applicable to projects developing, such as Garmin Smartwatch. |
| **8.27** | Secure system architecture and engineering principles | **Applicable** | Defense-in-depth and security-by-design principles are listed in the Secure Development Policy. |
| **8.28** | Secure coding | **Applicable** | Language specific coding standards are defined for Python, Monkey C and C# in the Secure Development Policy. PR Checklist for reviews also mandates secure coding. |
| **8.29** | Security testing in development and acceptance | **Applicable** | Trivy scanner and Dependabot is mandatory for all repositories. OWASP TOP10 review is required. |
| **8.30** | Outsourced development | **Not Applicable** | All development is done by the students in Redback Operations. |
| **8.31** | Separation of development, test and production environments | **Partial** | Main branch protection rules are defined in the Access Control Policy and Secure Development Policy. However, there are no formal separation processes of dev/test/prod environments. |
| **8.32** | Change management | **Applicable** | Pull request review process mandatres review before any code is merged into the repository. Workflow file changes is to be reviewed by SecDevOps and signed off. Policy changes are also version-controlled and dated. |
| **8.33** | Test information | **Not Applicable** | No production data is used in testing environments. Test data is synthetic or project generated. |
| **8.34** | Protection of information systems during audit testing | **Partial** | GitHub audit is conducted. A formal audit procedure company wide is not documented, next cohort should communicate with tutors on how to do so. |

## Document Review

The Statement of Applicability must be reviewed at the start of each trimester by the Ethics / GRC team. Any changes to the ISMS document suite, scope or systems will require the SoA to be revised. All changes must be version-controlled and dated.
