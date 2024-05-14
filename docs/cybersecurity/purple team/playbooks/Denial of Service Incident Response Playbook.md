---
sidebar_position: 2
---

# Denial of Service Incident Response Playbook 

Denial of Service Incident Response Playbook for Blue Team

:::info
**Effective Date:** 29 April 2024. **Last Edited:** 20 April 2024. **Author:** Pari **Document Reference:** DSIRP-2. **Expiry Date:** 29 April 2025. **Version:** 1.0.
:::

## 1 Introduction

### 1.1 Overview

Denial of Service (DoS) assaults are a serious threat to the availability and integrity of online services in today's interconnected digital ecosystem. A denial-of-service (DoS) attack attempts to stop a system, network, or service from operating normally by flooding it with excessive amounts of unauthorised traffic or resource requests. These assaults have the potential to cause downtime, monetary losses, reputational harm, and even jeopardise the privacy of private data.

### 1.2 Purpose

This Denial of Service (DoS) Incident Response Playbook aims to offer a thorough structure for identifying, preparing, and responding to DoS attacks. This playbook tries to protect vital assets and services from disruptive cyber threats and reduce the effect of DoS incidents on our organization's operations by providing preventive measures, detection methods, response protocols, and recovery plans.

### 1.3 Attack Definition

An attempt to bring down a computer or network and prevent its intended users from using it is known as a Denial-of-Service (DoS) attack. DoS attacks achieve this by transmitting information that causes a crash or by overloading the target with traffic. The denial of service or resource to legitimate users, such as employees, members, or account holders, is the result of a denial-of-service attack in both cases.

### 1.4 Scope

This playbook includes a thorough method for handling Denial of Service (DoS) attacks in the operating environment and infrastructure of our company. From pre-incident planning and detection to mitigation, recovery, and post-event review, it covers every stage of incident handling. The principles and processes described in this playbook can be applied to mitigate related threats, such as Distributed Denial of Service (DDoS) attacks, even if the primary focus of attack is DoS.

## 2 Attack Types

### 2.1 UDP Flood

Attackers using UDP floods take use of UDP's intrinsic simplicity—that is, its connectionless nature, in contrast to TCP. Attackers frequently target ports or services as they bombard the target system with a massive volume of UDP packets. When the target's network bandwidth is overloaded or its processing power is depleted by the flood of UDP packets, it stops responding to legitimate traffic. Because UDP does not ensure delivery or order, attackers can fake the IP addresses used to originate their attacks, making it challenging to identify their origins.

### 2.2 TCP SYN Flood

TCP SYN Flood attacks exploit the Transmission Control Protocol's (TCP) three-way handshake protocol. TCP SYN packets are sent by attackers in large quantities; these packets form the initial stage of a TCP connection. They do not, however, send the last ACK packet to complete the handshake, which leaves the target system with a backlog of partially open connections. As a result, valid users are unable to connect to the server because the target's RAM and connection table entries are depleted.

### 2.3 HTTP Flood

The goal of HTTP flood attacks is to overload web servers with many HTTP requests. Attackers can target URLs, forms, or online application functionalities with a large volume of requests by using botnets or other automated methods. HTTP Flood assaults cause the server's performance to deteriorate, rendering it incapable of responding to valid user requests by using up the server's memory, processing power, and network bandwidth. Consequently, there is a disruption in service or downtime because of the web server becoming slow or unresponsive to authorised users.

### 2.4 Ping Flood (ICMP Flood)

Ping Flood attacks, sometimes referred to as "Ping of Death" or ICMP Flood attacks, overwhelm the target system with an endless barrage of Internet Control Message Protocol (ICMP) echo request packets. These packets, which take advantage of flaws in operating systems or network devices, are sent quickly and are usually larger than the allowed size. The target machine experiences sluggish performance or even crashes because of overusing its CPU and network resources processing these packets. Ping Flood assaults are hard to counter because they might originate from several sources at once and are reasonably easy to carry out.

### 2.5 Slowloris

Attacks known as "slowloris" are named after the way they use server resources—low and slow. Slowloris keeps a small number of connections active for a long time rather than flooding the server with requests. Attackers make sure that every connection is active by sending HTTP headers to the server very slowly. Slowloris stops authentic users from creating new connections by filling the server's connection slots with incomplete requests. A denial-of-service attack against authorised users attempting to access the web server may result from this resource exhaustion approach.

### 2.6 DNS Amplification

DNS Amplification attacks exploit vulnerabilities in DNS servers to amplify the volume of traffic directed at the target system. Attackers send small DNS queries with a spoofed source IP address to vulnerable DNS servers, requesting large DNS responses. These responses, which are much larger than the original queries, are directed towards the victim's IP address, overwhelming its network bandwidth. DNS Amplification attacks leverage the inherent trust between DNS servers, making it difficult to trace the origin of the attack.

