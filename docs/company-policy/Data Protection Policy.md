**Data Protection Policy**

**Redback Operations**

**1\. Introduction**

Redback Operations is a student-led team that develops innovative projects integrating IoT sensors, web and mobile applications, data analytics pipelines, and Unity VR environments. In the course of these projects, the team handles various forms of data from personal user information and sensor readings to internal documentation and code. This **Data Protection Policy** outlines how Redback Operations protects all such data, ensuring its confidentiality, integrity, and availability. By adhering to this policy, the team builds trust with users and stakeholders and aligns with Australian privacy laws and best practices in information security.

This policy establishes a formal framework for responsible data handling within Redback. It defines how data is classified, who can access it, how it must be secured, and the procedures for data retention and breach response. The tone and expectations are set at a level appropriate for a student team environment while remaining professionally acceptable to academic supervisors and industry evaluators. All Redback team members are expected to be familiar with and follow this policy to maintain high standards of data protection throughout our project lifecycle.

**2\. Purpose & Scope**

**Purpose**  
The purpose of the Data Protection Policy is to ensure that Redback Operations manages data in compliance with relevant laws and ethical standards, and that all data collected, generated, or used by the team is protected against unauthorized access or misuse. This policy aims to safeguard personal information, project data, and intellectual property by providing clear guidelines on handling, storing, and sharing data. It also seeks to instill good data management habits in team members, reflecting both professional IT security practices and the requirements of Australian privacy regulations.

**Scope**  
This policy applies to **all data assets and systems** used in Redback Operations. It covers every project and sub-team under Redback, including:

- IoT devices and sensors
- Backend servers, APIs, and data pipelines (e.g. MQTT, Kafka, FastAPI)
- Web and mobile applications
- Databases and data lakes (PostgreSQL, MongoDB, MinIO, Dremio, etc.)
- Unity VR environments and associated services
- Internal documentation, reports, and communication channels

All team members (students, faculty advisors, and collaborators) must comply with these guidelines when handling data. The scope extends to all forms of data – digital or physical, structured (like databases) or unstructured (like documents or media files). It also includes any personal information about individuals (such as team members or pilot users) and any sensitive project information. Whether data is stored on on-prem servers, cloud services, team laptops, or transferred through networks, it falls under this policy. External parties who are given access to Redback data are expected to uphold equivalent data protection standards.

**3\. Data Categories & Systems**

Redback Operations handles multiple categories of data across a range of systems. Identifying these data types and systems is crucial to applying appropriate protection measures.

**3.1 Systems and Platforms**

- **IoT Devices and Sensors**  
    Smartbike sensors and other wearables stream telemetry data (e.g. speed, cadence, heart rate, IMU readings) via MQTT/Kafka into backend services.
- **Web and Mobile Applications**  
    The Redback dashboard and mobile app handle user registrations, authentication, profiles, and personalised performance analytics.
- **Data Processing Pipelines and Services**  
    Backend services (FastAPI, MQTT/Kafka brokers, Airflow jobs) ingest, transform, and route data between components and into storage or analytics tools.
- **Databases and Storage**
    - Relational and document databases (e.g. PostgreSQL, MongoDB)
    - Object storage (e.g. MinIO) for files, exports, model artefacts
    - Code repositories (e.g. GitHub) for source code and configuration
- **Unity VR Environment**  
    The Unity VR application consumes live or near-real-time data (via APIs/WebSockets/MQTT) to drive gameplay, visualisations, and feedback.

**3.2 Data Categories**

- **Personal Data**  
    Information relating to an identified or identifiable person, such as:
    - Names, email addresses, usernames, student IDs
    - Contact details, profile info, preferences
    - Credentials (usernames, salted/hashed passwords, auth tokens)
- **Telemetry and Sensor Data**  
    Data from IoT devices and wearables, including:
    - Heart rate, power, cadence, speed, IMU readings
    - Device IDs, timestamps, location (if used)

