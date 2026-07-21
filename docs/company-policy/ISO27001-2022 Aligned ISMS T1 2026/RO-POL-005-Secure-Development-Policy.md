# Secure Development Policy

## Redback Operations – ISO27001:2022 ISMS

| **Document Version** | 1.0 |
| --- | --- |
| **Document Code** | RO – POL – 005 |
| **Document Owner** | Ethics / GRC Team |
| **Review Interval** | Start of Each Trimester |
| **ISO27001 Reference** | ISO27001:2022 – Annex A Controls 8.4, 8.8, 8.9, 8.19, 8.25, 8.26, 8.27, 8.28, 8.29, 8.32 |

---

## Purpose

The purpose of this policy is to ensure that Redback Operations' source code and its development is held to this policy's standard, adhering to ISO27001:2022 standards. This policy will outline practices that need to be implemented within the project's development lifecycle.

## Scope

This policy is applicable to all applications and development concerning Redback Operations' development lifecycle in its projects:

- Source code contained within GitHub repositories and their respective projects
- All active members within Redback Operations developing code
- Development in IDEs and other code editor programs.
- React Native (Expo framework)
- Unity Simulation
- Garmin SDK
- Applications that are relevant to software development and its lifecycle are not listed.

## Principles

All development within Redback Operations must follow these secure development principles:

- **Security By Design:** This principle outlines the necessity for secure programming practices, threat modelling and mitigation of security risks is performed throughout development, not just at the end of its implementation.
- **Secure By Default:** Default configurations of the applications are to be the most secure settings. Settings are to be varied per development.
- **Defense in Depth:** Defense against attacks is supported by multiple security protocols. Risks and vulnerabilities are mitigated through the implementation of layering defense controls.
- **Least Privilege:** A person or process is to be granted the minimal number of permissions / settings that are only needed for their role and its responsibilities. Only to be given those permissions within the minimal timeframe.

## Code Review Requirements

### Review performed prior merging

All code committed to the GitHub repositories are to be reviewed by the SecDevOps team before being merged into the main branch in its respective repositories. No developer can review their own pull request and approve it. Applicable to all active repositories.

### Reviewers must check

SecDevOps and other code reviewers are responsible for ensuring that the following vulnerabilities and practices are flagged and fixed accordingly:

- **Hardcoded Personally Identifiable Information (PII):** Information that can identify a specific person or asset and is present in source code. This can look like sensitive information that has phone number, address, license numbers and information.
- **Error Handling:** Code handles errors in a way that does not output information relating to its system and sensitive information.
- **Input validation:** Utilized for consumer-facing products and their inputs are sanitized.
- **OWASP10 Vulnerabilities:** Separate review must be performed aside from the automated scanning that is present in the current repositories.

### Branch Protection Requirement

The Branch Protection feature must be present in all active repositories across Redback Operations.

## Secrets and Credentials Security

### Hardcoded secrets in code

If the following data is present within the GitHub repositories, then it is to be treated as a Critical severity level incident. The proper procedure is to be followed as per the Incident Response Policy (RO – POL – 004) if any of the information is present:

- Passwords
- Login Credentials
- API Keys and Tokens
- Personally Identifiable Information (PII)
- JSON Web Tokens
- OAuth tokens

### Response following Secret exposure

If any of the secrets are exposed in publicly facing platforms, the following procedure is to be enacted:

- Immediate action: rotate the exposed credential, do not delete the commit.
- Enable push protection on the repository that the exposure is on.
- Investigate commit history to check how long the exposure had existed.
- Notify SecDevOps immediately.

## Managing Dependencies in Secure Development

### Sources

All dependencies and libraries are to be downloaded from official and authorised repositories. Typosquatting is a common attack where packages with a similar name to an official package is malware.

### Pinning Dependencies

Dependencies and their versions must be listed in an application's requirement file. Floating versions are discouraged as they automatically utilise a version. This can look like:

Requirements.txt == mongodb == 10.0.1

### Dependabot

It is a requirement that Dependabot is active in all GitHub repositories. Dependabot alerts are to be reviewed and enacted upon by the SecDevOps team.

## OWASP Top 10

Redback Operations' active development teams are to be aware of the OWASP Top 10 vulnerabilities. These vulnerabilities should be considered by the developers during the projects' software development lifecycle.

| **AO1:2025** | Broken Access Control |
| --- | --- |
| **AO2:2025** | Security Misconfiguration |
| **AO3:2025** | Software Supply Chain Failures |
| **AO4:2025** | Cryptographic Failures |
| **AO5:2025** | Injection |
| **AO6:2025** | Insecure Design |
| **AO7:2025** | Authentication Failures |
| **AO8:2025** | Software or Data Integrity Failures |
| **AO9:2025** | Security Logging and Alerting Failures |
| **AO10:2025** | Mishandling of Exceptional Conditions |

## CI/CD Pipeline Security

GitHub Actions Workflows are to be secured accordingly:

- Workflow permissions are to be set to be read-only.
- If secrets are present within workflows, use GitHub Action Secrets to store those secrets, do not hardcode.
- Creation or alteration of workflow files must be reviewed by SecDevOps via pull request review.

## Secure Coding Standards in Coding Languages

### Python

- Utilise virtual environments, do not install packages that are on shared systems.
- Validate all inputs if developing consumer-facing products, use libraries wherever applicable.
- Store sensitive information in environment variables or locally, do not hardcode into files.
- Utilise prepared statements for input derived from users.

### Monkey C

- Practice strict type checking through utilizing the strict compiler setting to mitigate runtime errors.
- Avoid deep function call stacks and recursive calls as there is limited stack space.
- Do not create unnecessary objects as Monkey C uses reference counting. This is to prevent memory errors.
- Validate data received from external sources.

### C#

- Avoid storing credentials or API credentials in Unity applications.
- Disable debug logging in production builds.
- Do not use Resources.Load for assets that end users should not access.

## Pull Request Checklist

The SecDevOps and other code reviewers must perform a review utilizing this checklist on pull requests to ensure that the code is up to standard before approving the merge.

| **Security Feature** | **Approved** |
| --- | --- |
| No hardcoded credentials are present in the code. |  |
| No hardcoded PII are present in the code. |  |
| All dependencies are from verified sources and version is pinned in files. |  |
| Error messages does not display information that outputs data relating to paths or systems. |  |
| No commented code that presents sensitive information. |  |
| Trivy scanner and Dependabot alerts are cleared before approving pull request. |  |
| CI/CD pipeline passes automated scan. |  |
| OWASP10 Vulnerabilities is not present in the code. |  |
| Input validation is implemented in code relating to programs that are publicly-facing. |  |

## Non-Compliance Consequences

If this policy is breached, there are multiple penalties that are to be imposed, this includes:

- Rejection of Pull Request.
- If incidents containing sensitive information and PII is active, escalate to corresponding severity level and inform Ethics / GRC team.
- Escalate to tutor / unit chair if breaches are deliberate.

## Policy Review

The Secure Development Policy needs to be reviewed at the start of each trimester to reflect the current state of Redback Operations. Collaboration between SecDevOps and the Ethics/GRC team is to be enacted when reviewing this policy. Any changes should be dated and version-controlled.
