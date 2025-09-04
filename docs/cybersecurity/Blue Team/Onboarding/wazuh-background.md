---
id: wazuh-background
title: Wazuh Background & Onboarding
sidebar_position: 1
tags: [blue team, wazuh, onboarding]
---

# Wazuh Background

## What is Wazuh?
Wazuh is an open-source SIEM tool (Security Information and Event Management).  
It helps us keep an eye on what’s happening inside our systems by collecting and analysing logs from different places like servers, applications, and network devices.

Some of the main things it can do:
- Detect suspicious behaviour in real time.
- Track changes to important files (File Integrity Monitoring).
- Spot vulnerabilities and misconfigurations on agents.
- Show alerts in a web dashboard, linked to the MITRE ATT&CK framework.
- Help with compliance reporting and security audits.

At Redback, Wazuh is currently running on our VM through a Docker single-node setup.  
This makes it lightweight, easy to maintain, and good for student use.

---

## Why did we choose Wazuh?
When we looked at different SIEM and IDS tools (like Snort, Zeek, OSSEC, Splunk), Wazuh stood out because:
- It’s free and open-source (no licensing problems).
- Works well on Linux, which is what our VM uses.
- Has an active community that pushes out updates for rules and decoders.
- Easy to integrate with other tools we use or have tested (Suricata, ClamAV, VirusTotal, MISP).
- Can scale if we add more endpoints later.

For us, it hits the right balance of being practical to run, while also being a strong learning tool for students.

---

## Why do we also use Suricata?
Wazuh and Suricata do different jobs, so we use both:

- **Suricata** is a network intrusion detection system (NIDS). It looks at network traffic and packets to find things like port scans, brute force attacks, and suspicious connections.  
- **Wazuh** is more of a host-based SIEM. It focuses on logs, user activity, file changes, privilege escalation attempts, and compliance.  

Using them together gives us layered coverage:  
- Suricata = protects at the network edge.  
- Wazuh = protects inside the system.  

If we only used one, we’d have gaps.  
For example, Wazuh alone might miss a DDoS attempt on the network, and Suricata alone wouldn’t show failed login attempts or host activity inside the VM, while Wazuh provides that visibility.

---

## How to access Wazuh
1. Connect to the Deakin VPN using Cisco AnyConnect.  
   - Connect to `vpn.deakin.edu.au` and log in with your Deakin credentials (plus Duo Push).  
   - **Screenshot: Cisco AnyConnect login**  
![Cisco AnyConnect login](/img/wazuh-onboarding/VPN.png)

2. Open the Wazuh dashboard in a web browser:  
   [https://redback.it.deakin.edu.au/wazuh](https://redback.it.deakin.edu.au/wazuh)  

3. Log in with your **Entra ID account**.  
   - Contact your mentor or team lead (with Entra ID admin access) to create an account for you.  
   - Default credentials like `kibanaserver` are no longer used.  
      

Once logged in, you’ll see:  
- Security alerts  
- Linked agents and logs  
- MITRE ATT&CK mapping  
- Vulnerability information  

**Screenshot: Wazuh dashboard after login**
![Wazuh dashboard](/img/wazuh-onboarding/wazuh-dashboard.png)

---

## Note on SSH Access
If you need to connect to the Redback VM directly (for system admin or troubleshooting), you can do so with SSH after connecting to the Deakin VPN.  
Credentials will be provided by the Blue Team leads.  

For example:
ssh <username>@redback.it.deakin.edu.au


This is not required for Wazuh access but may be needed for backend tasks.
