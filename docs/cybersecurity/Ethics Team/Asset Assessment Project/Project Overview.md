---
sidebar_position: 1
---
# Project Overview

## Asset Assessment 

- **Project Name:** Redback Asset Assessment  
- **Purpose:**  
  Introduce stakeholders and new developers to the Redback Asset Assessment, its goals, scope, the problem it solves, and its classification system for sensitive data.

---

## Problem Statement

Before detailing the goals and structure of this project, it’s essential to define the core issue that the Redback Asset Assessment is designed to address:

> Sensitive data breaches remain one of the most common and damaging threats to organizations.

Such breaches can result in:
- Identity theft,
- Customer harm,
- Legal and regulatory penalties,
- Loss of trust and reputation.

Common causes include:
- Data stored without proper classification,
- Information retained beyond legal timeframes,
- Exposure of data during development or system integration,
- Lack of encryption or access control.

---

## Project Goals

The **Redback Asset Assessment** is designed to proactively combat these issues by automating the **classification** and **flagging** of sensitive data. This enables guided responses and automated actions, ensuring compliance with modern privacy standards.

This project aims to help Redback:
- Detect exposure risks early in the development lifecycle.
- Classify sensitive data by urgency, legal impact, and business sensitivity.
- Comply with key data privacy standards (e.g., **APP 11**, **Privacy Act 1988**).
- Automate DevOps-driven mitigation workflows for compliance enforcement.

---

## Scope

The tool scans:
- **Code repositories**
- **Documents**
- **Databases**

It locates **text** and **file-based sensitive data**, classifying it by:
- **Data Type:** PII, PHI, NPI, etc.
- **Storage Format:** JSON, TXT, MP4, etc.
- **Lifecycle Status:** Retained vs. Expired
- **Risk Level:** Low, Medium, High

**Integration targets** include CI/CD pipelines, file systems, and enterprise systems, providing early detection and containment of privacy risks.

---

## Key Features

- **Data Classification:** Supports types like PII, PHI, NPI, biometric, and more.
- **Risk Levels:** Flags data by sensitivity level (Low/Medium/High) and recommends controls.
- **DevOps Integration:** CI/CD pipelines, developer tools, SIEMs, etc.
- **Compliance Monitoring:** Detects expired, exposed, or misclassified data.

---

## Target Users

| Role              | Use Case                                          |
|-------------------|--------------------------------------------------|
| Development Teams | Prevent data leaks in code and builds            |
| Security Analysts | Proactively identify data breach risks           |
| Compliance Officers | Validate regulatory compliance and flag issues |

---

## Example Use Cases

- Preventing sensitive data from being pushed to public repositories.
- Detecting unencrypted medical or financial records.
- Automatically deleting records beyond their retention period.
- Alerting when real production data is used in test environments.

---

## Summary

The **Redback Asset Assessment** revolutionizes data protection by making data sensitivity detection:
- **Automatic**
- **Proactive**
- **Enforceable**

It is designed for **seamless integration** with existing company workflows to reduce data breach risks and ensure compliance as the company scales and evolves.

