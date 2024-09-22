---
sidebar_position: 3
sidebar_label: Project 4 - Player Tracking Audit Report
---

# Project 4 - Player Tracking Audit Report

:::info
**Published Date** 19/09/2024 (Trimester 2 2024) **Authors:** Liam Fern
:::

# Introduction

This report details the findings of a cyber audit of the Crowd Monitoring and Player Tracking team (Project 4) for Redback Operations. This audit occurred on Wednesday 11<sup>th</sup> September 2024 between Vincent Tran (Project Team Leader) and Liam Fern (Cyber Security Team). The purpose of this audit was to assess the compliance of the Player Tracking project with the cyber security policies, recommendations and best practice of Redback Operations. This report contains information regarding the systems and data utilised within the Player Tracking project, the audit questions and answers, and the findings and recommendations from the audit.

# Systems & Data Used

As part of the audit, the following systems were identified as in use within the Player Tracking project.

- MongoDB
- Github
- VSCode
- Python Programming
- TypeScript
- Roboflow
- IP Camera

# Audit

## Section 1 – Policy Compliance

### 1.1 Are the correct encryption methods being used for data in storage and transmission?

**Compliant**

**No**

**Observations / Comments**

API Key used to access data, data is not encrypted. Github not encrypted. IP Camera in use for live tracking MicroSD flash card used for storage, not keeping historic data.

**Recommendation / Action Required**

Investigate data encryption options for the data stored in databases (eg MongoDB) and the Github Repo.

### 1.2 Are the related DLP Policies being adhered to?

**Compliant**

**No**

**Observations / Comments**

Access Control – All team members using account to access Database

Encryption – not used

Watermarking – Logo in Database but no other watermarking

**Recommendation / Action Required**

Implement better access control including individual accounts instead of shared. Control access to database by implementing proper user management. Investigate Watermarking data in storage.

### 1.3 Are the related Data Classification Policies being adhered to?

**Compliant**

**No**

**Observations / Comments**

No data classification happening. Known sensitive data stored including Facial detection data stored in database, this data is not ranked by sensitivity.

**Recommendation / Action Required**

Run a data discovery project to identify and classify sensitive data, critical data and other forms of data. Since it is known there is sensitive data being stored, classifying this should be done as soon as possible.

### 1.4 Have forms of physical security for data protection been implemented?

**Compliant**

**N/A / NO**

**Observations / Comments**

No physical security for data, IP camera used but property of individual team member. IP camera planned to be physically put in place when program is implemented.

**Recommendation / Action Required**

While there is limited physical infrastructure in use, security of the physical ip camera should be considered.

### 1.5 Have forms of digital security for data protection been implemented?

**Compliant**

**Yes / Somewhat**

**Observations / Comments**

Notification have been setup if people access database, emails team leaders if people access/use database/account.

**Recommendation / Action Required**

While limited controls have been implemented, significantly greater controls are needed.

### 1.6 Have EASM Risks been identified?

**Compliant**

**No**

**Observations / Comments**

No EASM risks identified as project team unaware of EASM and related EASM policy.

**Recommendation / Action Required**

Project team need to make themselves aware of the EASM policy and identify any risks.

### 1.7 Have appropriate EASM risk management strategies been implemented?

**Compliant**

**No**

**Observations / Comments**

No EASM risks identified therefore no mitigation strategies have been implemented.

**Recommendation / Action Required**

Once project team have identified any EASM risks, they should implement mitigation strategies as per the EASM policy.

### 1.8 Have all employees undergone the appropriate User Awareness Training?

**Compliant**

**No**

**Observations / Comments**

No training has been undertaken by any member of the project team.

**Recommendation / Action Required**

Cyber Security team should develop user awareness training and deliver it to the Project 4 team.

## Section 2 – Ethical Considerations and Requirements

### 2.1 Are all forms of data collection briefed with customers, and consent is gathered?

**Compliant**

**No**

**Observations / Comments**

