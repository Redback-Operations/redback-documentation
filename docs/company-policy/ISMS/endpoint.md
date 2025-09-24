---
sidebar_position: 5
---

# Endpoint Security

Redback Operations Policy

:::info
**Document Creation:** 27 April, 2024.  **Authors:** Kaleb Bowen
:::

## Version History

| Version | Modified By | Approver | Edited On | Changes Made |
|---------|-------------|----------|-----------|--------------|
| V0.1    | Kaleb Bowen |  | 27/04/2024 | Initial document creation |
| V1.0    | Nathasha Liyanage |  | 17/05/2025 | Review/Update  |


## Purpose

The purpose of this policy is to provide formal structure and minimum security standards for endpoint devices owned by or through direct affiliation of Redback Operations. This is to ensure security is standardised for all users, to the best possible solutions that can be offered in the varies ways that users connect to Redback digital assets. 

The Endpoint Security policy will ensure the appropriate measures in place to protect users and company assets whilst ensuring that usage of these systems is not compromised by threats or overly impeded by these measures. A balance of practicality and security is essential in the ongoing protection.

The policy also intends to ensure ongoing assurance to support Redback Operations in its evolution over time, ensuring that this policy reflects the continuous needs of endpoint security, and so supporting business continuity, as well as promoting a mature security culture.

## Scope

The scope of this policy applies to all usage of physical endpoints owned or operated by Redback Operations and its affiliated contributors. Including but not limited to laptops, desktops, phones, servers, and research devices under Redback Operations such as the smart wearables and smart bikes.

Endpoint security also extends to software ran on Redback Operations’ devices, as these have potential to cause harm to the organisation or owner of the device.

The policy will cover Redback-owned devices and contributor-owned devices separately and will be complimented by the BYOD policy for those contributor endpoints, as well as the broader Information Security Management System (ISMS) policy.

## Definitions and References

Primary definitions can be used from the Information Security Management System and ISO / IEC 27001. All referenced framework controls also come from ISO 27001. Additional definitions for this document:

-	ISMS: Information Security Management System, the primary policy document for Redback Operations.
-	Affiliated contributors: Deakin University SIT capstone students working within the Redback Operations project.
-	Redback-owned device: This includes devices such as exercise bikes owned by Deakin University and thus used by Redback Operations.

## Roles and Responsibilities

Roles and Responsibilities are necessary to ensure appropriate delegation of tasks, accountabilities, and responsibilities are spread to the correct stakeholders in the organisation. 

### Leadership

Those in leadership roles have overall ownership and top level responsibility for the endpoints. Strategic decisions regarding the applicability of policies, overall security oversight, and design of the security structure are likewise a responsibility.

### IT and Security Teams

Responsible for the process of design to development of implementation for the endpoint policies. This includes thorough testing of the implementation through test environments and gradual rollouts to ensure full security accountability. IT and Security must also consult with both leadership and the end users to ensure practical solutions, whilst maintaining a secure environment, built upon least privilege. 

### End Users

End users, being the device users and / or owners, are responsible for the usage of the devices in which they own or have personal data on. 

#### For Owners
Owners must ensure that they are compliant in updating their device to the required software and hardware specifications determined by leadership. They must also ensure that any usage by people other than themselves is compliant with the policy.

#### For Users

Users must take care when accessing Redback endpoints. Their usage must ensure that no data is compromised, and that their digital hygiene remains a high priority.

## Physical Security

### Storage

Whilst cloud storage is the preferred storage method for Redback Operations, some situations may arise that demand use of portable storage methods such as USB drives or portable HDD / SSDs. Attention must be given to these devices to ensure the adequate security. Storage devices with sensitive data should be stored in locked containers when not in use. When in transit, these devices should be kept on the user or as close to as possible.

### Devices

#### Device Storage

Portable devices that contain sensitive data should be locked in secure containers when not in use to ensure full protection. Access to this storage should only be for approved users. Testing devices specific to Redback Operations such as VR headsets or exercise bicycles that may not be able to be contained in safes or secured draws should be kept in rooms with controlled access management and surveillance.

#### Asset Management

Corporate devices should be registered in the company asset register, including current device holder and storage location.  Corporate devices should have their asset number printed on them, as well as information for their return if found. 

### Accessories to Endpoints

