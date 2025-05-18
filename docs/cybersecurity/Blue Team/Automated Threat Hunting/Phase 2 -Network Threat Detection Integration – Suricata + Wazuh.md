---
sidebar_position: 3
---

> **📌 Author:** Syed Mahmood Aleem Huzaifa  
> **📅 Date:** 17 May 2025

**Overview**

Phase 2 covers the integration of **Suricata** with the Wazuh Manager to enable network threat detection capabilities. It begins with the installation of Suricata on the Ubuntu-based manager system using the official OISF repository to ensure up-to-date packages. **Suricata** is then configured to output logs in EVE JSON format, specifying relevant event types such as alerts, DNS, HTTP, TLS, and SSH to optimize log relevance and reduce noise. The HOME_NET variable is defined to accurately classify internal traffic, which is essential for proper rule application and threat identification.

The integration continues by modifying the Wazuh Manager's configuration to ingest Suricata logs, ensuring that event data from the network layer is monitored and correlated with existing host-level data. Suricata rules are verified and, if missing, fetched using the suricata-update utility to ensure the engine is actively detecting threats. The success of this integration is validated by generating simulated network attacks using Nmap from another system and checking whether the expected alerts are recorded in the Suricata log file.

This phase ensures that Wazuh is not only capable of host-based monitoring but also equipped to detect and respond to suspicious network behaviour. With Suricata fully integrated, the system gains visibility into intrusion attempts, malware traffic, and other network anomalies, significantly enhancing the overall detection and response capabilities of the security platform.

### Step 1: Install Suricata on the Wazuh Manager VM (Ubuntu) using the commands:
```
sudo apt update

sudo apt install software-properties-common -y

sudo add-apt-repository ppa:oisf/suricata-stable -y

sudo apt update

sudo apt install suricata -y
```
The command ```sudo apt install software-properties-common -y``` installs a package that provides essential tools for managing software repositories, including add-apt-repository. This is necessary when you want to enable external PPAs (Personal Package Archives) not included in the default Ubuntu sources. The command ```sudo add-apt-repository ppa:oisf/suricata-stable -y``` then adds the official Suricata stable PPA from the OISF (Open Information Security Foundation) to your system’s list of software sources, ensuring that you can install and receive updates for the latest stable version of Suricata directly from its maintainers. Finally, 
```
sudo apt install suricata -y
```
 installs the Suricata network threat detection engine itself using the package provided by the newly added PPA. The `-y` flag in these commands is used to automatically confirm prompts during installation. Together, these commands prepare the system to securely and correctly install Suricata from an official and up-to-date source.

### Step 2: Once Suricata is installed, Configure Suricata to Output EVE JSON.
The file can be opened with the command: sudo nano /etc/suricata/suricata.yaml
Ensure the following section is configured:
```
outputs:
  - eve-log:
      enabled: yes
      filetype: regular
      filename: /var/log/suricata/eve.json
      types:
        - alert
        - dns
        - http
        - tls
        - ssh
```
![Screenshot of suricata yaml file](img\pic28.png)

In the Suricata configuration, the HOME_NET variable within the vars → address-groups section is used to define the range of IP addresses considered as internal or protected network assets. This definition plays a pivotal role in determining how traffic is classified and analysed, as many detection rules rely on whether a packet's source or destination belongs to the home network. The value assigned to HOME_NET can either be a single IP address, such as "192.168.0.219", or a broader address range, such as "[192.168.0.0/16,10.0.0.0/8,172.16.0.0/12]", depending on the network topology and monitoring goals. A single IP is typically used in lab setups, isolated sensors, or endpoint-focused deployments where Suricata is tasked with inspecting traffic from or to a specific host. In contrast, specifying CIDR ranges allows for comprehensive visibility across entire subnets, making it suitable for environments monitoring traffic at the gateway, router, or span port level. The decision should be based on the scope of monitoring and the placement of the Suricata sensor within the network infrastructure. Accurately defining HOME_NET ensures that detection rules trigger appropriately and helps reduce false positives by clearly distinguishing internal from external traffic.
![Screenshot of suricata yaml file 2](img\pic29.png)
[suricata.yaml file](doc/suricata.yaml)

Including the types of field within the eve-log section of the Suricata configuration is a critical best practice in security monitoring environments, particularly when the system is integrated with SIEM and SOAR platforms such as Wazuh, MISP, TheHive, and Cortex. The types list explicitly defines which categories of events Suricata should output to the eve.json log file, enabling fine-grained control over what data is collected and processed. Common event types include alert for intrusion detection rule matches, dns for DNS query logs, http for HTTP transactions, tls for TLS handshake metadata, ssh for SSH session data, and others such as flow, stats, and files, depending on the network visibility required. In our current setup, the absence of explicitly defined types of list means Suricata defaults to logging all or a broader range of events, which can lead to excessive log volume, increased disk usage, and reduced parsing efficiency within Wazuh. This default behaviour may have been initially retained to simplify deployment or due to oversight, but it is not ideal for a streamlined threat detection pipeline. Defining types not only reduces noise and conserves resources but also ensures compatibility with decoders and rules within Wazuh that expect structured, minimal, and relevant JSON logs. General recommendations for production deployments strongly suggest specifying only those types that are necessary for correlation, detection, and forensic analysis. Doing so helps maintain optimal performance and clarity across all integrated components of the threat intelligence ecosystem.