No consent gathered, but did gather information to use the data. Clients not briefed or consent provided. Will have notification/consent before innofest as plans to use in room with clients inside.

**Recommendation / Action Required**

Project Team should develop a consent form to be signed by all clients/customers whose data will be collected. This should be completed prior to InnoFest.

### 2.2 Has all collected information and data been classified with data classification requirements?

**Compliant**

**No**

**Observations / Comments**

No, data has not been classified as per data classification question above.

**Recommendation / Action Required**

Processes should be put in place to classify data at the point of entry for all new future data.

### 2.3 Is data anonymity used to protect the privacy of customers?

**Compliant**

**No**

**Observations / Comments**

No anonymity added to data, all data is stored in plain text.

**Recommendation / Action Required**

Investigate data anonymisers and look to implement across all stored and collected personal or sensitive data.

### 2.4 Is the cryptography policy being adhered to?

**Compliant**

**No**

**Observations / Comments**

No as no data is being encrypted, policy is not being adhered to.

**Recommendation / Action Required**

Project team should make themselves aware of the cryptography policy and implement data encryption techniques on all stored data where required.

### 2.5 Is data minimalization being put in place when collecting data?

**Compliant**

**No**

**Observations / Comments**

No all data is collected initially, however some minimalization occurs afterwards, this is more from a storage/simplicity perspective and less due to privacy or ethical considerations.

**Recommendation / Action Required**

Investigate and implement data minimalization techniques when collecting data. Ensure project team is aware of the importance of minimizing the collection of sensitive/personal data.

### 2.6 Looping back to the ISMS policies, are they being adhered to when required?

**Compliant**

**No**

**Observations / Comments**

As project team are unaware of ISMS policies, it has not been a consideration to understand or comply with them. Therefore none are being adhered to.

**Recommendation / Action Required**

Project team need to make themselves aware of the ISMS policies, identify where they are applicable to their project and implement requirements of each policy as required.

## Section 3 – Governance

### 3.1 Is the team adhering to the company’s governance framework?

**Compliant**

**No**

**Observations / Comments**

Project team unaware of any governance framework.

**Recommendation / Action Required**

Project team need to make themselves aware of the governance framework and adhere as required.

### 3.2 Are team roles and responsibilities clearly defined and documented?

**Compliant**

**Yes**

**Observations / Comments**

Team roles and responsibilities are clearly documented, therefore these could be adapted to fit the role and responsibility requirements of the governance framework and the ISMS policies.

**Recommendation / Action Required**

N/A

### 3.3 Is there a risk management plan in place?

**Compliant**

**No**

**Observations / Comments**

No risk management plan in place.

**Recommendation / Action Required**

Project / Cyber Security team needs to investigate and build a risk management framework and plan.

### 3.4 Is there an incident response plan in place?

**Compliant**

**No**

**Observations / Comments**

No incident response plan in place.

**Recommendation / Action Required**

Project / Cyber Security team needs to investigate and build a project specific incident response plan that can be followed specifically by each project.

### 3.4 Are incidents logged and reviewed for continuous improvement?

**Compliant**

**No**

**Observations / Comments**

No previous incidents logged and no incident response framework or processes to log incidents.

**Recommendation / Action Required**

Build incident response plan and implement incident logging procedures to ensure all future incidents are adequately logged and reviewed.

## Section 4 – Project Specific Audit

### 4.1 Are all end-user devices up to date with the latest security software?

**Compliant**

**Yes**

**Observations / Comments**

According to project lead, all end user devices are currently up to date. The only applicable device is the projects IP camera.

**Recommendation / Action Required**

N/A

### 4.2 Do you have a process for updating and patching these systems regularly?

**Compliant**

**No**

**Observations / Comments**

**No current patch management processes or procedures. Patching is done on an ad-hoc basis.**

**Recommendation / Action Required**

Build and maintain a patch management policy and procedures to ensure all devices are kept up to date in order to mitigate vulnerabilities.

### 4.3 Is the server-security policy being actively adhered to for all networks?

**Compliant**

**N/A**

