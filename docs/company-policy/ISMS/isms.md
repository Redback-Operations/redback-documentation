---
sidebar_position: 1
sidebar_label: ISMS
---

# Information Security Management System

Redback Operations ISMS Guide

:::info
**Document Creation:** 5 April, 2024. **Last Edited:** 4 September, 2024. **Author:** Kaleb Bowen.
<br></br>**Document Code:** ISMS. **Effective Date:** 1 May 2024. **Expiry Date:** 1 May 2025. **Version:** 2.0
:::
## Version History

| Version | Date       | Author            | Approver | Changes                                                                 |
|---------|------------|-------------------|----------|-------------------------------------------------------------------------|
| 1.0     | 05/04/2024 | Kaleb Bowen       |          | Document Creation                                                      |
| 2.0     | 04/09/2024 | Tom Mirarchi      |          | Fixed numbering for compliance, added links to policies, added sections |
| 3.0     | 18/05/2025 | Nathasha Liyanage |          | Unified ISMS with NIST CSF, Essential 8, APA/APPs; added objectives, phased implementation, team roles, 6-month review cycle |

## 1. Purpose

The Information Security Management System (ISMS) provides a unified framework for managing Redback Operations’ information security risks and ensuring compliance with ISO/IEC 27001, NIST Cybersecurity Framework (CSF), Essential Eight, and Australian Privacy Principles (APP). It consolidates policies to protect information assets during Redback’s transitional stage across Google Cloud Platform (GCP), Azure, on-premises systems, and research activities.

The ISMS aims to:
- Achieve Essential 8 Maturity Level 1 to mitigate common cyber threats.
- Ensure full compliance with the Australian Privacy Act and APPs.
- Reduce technical debt-fuelled security risks by 50% within 12 months.
- Establish a defence-in-depth posture aligned with NIST CSF functions: Identify, Protect, Detect, Respond, Recover.
  
## 2. Scope

The Information Security Management System (ISMS) establishes the guiding principles and policies for Redback Operations, being the comprehensive and overarching system complying with ISO/IEC 27001.  This document is intended to provide a framework for Redback Operations and affiliated contributors to implement and continuously manage the security of its information assets.

The scope of this ISMS includes all information assets, including but not limited to:

-	Data Classification & Data Loss Prevention (DLP)
- Cloud Security (GCP, Azure)
- Server Security & Hardening
- Endpoint Security (e.g., laptops, smart wearables, exercise bikes)
- Encryption / Cryptography
- Monitoring & Log Analysis
- User Awareness Training
- External Attack Surface Management (EASM)
- Bring Your Own Device (BYOD) & Mobile Device Management (MDM)

## 3. Normative References

The ISMS aligns with:
- **ISO/IEC 27001:2013**: Information Security Management
- **NIST Cybersecurity Framework (CSF)**: Version 1.1, 2018. Available at: https://doi.org/10.6028/nist.cswp.04162018
- **Essential Eight**: Maturity Model, ACSC, 2017. Available at: https://www.cyber.gov.au/resources-business-and-government/essential-cybersecurity/essential-eight/essential-eight-maturity-model
- **Australian Privacy Principles (APP)**: Privacy Act, OAIC, 2024. Available at: https://www.oaic.gov.au/privacy/privacy-legislation/the-privacy-act

Terminology is sourced from:
- ISO Online Browsing Platform: https://www.iso.org/obp
- IEC Electropedia: https://www.electropedia.org/

## 4. Context of the Organisation 

### 4.1. Understanding the Organisation and its Context

Redback Operations is a student-led, open-source project (referred to as Redback Operations, or “the company”) with a focus on human biometrics, including through the use of wearable devices, fitness apparatus, and monitoring and tracking devices. The result of which leads Redback Operations to handle sensitive and personal data that may be required to be handled in such a way to comply with relevant legislation. Additional ISMS processes may also be adopted in consideration with the efforts and needs of the company and the appropriate protections following.

### 4.2. Understanding the Needs and Expectations of Interested Parties

Interested parties relevant to the project include Deakin University and its affiliated tutors and staff connected to the Redback Operations project, and students enrolled in SIT374/SIT764 and SIT378/SIT768. Tutors and students are split into individual projects within the company, as such students and tutors may have different needs and expectations depending on their role. 

| Stakeholders              | Internal/External | Issues                                              |
|---------------------------|-------------------|----------------------------------------------------|
| Tutors, Staff, Mentors    | Internal          | Organisation structure, roles, academic compliance |
| Project Leads, Students   | Internal          | Task delegation, policy adherence, data security   |
| Deakin University         | Internal          | Alignment with IT policies, resource constraints   |
| Government (e.g., OAIC)   | External          | Privacy Act, APPs, cybersecurity regulations       |

All issues listed in the above table will hope to be addressed throughout this ISMS policy. Whether it be through inquiries into each stakeholder to determine what the best course of action will be to mitigate these issues or company-wide reforms to eliminate all issues

