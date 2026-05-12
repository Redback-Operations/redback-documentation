# Port Security Guideline

Port security is an essential aspect of Redback's Virtual Machine's cybersecurity. It ensures that only authorised services and connections are permitted, reducing any potential risk. By properly managing and monitoring ports, the team can significantly minimise threats. 

This VM Port Security Guideline provides a straightforward guide on how to ensure that the VM’s ports are secure and operating as intended. It outlines a clear procedure for checking ports within the VM and what actions should be taken to ensure port security and prevent potential intrusions.

**NOTE:** This document does not guarantee 100% security. It should be regularly reviewed and improved.

---

## Port Security Guideline Access

To access the Port Security Guideline from the VM, use the below command on your host machine. The guideline will then be downloaded to the user’s own host machine for easy access:

```bash
scp username@vm-ip:/usr/local/share/doc/Port_Security_Guideline.pdf .
