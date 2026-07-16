# Gap Analysis

## Redback Operations – ISO27001:2022 ISMS

| **Document Code** | RO – GA – 001 |
| --- | --- |
| **Version** | 1.0 |
| **Review Date** | End of Each Trimester |
| **Document Owner** | Ethics / GRC Team |
| **ISO Reference** | ISO/IEC 27001:2022 – Clauses 9.1, 10.1, 10.2 |
| **Prepared By** | Ramon Garcia – Ethics / GRC Team leader, T1 2026 |

---

## Purpose

The Gap Analysis documents the information security controls and procedures that were not active or present during Trimester 1 2026. The analysis identifies each gap, priority and the recommended action for the next cohort of the Ethics / GRC team. This document supports the continual improvement requirement under ISO/IEC 27001:2022 Clauses 10.1 and 10.2. The analysis is meant to define what actions are needed to fortify the security posture of Redback Operations for T2 2026.

## Scope

The Gap Analysis covers all 93 Annex A controls assessed in the Statement of Applicability.

## What Was Completed This Trimester

The following ISMS deliverables were completed during Trimester 1, 2026:

- ISMS Scope Statement (RO-ISMS-001)
- Asset Register (RO-REG-001):  gathered via direct team lead outreach across all 8 teams
- Risk Register (RO-REG-002): risks identified, scored, and treatment actions assigned
- Information Security Policy (RO-POL-001)
- Access Control Policy (RO-POL-002)
- Acceptable Use Policy (RO-POL-003)
- Incident Response Policy (RO-POL-004)
- Secure Development Policy (RO-POL-005)
- Data Handling Policy (RO-POL-006)
- GitHub Audit Report (RO-AUDIT-GIT-001): audit conducted on 21-22 March 2026
- Onboarding & Offboarding Procedure (RO-CL-001)
- Statement of Applicability (RO-SOA-001): all ISO27001:2022 93 Annex A controls assessed
- Internal Audit Checklist (RO-AUD-001)

## Gap Register

This table documents all identified gaps. Priority is from High to Medium to Low based on Risk impact to Redback Operations.