### 4.3. Determining the Scope of the Information Security Management System

The ISMS encompasses all digital and physical items owned by or in direct affiliation with Redback Operations including cloud platforms, research devices, and collaboration tools (e.g., MS Teams, code repositories). Redback Operations does not have a physical headquarters, and has contributors in many different legal jurisdictions, so this must be taken into consideration when legislation or government policies are discussed.

### 4.4. Information Security Management System

As per the requirements of ISO/IEC 27001, Redback Operations has implemented this Information Security Management System (ISMS) and established procedures to continually improve the system following the structure of the organisation as a student-run, trimester-based project. If a response to a requirement can be written in small-form-factor, it will be done so in this manual, otherwise, this manual will reference the appropriate documentation and its location within the documentation system to provide further extended policy explanation. For the purpose of continuity, all auxiliary documentation will be listed in section 11 with links to the Redback Operations documentation website.

## 5. Leadership

### 5.1. Leadership and Commitment

Deakin University staff, project mentors, and student leaders commit to high-level information security, aligning policies with NIST CSF, Essential 8, and APPs. Mentors act as company leaders, ensuring strategic direction and resource allocation.

### 5.2. Policy

Protection of Redback Operations is regulated across several policies relating to the type of information or systems rather than one central policy. These policies are mentioned in section 1 and available to view in section 12. Further policies may be requested by company leaders as needed, or existing policies be reviewed, as is the nature of the continual evolution of this ISMS and other policies. 

### 5.3. Organisational Roles, Responsibilities, and Authorities

- **ISMS Manager (GRC Team Lead)**: Oversees policy development, compliance, and audits.
- **Policy Owners**: Maintain and update domain-specific policies.
- **Technical Leads (IT Team)**: Implement controls, monitor risks, report incidents.
- **All Staff/Contributors**: Comply with policies, complete training, report incidents.
The Cyber Security team coordinates ISMS implementation, with authority to request reviews or delegate tasks.

## 6. Planning

### 6.1. Actions to Address Risk and Opportunities

#### 6.1.1.	General

The ISMS addresses:
- Achieving Essential 8 Maturity Level 1 and APP compliance.
- Reducing technical debt by 50% within 12 months.
- Preventing IT incidents via defence-in-depth controls.
- Ensuring continual improvement with NIST CSF functions.

Following supplementary policy should sufficiently address the above mentioned in a way that also covers potential data breaches and their impact on Redback Operations, data protection, managing risks, and proactive remediation. 

#### 6.1.2.	Information Security Risk Assessment

In accordance with ISO/IEC 27001, a Risk Analysis and Treatment Plan, along with a Statement of Applicability should be created to work alongside this ISMS to ensure understanding of risks associated with Redback Operations are sufficiently known. This should be done in the near future in order to further solidify this policy's and company's compliance with ISO/IEC 27001

#### 6.1.3.	Information Security Risk Treatment

Risk treatments prioritize Essential 8 controls (e.g., patch applications, restrict admin privileges) and NIST CSF recommendations.

### 6.2. Information Security Objectives and Planning

To manage the company’s information security posture effectively and efficiently, it is essential to develop objectives, measurements, and reporting tools, compiled within an Information Security Metrics Repository (ISMP). The ISMP will ensure consistent information security measurement across all aspects of the company.

Objectives are tracked in the Information Security Metrics Repository (ISMP):
- **Level of Preparedness**: Breach response readiness.
- **Intrusion Attempts**: Detection and mitigation efficiency.
- **Security Incidents**: Recovery, root cause, prevention.
- **Mean Time to Detect (MTTD)**: Threat detection speed.
- **Mean Time to Resolve (MTTR)**: Threat resolution time.
- **Mean Time to Contain (MTTC)**: Attack containment time.
- **Access Management**: Sensitive data access control.

Using these metrics will allow us to stay ahead of any possible risks that may occur. These metrics will need to be reviewed on an ad-hoc basis

### 6.3. Planning of Changes

