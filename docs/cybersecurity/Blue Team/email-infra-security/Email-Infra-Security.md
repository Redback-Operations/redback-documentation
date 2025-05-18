---
sidebar_position: 1
---

**Last updated by:** bg-11, **Last updated on:** 16/05/2025


**Last updated by:** bg-11, **Last updated on:** 16/05/2025


**Last updated by:** bg-11, **Last updated on:** 16/05/2025


**Last updated by:** bg-11, **Last updated on:** 16/05/2025


# Implementation of a Secure Email Infrastructure for Redback Operations

:::info
**Document Creation:** 09 Dec, 2024. **Last Edited:** 09 Dec, 2024. **Authors:** Bikendra Gurung.
<br></br>**Effective Date:** 09 Dec 2024. **Expiry Date:** 09 Dec 2025.
:::

## Introduction
This document provides a brief overview of the objective, rationale, and methodology for developing a secure email infrastructure at Redback Operations. As Redback Operations has no existing domain and email infrastructure, this project focuses on implementing a robust, scalable, and secure email infrastructure to support the company’s operational and cybersecurity requirements. This project initiative aligns with Redback Operations’ mission of innovation, quality management, and security excellence.

---

## Project Background, Objectives and Justification

### Project Background
Redback Operations currently lacks an email infrastructure. As a result, it presents operational challenges which are outlined below:

1. **Communication Inefficiency**:  
     Challenges in establishing professional communication channels with stakeholders, clients, and team members.

2. **Susceptible to Security Threats**:  
     The absence of a domain-specific email infrastructure increases the exposure and attack surface to security threats such as phishing, spoofing, and BEC (Business Email Compromise).

3. **Lack of Scalability**:  
     The absence of a secure and centralized email infrastructure limits the company’s ability to:
     - Support future growth
     - Seamlessly integrate with the company’s systems, projects, and teams
     - Establish a centralized security administration for managing email identities and security policies.

---

## Project Objectives
The major objective of this project is to address the challenges listed above, and as a result, enable secure communication, improve operational efficiency, and safeguard the company against email-based threats. This is achieved through the following:

1. Establishment of a Secure Email Infrastructure  
2. Implementation of Email Security Protocols  
3. Implementation of Industry-Standard Security Controls (e.g., CIS Benchmarks)  
4. Enhancement of Scalability and Security  
5. Development of Comprehensive Documentation  

To support the achievement of the project objectives, **Microsoft 365 Exchange Online** was chosen as the preferred platform based on the following criteria:  
1.	Advanced security features, compliance, and governance capabilities.  
2.	Scalability features to support future growth and integration with the company’s other systems.  
3.	Support for advanced security capabilities and email authentication protocols such as SPF, DKIM, and DMARC.  
4.	High availability is supported by Microsoft’s global infrastructure.  

---

## Alternatives  
Before proceeding with this project initiative of implementing a secure infrastructure using Microsoft 365 and GoDaddy, alternative solutions were explored to address the communication and security needs of Redback Operations. The alternatives explored are outlined below:  
### 1.	Alternative 1: Use Free Email Services (e.g., Gmail, Hotmail, or Yahoo)  
**Description:** Utilize free email services such as Gmail, Hotmail or Yahoo to create email accounts for Redback Operations.  

**Advantages:**  
•	Zero initial setup cost.  
•	Easy to create and configure email accounts without requiring any specialized knowledge.  

**Disadvantages:**  
•	Lacks credibility and professionalism due to generic domains (eg: blueteam-redbackops@gmail.com).  
•	Limited options for advanced configuration, customization, and security features compared to enterprise-grade solutions.  
•	No provision for centralized administration of email identities and security policies.  

**Conclusion:** This alternative was not selected due to limitations in scalability, security, and brand alignment.  

### 2.	Alternative 2: Self-Hosted Email Server  
Description: Set up an on-premises email server within Redback Operations’ on-premises infrastructure.  

**Advantages:**  
•	Full control over email infrastructure and security configurations.  
•	No dependency on third-party providers.

**Disadvantages:**  
•	Requires an existing robust on-premises infrastructure, and likely incurs significant upfront implementation and ongoing maintenance efforts and costs.  
•	Requires dedicated resources – in terms of infrastructure and personnel.  
•	High risk of outages and downtime without proper redundancy mechanisms.  

**Conclusion:** This alternative was not selected due to the lack of an existing robust on-premises infrastructure at Redback Operations, as well as the significant cost and efforts required for implementation and maintenance.

