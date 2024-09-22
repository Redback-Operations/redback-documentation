---
sidebar_position: 1
---

# Project RedOps: LDAP Ubuntu Server 

:::info
**Document Creation:** 17 September, 2024. **Last Edited:** 19 September, 2024. **Authors:** Drew Baker.
<br></br>**Effective Date:** 18 September 2024. **Expiry Date:** 19 September 2025.
:::

## Introduction
Over the course of the trimester my contribution for this unit largely comprised of creating an on prem environment to replicate the functionality of Microsoft's AD. After a couple of viability assessments for alternatives and following direction from the company department lead at the time the decision was made to utilise OpenLDAP. To achieve this I elected to implement this in Ubuntu Server 22.04, while this lacks a GUI making it a little challenging at times to work with this decision was made due to it`s light-weight nature. In this Docusaurus page I aim to answer any question you may have regarding setting this up yourselves or where to go next with this.

## Ubuntu Environment Setup
To configure the environment to run the `RedOps Ubuntu Server` system I would recommend configuring this VM on a separate system largely for convenience. In my deployment I used a soon to be retired Windows 10 Pro host machine where I had added a registry key to execute a script which would start the VM on launch. If you would like to do the same please follow the following steps:

1. Please download the `Ubuntu Server Workspace` OVA file from the `Cyber Security Team > 2024 Trimester 2` folder in the company Sharepoint. 
    :::important
    **Note the system login credentials are:**
    **USER:** `rboadmin`
    **PASS:** `admin`
    :::

3. Once you have imported the appliance double check your network adapter settings to ensure that you are have either connected to the pfSense `internal` adapter or are using a `bridged` adapter. After successfully booting the machine, please sign in and run the following:
    ```bash
    sudo apt update && sudo apt upgrade
    ```

4. Before continuing please ensure that the systems password has been changed from `admin` and shared it with your team along with your IP and chosen external port (provided that the system will be port forwarded).
    > To check your IP, run:  
   ```bash
   curl ifconfig.me
   ```

## Windows Host Environment Setup
1. To enable it so the rest of your team is able to SSH into the server to tinker and work on their own individual projects you will need to port forward the devices IP in your router`s configuration (not pfSense) port 21 and 22 (FTP and SSH). 
    > **Please ensure that your ISP doesn`t use CGNAT or that it has been disabled as this will cause implementation issues.**

2. (Optional but strongly recommended) To set it up to automatically launch the VM on host system start you`ll need to create a script. Open your text editor of choice and insert the following command string:
    ```
    "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" startvm "Ubuntu Server Workspace"
    ```
Saving this as a `.bat` file will allow us to point the registry key to the command on start up via the `RUN` registry.
> Navigate to the `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` registry and add a string with the file path to the `.bat` file as the value.

## Learning opportunities
By working on this setup, you’ll gain knowledge in various areas:
- Get comfortable with Ubuntu’s command-line interface (CLI).
- Explore Microsoft Server Active Directory (AD) and Entra ID.
- Investigate key topics like:
  - Kerberos
  - OpenSSH
  - OpenLDAP

## Possible tasks and contributions
Here are some ways you can further enhance the LDAP setup:
- Integrate LDAP with Kerberos using SASL.
- Implement encryption for LDAP user credentials.
- Modify LDAP Access Control Lists (ACLs) to improve security.
- Add SSL to LDAP for encrypted communication.
- Expand the pfSense Snort configuration for improved network protection.

## Existing Documentation
The following have both been written in Markdown and should be available in the sidebar.
- [Ubuntu Server LDAP Configuration](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Ubuntu%20Server/LDAP%20Configuration)
- [Ubuntu Server Optional Services](https://redback-operations.github.io/redback-documentation/docs/cybersecurity/Ubuntu%20Server/Optional%20Services)

## Useful Links
- [Ubuntu install and configure LDAP](https://ubuntu.com/server/docs/install-and-configure-ldap)
- [LDAP vs. Kerberos](https://www.geeksforgeeks.org/difference-between-ldap-and-kerberos/)
- [IBM LDAP utilities](https://www.ibm.com/docs/en/zos/2.5.0?topic=utilities-ldapmodify-ldapadd)
- [LDAP over SSL](https://www.server-world.info/en/note?os=Ubuntu_22.04&p=openldap&f=4)
