---
sidebar_position: 5
---

:::info
**Document Creation:** 05 May, 2025. **Last Edited:** 05 May, 2025. **Authors:** Bikendra Gurung.
<br></br>**Effective Date:** 05 May, 2025. **Expiry Date:** 05 May, 2026.
:::

# Phase 4 – Additional security controls based on the CIS Foundations Benchmark guidelines

## Objective
The objective of this phase is to implement additional email security controls to further strengthen Redback Operations’ resilience against phishing, malware, spam, and other email-based threats. This implementation follows best practices aligned with the CIS Microsoft 365 Foundations Benchmark to ensure a secure, scalable, and compliant email infrastructure.

## Deliverables
The following security controls have been implemented and validated using PowerShell scripts, which can be found in the ‘redback-cyber’ GitHub repository (link below):  
[Redback Cyber GitHub Repo - Additional CIS Security Controls - Email & Collaboration.ps1](https://github.com/Redback-Operations/redback-cyber/blob/main/T3_2024/Email%20Infrastructure%20%26%20Security/Additional%20CIS%20Security%20Controls%20-%20Email%20%26%20Collaboration.ps1)

| Control | Description | CIS Benchmark Ref |
|---------|-------------|--------------------|
| Anti-Phishing Policy | This policy enables impersonation protection, spoof intelligence, DMARC enforcement, mailbox intelligence, and quarantine actions. | 2.1.7 |
| Anti-Spam Policy | This policy:<br></br>• Configures outbound spam filter to notify and alert administrators of suspicious outbound activities.<br></br>• Ensures inbound anti-spam policies do not contain any allowed domains, preventing filter bypass. | 2.1.6, 2.1.14 |
| Anti-Malware Policy | This policy:<br></br>• Enables internal sender malware notifications.<br></br>• Creates an anti-malware policy that blocks 186 malicious file types. | 2.1.3, 2.1.11 |
| Safe Attachments Policy | This policy:<br></br>• Ensures Safe Attachments Policy is enabled.<br></br>• Blocks malicious files, redirects them to an admin quarantine, and extends attachment protection to SharePoint, OneDrive and Teams. | 2.1.4, 2.1.5 |
| Safe Links Policy | This policy enables Safe Links for emails, Teams and Office applications, including protection such as URL click tracking, URL scanning, URL rewriting, and blocking user click-through on detected malicious links. | 2.1.1 |
| Common Attachment Types Filtering | This policy enables the default anti-malware policy’s file type filter to block common high-risk attachment types. | 2.1.2 |
| Connection Filtering Policy | This policy:<br></br>• Ensures no IP addresses are listed in the connection filtering policy to prevent filter bypass.<br></br>• Disables the safe sender list in the connection filter policy to prevent filter bypass. | 2.1.12, 2.1.13 |

## 10. Implement and validate additional security controls based on CIS Foundations Benchmark guidelines
Each control listed in the deliverables section was implemented step-by-step in a sequential order.

As for validation, each was validated using PowerShell cmdlets and via GUI validation immediately after implementation. The validation included checks for:
1. Policy creation and enablement status  
2. Scope assignment to all accepted domains  
3. Rule and policy priorities, and expected behaviours  
4. Flagging any missing configuration values and resolving any configuration anomalies.

Validation details and screenshot references are listed below.

## Implementation and Validation with Screenshot References

### PowerShell Setup Steps
Before implementing the controls, the following PowerShell setup steps were implemented:
•	Installed the ExchangeOnlineManagement PowerShell module.
•	Set execution policy to ‘Bypass’ for the current session  
•	Imported the module
•	Connected using an account with 'Global Administrator' or 'Exchange Administrator' permissions
•	Enabled organization customization using ‘Enable-OrganizationCustomization’
•	Verified that ‘IsDehydrated’ was set to ‘False’

- Installed the ExchangeOnlineManagement PowerShell module.
- Set execution policy to ‘Bypass’ for the current session.
- Imported the module.
- Connected using an account with 'Global Administrator' or 'Exchange Administrator' permissions.
- Enabled organization customization using `Enable-OrganizationCustomization`.
- Verified that `IsDehydrated` was set to `False`.
![0_Connecting_to_Exchange_Online.jpg](./img-phase4/0_Connecting_to_Exchange_Online.jpg)

### 10.1. Anti-phishing Policy
![1.1_Anti-phishing-policy_implement.jpg](./img-phase4/1.1_Anti-phishing-policy_implement.jpg)
![1.2_Anti-phishing-policy_implement.jpg](./img-phase4/1.2_Anti-phishing-policy_implement.jpg)
![1.3_Anti-phishing-policy_validate.jpg](./img-phase4/1.3_Anti-phishing-policy_validate.jpg)
![1.4_Anti-phishing-policy_validate.jpg](./img-phase4/1.4_Anti-phishing-policy_validate.jpg)
![1.5_Anti-phishing-policy_validate.jpg](./img-phase4/1.5_Anti-phishing-policy_validate.jpg)

### 10.2. Anti-spam Policy
![2.1.1_Anti-spam-outbound-policy _notify-admins.jpg](./img-phase4/2.1.1_Anti-spam-outbound-policy_notify-admins.jpg)
![2.1.2_Anti-spam-policy_notify admins_gui-validate.jpg](./img-phase4/2.1.2_Anti-spam-policy_notify-admins_gui-validate.jpg)
![2.2.1_Anti-spam-inbound-policy_no-allowed-domains.jpg](./img-phase4/2.2.1_Anti-spam-inbound-policy_no-allowed-domains.jpg)
![2.2.2_Anti-spam-inbound-policy_no-allowed-domains_gui-validate.jpg](./img-phase4/2.2.2_Anti-spam-inbound-policy_no-allowed-domains_gui-validate.jpg)

### 10.3. Anti-malware Policy
![3.1.1_Anti-malware-policy_notifs-for-internal-users.jpg](./img-phase4/3.1.1_Anti-malware-policy_notifs-for-internal-users.jpg)
![3.1.2_Anti-malware-policy_notifs-for-internal-users_gui-validate.jpg](./img-phase4/3.1.2_Anti-malware-policy_notifs-for-internal-users_gui-validate.jpg)
![3.2.1_Anti-malware-policy_comp-attach-filter_implement.jpg](./img-phase4/3.2.1_Anti-malware-policy_comp-attach-filter_implement.jpg)
![3.2.2_Anti-malware-policy_comp-attach-filter_implement.jpg](./img-phase4/3.2.2_Anti-malware-policy_comp-attach-filter_implement.jpg)
![3.2.3_Anti-malware-policy_comp-attach-filter_validate.jpg](./img-phase4/3.2.3_Anti-malware-policy_comp-attach-filter_validate.jpg)
![3.2.4_Anti-malware-policy_comp-attach-filter_validate.jpg](./img-phase4/3.2.4_Anti-malware-policy_comp-attach-filter_validate.jpg)
![3.2.5_Anti-malware-policy_comp-attach-filter_validate.jpg](./img-phase4/3.2.5_Anti-malware-policy_comp-attach-filter_validate.jpg)
![3.2.6_Anti-malware-policy_comp-attach-filter_validate.jpg](./img-phase4/3.2.6_Anti-malware-policy_comp-attach-filter_validate.jpg)
![3.2.7_Anti-malware-policy_comp-attach-filter_gui-validate.jpg](./img-phase4/3.2.7_Anti-malware-policy_comp-attach-filter_gui-validate.jpg)
![3.2.8_Anti-malware-policy_comp-attach-filter_gui-validate.jpg](./img-phase4/3.2.8_Anti-malware-policy_comp-attach-filter_gui-validate.jpg)

### 10.4. Safe Attachments Policy
![4.1.1_Safe-attachments-policy_implement.jpg](./img-phase4/4.1.1_Safe-attachments-policy_implement.jpg)
![4.1.2_Safe-attachments-policy_validate.jpg](./img-phase4/4.1.2_Safe-attachments-policy_validate.jpg)
![4.1.3_Safe-attachments-policy_gui-validate.jpg](./img-phase4/4.1.3_Safe-attachments-policy_gui-validate.jpg)
![4.2.1_Safe-attachments-policy_sp-od-teams.jpg](./img-phase4/4.2.1_Safe-attachments-policy_sp-od-teams.jpg)
![4.2.2_Safe-attachments-policy_sp-od-teams_gui-validate.jpg](./img-phase4/4.2.2_Safe-attachments-policy_sp-od-teams_gui-validate.jpg)

### 10.5. Safe Links Policy
![5.1.1_Safe-links-policy_implement.jpg](./img-phase4/5.1.1_Safe-links-policy_implement.jpg)
![5.1.2_Safe-links-policy_implement.jpg](./img-phase4/5.1.2_Safe-links-policy_implement.jpg)
![5.1.3_Safe-links-policy_validate.jpg](./img-phase4/5.1.3_Safe-links-policy_validate.jpg)
![5.1.4_Safe-links-policy_gui-validate.jpg](./img-phase4/5.1.4_Safe-links-policy_gui-validate.jpg)

### 10.6. Common Attachment Types Filtering Policy
![6.1.1_Comm-attach-types-filter.jpg](./img-phase4/6.1.1_Comm-attach-types-filter.jpg)
![6.1.2_Comm-attach-types-filter_gui-validate.jpg](./img-phase4/6.1.2_Comm-attach-types-filter_gui-validate.jpg)

### 10.7. Connection Filtering Policy
![7.1.1_Conn-filter-policy_no-ip-allow-list.jpg](./img-phase4/7.1.1_Conn-filter-policy_no-ip-allow-list.jpg)
![7.1.2_Conn-filter-policy_no-ip-allow-list_gui-validate.jpg](./img-phase4/7.1.2_Conn-filter-policy_no-ip-allow-list_gui-validate.jpg)
![7.2.1_Conn-filter_safe-list-off.jpg](./img-phase4/7.2.1_Conn-filter_safe-list-off.jpg)
![7.2.2_Conn-filter_safe-list-off_gui-validate.jpg](./img-phase4/7.2.2_Conn-filter_safe-list-off_gui-validate.jpg)

## References
- [Microsoft Admin Center](https://admin.microsoft.com/)
- [CIS Benchmark – Microsoft 365](https://www.cisecurity.org/benchmark/microsoft_365)
- [Redback Cyber GitHub Repo - Additional CIS Security Controls - Email & Collaboration.ps1](https://github.com/Redback-Operations/redback-cyber/blob/main/T3_2024/Email%20Infrastructure%20%26%20Security/Additional%20CIS%20Security%20Controls%20-%20Email%20%26%20Collaboration.ps1)