When linked to a person or containing health-related metrics, this is treated as sensitive personal data.

- **Project Operational Data**  
    Internal data used to operate and monitor systems:
    - Application and infrastructure logs
    - Configuration files and environment settings
    - Performance metrics, error reports, traces
- **Intellectual Property & Research Data**
    - Source code, algorithms, Unity scenes and assets
    - Designs, architecture diagrams, documentation
    - Research datasets (e.g. curated wearables data, annotation sets)
    - Partner-provided data (e.g. under NDA or specific licence terms)
- **Aggregated and Derived Data**
    - Analytics outputs, dashboards, summary statistics
    - ML model outputs, derived features, trained model parameters
    - Visualisations and reports built from underlying data

Each category is subject to classification and protection measures described in the next section.

**4\. Classification Framework**

All data handled by Redback is classified into one of four sensitivity levels. Classification determines how data must be stored, accessed, and shared.

**4.1 Classification Levels**

**Public** (Low Sensitivity)  
Information intended for open sharing that poses minimal risk if disclosed.  
Examples:

- Public documentation and marketing content
- Open-source code repositories intentionally published
- Approved public presentations and demo screenshots

**Internal** (Team-Only)  
Information for internal consumption within Redback only.  
Examples:

- Internal design docs, sprint notes, retrospective notes
- Non-sensitive emails or chat messages about project work
- Non-public architecture diagrams and planning documents

**Confidential** (Sensitive)  
Information that could cause harm if disclosed or tampered with.  
Examples:

- Personal data of team members or test users
- Health and performance metrics linked to individuals
- Detailed system configurations, internal API docs
- Partner-provided datasets or documents under NDA

**Highly Confidential** (Restricted)  
Information that is critical to system security or highly sensitive.  
Examples:

- Root passwords, private keys, API secrets, tokens
- Unanonymised research data involving human subjects
- Detailed security audit reports and threat models

**4.2 Classification Principles**

- When in doubt, treat data as **Confidential** or **Highly Confidential**.
- Personal data is **at least Confidential**; authentication secrets are **Highly Confidential**.
- Files, screenshots and exports inherit the highest classification of any data they contain.
- Classification should be applied at creation and reviewed if data usage changes.

**5\. Access, Use & Disclosure**

Redback applies **least privilege** and **need-to-know** principles to all data access.

**5.1 Access Control**

- Access to Internal, Confidential and Highly Confidential data is restricted to those who need it for their role.
- Role-based access control (RBAC) is implemented for:
    - Databases and data warehouses
    - Storage buckets (e.g. MinIO)
    - Analytics tools and dashboards
    - CI/CD and infrastructure management tools
- Administrative and root-level access is limited to designated leads (e.g. DevOps/Security leads).
- Shared credentials are avoided; each person uses their own account wherever possible.

**5.2 Authentication & Sessions**

- Strong passwords or passphrases are required; password reuse is discouraged.
- Multi-factor authentication (MFA) is enabled for critical systems where available (e.g. cloud consoles, GitHub orgs).
- Sessions for web/mobile/VR applications are time-limited and securely managed.
- Devices used for Redback work must have screen locks and up-to-date security patches.

**5.3 Use of Data**

- Data is used only for **clearly defined project purposes**, such as:
    - Delivering app functionality
    - Improving performance and user experience
    - Conducting agreed research and evaluation
- Data minimisation is applied:
    - Only collect what is necessary
    - Only query the subset needed for a specific task
    - Prefer aggregated/anonymised data when identity is not required
- Any new or secondary use of data (beyond original purpose) must be reviewed and, if personal data is involved, justified and documented.

**5.4 Consent and Participant Rights**

Where real individuals’ data is collected (e.g. test users, volunteers):

- They are informed about:
    - What data is collected
    - For what purpose
    - How long it will be kept
    - How it will be protected
