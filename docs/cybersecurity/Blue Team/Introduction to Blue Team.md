---
sidebar_position: 1
---

# About the Blue Team

:::info
**Document Creation:** 10 Sept., 2025. **Last Edited:** 10 Sept., 2025. **Authors:** Robin Spoerl.
:::

## 1. Introduction 

The Blue Team, under the Cyber Security team, is responsible for ensuring the security of Redback Operations' infrastructure, with a focus on defensive security, mimicking how a real-life SOC (Security Operations Centre) would operate. So far, the team's main technical focus has been enhancing the security of the shared company VM, with monitoring tools, anti-malware capabilities, web application firewalls, and so on. Additionally, the team has also worked on an email-based infrastructure.

## 2. Key Services

This section provides a brief overview of the existing Blue Team services running on the VM. Note that all installed tools on the VM are open source. 

### 2.1. Wazuh ###

Wazuh is a SIEM (Security Information and Event Management) used to centrally monitor logs from various sources. It acts as a host-based intrusion detection system (HIDS) that monitors key security events on a target system. In Redback Operations, Wazuh is used to monitor the shared VM. While it is a comprehensive security tool on its own, it's commonly integrated with other security tools. 

### 2.2. ClamAV ###

ClamAV is a popular anti-malware scanning tool used in Linux environments. It primarily uses static signatures to detect malware. ClamAV is installed on the VM and set to periodically scan the entire system in 12-hour increments. Its logs are synced with Wazuh, so that any malicious software can be detected and removed. 

### 2.3. Suricata ###

Suricata is a network-based intrusion detection system. It monitors network traffic within the VM and has a comprehensive ruleset to detect threats. Currently, Suricata is running on the VM, and its logs are synced with Wazuh. 

### 2.4. Nginx + ModSecurity ###

Currently, the company VM uses Nginx as a reverse proxy to handle requests going to some web apps. To analyse these requests, the ModSecurity web application firewall (WAF) is used. It contains a highly detailed ruleset of common web application attacks. When an attack is detected, the ModSecurity logs are extracted and sent to Wazuh. 

### 2.5. Email Infrastructure ###

The Blue Team also manages an email infrastructure based on Microsoft 365 Exchange Online. This is a cloud-based email service that has a domain name attached to it. Therefore, it is not installed on the VM.

## 3. Getting Started

Before you start working on anything, read through the Onboarding section. This explains some more concepts about Wazuh and how you can access it, along with Docker fundamentals. Understanding Docker is particularly important, as most services are setup in Docker containers. 

Afterwards, have a look at the Production section. This includes guides for all the services mentioned above and how you can maintain them. 

Finally, the Research section includes things that some team members have worked on in the past. This includes pure research and how-to installation guides for things tested on local VMs (not implemented).

After you've read through these sections, have a think about what you'd like to work on, and discuss this with the team. 