---

## Project Scope

### Included in Scope
1. Domain Registration  
2. Email Service Provider (ESP) Setup  
3. Email Account Creation  
4. DNS Configuration  
5. Email Security Implementation  
6. Documentation:
     - **As-Built Documentation**
     - **Handover Documentation**

### Excluded from Scope
1. Integration with third-party tools or services (except for Valimail used for DMARC monitoring).

---

## Methodology

### Phase 1 – Domain Registration & Email Infrastructure Setup
#### 1. Domain Registration
1.1. Register a new domain (e.g., `redbackops.com`) with a secure and reputable registrar.  
1.2. Enable domain security features such as **Domain Privacy** and **Domain Lock**.

#### 2. Email Service Provider (ESP) Setup
2.1. Research and select an ESP.  
2.2. Set up email infrastructure by configuring the selected ESP.  
2.3. Create an initial email account (e.g., `adm-redbackops@redbackops.com).

### Phase 2 – Initial Email Setup and DNS Configuration  
#### 3. Email Infrastructure Setup  
3.1.	Set up email infrastructure by configuring the selected ESP with the registered domain.

#### 4. DNS Configuration & Validation
4.1. Configure DNS records:  
4.1.1. Add a TXT record to verify domain ownership.  
4.1.2. Add an MX record to route emails to the domain.  
4.1.3. Add a CNAME record to configure email settings for users automatically.  
4.1.4. Add a TXT record to configure SPF.  
4.1.5. Add CNAME records to configure DKIM.  
4.1.6. Add a TXT record to configure DMARC.  

#### 5. DNS Propagation Validation:  
5.1. Using online tools such as **MXToolbox** and **Dmarcian**.  
5.2. Using command-line tools such as `nslookup`.  

#### 6. New E-mail Identities/Users Creation  
6.1.	Create the initial batch of new e-mail identities/users for Redback Operations.  

### Phase 3 – SPF, DKIM, and DMARC Implementation
#### 7. Email Authentication Protocols Implementation (SPF, DKIM, DMARC)  
7.1. Configure SPF  
7.2. Enable DKIM  
7.3. Implement DMARC:  
7.3.1. Configure DMARC policy  
7.3.2. Configure DMARC monitoring and reporting using Valimail   

#### 8. Email Authentication Protocols Validation (SPF, DKIM, DMARC)  
8.1. Use online tools such as **MXToolbox**, **Dmarcian**.  
8.2. Use command-line tools such as `nslookup`.  

#### 9. Email Authentication Protocols Functional Test (SPF, DKIM, DMARC)  
9.1.	Send test e-mail using a redbackops.com email account (e.g., adm-redbackops@redbackops.com) through Outlook, and checking e-mail headers.  
9.2.	Send a test e-mail using a third-party email service provider (e.g.: MailChimp), sending a test e-mail, and checking e-mail headers.  
9.3.	Perform a spoofing test using online tools such as https://www.dmarctester.com/ .  

### Phase 4 – Additional security controls based on the CIS Foundations Benchmark guidelines  
#### 10. Implement additional security controls based on **CIS Foundations Benchmark** guidelines:  
10.1. Anti-phishing Policy  
10.2. Anti-spam Policy  
10.3. Anti-malware Policy  
10.4. Safe Attachments Policy  
10.5. Safe Links Policy   
10.6. Common Attachment Types Filtering Policy  
10.7. Connection Filtering Policy

#### 11. Validate using the recommended audit guidelines per the **CIS Foundations Benchmark**.  

### Phase 5 – Additional Security Controls
12. Implement the use of mail transport rules to maintain a list of IoC and blocked senders list and reject emails from those IoC and blocked sender sources.  
13. Validate by adding a test sender address and IP address to the blocked senders list and confirming that the emails are blocked when sent from the listed sender address and IP address.  

14. Enforce **Strict TLS encryption** instead of Opportunistic TLS for all email transmissions to ensure data confidentiality and integrity during transport.  
15. Validate **Strict TLS encryption** by checking email headers and ensuring TLS is enforced.  

16. Enforce **Multi-Factor Authentication (MFA)** for email accounts.  
17. Validate MFA is enabled by attempting to log in and verifying that the second authentication step is prompted.  

18. Implement geofencing for email access.  
19. Validate by attempting email access from an unauthorized location and ensuring access is blocked.  

20. Implement email activity logging and auditing.  
21. Validate by reviewing logs and ensuring that email activities are captured.  

22. Implement email retention and **DLP (Data Loss Protection)** policies.  
23. Validate by attempting to delete sensitive emails and confirming that the policies prevent unauthorized deletion or sharing.

---

## Acceptance (Key Success Factors)

The acceptance criteria for the project are outlined below:

1. **Domain Registration**:  
     Successful registration of a domain that aligns with the company’s branding.

2. **Email Infrastructure**:  
     Successful implementation of a functional email infrastructure.

3. **Email Authentication Protocols**:  
     Successful implementation and validation of email authentication security protocols (SPF, DKIM, DMARC).

4. **CIS Benchmark Controls**:  
     Successful implementation and validation of CIS Benchmark recommended controls.

5. **Advanced Security Controls**:  
     Successful implementation and validation of advanced security controls:
     - Mail transport rules to block IoCs and unauthorized senders.
     - Strict TLS encryption for email transmissions.
     - Multi-Factor Authentication (MFA) for email accounts.
     - Geofencing to restrict email access by location.
     - Email activity logging and auditing.
     - Email retention and Data Loss Protection (DLP) policies.

---

## Outcomes

1. **Operational Efficiency and Improved Credibility**:
     - Enables professional email communication channels.
     - Increases trust and credibility among stakeholders and clients.

2. **Enhanced Security**:
     - Reduces exposure to email-based threats such as phishing, spoofing, and BEC.

3. **Scalability**:
     - Supports future growth and seamless integration with company systems and projects.

4. **Centralized Administration**:
     - Provides centralized oversight over email identities and security policies.

5. **Increased Visibility**:
     - DMARC reporting allows monitoring of unauthorized email use and continuous improvement in email security.

---

## Conclusion
The establishment of a robust, scalable, and secure email infrastructure enables Redback Operations to enhance its operational capabilities and uplift its security posture. By addressing the existing challenges, this project ensures professional communication, safeguards against email-based threats, and supports the company's growth.

---

## Terminology

| Acronym/Abbreviation | Definition |
|-----------------------|------------|
| **BEC**              | Business Email Compromise: A type of email-based cybercrime where a scammer uses email to abuse trust in the business processes to scam someone into sending money, goods, or divulging confidential company information. |
| **CIS**              | Center for Internet Security: A non-profit organization that helps people, businesses, and governments protect themselves against cyber threats. |
| **CNAME**            | Canonical Name Record: A type of DNS record that points a domain name (an alias) to another domain. |
| **DKIM**             | DomainKeys Identified Mail: An email authentication protocol that adds a digital signature to emails, verifying the sender’s identity and preventing email tampering, ensuring integrity. |
| **DLP**              | Data Loss Prevention: A security measure to prevent inappropriate sharing, transfer, or use of sensitive data. |
| **DMARC**            | Domain-based Message Authentication, Reporting, and Conformance: An email authentication protocol that provides a policy framework for enforcing SPF and DKIM checks and domain alignment, and generating reports on email authentication results. |
| **DNS**              | Domain Name System: A name database that maps domain names to their corresponding Internet Protocol (IP) addresses. |
| **ESP**              | Email Service Provider: A company or a platform that provides email hosting and delivery services. |
| **MFA**              | Multi-Factor Authentication: A multi-step account access process that requires users to provide two or more forms of verification. |
| **MX**               | Mail Exchange: A type of DNS record that points to where emails for a domain should be routed. |
| **SPF**              | Sender Policy Framework: An email authentication protocol that verifies whether or not the sender is authorized to send emails on behalf of a domain. |
| **TLS**              | Transport Layer Security: An encryption protocol that enables parties to communicate securely over the internet. |
| **TXT**              | Text Record: A type of DNS record that allows the domain owner to store text values in the DNS, often used for verification and authentication purposes. |

---

## References
- [Site24x7: DNS Record Types](https://www.site24x7.com/learn/dns-record-types.html)  
- [PowerDMARC: SPF, DKIM, DMARC](https://powerdmarc.com/all-about-spf-dkim-dmarc/)  
- [Cyber.gov.au: TLS Implementation](https://www.cyber.gov.au/sites/default/files/2023-03/PROTECT%20-%20Implementing%20Certificates%2C%20TLS%2C%20HTTPS%20and%20Opportunistic%20TLS%20%28October%202021%29.pdf)  
- [Microsoft: Data Loss Prevention (DLP)](https://www.microsoft.com/en-au/security/business/security-101/what-is-data-loss-prevention-dlp)

---
