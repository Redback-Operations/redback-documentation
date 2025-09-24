---
sidebar_position: 22
---

# OWASP TOP 10 review

Redback Operations Cybersecurity User Awareness Training Content

:::info
**Document Creation:** 07 Dec, 2024. **Last Edited:** 07 Dec, 2024. **Authors:** Tristan Apperley.
<br></br>**Effective Date:** 07 Dec 2024. **Expiry Date:** 07 Dec 2025.
:::

## OWASP TOP 10 

OWASP top 10 is created for web application developers to advise them of the top 10 most critical security risks to web application. It is used as the first steps towards more secure coding. 

Redback Operations utilises OWASP Top10 to conduct its secure code review to ensure the most critical risks are addressed before any code can be used. 


**NOTE: The current OWASP top 10 was last updated in 2021 with OWASP planning on releasing a new TOP in the first half of 2025. All Redback Operations code will need to be reviewed again based on OWASP top 10 of 2025** 


### The 10 OWASP Top 10 security risks are as follows (current as of 2021):

#### A01:2021 – Broken Access Control
Broken Access Control is a critical vulnerability that needs to be addresses when writing code. Access control ensures a user can only access areas of a program/operating system that they have a need to use. Failures of broken access control can lead to unauthorised access to data leading to possibility of the data being manipulated (modification, addition or even deletion). 

##### Examples of Access control Vulnerabilities can include: 
-	Users being given more access then required to do their job (not using least privileges/deny by default)
-	Viewing or editing someone else data 
-	Elevation of privileges – being able to act a user without actually being logged in or being able to make changes as If you are and admin however you are logged in as a user. 
-	Manipulating metadata such, such as replaying or tampering with a JSON Web Token access control token, or a cookie or hidden field manipulated to elevate privileges or abusing JWT invalidation.

##### How to Prevent 
-	Access control will only work when the attacker cannot modify access control checks or metadata. 
-	Use deny by default/least privileges wherever possible
-	Use access control mechanisms 
-	Alert admins of numerous failures to authenticate – Log access control failures
-	Enforce record ownership through access control rather than accepting that the user can create, read, update, or delete any record.

#### A02:2021 – Cryptographic Failures
Cryptographic Failures or complete lack of crypto refers to sensitive data being exposed/released to people with no need/authorisation to view/edit/manipulate the data. Type of data that should always be encrypted during transit include financial details, passwords and PII. A lot of this data is required to be kept secure under the Australian Privacy Principles. 

##### Example of Cryptographic Failures
-	Using unsecure protocols such as HTTP, SMTP and FTP to transmit sensitive data
-	The use of old or weak cryptographic algorithms or protocols
-	Default or weak crypto keys used or reused 
-	Not enforcing encryption 
-	Not properly validating a received server certificate 
-	Using passwords in lieu of crypto keys 
-	Not using deprecated hash functions when required 

##### How to Prevent 
-	Encrypt all sensitive data
-	Use up to date and strong encryption algorithms and protocols 
-	Encrypt all data in transit with secure protocols
-	Store passwords using strong adaptive and salted hashing function
-	Always use authenticated encryption instead of just encryption.
-	Keys generated cryptographically randomly and stored in memory as byte arrays.
#### A03:2021 – Injection
Injections attacks occur when an application has malicious data into it. 

##### Examples of when this can occur include; 
-	User-data is not properly checked, filtered or sanitised by an application
-	Hostile data is directly used or concatenated and the command contains the expected input but also malicious data (in a dynamic query). 
-	When hostile data is used within object-relational mapping search parameters to extract other sensitive records 

##### How to Prevent 
-	Use a safe API, which avoids using an interpreter entirely
-	User positive server-side input validation 
-	To prevent mass disclosures of records via SQL injection use LIMIT and other SQL Controls. 

#### A04:2021-Insecure Design 
Insecure design covers all different weaknesses in an application, these weaknesses come around because of missing on ineffective control design. Insecure design is not the same as insecure implementation as secure implementation will still not rectify issues with insecure design and vice versa secure design will not fix issues that arise as a result of insecure implementation.

To rectify this issue, we need to ensure we design our applications with security in mind. Secure design ensures that threats are constantly evaluated and ensures that code is robustly designed and tested to prevent attacks which are known.
When designing applications, we need to ensure that we use a secure development lifecycle which includes paved road methodology, secured component library, tooling, and threat modelling.

##### How to Prevent 
-	Use a secure development lifecycle when developing any application 
-	Use threat modelling for critical authentication, access control, business logic, and key flows
-	At each tier of your application integrate plausibility checks 
-	Integrate security language and controls into user stories