| **Gap ID** | **Area / Control** | **Description of Gap** | **Priority** | **Recommended Action** |
| --- | --- | --- | --- | --- |
| **GAP-001** | 5.5 – Contact with Authorities | Formal external authority contact procedure (e.g. law enforcement, CERT Australia) is not defined. Current escalation only covers internal tutor and unit chair. | **Medium** | Define an external escalation procedure referencing CERT Australia and relevant Victorian authorities. Add to IRP. |
| **GAP-002** | 5.13 – Labelling of Information | Classification levels are defined in the Asset Register and Data Handling Policy but a consistent labelling convention has not been enforced across documents and repositories. | **Low** | Establish a labelling convention (e.g. document headers, repository README classification tags) and enforce from next trimester. |
| **GAP-003** | 5.23 – Cloud Services | Personal cloud storage is prohibited for confidential data but a formal cloud configuration baseline covering approved cloud services has not been documented. | **Medium** | Document approved cloud services and their minimum security configuration requirements. Review which teams are using cloud storage. |
| **GAP-004** | 5.35 – Independent Review | The GitHub audit was conducted internally. An independent review of the ISMS has not been performed. Internal audit checklist was created but not yet operationally run by an independent reviewer. | **Medium** | Schedule an internal audit to be run in the first two weeks of next trimester by the incoming Ethics / GRC team using RO-AUD-001. |
| **GAP-005** | 6.6 – NDAs | Member Acknowledgement form covers policy acceptance but a formal Non-Disclosure Agreement for members handling confidential project data is not in place. | **Low** | Draft a simple NDA or confidentiality clause to be added to the onboarding acknowledgement form. Review with tutor before implementing. |
| **GAP-006** | 7.14 – Secure Disposal | A formal secure disposal procedure for Redback-managed hardware is not documented. The E-Waste Battery Extraction team handles disposal as a project focus but this is not formalised in the ISMS. | **Low** | Document a secure disposal procedure for hardware used by Redback teams. Coordinate with E-Waste Battery Extraction team. |
| **GAP-007** | 8.9 – Configuration Management | Secure-by-default principle and GitHub repository defaults are defined in policy but a formal configuration baseline register documenting expected states for all active systems has not been created. | **Medium** | Create a configuration baseline register covering GitHub repository settings, Entra ID role configurations, and HiveMQ access settings. |
| **GAP-008** | 8.12 – Data Leakage Prevention | GitHub secret scanning and push protection are referenced but formal DLP tooling has not been deployed. No systematic mechanism exists to detect data leakage beyond repository scanning. | **High** | Enable GitHub secret scanning and push protection across all active repositories. Evaluate lightweight DLP tooling options for next trimester. |
| **GAP-009** | 8.13 – Information Backup | ISMS documents are stored in GitHub providing version history, however a formal backup policy and schedule covering all Redback information assets has not been documented. | **Medium** | Document a backup schedule and responsibility assignment for all critical ISMS documents and registers. Confirm GitHub repository backup settings. |
| **GAP-010** | 8.31 – Dev/Test/Prod Separation | Branch protection rules are defined but formal separation of development, test and production environments has not been documented or consistently enforced across all 8 project teams. | **Medium** | Work with SecDevOps to define and enforce environment separation standards across all active repositories. Document in Secure Development Policy. |
| **GAP-011** | 8.34 – Audit Testing Protection | The GitHub audit was conducted without formal isolation procedures documented. Audit activities could potentially affect live operations if not carefully managed. | **Low** | Document audit testing procedures including scope boundaries, notification requirements, and rollback procedures for future audits. |
| **GAP-012** | Operational Evidence | The ISMS document suite describes what should happen but limited operational evidence exists of controls actually being performed, MFA confirmation, access review logs, team briefing records, and incident register entries are absent. | **High** | Collect and store operational evidence each trimester: MFA screenshots, access review sign-offs, team briefing attendance records, and at minimum one Incident Register entry. |
| **GAP-013** | Security Awareness Delivery | Policy awareness sessions were planned for all 8 teams but delivery and attendance were not formally documented. No evidence exists of security awareness training being completed. | **High** | Conduct and document security awareness sessions at the start of each trimester. Maintain attendance records as operational evidence. |
| **GAP-014** | Stale GitHub Members | GitHub audit identified 32 unaccounted members in the GitHub organisation beyond enrolled students. Status of remediation was not confirmed before end of trimester. | **High** | Confirm remediation of stale GitHub members with tutor. Implement a formal GitHub membership review as a mandatory start-of-trimester task. |
| **GAP-015** | Dependabot Vulnerabilities | Orion repository had 377 open Dependabot vulnerability flags at time of audit. Data Warehouse had 19 and Ethics repository had 6. Remediation status was not confirmed by trimester end. | **High** | Prioritise resolution of Orion Dependabot vulnerabilities with SecDevOps. Confirm all repositories have Dependabot alerts actively monitored and resolved. |

## Priority Summary

The incoming Ethics / GRC Team should address the gaps identified in this order:

- High Priority Gaps (GAP – 008, GAP – 012, GAP – 013, GAP – 014, GAP – 015) should be addressed ideally within the first two weeks of T2, 2026.
- Medium Priority Gaps (GAP-001, GAP-003, GAP-004, GAP-007, GAP-009, GAP-010) should be completed by the middle of the trimester, Week 6 – 8.
- Low Priority Gaps (GAP-002, GAP-005, GAP-006, GAP-011) should be completed in the second half of the trimester.

## Document Review

This document should be reviewed by the Ethics / GRC Team at the end of each trimester. Utilise this document for the next cohort to rectify gaps identified. All changes should be version-controlled and dated.
