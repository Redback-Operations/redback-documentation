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

| Version | Date | Author | Changes |
| ---- | ---- | ---- | ---- |
| 1.0 | 05/04/24 | Kaleb Bowen | Document Creation |
| 2.0 | 04/09/24 | Tom Mirarchi | Fixed numbering for compliance, Added Links to other policies, added sections not present in policy for future changes |

## 1. Scope

The Information Security Management System (ISMS) establishes the guiding principles and policies for Redback Operations, being the comprehensive and overarching system complying with ISO/IEC 27001.  This document is intended to provide a framework for Redback Operations and affiliated contributors to implement and continuously manage the security of its information assets.

The scope of this ISMS includes all information assets, including but not limited to:

-	Data Classification & Data Loss Prevention (DLP)

-	Cloud Security

-	Server Security & Hardening

-	Endpoint Security

-	Encryption / Cryptography 

-	Monitoring & Log Analysis

-	User Awareness Training

-	External Attack Surface Management

-	BYOD & MDM

## 2. Normative References

This section is not applicable with Redback Operations but is kept in to ensure further section numbering is compliant with ISO/IEC 27001.

## 3. Terms and Definitions 

For the purpose of this document, ISO/IEC 27001 apply unless specified otherwise.

ISO and IEC maintain terminology databases for use in standardisation at the following addresses:

- ISO Online browsing platform: available at https://www.iso.org/obp        
- IEC Electropedia: available at https://www.electropedia.org/

## 4. Context of the Organisation 

### 4.1. Understanding the Organisation and its Context

Redback Operations is a student-led, open-source project (referred to as Redback Operations, or “the company”) with a focus on human biometrics, including through the use of wearable devices, fitness apparatus, and monitoring and tracking devices. The result of which leads Redback Operations to handle sensitive and personal data that may be required to be handled in such a way to comply with relevant legislation. Additional ISMS processes may also be adopted in consideration with the efforts and needs of the company and the appropriate protections following.

### 4.2. Understanding the Needs and Expectations of Interested Parties

Interested parties relevant to the project include Deakin University and its affiliated tutors and staff connected to the Redback Operations project, and students enrolled in SIT374/SIT764 and SIT378/SIT768. Tutors and students are split into individual projects within the company, as such students and tutors may have different needs and expectations depending on their role. 

| Stakeholders | Internal / External | Issues |
|--------------|---------------------|--------|
| Tutors, Staff | Internal | Organisation structure, roles and accountabilities, top-level delegations. |
| Project Leads, Team Leads, Students | Internal | Delegation of tasks, fulfilment of commitments, compliance to policy and guidelines. |
| Government | External | Fulfilling the legal and regulatory requirements. |

All issues listed in the above table will hope to be addressed throughout this ISMS policy. Whether it be through inquiries into each stakeholder to determine what the best course of action will be to mitigate these issues or company-wide reforms to eliminate all issues

### 4.3. Determining the Scope of the Information Security Management System

The ISMS encompasses all digital and physical items owned by or in direct affiliation with Redback Operations. Redback Operations does not have a physical headquarters, and has contributors in many different legal jurisdictions, so this must be taken into consideration when legislation or government policies are discussed.

### 4.4. Information Security Management System

As per the requirements of ISO/IEC 27001, Redback Operations has implemented this Information Security Management System (ISMS) and established procedures to continually improve the system following the structure of the organisation as a student-run, trimester-based project. If a response to a requirement can be written in small-form-factor, it will be done so in this manual, otherwise, this manual will reference the appropriate documentation and its location within the documentation system to provide further extended policy explanation. For the purpose of continuity, all auxiliary documentation will be listed in section 11 with links to the Redback Operations documentation website.

## 5. Leadership

### 5.1. Leadership and Commitment

Deakin University, staff, tutors, and student leaders affiliated with the Redback Operations company must be committed to continue high-level information security and thus ensuring that the overall organisation is taking sufficient steps in ensuring the organisation’s security policies and objectives are in line with modern practices and the general strategic direction.

### 5.2. Policy

Protection of Redback Operations is regulated across several policies relating to the type of information or systems rather than one central policy. These policies are mentioned in section 1 and available to view in section 12. Further policies may be requested by company leaders as needed, or existing policies be reviewed, as is the nature of the continual evolution of this ISMS and other policies. 

### 5.3. Organisational Roles, Responsibilities, and Authorities

Presently, responsibility of this ISMS and other policies falls within the Cyber Security team of Redback Operations. As such, it is their responsibility to ensure compliance with ISO/IEC 27001 and all relevant legislation and governance on which Redback Operations falls within. Company leaders have the right to request review of the ISMS and affiliated policies, which again falls within the Cyber Security team. The Cyber Security team may request assistance from other teams to ensure complete understanding of their projects and what that entails in relation to the company policies; additionally, they may ask to delegate new / updated policies from a team should they have someone willing and able to complete it.