When there is a need to make changes to the ISMS policy in future. These will be planned well in advance in order to ensure that the changes have been well researched to keep the company and policy up to standard. All relevant documents for these planned changes should be made public accessible on the [documentation site](https://redback-operations.github.io/redback-documentation/) 

## 7. Support

### 7.1. Resources

Redback Operations, as a student-lead project, does not have the same resources as the typical IT organisation. As such, roles such as HR, Ethics and Policy Managers, and Risk Advisors are split amongst students, typically of the Cyber Security team, who wish to undertake tasks within these areas. This organisation structure also means Redback Operations does not have a Management Review Board as required by ISO/IEC 27001, however it can be determined that company leaders act in a similar capacity in terms of review and request of changes to the ISMS.

### 7.2 Competence

Redback Operations is committed to ensuring that all staff and students working on projects that use IT systems or handle sensitive information are working within the ISMS. This may include the need to provide training or time to get up to speed with the company standards, as well as implementing compliance and competence tracking systems on tasks that require so.

### 7.3. Awareness

Redback Operations ensures that all documentation relevant and including the ISMS are easily accessible via the [documentation site](https://redback-operations.github.io/redback-documentation/), and formatted in an easily viewable and accessible means for all that require.

### 7.4. Communication

Changes to the ISMS or other policies affecting the overall company will be communicated internally via the company’s Microsoft Teams platform. Changes to documentation will be reflected within the documentation itself via versioning notes, and where possible previous versions will be viewable as a way to reflect on changes.

### 7.5. Documented Information

#### 7.5.1. General

All controlled versions of Redback Operations documentation can be found on the [documentation site](https://redback-operations.github.io/redback-documentation/). All locally saved or printed copies are uncontrolled versions and may not be the most current.

#### 7.5.2. Creating and Updating

Creation of policy is formed through discussion of relevant teams, with team leaders, mentors, and company leaders having overall ownership of all documents. The student(s) responsible for creating specific documents also have ownership for the duration of their time within Redback Operations. Updating of documents must clearly number what revision it is of the document. The document must also list what changes were made and who it was by.

#### 7.5.3. Control of Documented Information

Given the size and nature of Redback Operations, at present the use of a Document Control Procedure and Document Control System Master Listing is not necessary. This should be reviewed on an ad-hoc basis.

## 8. Operation

### 8.1. Operational Planning and Control

The Cyber Security team oversees controls aligned with NIST CSF:
- **Identify**: Asset inventory, risk assessments.
- **Protect**: Access controls, encryption, patching.
- **Detect**: Monitoring, log analysis.
- **Respond**: Incident response plans.
- **Recover**: Data recovery, post-incident reviews.
Controls are platform-agnostic for GCP, Azure, and on-premises assets.

### 8.2. Information Security Risk Assessment

Bi-annual risk assessments are documented in the Risk Analysis and Treatment Plan

### 8.3. Information Security Risk Treatment

Treatments prioritize Essential 8 and NIST CSF controls, tracked via Trello.

## 9. Performance Evaluation

### 9.1. Monitoring, Measurement, Analysis, and Evaluation

Performance of policies should be reviewed on a regular basis, no less than once every year. Adjustments should be made and noted using version control. This can be in conjunction with previous sections of this ISMS that cover yet-to-exist audits due to the size of the company.

### 9.2. Internal Audit

#### 9.2.1. General

Bi-annual audits by the Cyber Security team assess ISO/IEC 27001 and Essential 8 compliance.

#### 9.2.2. Internal audit programme

Audits use an ISO/IEC 27001 checklist, with results reported to mentors.

### 9.3. Management Review

#### 9.3.1. General

Mentors and student leaders review ISMS performance bi-annually.

#### 9.3.2. Management Review Inputs

Inputs include audit results, ISMP metrics, and incident reports.

#### 9.3.3. Management Review Results

Results drive policy updates and corrective actions, documented on the Redback Documentation site.

## 10. Improvement

### 10.1. Continual Improvement

The company is committed to continually improving this ISMS and other policy documents as the company evolves over time. This will be done with consistent reviews of the policies to ensure their compliance

If a review of the current ISMS policy is undertaken it must adhere to the [checklist](..\docs\isms-checklist-blank.docx) which lists each requirement and whether it is currently compliant or not with ISO/IEC 27001

### 10.2. Nonconformity and Corrective Action

Nonconformities trigger:
- Issue identification and impact assessment.
- Corrective action implementation.
- Policy updates to prevent recurrence.
Actions are tracked via Trello and reported to mentors.

## 11. Supplementary Policies

This section contains links to supplementary policies affiliated with Redback Operations and this ISMS.

[Gap Analysis](https://redback-operations.github.io/redback-documentation/docs/company-policy/ISMS/gap-analysis)

[Cryptography](https://redback-operations.github.io/redback-documentation/docs/company-policy/ISMS/cryptography)

[DLP & Data Classification](https://redback-operations.github.io/redback-documentation/docs/company-policy/ISMS/dlp-data-classification)

[Endpoint Security](https://redback-operations.github.io/redback-documentation/docs/company-policy/ISMS/endpoint)

[External Attack Surface Management (EASM)](https://redback-operations.github.io/redback-documentation/docs/company-policy/ISMS/easm)

[Monitoring & Log Analytics](https://redback-operations.github.io/redback-documentation/docs/company-policy/ISMS/monitoring-log-analytics)

[Server Security](https://redback-operations.github.io/redback-documentation/docs/company-policy/ISMS/server-security)

[User Awareness Training](https://redback-operations.github.io/redback-documentation/docs/company-policy/ISMS/User-Awareness-Training)

[Review of ISMS](https://redback-operations.github.io/redback-documentation/docs/company-policy/Policy%20Reviews/isms-review)