Attention should be given to any accessories connected to Redback Operations affiliated devices. This includes peripherals such as keyboards, mice, headsets, and monitors, as well as storage devices and other devices that may have the ability to transmit data. Accessories should be purchased from trusted sites, and only used in a safe matter consistent with safe online practices. Any evidence of tampering or malicious files should be responded to with seizure of using the accessory and seeking assistance from IT leadership in taking the next steps to ensure safety of personal and corporate information on the host device.

### Unattended Devices

Endpoints must engage a lock-out of content through a shutdown or sign-out after 15 minutes of inactivity to prevent potential bad actors getting access to the device. Regardless, users, especially those with privileged access, should be locking their devices immediately when leaving the direct area around it. Devices used for testing or experimental purposes may be configured to stay awake for the duration of their tasking if adequate signage is in place, or the presence of an approved user is nearby, additionally programs not necessary to the tasking should be locked down where relevant.

## Minimum Security Requirements

### Device Security
- All devices must use full disk encryption (e.g., BitLocker for Windows, FileVault for macOS).
- Screen locks must be enabled with an auto-lock timeout of 10 minutes or less, requiring authentication for access.
- Endpoints must engage a lock-out (shutdown or sign-out) after 15 minutes of inactivity, unless configured for testing purposes with adequate signage or supervision.

### Antivirus and Malware Protection
- All devices must run real-time antivirus/malware protection (e.g., Microsoft Defender, Sophos, Avast) with full settings enabled.
- Virus signatures and scanning engines must be updated weekly or more frequently.
- All Windows endpoints must, at a minimum, run Windows Defender with full settings.

### Operating System and Software Updates
- Operating systems and applications must enable automatic updates where possible.
- Critical security patches must be applied within 48 hours of notification, and non-critical updates at the earliest reasonable time.
- Disconnected or obsolete operating systems (e.g., Windows 7, macOS less than 10.15) are prohibited, and end-of-life software must be removed with alternatives identified.

### Application Control
- Only necessary and authorized software may be installed on Redback devices.
- Scripting environments (e.g. Python, PowerShell) must be used responsibly and only with permission to access sensitive systems.
- Unauthorized software installation is prohibited.

### Administrator Privileges
- Routine operations must not use administrator/root accounts.
- Administrative access is restricted to system owners or those with absolute need, with specific permissions granted where possible.
- Non-administrative users must log into locked-down accounts via group policy to prevent changes to core operating system aspects.

### Network Access
- Devices must connect only to secure, password-protected Wi-Fi networks.
- Public Wi-Fi requires a secure VPN (e.g. university VPN or approved equivalent).
- Software firewalls must be enabled on all devices (default for most operating systems).
  
### Data Storage and Access
- Sensitive data must not be stored on unauthorized cloud platforms (e.g. personal Google Drive, Dropbox) unless pre-approved.
- Local sensitive data must be minimized and encrypted.
- Sensitive and business-critical data should be stored on shared cloud repositories with relevant users, not locally.
- Offsite physical backups are recommended for added redundancy.
  
### Authentication
- Two-factor or multi-factor authentication ('2FA/MFA') must be enabled wherever supported, using password and token generators (e.g., Authy, Google Authenticator) or physical tokens (e.g., Yubikey).
- Users must use a password manager and maintain strong password practices (e.g., passphrases, complex passwords, regular breach checks).

### Redundancy and Backups
- Regular backups must be conducted to ensure data redundancy.
- Sensitive and business-critical data should be stored on shared cloud repositories, with offsite physical backups as an additional layer of redundancy.

## Monitoring and Reporting

- Device logs must be regularly reviewed to identify suspicious activity.
- Suspected malware, unauthorized access, or lost/stolen devices must be reported to the Redback Cybersecurity Team or project mentors within 24 hours.
- Redback may require device conformance checks before granting access to critical systems.

## Training and Awareness

- All users must complete endpoint security awareness training upon joining Redback Operations, covering secure device use, data handling, phishing techniques, and incident reporting.
- Users with privileged access to systems must complete additional company-standard training.

## Non-Compliance

Failure to comply with this policy may result in:
- Suspension of access to Redback resources.
- Referral to Deakin University IT and/or disciplinary action where warranted.
- Mandatory retraining or device security review.

## Review and Maintenance

This policy will be reviewed every 6 months or upon significant changes to Redback’s operational model or security posture. Updates will be developed under version control and published on the Redback Documentation site.

