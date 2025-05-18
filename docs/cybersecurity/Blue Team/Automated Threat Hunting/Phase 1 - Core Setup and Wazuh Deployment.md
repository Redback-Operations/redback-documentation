---
sidebar_position: 2
---

> **📌 Author:** Syed Mahmood Aleem Huzaifa  
> **📅 Date:** 17 May 2025

**Overview**

Phase 1 covers the foundational setup of the Wazuh security monitoring system by deploying a manager on an Ubuntu virtual machine and an agent on a Debian virtual machine. It includes preparing the network, updating system packages, setting hostnames, and installing the Wazuh Manager and Agent using official repositories. The phase ensures secure communication between the manager and agent through key-based registration and custom configuration using ossec.conf. It also addresses logging limitations by installing rsyslog on Debian to enable proper authentication event logging. The phase concludes with the installation of the Wazuh Indexer and Dashboard to complete the all-in-one platform. This provides a web interface for managing alerts and agent activity, ensuring a fully functional and integrated Wazuh environment ready for threat detection and analysis.

### Step 1: Prepare your Virtual Machines

**Manager VM:** Ubuntu 22.04 or 20.04  
**Agent VM:** Debian 11 or 12  

**VMs Network Configuration:**

- Set both the VMs on the same network. Preferably use a **Bridged Adapter** or an **Internal Network**. (**IMPORTANT**)  
- Make sure both machines can ping each other to verify network connectivity.

 ![Network Configuration on Virtual Box](img\pic1.png)

 ### Step 2: Update and Set Hostnames

On both machines, first run the following command:
```
sudo apt update && sudo apt upgrade -y
```
On the manager VM: 
```
sudo hostnamectl set-hostname wazuh-manager
```
On the Agent VM: 
```
sudo hostnamectl set-hostname wazuh-agent
```
Now reboot both the VMs using the command 
```
sudo reboot
```
Setting the hostname on your Wazuh Manager and Agent VMs is not strictly mandatory, but it is highly recommended for clarity and proper configuration in your Wazuh environment. It helps with identification, making it easier to differentiate between multiple VMs, and ensures better organisation when reviewing logs and alerts, as some may include the hostname, simplifying troubleshooting. Additionally, configuration consistency is improved since some services rely on a stable hostname. 

### Step 2: Install Wazuh Manager on Ubuntu (Manager VM)

1.	Import the Wazuh GPG Key
```
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --dearmor -o /usr/share/keyrings/wazuh-archive-keyring.gpg
```
If curl is not installed then it can be installed using
```
sudo apt install curl
```
2.	Add the Wazuh repository:
``` 
echo "deb [signed-by=/usr/share/keyrings/wazuh-archive-keyring.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list
```
3.	Install Wazuh Manager:
a.	```sudo apt update```
b.	```sudo apt install wazuh-manager -y```
![Screenshot of installation](img\pic2.png)
4.	Start and enable Wazuh Manager:
a.	```sudo systemctl daemon-reload```
b.	```sudo systemctl enable wazuh-manager```
c.	```sudo systemctl start wazuh-manager```
The status of the wazuh manager can be checked using the command: ```sudo systemctl status wazuh-manager```
![Wazuh Manager running](img\pic3.png)

If active (running), the Manager is ready.

### Step 3: Install Wazuh Agent on Debian (Agent VM)

You can use any Linux distribution or even a Windows machine to act as an agent. In this setup, a **Debian** system has been chosen.

If you're installing Debian, it's important to ensure that **GRUB**, the bootloader, is properly installed and configured. GRUB plays a crucial role in managing the boot process, allowing for a smooth startup, troubleshooting, and easy selection between multiple operating systems. Without it, your system may fail to boot or have difficulty recognising installed OSes.

