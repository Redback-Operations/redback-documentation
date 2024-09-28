---
sidebar_position: 3
---

# Ubuntu Server Optional Services

:::info
**Document Creation:** 20 September 2024.  
**Last Edited:** 20 September 2024.  
**Authors:** Drew Baker.  
**Effective Date:** 20 September 2024.  
**Expiry Date:** 20 September 2025.  
:::

## Introduction
This document outlines several optional services that can be installed and configured to enhance the functionality, security, and remote accessibility of an Ubuntu server. It covers secure access methods such as SSH, secure file transfer through FTP, network management utilities, SSL encryption, and VirtualBox network settings. Each service is critical for managing and securing the server in a production environment.

## SSH Service (OpenSSH)
The **OpenSSH** package is essential for secure remote access to the server. SSH (Secure Shell) allows administrators to connect, execute commands, and manage files over an encrypted connection, ensuring that communication is secure from potential eavesdropping.

- **Commands used:**
```bash
sudo systemctl status ssh
sudo ufw allow ssh
```
Once installed and configured, SSH allows administrators to securely manage the server for tasks such as installing software, configuring services, and performing remote administration.

## net-tools
The **net-tools** package provides essential network management utilities such as **`ifconfig`**, which displays the current state of the network interfaces. It is used to view and manage IP addresses, subnet masks, and other configuration details critical to network services.
- **Commands used:**
```bash
sudo apt install net-tools
ifconfig
```
This tool is particularly useful for configuring networking on the server, especially when working with virtual machines or diagnosing network connectivity issues.

## FTP Service (vsftpd)
The **vsftpd** package (Very Secure FTP Daemon) is installed to provide **FTP** (File Transfer Protocol) services. FTP allows users to securely upload and download files between the server and remote clients. Additionally, **SSL certificates** are installed to secure FTP traffic, enabling FTPS (FTP Secure), which encrypts file transfers to prevent unauthorized access to sensitive data.

- **Commands used:**
```bash
sudo apt install vsftpd
sudo ufw allow 20/tcp && sudo ufw allow 21/tcp
```
Once installed, **vsftpd** provides secure and encrypted file transfer capabilities, which are essential for remote users who need to manage files on the server.

## SSL Certificates
During the installation process, the **ssl-cert** package was installed to enable **SSL/TLS** for secure communication. SSL certificates are crucial for encrypting data exchanged between the server and clients, especially when dealing with sensitive information such as login credentials and file transfers over FTP.

- **Command used:**
```bash
sudo apt install ssl-cert
```
By enabling SSL, services like FTP and web servers can encrypt traffic, preventing eavesdropping and data tampering during transmissions.

## VirtualBox Network Configuration
Though not a software package, VirtualBox network settings are critical for configuring virtual machines on the **Ubuntu Server Workspace**. The network adapter was set to **Bridged Mode**, which allows the VM to obtain an IP address and be accessible on the local network. Additionally, **Promiscuous Mode** was set to **Allow All**, enabling network monitoring and packet capturing from the virtual machine.
- **Settings applied:**
- Adapter 1: **Bridged Adapter**
- Promiscuous Mode: **Allow All**
- MAC Address: Configured automatically
These network configurations are vital for providing services such as SSH and FTP, ensuring the VM has proper network connectivity and can communicate externally.

## Checking Ports and Services
To ensure that the LDAP service (and other services like SSH and FTP) are running correctly and listening on the appropriate ports, two utilities were used: **lsof** and **netstat**.

### Checking LDAP Ports with `lsof`
The **`lsof`** command lists open files and the processes that are using them, which is helpful for checking which ports services like **slapd** (LDAP daemon) are using.

- **Command used:**
```bash
sudo lsof -i -P -n | grep slapd
```
This command shows that **slapd** is listening on **port 389** (the default LDAP port) for both IPv4 and IPv6 connections, confirming that the LDAP service is running and ready to accept connections.

### Checking Open Ports with `netstat`
The **`netstat`** command displays active connections, routing tables, interface statistics, and open ports. It can be used to verify that the necessary ports are open and listening for connections.
- **Command used:**

```bash
sudo netstat -tuln | grep :389
```
This output confirms that **port 389** is open and listening for both IPv4 and IPv6 traffic, validating that the LDAP service is available and functional.
