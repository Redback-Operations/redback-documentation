---
sidebar_position: 1
---

# Cybersecurity User Awareness Training

Redback Operations Cybersecurity User Awareness Training Content

:::info
**Document Creation:** 10 May 2024  
**Last Edited:** 10 May 2024  
**Authors:** Jamison Begley  
**Effective Date:** 10 May 2024  
**Expiry Date:** 10 May 2025
:::

## Purpose

This document defines the standards for training and upskilling employees at Redback Operations. It explains the importance of these standards and outlines the mandatory training required to ensure security compliance.

## Introduction

### What is user awareness training?

User awareness training is designed to educate employees about potential risks in their roles and the procedures for reducing these risks.  
While it often focuses on data protection, security, and compliance, it also promotes safe workplace behaviour.

### Purpose of user awareness training

User awareness training:

- Educates employees about risks linked to their job functions.  
- Provides strategies and procedures to mitigate or resolve risks.  
- Improves data security and company performance.  
- Helps prevent losses and fosters a positive, safe workplace.

---

## Job/Role-Specific Training

This training covers general safety practices and procedures.  
Job-specific training will be delivered separately but must be completed alongside this course.

---

## Understanding Routes for Help

At Redback Operations, our Cyber Team is divided into:

- **Purple Team** – Red + Blue collaboration  
- **Blue Team** – Secure coding  
- **Green Team** – Identity and access management  
- **Yellow Team** – Governance and policies  
- **Red Team** – Infrastructure/other

Know your team and your team leader. For gaps in knowledge:

1. Refer to documentation in **Docusaurus** or **GitHub**.  
2. Contact your team leader if you need more help.

---

## Understanding Major Areas

All employees must know Redback Operations’ major monitored areas:

1. **Cloud Infrastructure** – Monitor via 2FA.  
2. **Application Performance** – Use user feedback and reviews.  
3. **Resource & Usage Cost** – Use Datadog/Grafana; follow budgeting practices.  
4. **Security & Compliance** – Conduct regular compliance checks.  
5. **Network Performance** – Monitor latency and bandwidth in real-time.  
6. **Backup & Disaster Recovery** – Use automated backup systems.  
7. **User Activity & Usage** – Log authentication events.  
8. **System Updates & Patches** – Use patch management software.

See **"how can we monitor major areas.docx"** in the company repo for full details.

---

## Understanding Data Classification

As defined in the **Data Classification & DLP Policy**, data is classified into:

- **Public** – Intended for public disclosure.  
- **Internal Use Only** – Non-sensitive but internal.  
- **Confidential** – Sensitive; disclosure could harm the company.  
- **Restricted** – Highly sensitive; strict access controls required.

See the policy document for detailed handling instructions.

---

## Data Loss Prevention (DLP) Strategies

At Redback Operations, DLP strategies include:

1. Data classification.  
2. Access controls (least privilege principle).  
3. Watermarking confidential information.  
4. Encryption for sensitive data.  
5. Preventing unauthorised copies (e.g., screen-capture prevention).  
6. Content inspection.  
7. Policy enforcement checks.

---

## Encryption Standards

Encryption must align with the **Cryptography Policy**:

- **Symmetric encryption:** AES-256 for data at rest.  
- **Asymmetric encryption:** RSA (2048+) or ECC (256+).  
- **Hashing:** SHA-256 or higher.  
- **Data transfer:** Use TLS 1.2 or higher; avoid SSL2, SSL3, TLS 1.0/1.1.

---

## Playbook Awareness

Redback Operations maintains **Incident Response Playbooks** for:

### Attack Playbooks  
- Denial of Service (DoS)  
- Phishing  
- Ransomware  
- Malware  
- Data breach  
- ICS compromise

### Vector Playbooks  
- External/removable media  
- Attrition  
- Web/email vectors  
- Supply chain interdiction  
- Impersonation  
- Improper usage  
- Loss/theft of equipment

Each playbook covers:  
**Preparation → Identification → Notification → Containment → Eradication → Recovery → Post-incident review**

---

## Ethics

Ethics are the moral principles guiding our business.  
In cybersecurity, this means protecting sensitive data, ensuring transparency, and respecting privacy.

### Ethical Standards at Redback Operations

- **Transparency & Consent** – Explain data collection; get written consent.  
- **Confidentiality** – Apply access controls and encryption.  
- **Privacy** – Use data anonymity.  
- **Secure handling** – Collect, store, and transmit securely.  
- **Data minimisation** – Collect only what is needed.  
- **Compliance** – Follow all Redback Operations policies and procedures.

---