## 6. Planning

### 6.1. Actions to Address Risk and Opportunities

#### 6.1.1.	General

Following the issues and requirements outlined in sections 4.1 and 4.2, the following items should be addressed:

- Assurance that this ISMS can achieve its intended outcomes.

- Preventing avoidable IT-related incidents.

- Achieving continual improvement.

Following supplementary policy should sufficiently address the above mentioned in a way that also covers potential data breaches and their impact on Redback Operations, data protection, managing risks, and proactive remediation. 

#### 6.1.2.	Information Security Risk Assessment

In accordance with ISO/IEC 27001, a Risk Analysis and Treatment Plan, along with a Statement of Applicability should be created to work alongside this ISMS to ensure understanding of risks associated with Redback Operations are sufficiently known. This should be done in the near future in order to further solidify this policy's and company's compliance with ISO/IEC 27001

#### 6.1.3.	Information Security Risk Treatment

As stated in 6.1.2. This should also be done in the near future to ensure this policy's compilance with ISO/IEC 27001

### 6.2. Information Security Objectives and Planning

To manage the company’s information security posture effectively and efficiently, it is essential to develop objectives, measurements, and reporting tools, compiled within an Information Security Metrics Repository (ISMP). The ISMP will ensure consistent information security measurement across all aspects of the company.

There are 7 metrics we will aim to follow:
1.	Level of Preparedness – How prepared are we in the event of a breach
2.	Intrusion attempts – What is the process for detecting and mitigating intrusion attempts and how can it be more efficient?
3.	Security Incidents – What do we do in the event of an attack in terms of data recovery, root cause, average down time, preventative maintenance etc.
4.	Mean Time to Detect (MTTD) – What is the efficiency of our threat detection system?
5.	Mean Time to Resolve (MTTR) – How quickly can we resolve a threat?
6.	Mean Time to Contain (MTTC) – How long does it take to contain an attack and minimise its effectiveness?
7.	Access Management – How is access to sensitive data and systems controlled and monitored?


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

The Redback Operations Information Security Management System, under the direction of the Cyber Security team and company leaders, outlines the processes necessary to secure company information from threats. As with 7.5.3, the size of Redback Operations does not deem it necessary to have internal audit procedure or management review procedures, and these should be conducted on an ad-hoc schedule. Future growth or needs of the company may determine formal policy to cover these audits.

### 8.2. Information Security Risk Assessment

As stated in 6.1.2. This will need to be reviewed on an ad-hoc basis

### 8.3. Information Security Risk Treatment

As stated in 6.1.2. This will need to be reviewed on an ad-hoc basis

## 9. Performance Evaluation

### 9.1. Monitoring, Measurement, Analysis, and Evaluation

Performance of policies should be reviewed on a regular basis, no less than once every year. Adjustments should be made and noted using version control. This can be in conjunction with previous sections of this ISMS that cover yet-to-exist audits due to the size of the company.

### 9.2. Internal Audit

#### 9.2.1. General

As stated in 9.1. This will need to be reviewed on an ad-hoc basis

#### 9.2.2. Internal audit programme

As stated in 9.1. This will need to be reviewed on an ad-hoc basis

### 9.3. Management Review

#### 9.3.1. General

Redback Operations does not operate with a typical management structure and as such quarterly meetings, as outlined in ISO/IEC 27001 are not reasonable. Company goals and policy reviews should be done on an ad-hoc basis.

#### 9.3.2. Management Review Inputs

As stated in 9.3.1. May not be applicable to Redback Operations. This will need to be reviewed on an ad-hoc basis

#### 9.3.3. Management Review Results

As stated in 9.3.1. May not be applicable to Redback Operations. This will need to be reviewed on an ad-hoc basis

## 10. Improvement

### 10.1. Continual Improvement

The company is committed to continually improving this ISMS and other policy documents as the company evolves over time. This will be done with consistent reviews of the policies to ensure their compliance

If a review of the current ISMS policy is undertaken it must adhere to the [checklist](..\docs\isms-checklist-blank.docx) which lists each requirement and whether it is currently compliant or not with ISO/IEC 27001

### 10.2. Nonconformity and Corrective Action

When an instance of nonconformity is identified within the jurisdiction of the ISMS and affiliated policies, team and / or company leaders may act on it by implementing corrective actions. This should begin with identifying the issue itself and the ramifications it may bring, developing a fix for the issue and implementing it, and developing or fixing current solutions to ensure the nonconformity is unlikely to happen again.

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