---
sidebar_position: 5
---

# Phase 5 – Additional Security Controls

:::info
**Document Creation:** 16 May, 2025. **Last Edited:** 16 May, 2025. **Authors:** Bikendra Gurung.
<br></br>**Effective Date:** 16 May, 2025. **Expiry Date:** 16 May, 2026.
:::

## Objective

The objective of this phase is to further implement advanced email, identity and communication security controls to safeguard Redback Operations’ email and identity infrastructure against phishing, credential abuse, and unauthorised access.  

This phase focuses on enforcing sender filtering, identity protection, auditing and logging, and encrypted email transmission as per industry best practices.

---

## Deliverables

Outlined below are the security controls that have been implemented and validated in this phase.

- Controls 12, 13, 14 and 15 were implemented and validated using PowerShell, which can be found in the ‘redback-cyber’ GitHub repository (link below):  
  - Control 12–14: [Set-MailflowSecurity-AuditControls-Phase5.ps1](https://github.com/Redback-Operations/redback-cyber/blob/main/T1_2025/Email%20Infrastructure%20%26%20Security/Set-MailflowSecurity-AuditControls-Phase5.ps1)  
  - Control 15: [Set-MFAEnforcement-AllUsers-Phase5.ps1](https://github.com/Redback-Operations/redback-cyber/blob/main/T1_2025/Email%20Infrastructure%20%26%20Security/Set-MFAEnforcement-AllUsers-Phase5.ps1)

| Control # | Control Name                          | Control Description                                                                 |
|-----------|----------------------------------------|--------------------------------------------------------------------------------------|
| 12        | Block Malicious Senders and Domains   | Block emails from known malicious sender addresses and domains.                     |
| 13        | Block Malicious IP Addresses          | Block threat IPs using the Exchange Online connection filter policy.                |
| 14        | Enable Email Activity Auditing and Logging         | Enable mailbox-level auditing for visibility and traceability of email activity.    |
| 15        | Enforce MFA                           | Require multi-factor authentication for all user accounts (excluding breakglass).   |
| 16        | Enforce MTA-STS                       | Enforce strict TLS encryption using MTA-STS and TLS-RPT policy.                     |

---

## Important Notes
**For controls 12, 13, and 14:**
- Installed the ExchangeOnlineManagement PowerShell module  
- Set execution policy to ‘Bypass’ for the current session  
- Imported the ExchangeOnlineManagement PowerShell module  
- Connected using an account with 'Global Administrator', 'Exchange Administrator' or ‘Security Administrator’ permissions

![Exchange Online PowerShell](./img-phase5/12.0.1_exchange-online-ps.jpg)

**For control 15:**
- Installed Microsoft Graph SDK PowerShell module  
- Set execution policy to ‘Bypass’ for the current session  
- Imported the required Microsoft Graph SDK PowerShell module  
- Connected using an account with 'Global Administrator' permission with the required scope

![Microsoft Graph PowerShell](./img-phase5/12.0.2_ms-graph-ps.jpg)

---

## 12. Block Emails from Malicious Senders and Sender Domains (via Mail Flow Rule)

### 12.1. IMPLEMENT
![12.1](./img-phase5/12.1_implement-transport-rule.jpg)

### 12.2. VALIDATE
![12.2.1](./img-phase5/12.2.1_validate-transport-rule.jpg)  
![12.2.2](./img-phase5/12.2.2_validate-transport-rule.jpg)  
![12.2.3](./img-phase5/12.2.3_gui-validate-transport-rule.jpg)

---

## 13. Block Emails from Malicious IP Addresses (via Connection Filtering Policy)

### 13.1. IMPLEMENT
![13.1](./img-phase5/13.1_implement-block-ip.jpg)

### 13.2. VALIDATE
![13.2.1](./img-phase5/13.2.1_validate-block-ip.jpg)  
![13.2.2](./img-phase5/13.2.2_gui-validate-block-ip.jpg)

---

## 14. Enable Email Activity Logging and Auditing for all Mailboxes

### 14.1. IMPLEMENT
![14.1](./img-phase5/14.1_implement-audit-enable.jpg)

### 14.2. VALIDATE
![14.2](./img-phase5/14.2_validate-audit-enable.jpg)

---

## 15. Enforce Multi-Factor Authentication (MFA)

### 15.1. IMPLEMENT
![15.1](./img-phase5/15.1_implement-mfa.jpg)

### 15.2. VALIDATE
![15.2.1](./img-phase5/15.2.1_validate-mfa.jpg)  
![15.2.2](./img-phase5/15.2.2_gui-validate-mfa.jpg)  
![15.2.3](./img-phase5/15.2.3_gui-validate-mfa.jpg)  
![15.2.4](./img-phase5/15.2.4_gui-validate-mfa.jpg)  
![15.2.5](./img-phase5/15.2.5_gui-validate-mfa.jpg)

---

## 16. Enforce Strict TLS Encryption via MTA-STS

MTA-STS (Mail Transfer Agent Strict Transport Security) is an email security standard that ensures that:
- Inbound emails to your domain are encrypted using TLS
- Inbound emails are only sent to authorised mail servers (as specified in the MX record of your domain)

### 16.1. IMPLEMENT

#### 16.1.1. Host MTA-STS Policy via GitHub Pages
You should create a GitHub repo with the structure below:  
```plaintext
📁 redbackops-mta-sts-host/
├── 📄 _config.yml ← includes the .well-known directory
└── 📂 .well-known/
    └── 📄 mta-sts.txt ← your actual MTA-STS policy file
``` 
**16.1.1.1.	Create a GitHub Repo (Public)**  
•	**Name it**: `redbackops-mta-sts-host`   
•	**Add a folder**: `.well-known/`  
•	Inside `.well-known/`, create a file named: `mta-sts.txt`  

**16.1.1.2.	Add MTA-STS policy to the `mta-sts.txt` file**  
```
version: STSv1
mode: enforce
mx: *.mail.protection.outlook.com
max_age: 604800
```
![16.1.1.2](./img-phase5/16.1.1.2_mta-sts-policy.jpg)  

**16.1.1.3.	Add a _config.yml file with the following content**  
`include: [".well-known"]`  
![16.1.1.3](./img-phase5/16.1.1.3_config-yml.jpg)  

**16.1.1.4. Enable GitHub Pages**  
•	Go to **Settings -> Pages**  
•	Select the branch `main` and `root`  
•	**Custom domain**: `mta-sts.redbackops.com`   
•	The policy will now be hosted at: `https://mta-sts.redbackops.com/.well-known/mta-sts.txt`  
![16.1.1.4](./img-phase5/16.1.1.4_github-pages.jpg)

**16.1.1.5.	The policy will now be hosted at:** `https://mta-sts.redbackops.com/.well-known/mta-sts.txt`  
![16.1.1.5](./img-phase5/16.1.1.5_verify-hosted.jpg)

#### 16.1.2. Add DNS Records

**16.1.2.1.	Map to GitHub custom subdomain**
```
Name: mta-sts.redbackops.com
Type: CNAME
Value: <username>.github.io
```
![16.1.2.1](./img-phase5/16.1.2.1_dns-cname-github.jpg)  

**16.1.2.2.	Add TXT record for _mta-sts**
```
Name: _mta-sts.redbackops.com
Type: TXT
Value: v=STSv1; id=20250516T173050
```
> **Note:**  
The `id` value is a timestamp string used by external mail servers to detect changes. In this case, id=20250516T173050, which can be interpreted as:  
•	**Year**: 2025  
•	**Month**: 05  
•	**Day**: 16  
•	**Hour**: 17  
•	**Minute**: 30  
•	**Second**: 50  

**16.1.2.3.	TXT record for TLS-RPT reporting**  
```
Name: _smtp._tls.redbackops.com
Type: TXT
Value: v=TLSRPTv1; rua=mailto:blueteam@redbackops.com
```
> **Note:**  
> This enables daily TLS report aggregates from complaint mail providers (eg, Google, Microsoft, and Yahoo)

![16.1.2.2](./img-phase5/16.1.2.2_dns-cname-github.jpg)  

---

### 16.2. VALIDATE

#### 16.2.1. Using Command Line Tools (e.g., nslookup)
**16.2.1.1.	Validate DNS TXT record for _mta-sts**  
`nslookup -type=TXT _mta-sts.redbackops.com`  
![16.2.1.1](./img-phase5/16.2.1.1_nslookup-mta-sts.jpg)  

**16.2.1.2.	Validate TXT record for TLS-RPT reporting**  
`nslookup -type=TXT _smtp._tls.redbackops.com`  
![16.2.1.2](./img-phase5/16.2.1.2_nslookup-tls-rpt.jpg)

#### 16.2.2. Using Online Tools (MXToolbox, Hardenize)
**16.2.2.1.	Validate using MXToolbox**  
![16.2.2.1.1](./img-phase5/16.2.2.1.1_mxtoolbox-report.jpg)  
![16.2.2.1.2](./img-phase5/16.2.2.1.2_mxtoolbox-report.jpg)  

**16.2.2.2.	Validate using Hardenize**
![16.2.2.2.1](./img-phase5/16.2.2.2.1_hardenize-report.jpg)  
![16.2.2.2.2](./img-phase5/16.2.2.2.2_hardenize-report.jpg)

#### 16.2.3. Test Email Delivery
**16.2.3.1.	Send a test e-mail from a Gmail sender address (eg, redbackops24@gmail.com) to a @redbackops.com email account.**  
**16.2.3.2.	Check the e-mail headers.**  
![16.2.3.2](./img-phase5/16.2.3.2_mta-sts-headers.jpg)

#### 16.2.3.3. RESULT – Evidence of MTA-STS Enforcement
By design, there is no specific email header that directly shows that MTA-STS was applied because:
- MTA-STS is a transport-layer security mechanism
- It applies during the SMTP handshake and is not recorded in email headers

However, based on the screenshot above, it can be validated that MTA-STS was applied based on the points below:
- Encryption (TLS 1.3) was used when Gmail delivered the email
- The receiving domain (redbackops.com) had:
  - A valid `_mta-sts.redbackops.com` TXT record
  - A reachable `https://mta-sts.redbackops.com/.well-known/mta-sts.txt` file
  - An MTA-STS policy in enforce mode
- Senders like Gmail support and respect MTA-STS policy if one exists
- If Gmail (as the sender) was unable to establish a secure TLS connection, or if the TLS certificate on the receiving server (redbackops.com) did not match the MTA-STS policy requirements, Gmail would have refused to deliver the email because redbackops.com’s MTA-STS policy is set to enforce mode.


---

## References
- [Microsoft Exchange PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell?view=exchange-ps)
- [Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/powershell/microsoftgraph/?view=graph-powershell-1.0)
- [MTA-STS Overview – MXToolbox](https://mxtoolbox.com/dmarc/details/mta-sts/what-is-mta-sts-record)
- [MTA-STS Knowledge Base – Mailhardener](https://www.mailhardener.com/kb/mta-sts)
- [GitHub Pages Hosting Reference](https://github.com/jimeh/mta-sts-on-github-pages)
- [MTA-STS Lookup Tool – MXToolbox](https://mxtoolbox.com/mta-sts.aspx)
- [TLS and MTA-STS Reporting – Hardenize](https://www.hardenize.com/)
- [PowerShell Script – MFA Enforcement](https://github.com/Redback-Operations/redback-cyber/blob/main/T1_2025/Email%20Infrastructure%20%26%20Security/Set-MFAEnforcement-AllUsers-Phase5.ps1)
- [PowerShell Script – Mailflow & Audit Controls](https://github.com/Redback-Operations/redback-cyber/blob/main/T1_2025/Email%20Infrastructure%20%26%20Security/Set-MailflowSecurity-AuditControls-Phase5.ps1)