### 2.7 NTP Amplification

NTP amplification attacks are comparable to DNS amplification attacks in that they increase the amount of traffic going to the target system by taking advantage of vulnerable Network Time Protocol (NTP) servers. Attackers make small NTP queries to NTP servers, asking huge NTP answers, using a faked source IP address. The victim's IP address is the target of these replies, which are usually significantly larger than the initial queries and interrupt services by congesting the network. Because the NTP protocol is UDP-based, NTP amplification attacks are challenging to counter.

### 2.8 Smurf Attack

Smurf Attacks increase the amount of traffic going towards the target system by taking advantage of IP networks' ICMP Echo Reply functionality. A lot of ICMP echo request (ping) packets are sent by attackers to IP broadcast addresses, pretending that the victim's IP address is the originating IP address. As a result, the victim's IP address triggers responses from every computer on the network, exceeding its available bandwidth and resources. 

## 3 Stakeholders

- **IT Administration**: The IT administration oversees the organization's servers, networks, and other IT infrastructure. They are essential in identifying, assessing, and minimising a denial-of-service attack in addition to organising the response to the occurrence.
- **Cyber Incident Response Team**: An organization's cyber security incident response team (CSIRT) is a specialised unit tasked with handling security incidents and breaches. Their main objective is to quickly locate, contain, and address issues to lessen their effects. CSIRTs are essential for safeguarding an organization's priceless assets, good name, and customers.
- **External Service Providers**: For a variety of IT services, companies may depend on outside vendors like internet service providers (ISPs), cloud service providers, or managed security service providers (MSSPs). By working together with these suppliers, the company can better respond to the denial-of-service attack and make use of more resources and experience.
- **Technical Support Team**: To troubleshoot and resolve technical issues associated with the DoS attack, the technical support team provides assistance. They can assist in promptly returning regular operations to normal and offer support to end customers impacted by the occurrence.
- **End Users**: If the DoS attack prevents end users from accessing services or apps, it could influence them. Minimising the impact on the position they hold can be achieved by keeping them updated on the situation and offering advice on workarounds or substitute solutions.
- **Senior Management/Executive Leadership**: In deciding how to respond to the DoS attack, senior management, or executive leadership assigns resources, sets strategic direction, and takes choices. They could also be in charge of maintaining the organization's reputation and dealing with outside stakeholders.


## 4 Flow Diagram

![Denial of Service Incident Response Flowchart](img\dsirp1-flowchart.png)

1. **Preparation (Pink)**
    - Develop and maintain Cyber Incident Response Plan (CIRP) for DoS incidents.
    - Identify critical assets and prioritize them.
    - Train incident response teams and employees.
2. **Detection (Orange)**
    - Continuously monitor network traffic.
    - Set up alerts for suspicious patterns.
    - Validate incidents.
3. **Analysis (Yellow)**
    - Investigate attack vectors and affected systems.
    - Collaborate with relevant teams.
4. **Containment (Green)**
    - Implement immediate mitigation measures.
    - Isolate affected systems.
    - Communicate progress.
5. **Eradication (Blue)**
    - Identify vulnerabilities.
    - Patch and remediate.
    - Verify closure of attack vector.
6. **Recovery (Red)**
    - Gradually restore services.
    - Validate restoration.
    - Monitor for recurrence.
7. **Post-Incident Review (Brown)**
    - Conduct a thorough review.
    - Learn from the incident.
    - Update the CIRP.


## 5 Incident Response Stages

### 5.1 Preparation

- **Objective**: Establish a robust foundation for effective incident response.

- **Key Actions**
    - Risk Assessment: Use thorough risk assessments to find possible DoS vulnerabilities in systems, apps, and network infrastructure. 
    - Creating Cyber Incident Response Plan(CIRP): Make a thorough incident response plan for handling denial-of-service (DoS) incidents. Establish communication routes, escalation protocols, and roles and duties.
    - Resource Allocation: Ensure that the people, equipment, and technologies required to support incident response activities are available. 
    - Training and Awareness: To improve staff members' comprehension of DoS risks, detection methods, and response protocols, offer training and awareness programmes. 
    - Form an Incident Response Team: Assign people to specific areas of handling the response to denial-of-service (DoS) situations in order to create a specialised team.

### 5.2 Detection

- **Objective**: Promptly identify and confirm the occurrence of DoS attacks.

- **Key Actions**
    - Monitoring and Alerting: To identify indications of unusual behaviour suggestive of a denial-of-service attack, continuously monitor network traffic, system performance metrics, and security logs. 
    - Anomaly Detection: Use intrusion detection/prevention systems (IDS/IPS), network traffic analysis tools, and security information and event management (SIEM) systems to identify strange patterns or abrupt increases in traffic volume that could be signs of a denial-of-service assault. 
    - Alert Triage: Set alerts produced by monitoring systems in order of priority and look into them to see whether they point to a possible DoS assault. Correlate alerts with several data sources to validate them.

