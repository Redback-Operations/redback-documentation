---
sidebar_position: 2
sidebar_label: Server Security Implementation Plan
---

# Server Security Policy Implementation Plan

:::info
**Published Date** 19/09/2024 (Trimester 2 2024) **Authors:** Liam Fern
:::

## Introduction

This report will create and define implementation strategies to implement and comply with the Redback Operations Server Security Policy. These implementation strategies should be carried out by the roles listed in this report, once implemented, Redback Operations will meet compliance with the policy.

### Objective

To develop an easy to implement, cost effective deployment plan for our Server Security policies and procedures.

### Roles and responsibilities

The roles and responsibilities relevant to this implementation plan who will be implementing and adhering to the Server security are as follows:

**Security Team**

- Implement security controls and measures

**IT Department**

- Assist in implementing security controls; manage and maintain server hardware and software; ensure timely application of patches and updates; support the Security Team in incident response activities.
- Operational management of servers and ensuring their compliance with the security policy.

**System Administrators**

- Apply security configurations and settings; monitor system performance and logs; enforce access controls and permissions; directly handle the installation, maintenance, and upgrading of servers.

**Management**

- Budget and resource allocation

## Deployment Strategies

### **Implement Operating System Hardening**

In order to implement and comply with this section of the policy, it will require the following:

1. Secure and functional Operating Systems used on all infrastructure and end user devices. To achieve this we will implement the following:
    1. Windows Server 2022 for all Servers
    2. Up to date, in life software for all other use cases where required (eg. Switching, Linux, MacOS etc).
2. A strict and functional operating system patch management solution. In order to achieve this, we will implement the following:
    1. Microsoft Intune management for all Windows Servers. All servers will be required to be enrolled in Microsoft Intune and we will push updates through update rings. This will include a policy where the Servers will have a scheduled update period (overnight) and will be forced to download and install the latest operating system patches.

### **Implement Application Management and Control**

In order to implement and comply with this section of the policy, it will require the following:

1. Implement an application control software such as Intune, Carbon Black, Defender etc.
    1. This software will contain an allowed application list, and will be in block mode for any executables or applications not contained in this list.
2. Review and implement administrative privilege controls
    1. Develop a policy for administrative privileges and demote any non-required administrators. Ensure no local administrator access on Servers.
3. Restrict command prompt and PowerShell privileges
    1. Enforce policy through intune/gpo that will restrict the use of terminals (command prompt, powershell) on all servers.

### **Implement Intrusion Prevention, Software Firewalls, Antivirus, and Device Access Control**

In order to implement and comply with this section of the policy, it will require the following:

1. Deploy Advanced Antivirus / EDR on Servers
    1. This will require a advanced antivirus/endpoint detection and response software such as Defender Plan 2, Crowdstrike etc. This will provide a high level of antivirus coverage as well as at least basic endpoint detection and response capabilities on all servers.
2. Deploy Network Intrusion Detection Software
    1. Deploy a network based intrusion detection software such as Darktrace, this will monitor the network and servers for any abnormal behaviours that could signal a network intrusion. This software will also respond and attempt to block any potential intrusions/incidents.
3. Implement Windows Firewall on all Servers
    1. Turn on and configure Windows Firewall on all Servers as per Microsofts best practice, this will work hand in hand with the AV/EDR and IDS systems to protect against threats.

### **Implement Operating System Event Logging**

In order to implement and comply with this section of the policy, it will require the following:

1. Investigate and implement a centralized event logging system
    1. This will collate logs from all Servers and analyse/present them in a centralized event logging system.
2. Setup event logging on all servers (especially Domain Controllers)
    1. We will need to setup and configure windows event logging as per best practice to ensure we are capturing all required logs.

### **Implement User Application Hardening**

In order to implement and comply with this section of the policy, it will require the following:

1. Implement a patch management solution for all third party applications
    1. A patch management solution such as PatchMyPc should be implemented to handle automatic patching of all third party applications on servers.
    2. This will work hand in hand with Intune to patch all applications, as Intune will be able to automatically update some more common third-party applications.
2. Ensure we are correctly patching common third-party applications and following their update guidelines. E.g. Web Browsers, Microsoft Office Applications etc.

### **Implement Microsoft Office Macro restrictions/policies**

In order to implement and comply with this section of the policy, it will require the following:

1. Utilise Microsoft Intune to enforce policy blocking the use of Microsoft Office Macros
    1. We can build a policy in Intune and enforce on all servers that will block Office Macros.
    2. If there are Servers not enrolled in Intune this will need to be enforced by Group Policy

