# Threat Intelligence

## 1. Introduction

Threat intelligence, often referred to as cyber threat intelligence (CTI), is the process of collecting, analyzing, and utilizing information about potential or existing threats to an organization's digital infrastructure. It is an essential component of a proactive cybersecurity strategy, aimed at identifying and understanding the various risks posed by cyber threats.

Threat intelligence involves gathering data from a multitude of sources, including threat feeds, dark web monitoring, and open-source intelligence (OSINT), to anticipate and defend against cyberattacks.

One of the core activities in threat intelligence is hunting for **Indicators of Compromise (IOCs)**. IOCs are specific pieces of evidence that suggest a security breach or malicious activity within a network, such as unusual network traffic, malicious file signatures, or suspicious IP addresses. By actively searching for these indicators, cybersecurity professionals can detect and mitigate threats before they cause significant harm.

In addition to identifying IOCs, threat intelligence also involves the analysis of **Tactics, Techniques, and Procedures (TTPs)** used by cyber adversaries. TTPs are the methodologies and strategies employed by attackers to infiltrate, exploit, and maintain access to targeted systems. Understanding these patterns allows organizations to predict potential future attacks and develop more effective defensive measures.

The importance of threat intelligence cannot be overstated in today's increasingly digital world. As cyber threats become more sophisticated and persistent, organizations need to stay one step ahead of attackers. Effective threat intelligence not only helps in identifying and responding to current threats but also plays a crucial role in preventing future attacks by enhancing overall security posture and resilience.

Through the continuous monitoring and analysis of emerging threats, organizations can better protect their assets, reputation, and sensitive data from the ever-evolving cyber threat landscape.

## 2. Methodology

My main objective is to find and provide **IOCs** and create rules from **Tactics, Techniques, and Procedures (TTPs)** to be integrated into the SIEM solution so that the cyber-attacks associated with them can be proactively detected and responded to.

Following are the methodology steps that I intend to follow:

### 2.1. Threat Hunting

I will use Twitter feeds to search for the specific APT groups which are active in the region. Find their IOCs and then perform further threat hunting using **FOFA**, **Shodan**, **Verodin**, **VirusTotal**, and **Qinxin**.

### 2.2. Share IOCs

Then, I will share the TTPs and IOCs with the team to update their rules and IOCs management to defend the IT infrastructure proactively.

### 2.3. Create Rules

Afterward, I will create rules from the TTPs that will be integrated into the SIEM to detect and respond to such malicious activity.


![](img\ti-1.png)

## 3. Collecting IOCs from Twitter

Begin with the specific **Advanced Persistent Threats (APT)** group search feeds. **APT Lazarus** and **Bitter** are the North Korean and Indian groups, respectively, that are actively attacking IT infrastructure across the world. 

Considering them to be the threats to **Redback Organization**, and being the threat intelligence person, I will begin with their search tags as shown in Figures 2 and 3. Their results are shown in Figures 4 and 5.


![](img\ti-2.png)

![](img\ti-3.png)

![](img\ti-4.png)

![](img\ti-5.png)

After getting some latest search results, I will begin with collecting **IOCs** and share them afterward with the team to block them. 

Here are some of the latest IOCs that I have collected that I will share with the team to block:

| **APT Bitter IOCs**        | **APT Lazarus IOCs**   |
|----------------------------|------------------------|
| Kimfilippovision[.]com      | bitbucket[.]org        |
| devflowservice[.]com        | tpddata.com            |
| mcdavezonepanel[.]com       | itaddnet.com           |
| mxuconlinegame[.]com        | wifispeedcheck.net     |
| 194.36.191.199              | coinoen.org            |

**Table 1: Some of the Collected IOCs**

## 4. Threat Hunting

Collecting **IOCs** from the Internet has indeed some advantages; however, it is not sufficient to rely only on open-source intelligence. Hence, threat hunting becomes the optimal solution under these circumstances, helping in hunting and gathering more IOCs relevant to the reported IOCs.

Let's begin hunting some IOCs using **FOFA**, **Validin**, and **VirusTotal**:

The IOC `mxuconlinegame[.]com` is used to collect more IOCs relevant to it.

1. Search IOC on **FOFA**.
![](img\ti-6.png)

2. Analyze the information that can be used to hunt more IOCs as shown in Figure 7.
![](img\ti-7.png)

3. Create a query of the common patterns to search for more relevant IOCs. The goal is to filter out until the most prominent results are acquired.
![](img\ti-8.png)

4. Collect the results and analyze them further on **VirusTotal** and **Qianxin**. The following are the newly hunted IOCs:  
   - `patch-manger[.]com`  
   - `ferrinonlinemuseum[.]com`  
   - `82.221.136.1`  
   - `82.221.136.47`
![](img\ti-9.png)

5. Search further about the identified IOCs.
![](img\ti-10.png)
![](img\ti-11.png)

After analyzing further, it was concluded that these IPs and domains belong to **APT Bitter**, and they are acting as **C2 Servers**. 

Hence, the IOCs that can be shared with the team are:

- `patch-manger[.]com`
- `ferrinonlinemuseum[.]com`
- `82.221.136.1`
- `82.221.136.47`

## 5. Conclusion

**Threat Intelligence** is an important part of cybersecurity operations. This document thoroughly explained how threat intelligence can be useful in proactively defending against **APTs**. However, the document only focused on explaining a single unique and efficient method of hunting IOCs. 

There are further tools and platforms that are collectively used for threat intelligence, such as **MailTrail**, **SOC Radar**, **Group IB**, and **Zeek**. But the method demonstrated in this document is found to be the most effective and efficient in identifying and hunting more IOCs. The document is limited specifically to showcase a single case. If required, it can be expanded further to **malware** and **tactics, techniques, and procedures (TTPs)** analysis.

## 6. References

- EC-Council. (2024, March 7). *What is Cyber Threat Intelligence | Cyber Threat Intelligence Analyst | Types of Threat Intelligence | EC-Council*. Cybersecurity Exchange. [Link to article](https://www.eccouncil.org/cybersecurity-exchange/threat-intelligence/what-is-cyber-threat-intelligence/#:~:text=Cyber%20threat%20intelligence%20is%20information)

- Shen, G. (2023, March 20). *Use Searching Engines to Hunt For Threat Actors*. Medium. [Link to article](https://gustavshen.medium.com/use-searching-engines-to-hunt-for-threat-actors-74be52976e9f)

- [FOFA](https://en.fofa.info)

- [VirusTotal](https://www.virustotal.com)