- Consent is recorded (e.g. via a short form or online acknowledgment).
- On reasonable request, participants can:
    - Ask what data is held about them
    - Request corrections if information is inaccurate
    - Request deletion or anonymisation where feasible and consistent with project requirements

**5.5 Internal & External Disclosure**

- Internal disclosure is limited to team members who need the data for project tasks.
- External disclosure of Confidential or Highly Confidential data:
    - Requires explicit approval from project leads
    - Should use anonymisation/aggregation wherever possible
    - Must be communicated over secure channels
- Personal information is not shared with third parties unless:
    - It is required by law or university policies, or
    - Explicit consent has been obtained from the individual
- Sensitive data must **never** be posted in:
    - Public GitHub repos
    - Public chat channels or forums
    - Slides, screenshots or demos destined for external audiences, unless sanitised

**6\. Security Expectations**

Security is everyone’s responsibility. The following controls apply across Redback systems.

**6.1 Device, Infrastructure & Network Security**

- Keep all servers, containers, and devices patched and updated.
- Disable unused ports and services; enforce firewall rules.
- Use secure network paths (VPNs or restricted subnets) for administration access.
- Harden IoT devices:
    - Change default credentials
    - Remove unnecessary software and services
    - Apply firmware updates promptly

**6.2 Application & API Security**

- Apply secure coding practices and review code for common vulnerabilities (e.g. OWASP Top 10).
- Validate all inputs; avoid directly trusting client-side data.
- Do not hard-code secrets in source code; use environment variables or secret managers.
- Protect REST and WebSocket APIs with appropriate authentication and authorisation.

**6.3 Identity & Access Management**

- Use RBAC in databases, dashboards, and admin tools.
- Limit high-privilege accounts and protect them with MFA.
- Immediately disable accounts for team members who leave the project.
- Keep an auditable record of role assignments and access changes.

**6.4 Data Protection Controls**

- Encrypt Confidential and Highly Confidential data at rest where feasible.
- Enforce TLS for:
    - Web and API endpoints
    - MQTT/Kafka links carrying sensitive payloads
    - Database connections from remote clients
- Restrict who can export data and where exports may be stored.
- Sanitize or anonymise data before using it in presentations, documentation, or demos.

**6.5 Monitoring, Logging & Testing**

- Enable logging on critical systems (auth events, configuration changes, error conditions).
- Use monitoring tools (e.g. Wazuh, metrics dashboards) to detect anomalies.
- Conduct:
    - Regular vulnerability scans
    - Periodic manual security reviews
    - Targeted penetration tests within agreed scope
- Address identified vulnerabilities in a timely and documented way.

**6.6 Backups & Recovery**

- Regularly back up critical data (databases, configs, key artefacts).
- Store backups securely and, where possible, encrypted.
- Test recovery procedures so that data and services can be restored after failure or incident.

**7\. Retention & Disposal**

Redback keeps data only as long as necessary and disposes of it securely when no longer required.

**7.1 Retention**

- **Project data & records**
    - Retained for the duration of the project and a reasonable period afterward for continuity and assessment.
- **Personal information**
    - Retained only as long as needed to achieve the purpose it was collected for.
    - Removed or anonymised when:
        - The project is completed and the data is no longer needed
        - The participant withdraws consent (where feasible)
- **Logs & monitoring data**
    - Kept for limited periods (e.g. 3–6 months) for troubleshooting and security monitoring, then rotated or deleted.
- **Backups**
    - Retained in line with backup schedules and removed when obsolete.

**7.2 Archiving & Anonymisation**

- Where long-term insights are useful, data should be **anonymised** or **aggregated** before archival.
- Direct identifiers (names, emails, IDs) are removed or irreversibly transformed.
- Anonymised datasets can often be retained as Internal rather than Confidential.

**7.3 Secure Disposal**

- **Digital data**
    - Delete records from databases and storage systems.
    - For sensitive data, use secure deletion or destroy encryption keys where applicable.