### **Implement Server Application Hardening**

In order to implement and comply with this section of the policy, it will require the following:

1. Ensure all server applications follow secure-by-design and secure-by-default principles
2. If we develop in house applications that are present on Servers we need to ensure we are maintain secure programming practices
3. Ensure all applications on servers are compliant to our patch management policies and all applications are up-to-date with the latest security patches.
4. Restrict privileges for applications that do not require full access.

### **Implement Microsoft Active Directory Domain Services (AD DS) Hardening**

In order to implement and comply with this section of the policy, it will require the following:

1. Utilise Microsoft intune to deploy policies in compliance with the policy including
    1. Password Management
    2. Require Kerberos pre-authentication
    3. Domain Access Control – prevent standard users from adding computer objects etc.
2. Implement Active Directory account review process
    1. Members of the IT Department will conduct an annual audit of all active directory accounts, during which they will assess each accounts privileges and access and restrict/lock accounts that are no longer required.

### **Implement Microsoft AD DS Security Group Membership Hardening**

In order to implement and comply with this section of the policy, it will require the following:

1. Implement AD group membership review process
    1. Members of the IT Department will conduct quarterly reviews of all AD account memberships, during which they will ensure all groups are still required for each user and will remove users from groups if no longer required.
    2. Ensure all disabled accounts are removed from security groups.
    3. Ensure no user accounts are part of the Pre-Windows 2000 Compatible Access group.

### **Implement Authentication Hardening**

In order to implement and comply with this section of the policy, it will require the following:

1. Deploy multi-factor authentication across server environment.
    1. Utilise Azure/M365 SSO to require multi-factor authentication upon access to servers.
2. Review current credentials for privileged accounts including break glass, local administrator and service accounts.
3. Utilise Intune to build and enforce policies disabling insecure authentication methods
    1. Disable NTLM and LAN Manager
    2. Disable Authentication Methods susceptible to relay attacks.
4. Implement password change policies
    1. Change password every 12 months
    2. Change password when compromised or suspected of compromised
    3. Change shared passwords when staff leave
5. Utilise Intune to build and enforce the following lockout/account policies
    1. Lock accounts after five attempts.
    2. Terminate sessions daily
    3. Deploy company login banner
    4. Screen lock after 15 minutes of inactivity

### **Implement Virtualization Hardening**

In order to implement and comply with this section of the policy, it will require the following:

1. Review current virtual environment to determine compliance with the policy
    1. Ensure the following
        1. Type 1 Hypervisors: Run on bare metal and should be treated as lightweight operating systems.
        2. Type 2 Hypervisors: Run on top of general-purpose operating systems and should be treated as applications.
2. If non-compliance is found, VM’s should be remediated immediately to comply with this.

## Cost Effectiveness

Budgets and cost effectiveness have been strongly considered in the creation of this implementation and deployment plan. Where possible, cost saving measures have been chosen such as:

1. Utilising single systems to achieve compliance across multiple different sections of policy, and achieve the greatest return on investment.
    1. Microsoft Intune: Enforce patch management, enforce domain policies across a number of requirements.
    2. Azure/365 SSO to achieve MFA across multiple different platforms
2. Choosing systems that best meet the needs of our company and provide cost effective measures, such as Microsoft Defender for EDR/AV on servers. While Defender may not be the gold class of EDR solutions, it has a good industry reputation and provides adequate functionality that meets our needs at a really cost-effective price. If we were to go with other solutions, the cost would be significantly greater.

Overall, while it is important that we do not cut cost in the area of cyber security, we do recognize that this is a great cost to the company and have ensured we have presented the most cost-effective solution, maximizing return on investment in these implementation and deployment strategies.

## Ease of Implementation

Another key aspect considered in the planning of this implementation and deployment strategy was ease of implementation. We feel we have chosen deployment methods that fit the resourcing constraints of our company and will allow us to spend the least amount of time and resourcing available to achieve full compliance with the Server Security policy.

## Timeline

The timeline for achieving full compliance with the Server Security policy by following this implementation and deployment plan is **3-6 months.**

We feel this is achievable by splitting up relevant tasks between the Security team, IT department and System administrators. Upon analyzing the resources available, the work required and the systems we will need to implement, we feel this timeframe is more than reasonable.

## Conclusion

In conclusion, if the company decides to proceed with this plan we feel we have created a cost-effective and easy to implement implementation strategy that will see Redback Operations comply with the Server Security policy within a short-medium term.

Once all deployment strategies are followed, the security team should complete a compliance analysis to determine compliance with the policy.