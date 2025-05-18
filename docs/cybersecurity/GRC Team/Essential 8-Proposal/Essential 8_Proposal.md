---
sidebar_position : 1
---

# Essential 8 Cybersecurity Proposal for Redback

## Overview

In line with the Australian Cyber Security Centre (ACSC) recommendations, the Essential 8 provides a prioritized set of mitigation strategies to strengthen our cyber resilience. While initially designed for enterprise environments, these controls can be effectively scaled down and adapted to secure Redback’s infrastructure—including our VM environment, code repositories, and smart bike ecosystem.

We’ve assessed the relevance of each control in our context and propose a focused, phased implementation strategy aligned with our current maturity level.

---

## 1. Application Control

**Definition**: Only allow approved applications to run on our systems.

**Why it matters for us**:  
Our smartbike system and development VMs must run only approved software to avoid introducing malware or untested tools that could compromise system integrity.

**What we’ll do**:
- Whitelist only approved applications (development tools, diagnostic scripts, telemetry agents) on the VM.
- Use Defender Application Control or AppLocker for enforcement.
- Maintain a simple spreadsheet registry of approved tools and regularly review it.

**Practical Insight**:  
Think of it as making sure only the "right people with the right tools" get in—not just anyone walking by with a USB.

**Example**:  
Only allow tools like Visual Studio Code, Git, and our telemetry agent to run. Block games, installers, or other non-essential apps.

---

## 2. Patch Applications

**Definition**: Regularly update all software to fix security holes.

**Why it matters for us**:  
Outdated apps—whether they’re telemetry tools, browsers, or editors—can be exploited. We’ve got to patch fast, especially in a connected environment.

**What we’ll do**:
- Regularly check for updates on third-party software (e.g., Visual Studio Code, Python packages).
- Use manual checks or simple scripts for reminders until automation is possible.
- Patch within 48 hours if it’s a critical vulnerability.

**Practical Insight**:  
It’s like getting your bike serviced. If you skip it for too long, a small issue can turn into a breakdown.

**Example**:  
We updated Visual Studio Code after a recent vulnerability was reported to prevent potential remote code execution.

---

## 3. Configure Microsoft Office Macros

**Definition**: Block or control risky macros that can carry malware.

**Why it’s less relevant**:  
We don't use Microsoft Office products in our workflow, and macro-based threats are unlikely in this project.

**Action**:
- No specific configuration required now.
- If macros are introduced later (e.g., for reports), default to disabling macros and allowing only digitally signed ones.

**Example**:  
If we introduce Excel for project tracking, macros will be disabled by default unless they are signed by a trusted internal developer.

---

## 4. User Application Hardening

**Definition**: Lock down internet browsers and apps to reduce attack paths.

**Why it’s partially relevant**:  
Our use of browsers and apps on the VM is minimal, but still presents a risk—especially when downloading packages or checking documentation.

**What we’ll do**:
- Disable support for deprecated tech like Java and Flash.
- Turn on browser protection features like Safe Browsing.
- Educate team members to avoid unnecessary plugins.

**Example**:  
We disabled Java and Flash plugins in Firefox used on the VM, and enabled “HTTPS-only mode” to block unsafe connections.

---

## 5. Restrict Administrative Privileges

**Definition**: Limit admin access to only those who need it.

**Why it matters for us**:  
The VM used for Redback should have clear separation between developer tasks and admin rights.

**What we’ll do**:
- Use separate accounts (or at least separate roles) for dev work and admin actions.
- Rotate admin credentials periodically.
- Explore lightweight Just-In-Time access if scope expands.

**Practical Insight**:  
It’s like locking your bike tools in a separate pouch—you only open it when absolutely needed.

**Example**:  
A team member uses a standard account for coding but switches to an admin role only when changing VM settings.

---

## 6. Patch Operating Systems

**Definition**: Keep operating systems up to date with security patches.

**Why it matters for us**:  
Keeping our VM OS updated is critical. Exploiting outdated kernels or drivers is a common attack path.

**What we’ll do**:
- Enable automatic updates for the host and guest OS.
- Use Nessus Essentials or basic CLI tools to check for known CVEs.
- Patch critical vulnerabilities within 48 hours.

**Example**:  
Ubuntu VM was patched within 48 hours when a kernel vulnerability (CVE-2024-1234) was announced by the vendor.

---

## 7. Multi-Factor Authentication (MFA)

**Definition**: Require more than just a password to access systems.

**Why it matters for us**:  
MFA adds a critical layer of protection to our GitHub repo, especially for privileged team members.

**What we’ll do**:
- Enforce MFA on GitHub for all contributors.
- Encourage the use of hardware tokens or authenticator apps over SMS.
- Educate team members on securing credentials.

**Practical Insight**:  
It’s like locking your bike and putting an alarm on it—just in case someone tries to get clever.

**Example**:  
All contributors now use GitHub with an authenticator app, preventing unauthorized access even if a password is leaked.

---

## 8. Regular Backups

**Definition**: Create and test backups to recover data if lost.

**Why it matters for us**:  
Losing our codebase, sensor configurations, or experimental results would mean days of lost work.

**What we’ll do**:
- Schedule weekly backups of the VM and source code to a secure offsite location (e.g., encrypted external drive or cloud).
- Test restoration procedures every two sprints.

---

## Maturity Level and Next Steps

### Maturity Levels Explained

- **Maturity Level 0**: No or minimal implementation of controls. Ad-hoc practices. High risk.
- **Maturity Level 1**: Basic security hygiene. Controls are applied manually with limited consistency.
- **Maturity Level 2**: Controls are implemented consistently, with some automation and oversight.
- **Maturity Level 3**: Controls are fully enforced with minimal exceptions and monitored continuously.

---

### Our Target: Maturity Level 1

We are currently operating at Maturity Level 1 and aim to reach Maturity Level 2. This means moving from ad-hoc and manual methods to more consistent, semi-automated, and enforced controls across Redback systems.

---

### Steps to Reach Maturity Level 1

| Strategy                  | Actions for Maturity Level 1                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------|
| **Application Control**   | Implement automated enforcement using AppLocker or WDAC; monitor application usage logs.    |
| **Patch Applications**    | Use a centralized script or patch manager to check for updates weekly; patch within 48 hrs. |
| **Office Macros**         | Enforce Group Policy to block macros from the internet and allow only signed macros.        |
| **User App Hardening**    | Set browser policies centrally; disable Flash/Java; use threat-detection extensions.         |
| **Restrict Admin Privs**  | Enforce role-based access; JIT admin access; audit admin actions monthly.                   |
| **Patch OS**              | Enable automation; monitor compliance using tools like Nessus Essentials.                   |
| **MFA**                   | Require MFA for all tools; prefer authenticator apps over SMS.                              |
| **Regular Backups**       | Automate backups and test restoration monthly.                                              |

---

## Conclusion

By implementing these targeted Essential 8 strategies and moving towards Maturity Level 1, we will achieve:

- Stronger protection of Redback’s smartbike ecosystem, VMs, and codebase  
- Faster recovery from incidents with reliable backups  
- Reduced risk of cyber-attacks through consistent patching and access control  
- Increased cyber-awareness and disciplined security practices across the team  

Cybersecurity doesn’t have to be complicated to make a big impact. By building these simple, practical habits into our day-to-day work, Redback is setting itself up for a safer, more resilient future.
