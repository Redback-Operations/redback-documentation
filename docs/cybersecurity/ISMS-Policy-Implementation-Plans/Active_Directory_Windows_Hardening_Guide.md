---
sidebar_position: 99
---

**Last updated by:** Kaleb, **Last updated on:** 24/09/2024


**Last updated by:** Kaleb, **Last updated on:** 24/09/2024


**Last updated by:** Kaleb, **Last updated on:** 24/09/2024


# Active Directory Windows

# 1. Introduction

## 1.1. Purpose of this Document
This document is intended to guide administrators to secure Active Directory Windows Server 2016. All administrators should use this document for secure configuration.

## 1.2. Instructions

### 1.2.1. How to Use This Document
The security settings described in this document shall be configured on the Active Directory Windows Server 2016 by the administrators. All settings can only be done with administrative privileges. 

It is strongly recommended that the settings be tested in the staging environment before applying them in the production environment. It is further recommended that the administrators of the Active Directory Windows Server 2016 make note of the original values while changing the settings. For each setting, a detailed description is given, followed by the impact if the setting is not configured and the solution to fix it.

Implementing changes on production systems without first testing them on replica test systems may adversely affect the system/application and may cause it to stop working.



# 2. Configuration Document: Active Directory



## 2.1. Account Polices 

### 2.1.1. Password Policy & Account Lockout Policy 

#### Control Statement 

Password policies help administrator enforce the strength of passwords that users can set. Password policy is required to control user password characteristics including minimum length, maximum length and password aging. To help prevent password-based attacks from being successful, strong password and account lockout settings need to be configured.  

#### Risk/Impact 

The longer a user uses the same password, the greater the chance that an attacker can determine the password through brute force attacks.  Risk Rating 

High 

#### Implementation Steps 

Configure a strong Password and Account policy, as suggested in below table. To configure the policy, 

Press Windows key > type Run and type gpedit.msc or rsop.msc. 

Expand Computer Configuration > Windows Settings > Security Settings > Account Policy > Password Policy or Account Lockout Policy container and configure the settings as suggested in Appendix 1. 

  

 

## 2.2. Local Polices 

### 2.2.1. User Rights Assignments 

Control Statement 

The user rights settings determine which users or groups have logon rights and other privileges on the server. 

#### Risk/Impact 

If an account is given this right the user of the account may create an application that calls into Credential Manager and is returned the credentials for another user. 

Risk Rating 

Medium 

#### Implementation Steps 

Ensure user rights are configured as suggested in below table. To configure Security Options, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration > Windows Settings > Security Settings > Local Policies > User Rights Assignment container and configure the settings with the values as suggested in Appendix 2. 

### 2.2.2. Security Options 

#### Control Statement 

The security option settings include multiple settings that enable or disable security settings for the server, such as digital signing of data, Administrator and guest account names, floppy drive and CD ROM access, driver installation and logon prompts. 

#### Risk/Impact 

In some organizations, it can be a daunting management challenge to maintain a regular schedule for periodic password changes for local accounts. Therefore, you may want to disable the built-in Administrator account instead of relying on regular password changes to protect it from attack. 

Risk Rating 

High 

#### Implementation Steps 

Ensure security options are enabled as recommended in below table. To configure security options settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options and configure the settings with the values as suggested in Appendix 3. 

 

 

 

## 2.3. Windows Firewall with Advanced  

### 2.3.1. Public Profile 

#### Control Statement 

Windows Firewall offers three firewall profiles: domain, private and public. The default profile is the public profile, which is used to designate public networks such as Wi-Fi hotspots at coffee shops, airports, and other locations 

Risk/Impact 

Weak controls can result into unauthorized access to server and network 

Risk Rating 

Low 

#### Implementation Steps 

Ensure the profile parameters must be configured as per ORGANIZATION Public Profile policy. To configure these settings on standalone server:  

Click Start > Run and type Gpedit.msc  

Expand Computer Configuration\Policies\Windows Settings\Security Settings\Windows Firewall with Advanced Security\Windows Firewall with Advanced Security\Windows Firewall Properties\Private Profile and configure the settings with the values as suggested in Appendix 4. 

### 2.3.2. Private Profile 

#### Control Statement 

Windows Firewall offers three firewall profiles: domain, private and public. The private profile is a user-assigned profile and is used to designate private or home networks. 

Risk/Impact 

Weak controls can result into unauthorized access to server and network 

Risk Rating 

Low 

#### Implementation Steps 

Ensure the profile parameters must be configured as per ORGANIZATION Private Profile policy. To configure these settings on standalone server:  

Click Start > Run and type Gpedit.msc  

Expand Computer Configuration\Policies\Windows Settings\Security Settings\Windows Firewall with Advanced Security\Windows Firewall with Advanced Security\Windows Firewall Properties\Private Profile and configure the settings with the values as suggested in Appendix 4. 

### 2.3.3. Domain Profile 

#### Control Statement 

Windows Firewall offers three firewall profiles: domain, private and public. The domain profile applies to networks where the host system can authenticate to a domain controller.  Risk/Impact 

Weak controls can result into unauthorized access to server and network 

Risk Rating 

Low 

#### Implementation Steps 

Ensure the profile parameters must be configured as per ORGANIZATION Domain Profile policy. To configure these settings on standalone server:  

Click Start > Run and type Gpedit.msc  

Expand Computer Configuration\Policies\Windows Settings\Security Settings\Windows Firewall with Advanced Security\Windows Firewall with Advanced Security\Windows Firewall Properties\Private Profile and configure the settings with the values as suggested in Appendix 4. 

 	 

## 2.4. Auditing, Logging and Monitoring 

### 2.4.1. Account Policies 

#### Control Statement 

The audit entry shows an event or action performed, the user account and the date and time of the action. Security auditing is important for any enterprise server, as audit logs can provide vital information about any security breach. 

#### Risk/Impact 

Malicious activity may not be detected if sufficient audit logs are not enabled. Early warning towards attempts at malicious access will go undetected. Risk Rating 

High 

#### Implementation Steps 

Ensure auditing is enabled as recommended in below table. To configure audit settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies and configure the settings with the values as suggested in Appendix 5. 

### 2.4.2. Event log Sizes 

#### Control Statement 

Event viewer maintains logs about program, security and server events. Event viewer can be used to view and manage the event logs, gather information about hardware and software problems and monitor windows security events. 

#### Risk/Impact 

Critical logs may get overwritten in the absence of sufficient event viewer file size. Default value for the log is 

20MB 

Risk Rating 

Medium 

#### Implementation Steps 

Ensure that at least 102400 KB (100MB) size is allocated for Application, Security and Server Event Viewer log files. To configure log file size, 

Click Start > Run and type eventvwr.msc. 

Expand Windows Logs > Right click on Application, choose the Properties and set the Maximum Log Size to any size = or > than 100MB. 

Right click on Security, choose the Properties and set the Maximum Log Size to any size = or > than 100MB. 