#### A05:2021 – Security Misconfiguration
Security misconfiguration occurs when an application is not configured securely allowing it to become vulnerable to hostiles actors. 
An application can become vulnerable is it is: 
-	The application stack is missing appropriate security harding 
-	Cloud services permissions are improperly configured 
-	Features not required are installed or enabled 
-	Passwords are still set to defaults
-	Software is out of date 
##### How to Prevent
	To minimise the risk of security misconfigurations a secure installation process should be implemented which is made up of the following:
-	A repeatable hardening process makes it fast and easy to deploy another environment that is appropriately locked down.
-	Ensure your application has no unnecessary features 
-	Implement a segmented application architecture on your application
-	Have a patch process which ensure updated happen as soon as possible


#### A06:2021-Vulnerable and Outdated Components 
Vulnerable and Outdated Components is exactly as it sounds, it occurs when out application and systems use known Vulnerable and Outdated Components in our applications putting ourselves at risk from hostile actors. 

##### Applications can be at risk when: 
-	You do not know the version of all components you use (both ones you use directly and that are nested within the overall systems) 
-	You are using known vulnerable software or you software is not up to date
-	You do not conduct regular vulnerability scans on your system 
-	When a vulnerability is identified you do not rectify the issue
-	If you do not secure the components’ configurations
##### How to Prevent
-	Have a patch management system in place 
-	Remove unused dependencies, unnecessary features, components, files, and documentation.
-	Keep track of both client-side and server-side components and ensure they are kept up to date
-	Only obtain components from official sources over secure links


#### A07:2021 – Identification and Authentication Failures
This occurs when someone who does not have permission to access a system or a certain area of a system is able to bypass (intentionally or not) checks to gain access to the data. Confirm someone’s identity and authentication is critical to ensuring a system is secure 
##### An application or system may have weak authentication if it:
-	Allows brute force or automated attacks 
-	Has in use default or weak passwords
-	Uses weak or ineffective credential recovery and forgot-password processes
-	Stores passwords in plain text, or with weak encryption 
-	Missing or weak MFA
-	Session identifier is exposed in URL 
##### How to Prevent
-	Implement MFA 
-	Always ensure default credentials are not used when application is shipped or deployed 
-	Check for weak passwords 
-	Use complex passwords
-	Limit amount of logon attempts 

#### A08:2021 – Software and Data Integrity Failures
This category refers to software and data integrity failures in code and infrastructure that does not protect against integrity violations. Examples of this can include:
-	Where an application relies upon plugins, libraries, or modules from untrusted sources leaving it vulnerable
-	Insecure CI/CD pipeline can introduce the potential for unauthorised access, malicious code, or system compromise. 
-	Using automatic updates without sufficiently verifying the integrity of the update can leave the system vulnerable to attackers who hide their code in the update. 
##### How to Prevent
-	Verify software or data is from the expected source and has not been altered.
-	Ensure libraries and dependencies are consuming trusted repositories
-	Use a software supply chain security tool 
-	Use a code review process for code and configuration changes
-	Your CI/CD pipeline should have proper segregation, configuration, and access control

#### A09:2021 – Security Logging and Monitoring Failures
This vulnerability occurs when Security Logging and Monitoring is not conducted properly or at all on a system or application. Without proper logging and monitoring breached may not be detected or responded to as required.  
##### Examples of issues can include: 
-	Login event failures not being logged 
-	 Warnings and errors generate inadequate or unclear log messages 
-	Logs are not actually reviewed or monitored 
-	Log only stored locally and not backed up 
-	Alerts and issues are not detected and raised in real time 
##### How to Prevent
Developers should consider the following:
-	All login, access controls, and server-side input validation should be logged 
-	Logs need to be created in a format that is easily consumed 
-	Ensure logs and their data are encoded correctly to stop attacks against the logs themselves 
-	DevSecOps teams need to ensure that monitoring and alerting is effective and occurs 
-	Have an incident response plan for when an incident is detected. 

#### A10:2021-Server-Side Request Forgery
This vulnerability occurs when a web application fetches a remote resource without validating the user-supplied URL, as a result it allows an attacker to force the application to send an altered request to an unexpected destination. 
##### Developers can do the following to mitigate this type of vulnerability

###### From Network Layer:
-	Segment remote resource access functionality in separate networks – this is to minimise the impact of this vulnerability 
-	Use Deny by default 
###### From Application Layer 
-	All client supplied data should be checked and validated
-	Use an allow list 
-	Clients should not be sent raw responses 
-	Do not allow HTTP redirections 

#### Reference list:
OWASP (Open Worldwide Application Security Project) 2024, OWASP Top Ten Project, viewed 7 December 2024, https://owasp.org/www-project-top-ten/.



