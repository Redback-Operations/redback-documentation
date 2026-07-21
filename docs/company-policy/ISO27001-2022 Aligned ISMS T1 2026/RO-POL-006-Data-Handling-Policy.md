# Data Handling Policy

## Redback Operations – ISO27001:2022 ISMS

| **Document Code** | RO – POL - 006 |
| --- | --- |
| **Version** | 1.0 |
| **Document Owner** | Ethics / GRC Team |
| **ISO27001 Reference** | Annex A Controls 5.12, 5.13, 5.14, 5.33, 5.34, 7.10, 8.10, 8.13 |
| **Review Interval** | Start of each trimester |

---

## Purpose

This policy establishes the mandates for data handling within Redback Operations. The policy entails are assets are stored, transmitted, secured and disposed. Data is to be handled consistently based on its sensitivity. This policy is established due to the procedures of Redback Operations with a dedicated Data Warehouse team, Private AI platform and software development.

## Scope

This policy is applicable to the following stakeholders:

- Active Redback Operations members
- All data that is collected and utilised by Redback Operations
- Systems that are in place that specifically handles information and data, such as the Data Warehouse's architecture.

## Data Classification

Data assets within Redback Operations are assigned a classification level. This determines what controls are applied to the data and how it must be handled if there is an incident.

| **Classification** | **Definition** | **Examples** | **Controls Required** |
| --- | --- | --- | --- |
| **Confidential** | **Data that would cause harm to Redback Operations if leaked or exposed.** | **Credentials, API Keys or Tokens, Personally Identifiable Information, Database information,** | **Encryption at rest, Offboarding access to information, Access Control** |
| **Internal** | **Data that is only utilised within Redback Operations only. Not to be shared with public.** | **Documentation including policies, procedures or onboarding files. Communication between members** | **Access is available to only Redback Operations members. Secured within non-public facing systems** |
| **Public** | **Data available to the public** | **Source code. GitHub repositories. Company description and information.** | **Information must be reviewed before being made public.** |

## Data Storage

Data must be stored in systems relevant to their classification level. Different levels equate to different mandates on the security of storage.

| **Classification** | **Storage method** | **Restricted storage** | **Encryption method** |
| --- | --- | --- | --- |
| **Confidential** | Virtual Machines supervised by Deakin IT. Security managed platforms. | Personal cloud storage. Public repositories. Present in communication channels. | Yes, at rest and in transit, |
| **Internal** | Virtual Machines supervised by Deakin IT. Security managed platforms. University managed programs. | Personal cloud storage. Public facing platforms such as GitHub or Docusaurus. | In transit. |
| **Public** | Appropriate GitHub repositories. Any public platform. | No Restrictions | Not Needed |

### Personal Devices

Confidential data is restricted on personal devices. Internal data can only be stored on personal devices if there are no other platforms to store information on. If a student has personal information relating to Redback Operations, offboarding must dictate that they will need to delete the information when concluding.

### GitHub Repository Storage

GitHub repositories are only storage for source code and approved documentation. The following information should not be stored in the company's repositories:

- Credentials, including username and passwords.
- API Keys or tokens.
- Personally Identifiable Information
- Private keys or certificates.

## Data Transmission

### Encryption in Transit

All data classified under Confidential must be encrypted in transit. For example, communications must be undertaken utilising encrypted channels or methods. MQTT broker connections via HiveMQ must utilise TLS. API communications should only use HTTPS.

### Email and Communication Restrictions

Confidential information and data should not be carried over messaging platforms. Redback Operations primarily utilises emails and Microsoft Teams as its communication platforms. Internal data can be transmitted over Teams but not be shown to the public.

### External Sharing

Confidential or Internal Redback Operations data cannot be shared with external or public parties without approval from the respective team tutor. External is defined as those not employed within Redback Operations.

## Data Retention

### Retention length

Data should only be retained or kept for its intended purpose.

- Active project data: retained for the duration of the project.
- Security audit findings and incidents: retained for at least two trimesters to support strengthening and continuity.
- Policy Documents and ISMS components: remains indefinitely and must be version-controlled to ensure governance.
- Onboarding and access records: retained for the trimester and one trimester after offboarding.
- Backup Data: retained according to Data Warehouse's backup schedule.

### Trimester Rotation Consideration

Redback Operations operates on a trimester rotation. All active project data has to be reviewed at the end of each trimester. Data that is not required should be disposed in accordance with Section 7.

## Data Disposal

### Secure Disposal Requirements

When data is no longer required, it must be disposed of securely.

- Digital data must be permanently deleted from all storage locations, which includes repositories or information in Data Warehouse's lakehouse architecture.
- Data deleted from a repository does not result in secure disposal as the information will still be present in commit histories. Ensure that the repository history is reviewed.
- Personal devices utilised in Redback Operations' procedures should have their project data removed upon offboarding.

### Offboarding Data Removal

As a requirement of the offboarding process, offboarding students should confirm that they have deleted all Confidential data related to Redback Operations from their personal devices. The Ethics / GRC team have the responsibilities of confirming this in the offboarding register.

## Special Data

### Private AI Platform Data

The Data Warehouse's Private AI model collects and processes data from Redback Data, for the purposes of querying and automation. The AI processes information sensitive to Redback Operations and therefore these requirements are set out:

- The data sources that the AI platform derives its from must be verified and approved by the Ethics / GRC team.
- Data sources containing PII must be approved and have the relevant controls.
- Outputs generated by this A.I must not be treated as authoritative without verifying the information.
- Access to the AI platform is only permitted to the Data Warehouse team.

### Personally identifiable Information (PII)

PII is defined as data that can identify someone. Redback Operations does not specifically collect PII but can be present in sensor data, onboarding records or development tools. PII is to be classified under Confidential level and handled in accordance to the Australian Privacy Act 1988. PII must never be hardcode or committed in any repositories. PII that is utilised in testing should be anonymous. Any breaches of PII should be reported to the Ethics / GRC Team as a Critical Incident, reporting to those relevant.

## Access Controls for Data

Access to data must be governed by the Access Control Policy (RO-POL-002). It must be governed by the principles of least privilege and need-to-know.

## Data Breach Incident Response

Any suspected or confirmed incidents relating to loss or corruption of Redback Operations' data must be reported to the Ethics / GRC Team. The Incident Response Policy (RO-POL-004) lays out the steps for incident response of the data.

## Policy Review

This policy must be reviewed at the start of each trimester by the Ethics / GRC Team. The review must assess any new data classification or types, systems or tools introduced in that trimester. Any changes must be version-controlled, dated and approved before taking effect.
