---
sidebar_position: 2
---

# Ubuntu Server LDAP Configuration

:::info
**Document Creation:** 16 September, 2024. **Last Edited:** 18 September, 2024. **Authors:** Drew Baker.
<br></br>**Effective Date:** 18 September 2024. **Expiry Date:** 18 September 2025.
:::

## Introduction
This document provides detailed instructions for configuring an LDAP directory on an Ubuntu server. It is designed to help users understand the basics of LDAP, its practical uses, and how to contribute to the company’s ongoing development efforts. The aim is to give users a working understanding of LDAP configurations so they can expand upon the system and apply it to their projects or initiatives.

## LDAP Setup
To set up the `RedOps Ubuntu Server` with LDAP, it's recommended to deploy this virtual machine (VM) on a separate system for convenience. For example, in my deployment, I used a Windows 10 Pro host that is scheduled for retirement, with an added registry key to auto-launch the VM at startup. If you`d like to replicate this setup, follow these steps:

1. Download the `Ubuntu Server Workspace` OVA file from the `Cyber Security Team > 2024 Trimester 2` folder on the company SharePoint.
> The system credintials should have modified from the defualt **USER:** `rboadmin` **PASS:** `admin`
:::important
**Note the LDAP login credentials are:**
**USER:** `rbosys`
**PASS:** `admin`
:::

2. After importing the appliance and ensuring your network adapter settings are correct, boot the machine, sign in, and run the following commands to update the system:
```bash
sudo apt update
sudo apt upgrade
```
   
3. Install LDAP-related packages:
```bash
sudo apt install slapd ldap-utils
sudo dpkg-reconfigure slapd
```

4. Manage the `slapd` service using the following commands:
```bash
sudo systemctl start slapd
sudo systemctl status slapd
sudo systemctl stop slapd
sudo systemctl restart slapd
```

5. Change the default password from `admin` and share it, along with the server’s IP address and chosen external port (if port forwarding is enabled), with your team.
> To check your IP, run:  
```bash
curl ifconfig.me
```

6. Perform a basic LDAP search to verify the setup:
```bash
ldapsearch -x -LLL -H ldap:/// -b dc=redbackops,dc=org,dc=au
```
> or
```bash
ldapsearch -Q -LLL -Y EXTERNAL -H ldap:///
```


## LDAP Directory Structure and Entries
The `/etc/ldap/ldap.conf` has been modified to allow easier use of the LDAP utilities, 
To add some initial LDAP entries, create a base structure for People and Groups as follows:

1. Create the base structure in an LDIF file (e.g., `base.ldif`):
```bash
dn: ou=People,dc=redbackops,dc=org,dc=au
objectClass: organizationalUnit
ou: People

dn: ou=Groups,dc=redbackops,dc=org,dc=au
objectClass: organizationalUnit
ou: Groups
```

2. Add these entries to the LDAP directory:
```bash
sudo ldapadd -x -D cn=admin,dc=redbackops,dc=org,dc=au -W -f base.ldif
```

3. Add a user (`jdoe`) and a group (`developers`) in an LDIF file (e.g., `add_entries.ldif`):
```bash
dn: uid=jdoe,ou=People,,dc=redbackops,dc=org,dc=au
objectClass: inetOrgPerson
uid: jdoe
sn: Doe
givenName: John
cn: John Doe
displayName: John Doe
userPassword: secret
mail: jdoe@example.com

dn: cn=developers,ou=Groups,dc=redbackops,dc=org,dc=au
objectClass: posixGroup
cn: developers
gidNumber: 5000
memberUid: jdoe
```

4. Add the entries to the LDAP directory:
```bash
sudo ldapadd -x -D cn=admin,dc=redbackops,dc=org,dc=au -W -f add_entries.ldif
```

5. Verify that the user `jdoe` was added successfully:
```bash
ldapsearch -x -LLL -b dc=redbackops,dc=org,dc=au `uid=jdoe`
```