Right click on Server, choose the Properties and set the Maximum Log Size to any size = or > than 100MB. 

### 2.4.3. Permission on Event logs 

#### Control Statement 

Event viewer holds the System, Security and Application logs for a Windows server. Unauthorized users can be given access to event logs, by default Guest has read access to event logs. 

#### Risk/Impact 

Unauthorized access to event logs may allow users to get important information. Risk Rating 

Low 

#### Implementation Steps 

To configure permissions on event logs navigate to the following file, 

C:\windows\System32\winevt\Application.evtx. 

Right click and go to Permissions and remove invalid users. Similarly for \security.evtx and \system.evtx 

Ensure that Guest access to event logs is not allowed. To configure the registry key, 

Click Start > Run and type regedit. Navigate to the following registry hive, 

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\SYSTEM 

In the sub keys check Application for the DWORD RestrictGuestAccess. Double click on 

RestrictGuestAccess and assign value 1 to restrict guest access. If the DWORD RestrictGuestAccess does not exist it needs to be created. Right click and click New and then click DWORD. Rename the new DWORD to RestrictGuestAccess. Double click on RestrictGuestAccess and assign value of 1 to the RestrictGuestAccess DWORD. 

Follow the same procedure for Security and Application sub keys. 

### 2.4.4. Auditing of sensitive system and application files and directories should be enabled for servers 

#### Control Statement 

Enable Windows native auditing feature on the following sensitive system and application files and directories: 

%systemroot%\ 

%systemroot%\system32 

%systemroot%\system32\drivers 

%systemroot%\system32\config 

%systemroot%\system32\spool 

The recommended guidelines state to audit the following actions for the Everyone group: 

Create Files / Write Data - Failure 

Create Folders / Append Data - Failure 

Delete Subfolders and Files - Failure 

Delete - Success and Failure 

Change Permissions - Failure 

Take Ownership - Failure Risk/Impact 

Auditing access to sensitive system and application files and directories increases the chance unauthorized access to the system will be detected and terminated in a timely manner. Risk Rating 

Medium 

#### Implementation Steps 

Enable Windows native auditing feature on the directories listed in the Technical Control Procedure. 

Open Windows Explorer and browse to the appropriate directory; 

Locate the folder/file, right click it, and select Properties from the drop down menu; 

Select the Security tab; 

Click the Advanced button; 

Select the Auditing tab; 

Click the Continue button if User Account Control is enabled; 

Click the Add button then enter the name of the user or group object whose actions to audit; 

Click OK and click the appropriate actions and respective success and failure checkboxes; 

Click OK three times to confirm changes and close the window; and 10) Repeat steps 2 through 9 for each of the directories listed. 

### 2.4.5. Auditing of sensitive system registry keys should be enabled on servers 

#### Control Statement 

Enable Windows native auditing feature on all sensitive system registry keys for servers. These sensitive keys may include: 

HKLM\SYSTEM HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\PerfLib 

HKLM\Software\Microsoft\WindowsNT\CurrentVersion\Winlogon 

HKLM\SYSTEM\CurrentControlSet\Control\Lsa 

HKLM\SYSTEM\CurrentControlSet\Control\SecurePipeServers 

HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs 

HKLM\SYSTEM\CurrentControlSet\Control\SecurePipeServers\winreg\AllowedPaths 

HKLM\SYSTEM\CurrentControlSet\Services\LanManServer\Shares 

HKLM\SYSTEM\CurrentControlSet\Services\UPS HKEY_USERS\.default 

HKLM\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\ValidCommunities 

HKLM\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\PermittedManagers 

HKLM\SOFTWARE\Policies\SNMP\Parameters\ValidCommunities 

HKLM\SOFTWARE\Policies\SNMP\Parameters\PermittedManagers 

HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run 

HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce 

HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx HKCR (all subkeys) 

HKLM\SOFTWARE HKLM\SOFTWARE\MICROSOFT\Rpc (and all subkeys) 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\ 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\AeDebug 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\Compatibility 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\Drivers 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\Embedding 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\Fonts 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\FontSubstitutes 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\FontDrivers 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\FontMapper 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\GRE_Initialize 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\MCI 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\MCIExtensions 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\Ports (all subkeys) 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\Type1Installer 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\ProfileList 

HKLM\SOFTWARE\MICROSOFT\WindowsNT\CurrentVersion\WOW (all subkeys) 

The recommended guidelines state to audit the following actions for the Everyone group: 

Set Value - Failure 

Create Subkey - Failure 

Delete - Success and Failure 

#### Risk/Impact 

Auditing access to sensitive system registry keys increases the chance that unauthorized access to the system will be detected and terminated in a timely manner. 

 

Risk Rating 

Medium 

#### Implementation Steps 

Enable Windows native auditing feature on all sensitive system registry keys for sensitive servers. 

Open regedit; 

Locate the key, right click it, and select Permissions from the drop down menu; 

Select the Security tab; 

Click the Advanced button; 

Select the Auditing tab; 

Click the Continue button if User Account Control is enabled; 

Click the Add button then enter the name of the user or group object whose actions to audit; 

Click OK and click the appropriate actions and respective success and failure checkboxes; 

Click OK three times to confirm changes and close the window; and 

Repeat steps 2 through 9 for each of the keys listed. 

 

 



 

## 2.5. Administrative Templates (Computer) 

### 2.5.1. Control Panel 

Control Statement 

This section contains recommendations for configuring lock screen settings 

Risk/Impact 

Insecure personalization settings may lead to unauthorized access. 

Risk Rating 

High 

#### Implementation Steps 

Ensure security options are enabled as recommended in below table. To configure security options settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration\Administrative Templates\Control Panel\Personalization and configure the settings with the values as suggested in Appendix 6. 

### 2.5.2. MSS (Legacy) 

Control Statement 

Ensure the Microsoft security settings should be configured appropriately. 

Risk/Impact 

Weak controls can result into unauthorized access to server and network. 

Risk Rating 

High 

#### Implementation Steps 

Ensure security options are enabled as recommended in below table. To configure security options settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration\Administrative Templates\MSS (Legacy) and configure the settings with the values as suggested in Appendix 6. 

Note: This Group Policy path does not exist by default. An additional Group Policy template (MSSlegacy.admx/adml) is required - it is included with Microsoft Security Compliance Manager (SCM) 

 	 

### 2.5.3. Network 

Control Statement 

This section contains recommendations for network settings. 

Risk/Impact 

Insecure network settings may leads to information leak. 

Risk Rating 

High 

#### Implementation Steps 

Ensure security options are enabled as recommended in below table. To configure security options settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration\Administrative Templates\Network\ and configure the settings with the values as suggested in Appendix 6. 