**Observations / Comments**

**Not applicable, no network or servers in use.**

**Recommendation / Action Required**

N/A

### 4.4 Have Key assets and Data Categories been identified and organised correctly in relevance to the Monitoring & Log Analytics Policy

**Compliant**

**No**

**Observations / Comments**

**No key assets or data categories identified.**

**Recommendation / Action Required**

Project team to investigate monitoring and log analytics policy and build documentation identifying key assets and data categories.

### 4.5 What is your approach/policy with managing passwords required within your project team?

**Compliant**

**No**

**Observations / Comments**

Text passwords to team members. Team leaders know the password and can send to other team members.

**Recommendation / Action Required**

Implement proper password management solution, potentially systems such as a enterprise password manager. Additionally, ensure best practice is followed and passwords are changed and managed appropriately when team members leave the project in order to ensure proper access control to data and systems.

### 4.6 Do you use multi-factor authentication for any systems you use within your project?

**Compliant**

**No**

**Observations / Comments**

No MFA enabled, Single factor in use for all accounts

**Recommendation / Action Required**

Implement MFA for all systems where possible. If current systems do not have MFA capability then it is recommended to move away and utilise only MFA capable systems.

### 4.7 Do you train your project team members in cybersecurity and best practice?

**Compliant**

**No**

**Observations / Comments**

No training delivered around security.

**Recommendation / Action Required**

Investigate and deliver cyber security best practice training to all team members, this should include topics such as password management, multi-factor authentication, data storage best practice, data privacy and consent.

### 4.8 What steps would you take if a cyber related incident was discovered?

**Compliant**

**No**

**Observations / Comments**

In the example of a breached database shared account, the following response was given:

Lock the account, remove that user, notify the team and ask if they have given access or password.

**Recommendation / Action Required**

Investigate incident response plan to address issues here, key aspects where missed including notifying company leadership, building an incident response team and logging and reviewing incident post recovery.

### 4.9 Are previous incidents documented or noted anywhere?

**Compliant**

**No / N/A**

**Observations / Comments**

As the project lead is unaware of any past incidents, there is no documentation or logs.

**Recommendation / Action Required**

While there is no documented incidents, we can not rule out previous cyber incidents as the project is non-compliant with the incident response and logging procedures.

### 4.10 What is your process for backing up data and how frequent are these backups performed?

**Compliant**

**Yes**

**Observations / Comments**

Data is backed up on GitHub, once a week.

**Recommendation / Action Required**

While this does meet compliance requirements. There should be further processes around access to backed up data to ensure immutability, and backups of all systems and data stored should be investigated and implemented.

# Findings & Conclusion

Overall findings indicate that Project 4 – Player Tracking is non-compliant with the majority of audit points. Breakdown is as follows:

**4 Compliant Audit Points**

**23 Non-compliant Audit Points**

**3 Not applicable Audit points**

Therefore, it is my strong recommendation that the recommended actions listed for each audit point in this report be actioned as soon as possible.

Many of the non-compliant audit points are due to a lack of knowledge or awareness of the cyber security policies, procedures and frameworks built and implemented by the Redback Operations Team. I feel many of the shortcomings addressed in this report could be addressed by better education and awareness of these policies and frameworks within the projects and team outside of the direct cyber team.

A prospective idea that Vincent and I discussed was assigning a member of the cyber security team to each specific project for a trimester, this way that team member could work with the projects to build awareness and understanding of these policies, uplift their cyber security posture and deliver on many of the recommendations provided by the cyber audits the GRC team has completed this trimester.

Overall, the experience of completing this audit has been highly rewarding from both the perspective of the GRC/Cyber Security Team and the individual projects outside of this. I feel it has helped build awareness of the ever increasing risks of cyber security, and the strong emphasis that should be placed on ensuring compliance with the companies cyber security policies and frameworks, across all projects and teams within Redback Operations. I hope the results of these audits are built upon in future trimesters and can act as a gap analysis for future cyber security team members to uplift compliance within the projects.