Additionally, Debian includes a desktop environment by default during installation, with **GNOME** often being the standard choice. However, users can opt for alternatives like **Xfce**, **KDE**, or **LXQt** if they prefer a different look and feel. Choosing the right desktop environment enhances usability by providing an intuitive graphical interface, making system navigation much more seamless compared to using only the command line.
1.	Import Wazuh GPG key: 
```
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --dearmor -o /usr/share/keyrings/wazuh-archive-keyring.gpg
```
2.	Add Wazuh repository: 
```
echo "deb [signed-by=/usr/share/keyrings/wazuh-archive-keyring.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list
```
3.	Install Wazuh Agent:
```
sudo apt update
sudo apt install wazuh-agent -y
```
![Debian-Wazuh agent setup](img\pic4.png)
4.	Configure the agent to connect to the Manager: Open the agent configuration file using the command sudo nano /var/ossec/etc/ossec.conf, and where MANAGER_IP is mentioned, enter the IP address of the Ubuntu VM or where your Wazuh Manager is installed.
![ossec.conf screenshot](img\pic5.png)
Replace the content of the files with the content of the linked file
[ossec.conf file](doc/ossec.conf)

The changes in the attached file from the default file are outlined in the table below
### Configuration Feature Comparison

| **Feature**                      | **New Config**                                   | **Default Config**                             | **Importance/Impact**                                                                 |
|----------------------------------|--------------------------------------------------|------------------------------------------------|----------------------------------------------------------------------------------------|
| Enrollment Block                 | Present (`<enrollment>`)                         | Missing                                        | Important for auto-enrolling agents. Removal means agents must be registered manually. |
| Rootcheck - Ignore Docker Paths | Not present                                      | Ignores `/var/lib/containerd` and `/var/lib/docker/overlay2` | Reduces noise if containers are used; beneficial only if Docker or containerd is present. |
| Wodle - osquery                  | Enabled (`<disabled>no</disabled>`)              | Disabled (`<disabled>yes</disabled>`)          | Disabling reduces system visibility; osquery collects detailed system information useful for security. |
| Log Collection Method            | Collects specific logs (Apache, Auth, Syslog, Suricata) | Collects only system logs via Journald         | Original provides better and more granular monitoring. Journald-only approach risks missing specific service logs. |
| Apache, Suricata, Auth Logs      | Explicitly monitored                             | Not monitored separately                       | Important for detecting web attacks, authentication events, and network intrusion alerts. Their removal weakens detection capabilities. |
| Localfile Count                  | More targeted logfiles                           | Fewer generalised logs                         | Targeted logfile monitoring is better for specific security detections.                |
| Active Response                  | Enabled                                          | Enabled                                        | No difference.                                                                         |
| SCA and Syscheck                 | Same                                             | Same                                           | No impact.                                                                             |

5.	Start and enable the Wazuh Agent:
	```
    sudo systemctl daemon-reload
	sudo systemctl enable wazuh-agent	
    sudo systemctl start wazuh-agent
    ```
6.	Check Wazuh Agent status: 
```
sudo systemctl status wazuh-agent
```
![Wazuh Agent running](img\pic6.png)

### Step 4: Register Agent on the Manager
Part 1: On the Manager (Ubuntu VM), add the agent manually using the command: ```sudo /var/ossec/bin/manage_agents```
Inside manage_agents:

•	Press A to add an agent.

•	Enter a name (example: debian-agent).

•	Enter the agent IP address.

•	The default group is fine unless you want a custom one.

You will get a Key after creation. Copy the Key.
![Manage Agent screen](img\pic7.png)

Part 2: On the Agent (Debian VM), import the Key using the command 
```
sudo /var/ossec/bin/agent-auth -m MANAGER_IP_ADDRESS -p 1515 -k <PASTE_YOUR_KEY_HERE>
```
![Key importing](img\pic8.png)

In this step, the Wazuh agent on the Debian virtual machine is being enrolled with the Wazuh Manager using the agent-auth command. The terminal shows the agent initiating a secure connection to the manager at IP address 192.168.0.225 on port 1515, using a provided pre-shared registration key. This method avoids the need for password-based authentication and relies on key-based trust to ensure secure communication. The agent identifies itself with the hostname "vbox" and waits for a response from the manager. Upon successful verification of the key, the manager confirms the registration by returning a "Valid key received" message. This enrollment is essential because it establishes a trusted link between the agent and the manager, allowing the agent to begin sending security events and system logs for monitoring. Without this step, the manager would reject data from the agent, as only registered agents are authorized to communicate with it.

