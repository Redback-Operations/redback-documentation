---
sidebar_position: 6
---

# Wazuh Documentation

Documentation of the Wazuh open-source security platform:

:::INFO

Author: **Lachlan Harrison**, **31/08/2024**

:::

## Section 1 - Capabilities of Wazuh

Wazuh is an open source and completely free security platform which can be utilized for many features and learning which will be discussed in this documentation. The tool itself is accessible via this link: https://wazuh.com/ 

When we utilize the Wazuh platform, every user that interacts with the platform is presented with many opportunities to learn various concepts ranging from hacking methods to security methods to strengthen your systems and protect yourself from any attacker in which may discover the various vulnerabilities and exploit them for their own gains. These are all a threat in the modern world and thus we have adopted to utilizing Wazuh to assist in detecting these threats and mitigating them as soon as possible to reduce the liklihood of a compromise or enumeration agaisnt members of the company.

When we mention these systems, they are referred to as Agents in which we can deploy various agents across the platform. The tool itself as well allows for further analysis into your agents across the dashboard in which the user can also discover various information about their agent, various configurations and standards to improve their security with this platform.

- We can also allow for Wazuh to send security alerts to our devices via a chosen method which can range from platforms like Slack to our own Emails. This tool is referred to as a SIEM tool (Security, Information and Event Management) which all of these elements are showcased in Wazuh’s interface. SIEM categorised tools are very important in Cyber Security elements as they are efficient with providing the appropriate analysis, detailed information, security recommendations and also real-time events that are occurring within our linked agents.

- Wazuh utilizes a simplistic method of analyzing our agents and due to this, the platform itself only requires a Linux server along with another machine to monitor the output of the tool which includes another computer. Many Linux servers are supported with Wazuh including various popular services such as Ubuntu and Debain. The implementation of this tool is also relatively easy and has already been discussed on another one of our documents. 

- The open-sourced tool as stated before provides users with a unique learning experience in which there is plenty of learning opportunities to grow and develop their knowledge in how to keep their devices safer from discovered vulnerabilities as well as providing users with knowledge of potential risks and how they can be mitigated to prevent enumeration, exploitation and compromises. This allows for users to become more cyber safe, reinforces their agent’s defences against cyber attacks and provides users with the knowledge to prevent these cases in the future.

- Wazuh’s system requirements are quite slim even if utilizing a Virutal machine, this creates for easier access to reach more users as well as easier performance on the machine. These include a minimum requirement of 2GB of RAM along with 2 CPU cores whereas the recommended requirements aim for 4GB of RAM and 8 CPU cores allowing for a better performance and smoother experience when analyzing agents.

Wazuh provides a lot of analysis opportunities for users to discover while utilizing the platform along with users to learn various concepts and potential vulnerabilities within their linked agents.



## Section 2 - What can we learn from Wazuh?

- The platform informs the user of any security configurations that need to be implemented to further enhance their security on the linked agent/s. These security configurations are also referred to as misconfigurations in which some of these the user may not intentionally select as it may have been from a previous user or default settings. Wazuh provides methods into configuring these misconfigurations properly along with what the misconfiguration actually is.

- Wazuh focuses on vulnerabilities a lot as it is the source of many cyber attacks and the platform explains these vulnerabilities, categorises them into severity of the vulnerability and also how we can mitigate some of these vulnerabilities so that the user cannot be discovered by an attacker via enumeration/social engineering tactics which can further lead to a potential compromise. A list of common vulnerabilities is accessible which can make the user more aware of the risk of enumeration and exploitation which can be mitigated by the user and prevent attackers from performing their reconnaissance on the targeted agent.

- Wazuh explores various threats in which malware is another area explored in which the interface is able to gather the type of malware being executed within the machine should the agent be compromised along with the severity of the malware. Other threats explored include brute-force attacks which can occur at any time in which Wazuh is able to alert the user that an attack is occurring and allows for the user to respond accordingly. This involves blocking the attacking IP address where the attack is being traced to which allows for proper incident response to the situation. With constant evolving cyber threats growing every day, Wazuh adapts to this with constant updates to its cyber attacks and is able to detect various new attacks within the linked agents.

- The MITRE ATT&CK framework is a major implementation within Wazuh as it is an important framework to learn and understand so that users can become aware of the various categories of attacks and what each of these attacks are. Detected vulnerabilities within an agent also provide for MITRE techniques to be classified and sorted with the associated vulnerability which each technique has a unique tag and allows for the user to learn about the associated attack method which is linked to the vulnerability. For example, a brute force technique is categorised into the Credential Access category with a unique ID of T1110.