In the same file, the interface also needs to be updated based on the interface of your system, which can be checked using the command `ip a`
![Screenshot of interface](img\pic30.png)
Once all the configurations and changes are done as per the requirements, Suricata, similar to Wazuh, needs to be restarted for the new changes to reflect. 
This can be done using the command ```sudo systemctl restart suricata```

### Step 3:  Integrate Suricata Logs into Wazuh
Edit the Wazuh manager's localfile configuration: ```sudo nano /var/ossec/etc/ossec.conf```
Inside the `<localfile>` section, add the following: (If the content of ossec.conf has already been copied from the provided file, then it should have this in it. It is still better to cross-check before moving ahead)
```
<localfile>
  <log_format>json</log_format>
  <location>/var/log/suricata/eve.json</location>
</localfile>
```
To integrate Suricata logs with the Wazuh manager, the Wazuh configuration file (ossec.conf) must be updated to instruct it to monitor the Suricata event log. This involves editing the file using a text editor such as nano and adding a `<localfile>` block that specifies the log format as json and sets the log file path to /var/log/suricata/eve.json, which is where Suricata writes its events. If the configuration file has already been replaced or preconfigured from a known working version, this entry may already be present, but it is still important to verify its inclusion to ensure proper log ingestion. 
Restart the Wazuh manager (```sudo systemctl restart wazuh-manager```)

### Step 4: Loading Suricata rules
We can check if suricata has rules loaded or not with the command ```sudo suricata -T -c /etc/suricata/suricata.yaml -v```
If it says 0 rules loaded, then we can download all the rules with the command: 
	```sudo suricata-update ```

Download the rules with the command ```sudo systemctl restart suricata```
Restarts suricata so that the rules downloaded are now loaded
We can now again check if the rules are present using the same command as used earlier, which is ```sudo suricata -T -c /etc/suricata/suricata.yaml -v```
![Suricata rules check 1](img\pic31.png)
![Suricata rules check 2](img\pic32.png)

### Step 5: Validate Network Alert Ingestion
On another machine, where nmap is installed (can be the agent machine) run the command ```sudo nmap -sS -T4 -p1-1000 --script http-malware-host 192.168.0.225```

![nmap scan](img\pic33.png)

We can now look at the eve.json file to check if Suricata is monitoring the alerts: 
```sudo grep '"event_type":"alert"' /var/log/suricata/eve.json```
![Suricata logs check](img\pic34.png)

In this step, the objective is to validate that Suricata is actively monitoring network traffic and is capable of generating alerts based on known malicious or suspicious patterns. To simulate such traffic, a scan was performed from a separate machine (in this case, the agent system) using the Nmap tool. The specific command used was ```sudo nmap -sS -T4 -p1-1000 --script http-malware-host 192.168.0.225```, which performs a fast TCP SYN scan across ports 1 to 1000 and includes a script to detect HTTP-based malware behaviour. This traffic was directed towards the Wazuh manager machine (running Suricata) to trigger potential alerts.

Users attempting this validation step should ensure that the interface Suricata is monitoring corresponds to the one receiving this simulated traffic. If alerts do not show up immediately, you may be tempted to believe Suricata is not working; however, the absence of alerts can also mean either Suricata is not listening on the correct interface or that no relevant rules are being applied to detect this type of traffic. Therefore, it is important to double-check your HOME_NET and EXTERNAL_NET variables in the suricata.yaml configuration file and ensure the correct network segment is being monitored.

One common issue user might face is a warning during Suricata startup, such as *“No rule files match the pattern /var/lib/suricata/rules/suricata.rules.”* This essentially means no detection rules have been loaded, which would prevent any alert from being generated regardless of the traffic. If you see this, it's advisable to run suricata-update to fetch and install the default or community ruleset. Once updated, restart Suricata and confirm using the `suricata -T -c /etc/suricata/suricata.yaml` command that the rules are indeed being loaded, ideally noting the number of rules successfully loaded in the output.

After running the Nmap command, you can verify the alerts by filtering the eve.json log using:
```sudo grep '"event_type":"alert"' /var/log/suricata/eve.json```.

If everything is working as expected, you should see alert entries such as ICMP packets with unknown codes or malformed HTTP headers being flagged by Suricata. These entries confirm that Suricata is functioning properly and that alerts are being generated and logged.

For users who still don’t see alerts even after applying rules and generating traffic, it is recommended to check the logging configuration under eve-log in the YAML file and confirm that the alert type is enabled. You may also consider enabling additional logging types like dns, http, and tls for broader visibility into what Suricata is observing.