Note: This change does not take effect until the computer has been restarted. Note #2: Although Microsoft does not provide an ADMX template to configure this registry value, a custom .ADM template (Set-NetBIOS-nodetype-KB160177.adm) needs to be implemented. Be aware though that simply turning off the group policy setting in the .ADM template will not "undo" the change once applied. Instead, the opposite setting must be applied to change the registry value to the opposite state. 

### 2.5.4. System 

Control Statement 

This section contains recommendations for System settings. 

Risk/Impact 

Insecure network settings may leads to information leak or data loss. 

Risk Rating 

High 

#### Implementation Steps 

Ensure security options are enabled as recommended in below table. To configure security options settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration\Administrative Templates\Network\ and configure the settings with the values as suggested in Appendix 6. 

### 2.5.5. Windows Component 

Control Statement 

This section contains recommendations for Windows Component settings. 

#### Risk/Impact 

As to mitigate the users of a system could accidentally share sensitive data with other users on the same system. 

Risk Rating 

High 

#### Implementation Steps 

Ensure security options are enabled as recommended in below table. To configure security options settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration\Administrative Templates\Windows Components and configure the settings with the values as suggested in Appendix 6. 

### 2.5.6. LAPS 

#### Control Statement 

This section contains recommendations for configuring Microsoft Local Administrator Password Solution Risk/Impact 

When installed and registered properly, AdmPwd.dll takes no action unless given appropriate GPO commands during Group Policy refresh. Risk Rating 

High 

#### Implementation Steps 

Ensure security options are enabled as recommended in below table. To configure security options settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration\Administrative Templates\LAPS and configure the settings with the values as suggested in Appendix 6. 

Note: This Group Policy path does not exist by default. An additional Group Policy template 

(AdmPwd.admx/adml) is required - it is included with Microsoft Local Administrator Password Solution (LAPS).  

### 2.5.7. SCM: Pass the Hash Mitigations 

Control Statement 

This section contains recommendations for mitigating Pass-the-Hash attacks. 

#### Risk/Impact 

Local accounts are at high risk for credential theft when the same account and password is configured on multiple systems. Ensuring this policy is Enabled significantly reduces that risk. 

 

Risk Rating 

High 

#### Implementation Steps 

Ensure security options are enabled as recommended in below table. To configure security options settings, 

Press Windows key > type Run and type gpedit.msc. 

Expand Computer Configuration\Administrative Templates\SCM: and configure the settings with the values as suggested in Appendix 6. 

Note:  

This Group Policy path does not exist by default. An additional Group Policy template (PtH.admx/adml) is required - it is included with Microsoft Security Compliance Manager (SCM). 

 

 

## 2.6. Encryption 

### 2.6.1. Disable weak encryption protocol 

#### Control Statement 

If configured to require client side certificates, TLS can also play a role in client authentication to the server.  TLS also provides two additional benefits that are commonly overlooked; integrity guarantees and replay prevention. A TLS stream of communication contains built-in controls to prevent tampering with any portion of the encrypted data. In addition, controls are also built-in to prevent a captured stream of TLS data from being replayed at a later time. 

 

TLS provides the above guarantees to data during transmission. TLS does not offer any of these security benefits to data that is at rest. Therefore appropriate security controls must be added to protect data while at rest within the application or within data stores. 

 

Risk/Impact 

An attacker may try to break the integrity of data and also sniff the sensitive information. 

 

Risk Rating 

Medium 

#### Implementation Steps 

To Ensure the SSL 2.0, SSL 3.0 protocol must be disabled on the server and make sure that the stronger TLS protocols are used, follow these instructions to disable Weak SSL protocols: 

Click Start, click Run, type regedit, and then click OK. 

In Registry Editor, locate the following registry key/folder: 

 HKey_Local_Machine\System\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols 3. Right-click on the SSL 2.0 folder and select New and then click Key. Name the new folder Server. 

Inside the Server folder, click the Edit menu, select New, and click DWORD (32-bit) Value. 

Enter Enabled as the name and hit Enter. 

Ensure that it shows 0x00000000 (0) under the Data column (it should by default). If it doesn't, right-click and select Modify and enter 0 as the Value data. 

Now to disable SSL 3.0, right-click on the SSL 3.0 folder and select New and then click Key. Name the new folder Server. 

Inside the Server folder, click the Edit menu, select New, and click DWORD (32-bit) Value. 

Enter Enabled as the name and hit Enter. 

### 2.6.2. Enable TLS 1.2 and above protocol  

#### Control Statement 

If configured to require client side certificates, TLS can also play a role in client authentication to the server.  TLS also provides two additional benefits that are commonly overlooked; integrity guarantees and replay prevention. A TLS stream of communication contains built-in controls to prevent tampering with any portion of the encrypted data. In addition, controls are also built-in to prevent a captured stream of TLS data from being replayed at a later time.  

 

TLS provides the above guarantees to data during transmission. TLS does not offer any of these security benefits to data that is at rest. Therefore appropriate security controls must be added to protect data while at rest within the application or within data stores. 

 

 

Risk/Impact 

An attacker may try to break the integrity of data and also sniff the sensitive information. 

 

Risk Rating 

Medium 

#### Implementation Steps 

The TLS 1.2 & above protocol must be enabled on the server and make sure that the stronger TLS protocols are used, follow these instructions to enable TLS protocols: 

Click Start, click Run, type regedit, and then click OK. 

In Registry Editor, locate the following registry key/folder: 

 HKey_Local_Machine\System\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols 3. Create TLS 1.2 folder and then click Key. Name the new folder Server. 

Inside the Server folder, click the Edit menu, select New, and click DWORD (32-bit) Value. 

Enter Enabled as the name and hit Enter. 

Ensure that it shows 0x00000001 (1) under the Data column. If it doesn't, right-click and select Modify and enter 1 as the Value data. 

Now to Enable TLS 1.2 protocol right-click on the TLS 1.2 folder and select New and then click Key. Name the new folder Server. 

Inside the Server folder, click the Edit menu, select New, and click DWORD (32-bit) Value. 

Enter Enabled as the name and hit Enter. 

Ensure that it shows 0x00000001 (1) under the Data column (it should by default). If it doesn't, right-click and select Modify and enter 1 as the data value. 

Restart the computer. 

 

 

## 2.7. SMB Protocol 

### 2.7.1. Disable Weak SMB Protocol 

Control Statement 

The Server Message Block (SMB) Protocol is a network file sharing protocol 

 

#### Risk/Impact 

This may lead to transmit passwords in plaintext across the network to other computers that offer weak SMB services. 

 

Risk Rating 

High 	 

#### Implementation Steps 

Weak SMB protocol must be disabled on the servers. 

Steps to disable weak SMB protocol using the registry:  Registry subkey:  

 

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters  Registry entry: SMB1  

REG_DWORD: 0 = Disabled  

## 2.8. Non-Essential Services 

### 2.8.1. Disable Non-Essential Services 

#### Control Statement 

Network services that compromise the security of the server should not be installed and only necessary services should be running on the server. 