### 5.3 Analysis

- **Objective**: Conduct in-depth analysis of the DoS attack to understand its nature, scope, and impact.

- **Key Actions**

    - Traffic Analysis: Examine network traffic patterns to determine the nature of the traffic, source IP addresses, and services or apps that are being targeted in order to determine the characteristics of the DoS attack. 
    - Log analysis: Look through firewall logs, system logs, and other pertinent log data to find any unusual activity or attempted illegal access that may have been connected to the DoS incident. 
    - Forensic Investigation: Gather and store digital evidence connected to the DoS assault for forensic examination. Memory dumps, system snapshots, and packet captures are a few examples of this. 
    - Root produce Analysis: Find the vulnerabilities or misconfigurations that the attacker may have exploited in order to trigger the denial of service (DoS) incident. 

### 5.4 Containment
- **Objective**: Limit the impact of the attack and prevent its spread.

- **Key Actions**
    - Traffic Filtering: To stop or filter malicious traffic linked to the DoS attack, use firewall rules, access control lists (ACLs), and other network filtering techniques. 
    - Rate limitation: To reduce excessive traffic flows and avoid network congestion, use rate limitation or traffic shaping techniques. 
    - Isolation: To stop the DoS attack from spreading and lessen its effects on other infrastructure components, isolate the compromised systems or network segments. 
    - Cloud-Based Mitigation: Use content delivery networks (CDNs) or cloud-based mitigation services to reduce the amount of DoS attack traffic before it enters the network perimeter of the company.

### 5.5 Eradication

- **Objective**: Eliminate the root cause of the attack and remove the presence of the attacker.

- **Key Actions**
    - Patch and Update Deployment: To address vulnerabilities that the attacker exploited and stop future denial-of-service assaults, apply patches, security updates, and configuration modifications. 
    - System Hardening: To strengthen systems and lessen their vulnerability to DoS attacks, take additional security precautions. Some of them include turning off unused services, tightening access limits, and putting security best practices into practice. 
    - Network Redesign: To increase resilience and better withstand DoS assaults, think about revamping the network architecture or implementing more network security measures.

### 5.6 Recovery

- **Objective**: Restore normal operations.

- **Key Actions**
    - System Restoration: Assure data integrity and uninterrupted operations by restoring impacted systems and services from backups. 
    - Service Verification: To make sure the restored systems and services are operating correctly and securely, thoroughly test and verify them.
    - Communication with Stakeholders: Give advice on how to resume regular activities and update stakeholders on the status of the recovery efforts.

### 5.7 Post-Incident Review

- **Objective**: Conduct a comprehensive review of the DoS incident response process to learn from the incident and improve future response.

- **Key Actions**
    - Debriefing: Conduct a debriefing session with the members of the incident response team to evaluate the success of the response efforts and pinpoint any obstacles that may have arisen. 
    - Root Cause Analysis: To determine the underlying causes of the DoS occurrence, such as security control gaps or vulnerabilities, conduct a root cause analysis. 
    - Documentation of Lessons Learned: Provide a record of the takeaways that were discovered from the DoS incident, outlining effective response tactics, areas that require development, and suggestions for improving incident response capabilities. 
    - Updates to the Incident Response Plan: To resolve identified shortcomings and integrate improvements, update the incident response plan in light of the post-event review results.

## 6 Terminology

- **CIRP (Cyber Incident Response Plan)**: It is a documented set of procedures and guidelines for organization to follow when responding to and managing security incidents. It outlines roles, responsibilities, communication channels, and technical steps necessary to detect, analyse, contain, eradicate, and recover from incidents. It is essential to have a well-prepared CIRP for effective incident response and minimizing the impact of security threats.

- **CSIRT (Cyber Security Incident Response Team)**: It an expert group that handles cyber security incidents. They are responsible for detecting, analysing, containing, eradicating, and recovering from security incidents affecting an organization. CSIRTs play a critical role in safeguarding an organization’s assets and maintaining trust with stakeholders.

- **UDP (User Datagram Protocol)**: It is a communication protocol used for time-sensitive transmissions such as video playback or DNS lookups. It does not establish a connection before data transfer and directly send them to a target computer without checking whether they arrived as intended or indicating their order.

- **TCP three-way handshake**: It is a protocol for establishing a connection between a server and a client in a TCP/IP network. It involves three steps: client sends a SYN segment to the server, server responds with a SYN-ACK segment, client acknowledges the server’s response with an ACK segment and establishing a reliable connection for data transfer.