- Other elements that Wazuh can analyse and inform us about is any changes within the Windows registry (if agent is windows) as well as any directory and file. These can range from changes to Windows registry keys including modifications, deleting and creating key values. Wazuh also analyses changes to a file and directory including adding, deleting and editing these files and directories.

- Wazuh provides insight into various compliance standards in a matter for users to follow which includes but are not limited to up to date updates, constant securing of devices which may involve MFA (Multi-Factor Authentication) and mitigating discovered vulnerabilities.

- The platform also displays to the user a Secure Configuration Assessment (SCA) which is able to inform users of why they need to follow certain actions to reduce the risk of being compromised and further keep themselves protected. The score given in the assessment further entails the user to perform various actions to achieve a higher score in their SCA which may involve for example installing certain software onto the associated agent. These are also considered misconfigurations which also utilize MITRE technique tags to classify them and the tool also informs the user with how they can check for these various misconfigurations and what they are.

- Intel provided on various security events is extremely critical for incident response and for developing a safer agent and reduce the risk of enumeration and compromise. The intel Wazuh provides includes authentication failures/success, top alerts as well as providing an entire list of security alerts for the associated agent in which we can obtain in the interface.

The tool provides so much information for the user and assists in becoming more secure with their agents as well as constant monitoring for any new changes needed to mitigate vulnerabilities that are discovered and any abnormal behaviour detected in which the user is able to respond accordingly. 



## Section 3 - Why Wazuh? Why do we need this tool?

Since implementing Wazuh into Redback Operations, Wazuh provides many reasons as to why this tool should be utilized including various elements that provide an opportunity for the user to develop their own cyber safe environment.

1. **Security Awareness** – Wazuh provides users knowledge of potential vulnerabilities and also how to mitigate these vulnerabilities to reduce the risk of a compromise or enumeration by an attacker by providing detailed information and solutions to make the user more aware of what is happening and why this is a risk.

2. **Incident Response** – The platform allows for active response to real events occurring on their linked agents including various attacks and file changes to at which the user can act upon these incidents and take the necessary steps required to mitigate these attacks and risks.

3. **Securing of Devices** – With the constant evolution of Cyber threats, Wazuh adapts and informs the user of these new threats by creating awareness of new exploits/vulnerabilities discovered within an agent and how to mitigate these risks hence why this tool provides a great opportunity for users to further secure their devices by adjusting configurations and making appropriate changes to mitigate the security alerts that are being detected.

4. **Safety** – The tool itself protects user’s machines by providing adequate information to the user as to how to improve their safety and security to protect themselves from foreign attacks/interference which in turn creates ease of access for company members to continue their work on their projects knowing that the agent they are utilizing has its security enhanced due to the correct configurations and implementations utilized within the agent.

5. **Accessibility** – Having a relatively easy to understand User Interface (UI), many users can easily navigate Wazuh’s dashboard to locate their agents and analyse the discovered elements. This creates an easy and also safe method of learning of what is being displayed to the user which for example, various vulnerabilities along with their MITRE techniques utilized to exploit this vulnerability and solutions to mitigate these vulnerabilities.

6. **Compliance** – Wazuh provides members the opportunity to be compliant with various standards that are followed throughout many companies including but not limited to MFA and minimalized password sharing. Through this, users can become more cyber safe and also by following these standards, users can also create a more cyber safe environment for their companies.

### Conclusion:
As a free open-sourced platform, Wazuh provides plenty of information and opportunities for members to learn about various cyber security principles, concepts and risks in which every one can learn how to mitigate and also utilize the platform in a positive manor to assist in protecting themselves from the evolving world of cyber threats and attacks. 

From easy implementation, low requirements and plenty of concepts that can be learnt, this platform is an extremely important asset to utilize in further enhancing a cyber safe environment to reduce the risk of exploitation, enumeration and compromise of a linked agent while also having various areas to develop our understanding of cyber security principles including but not limited to, Incident Response, Security awareness and safety.

### Extra Resources:

- MITRE ATT&CK Framework: https://attack.mitre.org/ 
- Security Awareness Training Modules: https://classroom.google.com/c/NzAzMjgwOTI3MDIw?cjc=ppfbboc 
- Link to Wazuh PowerPoint: (INSERT ONCE IMPLEMENTED)
- Link to Wazuh Video Documentation: (INSERT ONCE UPLOADED WITH VALID LINK)
