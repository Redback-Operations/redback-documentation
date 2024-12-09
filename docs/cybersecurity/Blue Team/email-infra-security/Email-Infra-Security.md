---
sidebar_position: 1
---

# Implementation of a Secure Email Infrastructure for Redback Operations

:::info
**Document Creation:** 09 Dec, 2024. **Last Edited:** 09 Dec, 2024. **Authors:** Bikendra Gurung.
<br></br>**Effective Date:** 09 Dec 2024. **Expiry Date:** 09 Dec 2025.
:::

## Introduction
This document provides a brief overview of the objective, rationale, and methodology for developing a secure email infrastructure at Redback Operations. As Redback Operations has no existing domain and email infrastructure, this project focuses on implementing a robust, scalable, and secure email infrastructure to support the company’s operational and cybersecurity requirements. This project initiative aligns with Redback Operations’ mission of innovation, quality management, and security excellence.

---

## Project Background and Justification

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

---

## Project Scope

### Included in Scope:
1. Domain Registration  
2. Email Service Provider (ESP) Setup  
3. Email Account Creation  
4. DNS Configuration  
5. Email Security Implementation  
6. Documentation:
     - **As-Built Documentation**
     - **Handover Documentation**

### Excluded from Scope:
1. Integration with third-party tools or services (except for Valimail used for DMARC monitoring).

---

## Methodology

### Phase 1 – Domain Registration & Email Infrastructure Setup
#### 1. Domain Registration
1.1. Register a new domain (e.g., `redbackops.com`) with a secure and reputable registrar.  
1.2. Enable domain security features such as **Domain Privacy** and **Domain Lock**.

#### 2. Email Service Provider (ESP) Setup
2.1. Research and select an ESP.  
2.2. Set up email infrastructure by configuring the selected ESP with the registered domain.  
2.3. Create initial email accounts (e.g., `admin@redbackops.com`).

### Phase 2 – Initial Email Setup and DNS Configuration
#### 3. DNS Configuration & Validation
3.1. Configure DNS records:  
     - Add a TXT record to verify domain ownership.  
     - Add an MX record to route emails to the domain.  
     - Add a CNAME record to configure email settings for users automatically.  
     - Add a TXT record to configure SPF.  
     - Add CNAME records to configure DKIM.  
     - Add a TXT record to configure DMARC.

3.2. Validate DNS propagation:  
     - Use online tools such as **MXToolbox** and **Dmarcian**.  
     - Use command-line tools such as `nslookup`.

### Phase 3 – SPF, DKIM, and DMARC Implementation
#### 4. Security Controls Implementation & Validation
4.1. Implement fundamental email authentication protocols:  
     - Configure SPF  
     - Enable DKIM  
     - Implement DMARC:
          - Configure DMARC policy  
          - Configure DMARC monitoring and reporting using Valimail

4.2. Validate email authentication protocols:  
     - Use online tools such as **MXToolbox**, **Dmarcian**.  
     - Use command-line tools such as `nslookup`.

### Phase 4 – Additional security controls based on the CIS Foundations Benchmark guidelines
4.3. Implement additional security controls based on **CIS Foundations Benchmark** guidelines:  
     - Anti-phishing Policy  
     - Anti-spam Policy  
     - Anti-malware Policy  
     - Safe Attachments Policy  
     - Safe Links Policy  
     - Content Filtering Policy  
     - Common Attachment Types Filtering Policy  
     - Connection Filtering Policy  
     - Alert Policies  

4.4. Validate using the recommended audit guidelines per the **CIS Foundations Benchmark**.  

## Phase 5 – Additional Security Controls
4.5.  Implement the use of mail transport rules to maintain a list of IoC and blocked senders list and reject emails from those IoC and blocked sender sources.  
4.6.  Validate by adding a test sender address and IP address to the blocked senders list and confirming that the emails are blocked when sent from the listed sender address and IP address.  

4.7.  Enforce **Strict TLS encryption** instead of Opportunistic TLS for all email transmissions to ensure data confidentiality and integrity during transport.  
4.8.  Validate **Strict TLS encryption** by checking email headers and ensuring TLS is enforced.  

4.9.  Enforce **Multi-Factor Authentication (MFA)** for email accounts.  
4.10. Validate MFA is enabled by attempting to log in and verifying that the second authentication step is prompted.  

4.11. Implement geofencing for email access.  
4.12. Validate by attempting email access from an unauthorized location and ensuring access is blocked.  

4.13. Implement email activity logging and auditing.  
4.14. Validate by reviewing logs and ensuring that email activities are captured.  

4.15. Implement email retention and **DLP (Data Loss Protection)** policies.  
4.16. Validate by attempting to delete sensitive emails and confirming that the policies prevent unauthorized deletion or sharing.

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