### Step 5: Verifying connection between the manager and the agent

To verify that the Wazuh agent has been successfully installed and registered with the Wazuh manager, we can use the agent_control utility provided by Wazuh. By running the command ```sudo /var/ossec/bin/agent_control -l``` on the manager machine, we can list all agents currently registered with the server. This command displays important information such as the agent ID, agent name, IP address, connection status, and last keepalive time, confirming that the agent is active and communicating properly with the manager.
![Key importing](img\pic9.png)

On minimal or custom Debian installations, particularly on virtual machines like VirtualBox, the traditional system log service *rsyslog* is often missing, resulting in the absence of critical log files such as /var/log/auth.log. Without this file, authentication events—including SSH login failures—are not captured in a format that security monitoring tools like Wazuh can process. Although modern systems may log authentication attempts within journald accessible via journalctl, Wazuh agents by default monitor traditional log files rather than querying journald directly.

To resolve this, rsyslog must be installed and configured. Installing rsyslog (```sudo apt update && sudo apt install rsyslog```) and enabling its service (```sudo systemctl enable --now rsyslog```) ensures that authentication events are correctly written to /var/log/auth.log. Once rsyslog is active, SSH login attempts, both successful and failed, are properly logged. 
![Installing rsyslog](img\pic10.png)
![Enabling rsyslog](img\pic11.png)

Wazuh agents configured to monitor /var/log/auth.log can then detect and alert on events such as invalid user logins (Rule 5710) and multiple failed authentication attempts (Rule 2502), restoring full visibility into SSH activity for security operations. 
We can perform a deliberate SSH login failure by attempting to SSH to localhost with an invalid username: ```ssh wronguser@localhost```. Enter any random password to trigger authentication logs. 
![ssh command](img\pic12.png)

The logs can be monitored using the command sudo tail -f /var/ossec/logs/alerts/alerts.json. on the Wazuh Manager machine.

![Wazuh tail logs](img\pic13.png)

Restarting the Wazuh agent (sudo systemctl restart wazuh-agent) ensures the agent picks up the new log sources, and alerts can be validated by tailing /var/ossec/logs/alerts/alerts.json on the Wazuh Manager.
Similarly, we can configure multiple agents as needed with the Wazuh manager by following the steps outlined above. 


### Step 6:  Wazuh Platform Setup: Manager, Indexer, and Dashboard

To build a complete security monitoring and threat detection platform, we will extend the existing Wazuh Manager setup by installing the Wazuh Indexer and the Wazuh Dashboard, thereby completing the Wazuh All-in-One architecture. The Wazuh Manager acts as the core backend component responsible for receiving and processing security events from the agents. The Wazuh Indexer, a customised and optimised fork of OpenSearch, is responsible for storing and indexing event data efficiently. The Wazuh Dashboard provides an intuitive web-based graphical user interface (GUI) to visualise alerts, manage security rules, monitor agent statuses, and perform investigations in real-time. By setting up the full Wazuh Platform, users can achieve seamless log management, advanced threat detection, and centralised security event analysis without relying on external components such as Elasticsearch, Logstash, or Kibana. This self-contained setup enhances system simplicity, reduces operational overhead, and improves integration between core platform services.

:::note **System Requirements**

Before proceeding with the installation, ensuring that the underlying system can support all components of the Wazuh Platform efficiently is critical. The Ubuntu VM intended for deployment should meet the minimum requirements: at least 2 virtual CPUs, 4 GB of RAM (although 6–8 GB is recommended for better performance), and 20 GB or more of available disk space. These resources are necessary to handle the simultaneous operation of the Wazuh Manager, Wazuh Indexer, and Wazuh Dashboard services, particularly as the volume of log ingestion and alert generation increases. Additionally, the server must have a stable internet connection to fetch packages from official Wazuh repositories, and administrative privileges (sudo access) are required for software installation and configuration.
:::

Pre-requisite: Since we have already set up the Wazuh manager, we will not be adding the Wazuh repository again, but if you are not sure, you can always add the official repository and import its GPG signing key using the command: 
```
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --dearmor -o /usr/share/keyrings/wazuh-archive-keyring.gpg
```

