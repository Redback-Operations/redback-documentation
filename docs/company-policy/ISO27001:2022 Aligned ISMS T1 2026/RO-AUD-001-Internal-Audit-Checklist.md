# Internal Audit Checklist

## Redback Operations – ISO27001:2022 ISMS

| **Document Code** | RO – AUD – 001 |
| --- | --- |
| **Version** | 1.0 |
| **Review Interval** | Start of Each Trimester |
| **Document Owner** | Ethics / GRC Team |
| **ISO Reference** | ISO/IEC 27001:2022 – Clause 9.2 |
| **Conducted by** |  |
| **Date Conducted** |  |

---

## Purpose

This checklist is to verify that the information security controls established in the ISMS are active and functioning per trimester. Results should be recorded and any failures or partial responses should be registered in the Gap Analysis.

## Utilisation of Internal Audit Checklist

- Work through each audit question and mark Yes, No or Partial
- For any No or Partial response, document findings in Evidence / Notes column and add to the Gap Analysis for it to be identified and rectified.
- Internal Audit Checklist should be stored with the rest of the ISMS suite.
- Audit should be completed independently by a member of the Ethics / GRC Team Member or Leader.

## Audit Questions

| **#** | **Control Area** | **Audit Question** | **Yes / No / Partial** | **Evidence / Notes** |
| --- | --- | --- | --- | --- |
| **1** | Access Control | Has a GitHub membership review been conducted this trimester? Are all members current enrolled students or authorised tutors? | ☐ Yes   ☐ No   ☐ Partial |  |
| **2** | Access Control | Has MFA been confirmed as enabled for all active members across GitHub, Microsoft Entra ID, and HiveMQ within 5 days of enrolment? | ☐ Yes   ☐ No   ☐ Partial |  |
| **3** | Access Control | Have all members from the previous trimester had their GitHub access, PATs, and platform access revoked as per the offboarding procedure? | ☐ Yes   ☐ No   ☐ Partial |  |
| **4** | Access Control | Are repository access permissions restricted to team members only, with admin access limited to SecDevOps, tutors, and team leads? | ☐ Yes   ☐ No   ☐ Partial |  |
| **5** | Vulnerability Management | Are Dependabot alerts active across all repositories? Have alerts from the previous trimester been reviewed and actioned by SecDevOps? | ☐ Yes   ☐ No   ☐ Partial |  |
| **6** | Vulnerability Management | Is the Trivy scanner workflow active and running on all active repositories? Are code scanning alerts being reviewed before merges? | ☐ Yes   ☐ No   ☐ Partial |  |
| **7** | Secure Development | Are branch protection rules enabled on all active repository main branches? Is pull request review enforced before any merge? | ☐ Yes   ☐ No   ☐ Partial |  |
| **8** | Secure Development | Has a check been performed to confirm no hardcoded credentials, API keys, or PII are present in any active repository? | ☐ Yes   ☐ No   ☐ Partial |  |
| **9** | Incident Management | Has the Incident Register been reviewed? Are all incidents from the previous trimester documented with resolution status recorded? | ☐ Yes   ☐ No   ☐ Partial |  |
| **10** | Policy Compliance | Have all active members acknowledged and read the ISMS policies (AUP, ACP, IRP) as part of their onboarding this trimester? | ☐ Yes   ☐ No   ☐ Partial |  |
| **11** | Policy Compliance | Have all ISMS documents been reviewed and updated to reflect the current trimester including effective dates, team names, and member counts? | ☐ Yes   ☐ No   ☐ Partial |  |
| **12** | Asset Management | Has the Asset Register been reviewed and updated this trimester? Are all active assets documented with correct owners and classification? | ☐ Yes   ☐ No   ☐ Partial |  |
| **13** | Risk Management | Has the Risk Register been reviewed this trimester? Have new risks been added and treatment statuses updated from the previous trimester? | ☐ Yes   ☐ No   ☐ Partial |  |
| **14** | Security Awareness | Have security awareness briefings been conducted with all 8 teams this trimester? Is attendance documented? | ☐ Yes   ☐ No   ☐ Partial |  |
| **15** | ISMS Documents | Are all ISMS documents stored in the shared GitHub repository or Docusaurus wiki, not on personal drives and accessible to all current members? | ☐ Yes   ☐ No   ☐ Partial |  |

## Document Review

This checklist is to be reviewed and updated at the start of each trimester to reflect any additional controls, policies or systems to the ISMS. Questions are to be added or removed based on the findings from the previous Gap Analysis