#### Risk/Impact 

Running additional, unnecessary services increases the risk of a malicious user utilizing these services to compromise the security of the systems. Any vulnerability that exists for these services may be used to exploit the system. 

Risk Rating 

Medium  

#### Implementation Steps 

Ensure that all non-essential services are disabled. To configure the services,  1. Click Start > Run and type services.msc.  

2. Stop the non-essential services and also modify the startup type of the service.  Refer Appendix – 7 

 

 

 

 

 

 

 

 

 

 

## 2.9. System Folder Permissions 

2.9.1. Directories that contain sensitive Windows system files should be secured. 

### Control Statement 

Restrict access to sensitive Windows directories. The following directories should be secured: 

%systemdrive% 

%systemroot% 

%systemroot%\System32 

%systemroot%\System32\drivers 

%systemroot%\System32\spool 

%systemroot%\System32\config 

%systemroot%\sysvol 

%systemroot%\security 

%systemroot%\ntds 

%systemroot%\ntfrs 

The recommended guidelines state: 

TrustedInstaller - Full control - This folder and subfolders 

SYSTEM - Full control - This folder, subfolders and files 

Administrators - Full control - This folder, subfolders and files 

CREATOR OWNER - Full control - Subfolders and files only 

Users - Read &amp; execute - This folder, subfolders and files 

### Risk/Impact 

If unauthorized users gain access to sensitive system files, they could potentially execute a Trojan horse or create a denial of service on the server. 

Risk Rating 

Low 

### Implementation Steps 

Secure sensitive Windows directories by performing the following steps: 

Open Windows Explorer; 

Right click on the directory or file and select Properties from the menu; 

Select the Security tab; 

Highlight each group that should not have access as recommended below and click the Remove button; 

click the Add button to add the appropriate groups; 

Type in the Group name; 

Click OK to accept these changes; 

Click the advanced button; 

Review the permissions set; 

If they are not in compliance with corporate standards or the recommended guidelines, highlight the group and click the Edit... button; 

Click the down arrow of the Apply onto: field and select the appropriate access; 

Click OK to return to the Access Control Settings window; 

Repeat steps 9 through 12 for each group; 14) Click OK to return to the Properties window; and 

15) Click OK to confirm access changes. 



## 2.10. Security setting 

### 2.10.1. PIM solution must integrate all admin accounts 

#### Control Statement 

Reconciliation accounts feature from PIMS can be used to ensure that critical accounts are vaulted and password lockout problems do not arise.  Risk/Impact 

Without PIM solution, limiting and auditing activity of privileged users will not be possible. 

Risk Rating 

Medium 

Implementation Steps 

PIM solution must be deployed and all admin accounts should be integrated with it.



## 2.11. AD Replication 

### 2.11.1. Active Directory Replication 

#### Control Statement 

By default, active directory is robust and runs under active-active mode. However, it is important to keep a check to ensure that replication issues are tracked in real time. 

#### Risk/Impact 

AD replication ensures that secondary Domain controller is available for switchover in case the primary domain controller fails due to any reason. 

Risk Rating 

Medium 

Implementation Steps 

AD replication status should be monitored frequently so that issues do not get unnoticed.  

# 3. Appendix 

## 3.1. Appendix 1 

 | Sr.No | Policy                                      | Suggested Setting                      |
|-------|---------------------------------------------|----------------------------------------|
| 1     | Enforce password history                    | 5                                      |
| 2     | Maximum password age                        | 90                                     |
| 3     | Minimum password age                        | '1 or more day(s)'                     |
| 4     | Minimum password length                     | 8                                      |
| 5     | Password must meet complexity requirements  | 'Enabled'                              |
| 6     | Store passwords using reversible encryption | 'Disabled'                             |
| 7     | Account lockout duration                    | 30 minutes                             |
| 8     | Account lockout threshold                   | 3                                      |
| 9     | Reset account lockout counter after         | 0 (Only administrator can reset account) |


## 3.2. Appendix 2 

 | Sr.No | Policy                                                          | Suggested Setting for Member Server                                                      | How to Verify                                                                                          |
|-------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| 1     | Access credential manager as a trusted caller                   | No One                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Access Credential Manager as a trusted caller |
| 2     | Access this computer from the network                           | Administrators, Authenticated Users, ENTERPRISE DOMAIN CONTROLLERS, Everyone, NETWORK SERVICE | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Access this computer from the network |
| 3     | Act as part of the operating system                             | Revoke all security groups and accounts                                                   | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Act as part of the operating system |
| 4     | Add workstations to domain                                      | Administrators, LOCAL SERVICE                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Add workstations to domain |
| 5     | Adjust memory quotas for a process                              | Administrators, NETWORK SERVICE, LOCAL SERVICE                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Adjust memory quotas for a process |
| 6     | Allow log on locally                                            | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Allow log on locally |
| 7     | Allow log on through Remote Desktop Services                    | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Allow log on through Remote Desktop Services |
| 8     | Backup files and directories                                    | Administrators                                                                            |                                                                                                        |
| 9     | Bypass traverse checking                                        | Administrators, Authenticated Users, Local Service, Network Service, GITCDOM\0365sqlsvr    |                                                                                                        |
| 10    | Change the system time                                          | Administrators, LOCAL SERVICE                                                             | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Change the system time |
| 11    | Change the time zone                                            | Administrators, Local Service                                                             | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Change the time zone |
| 12    | Create a pagefile                                               | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Create a pagefile |
| 13    | Create a token object                                           | No one                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Create a token object |
| 14    | Create global objects                                           | Administrators, service, Local Service, Network Service, SERVICE                           | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Create global objects |
| 15    | Create permanent shared objects                                 | No One                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Create permanent shared objects |
| 16    | Create symbolic link                                            | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Create symbolic links |
| 17    | Debug programs                                                  | No One                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Debug programs |
| 18    | Deny access to this computer from the network                   | Guests                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Deny access to this computer from the network |
| 19    | Deny log on as a batch job                                      | Guests                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Deny log on as a batch job |
| 20    | Deny log on as a service                                        | Guests                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Deny log on as a service |
| 21    | Deny log on locally                                             | Guests                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Deny log on locally |
| 22    | Deny log on through Terminal Services                           | Guests                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Deny log on through Remote Desktop Services |
| 23    | Enable computer and user accounts to be trusted for Delegation  | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Enable computer and user accounts to be trusted for delegation |
| 24    | Force shutdown from a remote system                             | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Force shutdown from a remote system |
| 25    | Generate security audits                                        | NETWORK SERVICE, LOCAL SERVICE, gitcdom\o365adfssvr                                       | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Generate security audits |
| 26    | Impersonate a client after authentication                       | Administrators, Service, NETWORK SERVICE, LOCAL SERVICE                                   | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Impersonate a client after authentication |
| 27    | Increase a process working set                                  | Administrators, Local Service                                                             |                                                                                                        |
| 28    | Increase scheduling priority                                    | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Increase scheduling priority |
| 29    | Load and unload device drivers                                  | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Load and unload device drivers |
| 30    | Lock pages in memory                                            | No one                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Lock pages in memory |
| 31    | Log on as a batch job                                           | Administrators                                                                            | Computer Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Log on as a batch job |
| 32    | Manage auditing and security log                                | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Manage auditing and security log |
| 33    | Modify an object label                                          | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Modify an object label |
| 34    | Modify firmware environment values                              | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Modify firmware environment values |
| 35    | Perform volume maintenance tasks                                | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Perform volume maintenance tasks |
| 36    | Profile single process                                          | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Profile single process |
| 37    | Profile system performance                                      | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Profile system performance |
| 38    | Replace a process level token                                   | NETWORK SERVICE, LOCAL SERVICE                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Replace a process level token |
| 39    | Restore files and directories                                   | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Restore files and directories |
| 40    | Shut down the system                                            | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Shut down the system |
| 41    | Synchronize directory service data                              | No one                                                                                    | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Synchronize directory service data |
| 42    | Take ownership of files or other objects                        | Administrators                                                                            | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Take ownership of files or other objects |
| 43    | Set 'Deny log on through Remote Desktop Services' to include 'Guests, Local account' | Guests, Local account                                                                     | Computer Configuration\Windows Settings\Security Settings\Local Policies\User Rights Assignment\Deny log on through Remote Desktop Services |






 

 

 