```
echo "deb [signed-by=/usr/share/keyrings/wazuh-archive-keyring.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list

sudo apt update
```

1.	First, install the required Java 17 runtime environment: sudo apt install openjdk-17-jdk -y
If you already have Java installed or want to check if it’s installed, then you can use the command `java -version`
![Checking java installation](img\pic14.png)

2.	Download the official installation assistant:
```
curl -sO https://packages.wazuh.com/4.12/wazuh-install.sh

curl -sO https://packages.wazuh.com/4.12/config.yml
```
![Downloading the official installation assistant](img\pic15.png)

3.	Edit config.yml using the command *nano config.yml* and find the nodes section and enter the IP address of your Ubuntu VM in all the fields where your Ubuntu IP address is mentioned.
4.	Generate SSL certs and passwords using the command ```bash wazuh-install.sh --generate-config-files```
![Generate SSL certs and passwords](img\pic16.png)
5.	Install Wazuh Indexer using Assisted Method: ```bash wazuh-install.sh --wazuh-indexer node-1```
![Install Wazuh Indexer using Assisted Method](img\pic17.png)
6.	Initialise Wazuh Cluster (Start Security) with the command ```bash wazuh-install.sh --start-cluster```
![Initialise Wazuh Cluster](img\pic18.png)
This automatically runs securityadmin, sets up passwords, and cluster keys
7.	Get the admin password: 
```
tar -axf wazuh-install-files.tar wazuh-install-files/wazuh-passwords.txt -O | grep -P "'admin'" -A 1
```
8.	Then test: 
```
curl -k -u admin:<your-found-password> https://<your-ubuntu-ip-address>:9200
```
![Testing](img\pic19.png)
9.	We will now install the Wazuh dashboard, which can be done using the command 
```
bash wazuh-install.sh --wazuh-dashboard dashboard
```
dashboard matches the dashboard name you wrote in *config.yml (dashboard: section)*. This will install the full Wazuh Dashboard, SSL certs, Nginx proxy, everything.
![Wazuh Dashboard installation](img\pic20.png)
*Make a note of the username and password. These are the credentials that we will be using to log in to the dashboard.*
10.	After Installation, start the Cluster: ```bash wazuh-install.sh --start-cluster```
This connects the Wazuh Indexer, Wazuh Server, and Dashboard securely.
![Start dashboard cluser](img\pic21.png)
The Wazuh Dashboard can now be accessed using ```https://<your-server-ip>/```
For the first time, we will see that a connection isn’t a private message being displayed in the browser, which is expected.
![Private connection warning screen](img\pic22.png)
Click on **Advanced**, and then continue to Ubuntu Manager IP Address
![Continue from the warning screen](img\pic23.png)
The wazuh dashboard will now load, where we can log in with the set of credentials that we had noted down earlier during the installation.
![Wazuh screen](img\pic24.png)

Another way to install **all 3 (Wazuh – manager, indexer, and dashboard) together** would be using the command: 
```
bash wazuh-install.sh -a
```

The command bash wazuh-install.sh -a runs the Wazuh installation script with the -a flag, which typically initiates an automated installation of the Wazuh components, including the manager, indexer, and dashboard, in a single deployment. While this approach simplifies setup, installing these components separately allows for better scalability, performance optimisation, and fault isolation. By configuring the manager, indexer, and dashboard independently, administrators gain greater flexibility to fine-tune each service according to workload demands, improving resource allocation and system stability. Additionally, separating these components facilitates troubleshooting and maintenance, reducing the risk of a single point of failure affecting the entire system. This modular installation also enhances security by enabling stricter access controls for each service.
![All in one wazuh installation](img\pic25.png)

Once everything is installed, you should see the status like this. The command to check the status of all 3 together would be 
```
sudo systemctl status wazuh-manager  wazuh-dashboard wazuh-indexer
```
*(They can be in any order in the above command)*

![Status of all wazuh related component running](img\pic26.png)

Once everything is set up and connected, we can check the connection status between the Wazuh Manager and its **agent** on the agents page in Wazuh.
![Wazuh agent page](img\pic27.png)