- **Physical media**
    - Shred printed documents containing Confidential or Highly Confidential information.
    - Wipe or physically destroy drives and removable media before disposal or reuse.
- **Cloud and third-party services**
    - Explicitly delete project data and instances when no longer required, not just “abandon” them.

Basic records of major deletions/archivals should be kept for accountability (e.g. “Participant test dataset deleted on &lt;date&gt;”).

**8\. Breach Management**

A **data breach** occurs when data is lost, accessed, or disclosed without authorisation, or is altered/destroyed in an unauthorised way.

**8.1 Reporting**

All team members must **immediately report** suspected or confirmed data breaches to the project lead and the designated security/contact person. Examples:

- Unexpected data exposure in a public repo
- Loss/theft of a laptop containing project data
- Logs or dashboards showing access from unknown users or locations

**8.2 Containment**

Initial response focuses on stopping further damage:

- Revoke or rotate compromised credentials (passwords, API keys, tokens).
- Disable affected services or interfaces temporarily if needed.
- Isolate compromised systems from the network.

**8.3 Assessment**

After containment, the team:

- Identifies:
    - What happened and how
    - Which systems and datasets are affected
    - Whether personal or Highly Confidential data is involved
- Evaluates the **risk of harm** to individuals and to Redback/Deakin (e.g. identity misuse, reputational harm, security threats).

**8.4 Notification**

If personal information is involved and serious harm is likely:

- Notify affected individuals promptly with:
    - What occurred
    - What data was involved
    - What steps they should take (e.g. change passwords)
- Follow the principles of the **Notifiable Data Breaches (NDB) scheme**, including notifying the OAIC if the project falls under those obligations.
- Inform faculty supervisors or relevant university contacts in line with Deakin policies.

Even if not strictly required, Redback favours transparency with supervisors and stakeholders.

**8.5 Remediation & Recovery**

- Fix root causes (patch vulnerabilities, correct misconfigurations, improve access controls).
- Restore systems and data from clean backups where necessary.
- Increase logging or monitoring temporarily to detect any follow-up activity.

**8.6 Post-Incident Review**

- Document the incident, response steps, and outcomes.
- Conduct a short review with the team:
    - What went wrong?
    - What worked well?
    - What needs to change?
- Update this policy, procedures, or training if gaps are identified.

**9\. Ethical & Compliance Alignment**

Redback’s data protection practices are grounded in both **legal** and **ethical** expectations.

**9.1 Legal Alignment (High-Level)**

This policy is designed to align with:

- **Privacy Act 1988 (Cth)** – primary Australian privacy legislation[OAIC+1](https://www.oaic.gov.au/privacy/privacy-legislation/the-privacy-act?utm_source=chatgpt.com)
- **Australian Privacy Principles (APPs)** – especially: APP 1 (transparency), APP 3 (collection), APP 6 (use & disclosure), APP 11 (security), APP 12–13 (access & correction)[OAIC+1](https://www.oaic.gov.au/privacy/australian-privacy-principles?utm_source=chatgpt.com)
- **Notifiable Data Breaches (NDB) scheme** – guidance on identifying and responding to eligible data breaches (likely to cause serious harm)[OAIC+2OAIC+2](https://www.oaic.gov.au/privacy/notifiable-data-breaches/about-the-notifiable-data-breaches-scheme?utm_source=chatgpt.com)

While Redback operates as a student capstone project and may not be a formal APP entity, we treat these as best-practice benchmarks.

**9.2 Ethical Alignment**

Redback aligns with the **Australian Computer Society (ACS) Code of Professional Ethics**, including values of honesty, trustworthiness, and respect for privacy.[ACS+2Zaco+2](https://www.acs.org.au/memberships/professional-ethics-conduct-and-complaints.html?utm_source=chatgpt.com)

Practically, this means:

- Avoiding unnecessary collection or retention of personal data
- Treating any human-related data (especially health metrics) with care and respect
- Being honest and transparent about how data is used
- Speaking up if something feels ethically wrong in how data is handled

**9.3 Standards & Good Practice**

Where practical, this policy draws on:

- **ASD Essential Eight** mitigation strategies for securing systems[Cyber.gov.au+2Cyber.gov.au+2](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight?utm_source=chatgpt.com)
- Broader security frameworks such as ISO/IEC 27001 (information security management)
- University information security and research ethics guidelines

These are used as guidance, not strict certifications, to ensure Redback is aligned with contemporary cybersecurity and privacy expectations.

**10\. Governance & Review**

**10.1 Roles & Responsibilities**

**Project Leadership (e.g. Project Manager / Technical Lead)**

- Owns this policy and ensures it is applied.
- Makes decisions on edge cases (e.g. new datasets, new third-party tools).
- Ensures necessary tools and time for security tasks (e.g. code reviews, patches).

**Data Steward (can be one of the leads)**

- Oversees data classification and retention decisions.
- Maintains awareness of what data exists where.
- Coordinates responses to access/correction/deletion requests.

**Security / DevOps Lead**

- Manages infrastructure security, access controls, backups, and monitoring.
- Coordinates technical breach response.
- Ensures secrets management and secure configurations are in place.

**Documentation / Compliance Lead**

- Keeps policies, procedures, and diagrams up-to-date.
- Ensures new members are onboarded with this policy.
- Coordinates periodic reviews and updates.

**All Team Members**

- Read and follow this policy.
- Protect credentials and devices used for project work.
- Raise potential issues, incidents, or uncertainties early.

**10.2 Training & Onboarding**

- New members receive an introduction to this policy and key expectations.
- Short refreshers are provided when:
    - Policies are updated
    - New systems are introduced
    - Lessons are learned from incidents or near misses

**10.3 Review Cycle**

- This policy is reviewed **at least annually** and at the start of major new project phases.
- Reviews consider:
    - Changes in laws or university policies
    - New tools, infrastructure, or data flows
    - Feedback from team members and evaluators
    - Lessons learned from any incidents
- Changes are versioned, documented, and communicated to the team.

**10.4 Enforcement**

- Adherence to this policy is mandatory for all Redback members.
- Accidental breaches are treated as learning opportunities, but must be reported and rectified.
- Repeated or serious non-compliance may lead to:
    - Restricted access to systems or data
    - Escalation to academic supervisors

The focus is on improvement, accountability, and professionalism, not punishment.

**References & Further Reading**

- Privacy Act 1988 – Australian Government (Attorney-General’s Department)[OAIC+1](https://www.oaic.gov.au/privacy/privacy-legislation/the-privacy-act?utm_source=chatgpt.com)
- Australian Privacy Principles (APPs) – OAIC overview and quick reference[OAIC+1](https://www.oaic.gov.au/privacy/australian-privacy-principles?utm_source=chatgpt.com)
- APP Guidelines – OAIC detailed PDF guidance[OAIC+1](https://www.oaic.gov.au/__data/assets/pdf_file/0009/1125/app-guidelines-july-2019.pdf?utm_source=chatgpt.com)
- Notifiable Data Breaches (NDB) Scheme – OAIC overview and guidance[OAIC+2OAIC+2](https://www.oaic.gov.au/privacy/notifiable-data-breaches/about-the-notifiable-data-breaches-scheme?utm_source=chatgpt.com)
- ACS Code of Professional Ethics – Australian Computer Society[ACS+2Zaco+2](https://www.acs.org.au/memberships/professional-ethics-conduct-and-complaints.html?utm_source=chatgpt.com)
- Essential Eight – Australian Signals Directorate / ACSC guidance[Cyber.gov.au+2Cyber.gov.au+2](https://www.cyber.gov.au/business-government/asds-cyber-security-frameworks/essential-eight?utm_source=chatgpt.com)