## 3.3. Appendix 3 

 | Sr.No | Policy                                                                      | Suggested Setting for Member Server                                     | How to Verify                                                                                      |
|-------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| 1     | Accounts: Block Microsoft accounts                                          | Users can't add or log on with Microsoft accounts                       | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System:NoConnectedUser        |
| 2     | Accounts: Guest account status                                              | 'Disabled'                                                              | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Accounts: Guest account status |
| 3     | Accounts: Limit local account use of blank passwords to console logon only  | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:LimitBlankPasswordUse                      |
| 4     | Account: Rename administrator account                                       | Rename the 'Administrator' account name                                 | Rename administrator account                                                                       |
| 5     | Audit: Force audit policy subcategory settings to override audit policy category settings | 'Enabled'                                                               |                                                                                                    |
| 6     | Audit: Shut down system immediately if unable to log security audits        | 'Disabled'                                                              | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:CrashOnAuditFail                           |
| 7     | Devices: Allowed to format and eject removable media                        | 'Administrators'                                                        | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon:AllocateDASD              |
| 8     | Devices: Prevent users from installing printer drivers                      | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\Providers\LanMan Print Services\Servers:AddPrinterDrivers |
| 9     | Domain controller: Allow server operators to schedule tasks                 | 'Disabled'                                                              | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:SubmitControl                              |
| 10    | Domain controller: LDAP server signing requirements                         | 'Require signing'                                                       | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NTDS\Parameters:LDAPServerIntegrity           |
| 11    | Domain controller: Refuse machine account password changes                  | 'Disabled'                                                              | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters:RefusePasswordChange      |
| 12    | Domain member: Digitally encrypt or sign secure channel data (always)       | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters:RequireSignOrSeal         |
| 13    | Domain member: Digitally encrypt secure channel data (when possible)        | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters:SealSecureChannel         |
| 14    | Domain member: Digitally sign secure channel data (when possible)           | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters:SignSecureChannel         |
| 15    | Domain member: Disable machine account password changes                    | 'Disabled'                                                              | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters:DisablePasswordChange     |
| 16    | Domain member: Maximum machine account password age                        | 'Finite days'                                                           | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Domain member |
| 17    | Domain member: Require strong session key                                   | 'Enabled'                                                               |                                                                                                    |
| 18    | Interactive logon: Do not display last user name                            | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System:DontDisplayLastUserName |
| 19    | Interactive logon: Do not require CTRL+ALT+DEL                              | 'Disabled'                                                              | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System:DisableCAD            |
| 20    | Interactive logon: Machine inactivity limit                                 | '900 or fewer second(s), but not 0'                                     | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System:InactivityTimeoutSecs |
| 21    | Interactive logon: Number of previous logons to cache                       | '1 or fewer logon(s)'                                                   | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon:CachedLogonsCount         |
| 22    | Interactive logon: Prompt user to change password before expiration         | 'Between 7 and 14 days'                                                 | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon:PasswordExpiryWarning     |
| 23    | Interactive logon: Require Domain Controller Authentication to unlock workstation | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon:ForceUnlockLogon          |
| 24    | Interactive logon: Smart card removal behavior                              | 'Lock Workstation' or higher                                            | HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon:ScRemoveOption            |
| 25    | Microsoft network client: Digitally sign communications (always)            | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters:RequireSecuritySignature |
| 26    | Microsoft network client: Digitally sign communications (if server agrees)  | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters:EnableSecuritySignature |
| 27    | Microsoft network client: Send unencrypted password to third-party SMB servers | 'Disabled'                                                              | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters:EnablePlainTextPassword |
| 28    | Microsoft network server: Amount of idle time required before suspending session | '15 or fewer minute(s), but not 0'                                       | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanManServer\Parameters:AutoDisconnect        |
| 29    | Microsoft network server: Digitally sign communications (always)            | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanManServer\Parameters:RequireSecuritySignature |
| 30    | Microsoft network server: Digitally sign communications (if client agrees)  | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanManServer\Parameters:EnableSecuritySignature |
| 31    | Microsoft network server: Disconnect clients when logon hours expire        | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanManServer\Parameters:EnableForcedLogoff    |
| 32    | Microsoft network server: Server SPN target name validation level           | 'Accept if provided by client' or higher (MS only)                      | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanManServer\Parameters:SMBServerNameHardeningLevel |
| 33    | Network access: Allow anonymous SID/Name translation                        | 'Disabled'                                                              | Computer Configuration\Policies\Windows Settings\Security Settings\Local Policies\Security Options\Network access: Allow anonymous SID/Name translation |
| 34    | Network access: Do not allow anonymous enumeration of SAM accounts          | 'Enabled' (MS only)                                                     | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:RestrictAnonymousSAM                        |
| 35    | Network access: Do not allow anonymous enumeration of SAM accounts and shares | 'Enabled' (MS only)                                                     | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:RestrictAnonymous                          |
| 36    | Network access: Do not allow storage of passwords and credentials for network authentication | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:DisableDomainCreds                         |
| 37    | Network access: Let Everyone permissions apply to anonymous users           | 'Disabled'                                                              | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:EveryoneIncludesAnonymous                  |
| 38    | Network access: Restrict anonymous access to Named Pipes and Shares         | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanManServer\Parameters:RestrictNullSessAccess |
| 39    | Network access: Restrict clients allowed to make remote calls to SAM        | 'Administrators: Remote Access: Allow' (MS only)                        | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:restrictremotesam                           |
| 40    | Network access: Shares that can be accessed anonymously                     | 'None'                                                                  | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanManServer\Parameters:NullSessionShares      |
| 41    | Network access: Sharing and security model for local accounts               | 'Classic - local users authenticate as themselves'                      | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:ForceGuest                                  |
| 42    | Network security: Allow Local System to use computer identity for NTLM      | 'Enabled'                                                               | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa:UseMachineId                               |
| 43    | Network security: Allow LocalSystem NULL session fallback                   | 'Disabled'                                                              | HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\MSV1_0:AllowNullSessionFallback            |
| 44    | Network Security: Allow PKU2U authentication requests to this computer to use online identities | 'Disabled'                                                              |





  
## 3.4. Appendix 4 

 
| Profile        | Policy                                                     | Suggested Setting           | How to Verify                                                                                                     |
|----------------|------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------|
| **Domain Profile**  |                                                          |                             |                                                                                                                   |
|                | Windows Firewall: Domain: Firewall state                   | 'On (recommended)'          | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\EnableFirewall                       |
|                | Windows Firewall: Domain: Inbound connections               | 'Allow (default)'           | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\DefaultInboundAction                 |
|                | Windows Firewall: Domain: Outbound connections              | 'Allow (default)'           | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\DefaultOutboundAction                |
|                | Windows Firewall: Domain: Settings: Display a notification  | 'Yes'                       | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\DisableNotifications                 |
|                | Windows Firewall: Domain: Settings: Apply local firewall rules | 'Yes (default)'             | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\AllowLocalPolicyMerge                |
|                | Windows Firewall: Domain: Settings: Apply local connection security rules | 'Yes (default)'           | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\AllowLocalIPsecPolicyMerge           |
|                | Windows Firewall: Domain: Logging: Name                     | '%SYSTEMROOT%\System32\logfiles\firewall\domainfw.log' | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging\LogFilePath                 |
|                | Windows Firewall: Domain: Logging: Size limit (KB)          | '16,384 KB or greater'      | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging\LogFileSize                  |
|                | Windows Firewall: Domain: Logging: Log dropped packets      | 'Yes'                       | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging\LogDroppedPackets            |
|                | Windows Firewall: Domain: Logging: Log successful connections | 'Yes'                     | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile\Logging\LogSuccessfulConnections     |
|                | Windows Firewall: Domain: Allow unicast response            | 'No'                        | Computer Configuration\Windows Settings\Security Settings\Windows Firewall with Advanced Security\Windows Firewall Properties\Domain Profile\Windows Firewall: Domain: Allow unicast response |
| **Private Profile** |                                                       |                             |                                                                                                                   |
|                | Windows Firewall: Private: Firewall state                  | 'On (recommended)'          | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\EnableFirewall                      |
|                | Windows Firewall: Private: Inbound connections              | 'Allow'                     | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\DefaultInboundAction                |
|                | Windows Firewall: Private: Outbound connections             | 'Allow'                     | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\DefaultOutboundAction               |
|                | Windows Firewall: Private: Settings: Display a notification | 'No'                        | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\DisableNotifications                |
|                | Windows Firewall: Private: Settings: Apply local firewall rules | 'Yes (default)'           | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\AllowLocalPolicyMerge               |
|                | Windows Firewall: Private: Settings: Apply local connection security rules | 'Yes (default)'           | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\AllowLocalIPsecPolicyMerge          |
|                | Windows Firewall: Private: Logging: Name                    | '%SYSTEMROOT%\System32\logfiles\firewall\privatefw.log' | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging\LogFilePath                |
|                | Windows Firewall: Private: Logging: Size limit (KB)         | '16,384 KB or greater'      | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging\LogFileSize                 |
|                | Windows Firewall: Private: Logging: Log dropped packets     | 'Yes'                       | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging\LogDroppedPackets           |
|                | Windows Firewall: Private: Logging: Log successful connections | 'Yes'                     | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PrivateProfile\Logging\LogSuccessfulConnections    |
| **Public Profile**  |                                                       |                             |                                                                                                                   |
|                | Windows Firewall: Public: Firewall state                   | 'On (recommended)'          | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\EnableFirewall                       |
|                | Windows Firewall: Public: Inbound connections               | 'Allow'                     | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\DefaultInboundAction                 |
|                | Windows Firewall: Public: Outbound connections              | 'Allow'                     | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\DefaultOutboundAction                |
|                | Windows Firewall: Public: Settings: Display a notification  | 'Yes'                       | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\DisableNotifications                 |
|                | Windows Firewall: Public: Settings: Apply local firewall rules | 'No'                      | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\AllowLocalPolicyMerge                |
|                | Windows Firewall: Public: Settings: Apply local connection security rules | 'No'                      | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\AllowLocalIPsecPolicyMerge           |
|                | Windows Firewall: Public: Logging: Name                     | '%SYSTEMROOT%\System32\logfiles\firewall\publicfw.log' | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\Logging\LogFilePath                 |
|                | Windows Firewall: Public: Logging: Size limit (KB)          | '16,384 KB or greater'      | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\Logging\LogFileSize                  |
|                | Windows Firewall: Public: Logging: Log dropped packets      | 'Yes'                       | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\Logging\LogDroppedPackets            |
|                | Windows Firewall: Public: Logging: Log successful connections | 'Yes'                     | HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\WindowsFirewall\PublicProfile\Logging\LogSuccessfulConnections     |




  

 

 

 

 

 

 



## 3.5. Appendix 5 

 
| Category         | Policy                                                   | Suggested Setting           | How to Verify                                                                                                           |
|------------------|----------------------------------------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Account Logon**  |                                                        |                             |                                                                                                                         |
|                  | Audit Credential Validation                              | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Logon\Audit Credential Validation |
| **Account Management** |                                                   |                             |                                                                                                                         |
|                  | Audit Application Group Management                       | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Management\Audit Application Group Management |
|                  | Audit Computer Account Management                        | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Management\Audit Computer Account Management |
|                  | Audit Distribution Group Management                      | 'Success and Failure' (DC only) | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Management\Audit Distribution Group Management |
|                  | Audit Other Account Management Events                    | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Management\Audit Other Account Management Events |
|                  | Audit Security Group Management                          | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Management\Audit Security Group Management |
|                  | Audit User Account Management                            | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Account Management\Audit User Account Management |
| **Detailed Tracking** |                                                     |                             |                                                                                                                         |
|                  | Audit PNP Activity                                       | 'Success'                    | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Detailed Tracking\Audit PNP Activity |
|                  | Audit Process Creation                                   | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Detailed Tracking\Audit Process Creation |
|                  | Audit DPAPI Activity                                     | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Detailed Tracking\Audit DPAPI Activity |
| **DS Access**     |                                                        |                             |                                                                                                                         |
|                  | Audit Directory Service Access                           | 'Success and Failure' (DC only) | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\DS Access\Audit Directory Service Access |
|                  | Audit Directory Service Changes                          | 'Success and Failure' (DC only) | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\DS Access\Audit Directory Service Changes |
| **Logon/Logoff**  |                                                        |                             |                                                                                                                         |
|                  | Audit Account Lockout                                    | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Logon/Logoff\Audit Account Lockout |
|                  | Audit Group Membership                                   | 'Success'                    | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Logon/Logoff\Audit Group Membership |
|                  | Audit Logoff                                             | 'Success'                    | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Logon/Logoff\Audit Logoff |
|                  | Audit Logon                                              | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Logon/Logoff\Audit Logon |
|                  | Audit Other Logon/Logoff Events                          | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Logon/Logoff\Audit Other Logon/Logoff Events |
|                  | Audit Special Logon                                      | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Logon/Logoff\Audit Special Logon |
| **Object Access**  |                                                        |                             |                                                                                                                         |
|                  | Audit Removable Storage                                  | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Object Access\Audit Removable Storage |
| **Policy Change**  |                                                        |                             |                                                                                                                         |
|                  | Audit Audit Policy Change                                | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Policy Change\Audit Audit Policy Change |
|                  | Audit Authentication Policy Change                       | 'Success'                    | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Policy Change\Audit Authentication Policy Change |
|                  | Audit Authorization Policy Change                        | 'Success'                    | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Policy Change\Audit Authorization Policy Change |
| **Privilege Use**  |                                                        |                             |                                                                                                                         |
|                  | Audit Sensitive Privilege Use                            | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\Privilege Use\Audit Sensitive Privilege Use |
| **System**         |                                                        |                             |                                                                                                                         |
|                  | Audit IPsec Driver                                       | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\System\Audit IPsec Driver |
|                  | Audit Other System Events                                | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\System\Audit Other System Events |
|                  | Audit Security State Change                              | 'Success'                    | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\System\Audit Security State Change |
|                  | Audit Security System Extension                          | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\System\Audit Security System Extension |
|                  | Audit System Integrity                                   | 'Success and Failure'        | Computer Configuration\Policies\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\System\Audit System Integrity |





 

 



 

 

## 3.6. Appendix 6 

 
| Path                                                                                  | Policy                                                                        | Suggested Setting                                                                                 |
|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Control Panel**                                                                     |                                                                               |                                                                                                   |
| Computer Configuration\Administrative Templates\Control Panel\Personalization          | Prevent enabling lock screen camera                                           | 'Enabled'                                                                                         |
|                                                                                       | Prevent enabling lock screen slide show                                       | 'Enabled'                                                                                         |
|                                                                                       | Allow Input Personalization                                                   | 'Disabled'                                                                                        |
| **MSS**                                                                               |                                                                               |                                                                                                   |
| Computer Configuration\Administrative Templates\MSS (Legacy)                          | MSS: (AutoAdminLogon) Enable Automatic Logon (not recommended)                | 'Disabled'                                                                                        |
|                                                                                       | MSS: (DisableIPSourceRouting IPv6) IP source routing protection level          | 'Enabled: Highest protection, source routing is completely disabled'                               |
|                                                                                       | MSS: (DisableIPSourceRouting) IP source routing protection level               | 'Enabled: Highest protection, source routing is completely disabled'                               |
|                                                                                       | MSS: (EnableICMPRedirect) Allow ICMP redirects to override OSPF generated routes | 'Disabled'                                                                                        |
|                                                                                       | MSS: (KeepAliveTime) How often keep-alive packets are sent in milliseconds     | 'Enabled: 300,000 or 5 minutes (recommended)'                                                     |
|                                                                                       | MSS: (NoNameReleaseOnDemand) Allow the computer to ignore NetBIOS name release requests except from WINS servers | 'Enabled'                                                                                        |
|                                                                                       | MSS: (PerformRouterDiscovery) Allow IRDP to detect and configure Default Gateway addresses (could lead to DoS) | 'Disabled'                                                                                        |
|                                                                                       | MSS: (SafeDllSearchMode) Enable Safe DLL search mode (recommended)             | 'Enabled'                                                                                        |
|                                                                                       | MSS: (ScreenSaverGracePeriod) The time in seconds before the screen saver grace period expires (0 recommended) | 'Enabled: 5 or fewer seconds'                                                                     |
|                                                                                       | MSS: (TcpMaxDataRetransmissions IPv6) How many times unacknowledged data is retransmitted | 'Enabled: 3'                                                                                       |
|                                                                                       | MSS: (TcpMaxDataRetransmissions) How many times unacknowledged data is retransmitted | 'Enabled: 3'                                                                                       |
|                                                                                       | MSS: (WarningLevel) Percentage threshold for the security event log at which the system will generate a warning | 'Enabled: 90% or less'                                                                            |
| **Network**                                                                           |                                                                               |                                                                                                   |
| Computer Configuration\Policies\Administrative Templates\Network\DNS Client\Turn off multicast name resolution | Turn off multicast name resolution                                             | 'Enabled' (MS Only)                                                                               |
| Computer Configuration\Policies\Administrative Templates\Network\Fonts\Enable Font Providers | Enable Font Providers                                                          | 'Disabled'                                                                                        |
|                                                                                       | Enable insecure guest logons                                                  | 'Disabled'                                                                                        |
|                                                                                       | Turn on Mapper I/O (LLTDIO) driver                                             | 'Disabled'                                                                                        |
|                                                                                       | Turn on Responder (RSPNDR) driver                                              | 'Disabled'                                                                                        |
|                                                                                       | Turn off Microsoft Peer-to-Peer Networking Services                             | 'Enabled'                                                                                        |
|                                                                                       | Prohibit installation and configuration of Network Bridge on your DNS domain network | 'Enabled'                                                                                        |
|                                                                                       | Prohibit use of Internet Connection Sharing on your DNS domain network          | 'Enabled'                                                                                        |
|                                                                                       | Require domain users to elevate when setting a network's location              | 'Enabled'                                                                                        |
|                                                                                       | Disable IPv6 (Ensure TCPIP6 Parameter 'DisabledComponents                      | '0xff (255)'                                                                                      |
|                                                                                       | Configuration of wireless settings using Windows Connect Now                  | 'Disabled'                                                                                        |
|                                                                                       | Prohibit access of the Windows Connect Now wizards                            | 'Enabled'                                                                                        |
|                                                                                       | Minimize the number of simultaneous connections to the Internet or a Windows Domain | 'Enabled'                                                                                        |
|                                                                                       | Prohibit connection to non-domain networks when connected to domain authenticated network | 'Enabled'                                                                                        |
| **System**                                                                            |                                                                               |                                                                                                   |
| Computer Configuration\Policies\Administrative Templates\System\Audit Process Creation\Include command line in process creation events | Include command line in process creation events                                 | 'Disabled'                                                                                        |
|                                                                                       | Continue experiences on this device                                            | 'Disabled'                                                                                        |
|                                                                                       | Turn off background refresh of Group Policy                                    | 'Disabled'                                                                                        |
|                                                                                       | Turn off access to the Store                                                   | 'Enabled'                                                                                        |
|                                                                                       | Turn off Internet Connection Wizard if URL connection is referring to Microsoft.com | 'Enabled'                                                                                        |
|                                                                                       | Turn off Internet download for Web publishing and online ordering wizards      | 'Enabled'                                                                                        |
|                                                                                       | Turn off printing over HTTP                                                    | 'Disabled'                                                                                        |
|                                                                                       | Turn off Registration if URL connection is referring to Microsoft.com           | 'Enabled'                                                                                        |
|                                                                                       | Turn off Search Companion content file updates                                 | 'Enabled'                                                                                        |
|                                                                                       | Turn off the "Order Prints" picture task                                       | 'Enabled'                                                                                        |
|                                                                                       | Turn off the "Publish to Web" task for files and folders                        | 'Enabled'                                                                                        |
|                                                                                       | Turn off the Windows Messenger Customer Experience Improvement Program         | 'Enabled'                                                                                        |
|                                                                                       | Turn off Windows Customer Experience Improvement Program                        | 'Enabled'                                                                                        |
|                                                                                       | Turn off Windows Error Reporting                                               | 'Enabled'                                                                                        |
|                                                                                       | Disallow copying of user input methods to the system account for sign-in        | 'Enabled'                                                                                        |
|                                                                                       | Block user from showing account details on sign-in                             | 'Enabled'                                                                                        |
| **Logon**                                                                             |                                                                               |                                                                                                   |
| Computer Configuration\Policies\Administrative Templates\System\Logon\Do not display network selection UI | Do not display network selection UI                                             | 'Enabled'                                                                                        |
|                                                                                       | Do not enumerate connected users on domain-joined computers                    | 'Enabled'                                                                                        |
|                                                                                       | Enumerate local users on domain-joined computers                                | 'Disabled'                                                                                        |
|                                                                                       | Turn off app notifications on the lock screen                                  | 'Enabled'                                                                                        |
|                                                                                       | Turn on convenience PIN sign-in                                                | 'Disabled'                                                                                        |
| **Remote Procedure Call**                                                             |                                                                               |                                                                                                   |
|                                                                                       | Enable RPC Endpoint Mapper Client Authentication                               | 'Enabled'                                                                                        |
|                                                                                       | Restrict Unauthenticated RPC clients                                           | 'Enabled: Authenticated'                                                                          |
| **Windows Time Service**                                                              |                                                                               |                                                                                                   |
| Computer Configuration\Policies\Administrative Templates\System\Windows Time Service\Time Providers\Enable Windows NTP Client | Enable Windows NTP Client                                                      | 'Enabled'                                                                                        |
| Computer Configuration\Policies\Administrative Templates\System\Windows Time Service\Time Providers\Enable Windows NTP Server | Enable Windows NTP Server                                                      | 'Enabled'                                                                                        |
| **LAPS**                                                                              |                                                                               |                                                                                                   |
| Computer Configuration\Policies\Administrative Templates\LAPS\Enable Local Admin Password Management | Enable Local Admin Password Management                                          | 'Enabled'                                                                                        |
| Computer Configuration\Policies\Administrative Templates\LAPS\Password Settings       | Password Complexity: Large letters + small letters + numbers + special characters | 'Enabled'                                                                                        |
|                                                                                       | Password Length: 8 or more                                                     | '8 or more'                                                                                       |
|                                                                                       | Password Age (Days): 90 or fewer                                               | '90 days'                                                                                        |
| **SCM**                                                                               |                                                                               |                                                                                                   |
| Computer Configuration\Policies\Administrative Templates\SCM: Pass the Hash Mitigations\Apply UAC restrictions to local accounts on network logons | Apply UAC restrictions to local accounts on network logons                      | 'Enabled'                                                                                        |
|                                                                                       | WDigest Authentication                                                        | 'Disabled'                                                                                        |

















 

 

 

 

 

 

 

 

 

 

 

 

 

 

## 3.7. Appendix 7 

 

 

 | Service Name                                | Recommended Startup Type  | Comment                                                                                                                                                 |
|---------------------------------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Alerter                                      | Disabled                  |                                                                                                                                                         |
| Client Services for Netware                  | Disabled                  |                                                                                                                                                         |
| DHCP Client                                  | Disable                   | Enable, if the System takes dynamic IP from DHCP Server or server configured is in cluster                                                              |
| Error Reporting Service                      | Disabled                  |                                                                                                                                                         |
| Fax Service                                  | Disabled                  | Enable, if Fax service is required on the system.                                                                                                       |
| File Services for Macintosh                  | Disabled                  |                                                                                                                                                         |
| FTP Publishing Service                       | Disabled                  |                                                                                                                                                         |
| Help and Support                             | Disabled                  |                                                                                                                                                         |
| Human Interface Device Access                | Disabled                  |                                                                                                                                                         |
| IIS Admin Service                            | Enabled                   |                                                                                                                                                         |
| IMAPI CD – Burning COM Service               | Disabled                  |                                                                                                                                                         |
| Internet Connection Sharing                  | Disabled                  |                                                                                                                                                         |
| Messenger                                    | Disabled                  |                                                                                                                                                         |
| Microsoft POP3 Service                       | Disabled                  |                                                                                                                                                         |
| Network DDE                                  | Disabled                  |                                                                                                                                                         |
| Network DDE DSDM                             | Disabled                  |                                                                                                                                                         |
| Portable Media Serial Number                 | Disabled                  |                                                                                                                                                         |
| Print Server for Macintosh                   | Disabled                  |                                                                                                                                                         |
| Shell Hardware Detection                     | Disabled                  | Enable, if Shell Hardware Detection (ShellHWDetection) service is required to monitor and provide notification for AutoPlay hardware events.              |
| Simple Mail Transfer Protocol                | Disabled                  | Enable, if SMTP server is used.                                                                                                                          |
| Simple Network Management Protocol (SNMP) Service | Disabled              | Enable, if SNMP service is required.                                                                                                                     |
| Simple Network Management Protocol (SNMP) Trap | Disabled              |                                                                                                                                                         |
| Smart Card                                   | Disabled                  | Enable it if you are using a smart card                                                                                                                  |
| Special Administration Console Helper        | Disabled                  |                                                                                                                                                         |
| Telephony                                    | Disabled                  |                                                                                                                                                         |
| Telnet                                       | Disabled                  |                                                                                                                                                         |
| Uninterruptible Power Supply                 | Disabled                  |                                                                                                                                                         |
| Upload Manager                               | Disabled                  |                                                                                                                                                         |
| WebClient                                    | Disabled                  |                                                                                                                                                         |
| Wireless Configuration                       | Disabled                  |                                                                                                                                                         |
| Bluetooth Service                            | Disabled                  |                                                                                                                                                         |


