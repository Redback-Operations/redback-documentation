---
id: installing-wazuh
title: Installing Wazuh (Docker Single-Node)
sidebar_position: 3
---





This guide explains how to install Wazuh in a single-node Docker deployment on a local VM for learning and onboarding purposes.


# Installing Wazuh (Docker Single-Node)

This document explains how Wazuh was set up on the Redback VM.  
We use a Docker single-node setup because it’s simple, lightweight, and works well for our project.  
The installation is already done, but these steps show how it was set up so new team members understand the process.

---

## 1. What you need first
Before you start, make sure you have:
- Access to the Redback VM with admin (sudo) rights.  
- A working internet connection on the VM.  
- Cisco AnyConnect VPN access if you are off-campus.  
- Some basic Linux terminal knowledge.  

---

## 2. Preparing the system
First, become the root user:
```
sudo su
```
Update and upgrade the system so everything is current:
```
apt update && apt upgrade -y
```

Then set a system parameter needed by Docker:
```
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```


## 3. Installing Docker

Install Docker with this command:
```
curl -sSL https://get.docker.com/ | sh
```

Now install Docker Compose:
```
curl -L "https://github.com/docker/compose/releases/download/v2.20.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```


## 4. Deploying Wazuh

Create a folder and download the Wazuh Docker files:
```
cd /opt/ && mkdir deploy && cd deploy
git clone https://github.com/wazuh/wazuh-docker.git -b v4.5.0
cd wazuh-docker/single-node/
```

Generate the certificates Wazuh needs:
```
docker-compose -f generate-indexer-certs.yml run --rm generator
```

Now start Wazuh:
```
docker-compose up -d

```


## 5. Checking it works
```
docker-compose ps
```
You should see Wazuh Manager, Wazuh Indexer, and Wazuh Dashboard all showing as “Up”.


## 6. Using the Wazuh dashboard

1. Connect to the Deakin VPN.
2. Open your browser and go to:
   ```
   https://localhost:5601  or  https://<VM-IP>:5601 (if accessing from another machine)
   ```
3. Log in with your Entra ID account.
   If you don’t have one, ask your mentor or team lead to create it.
   Old default logins (like kibanaserver) don’t work anymore.



   ## Conclusion
   That’s how Wazuh was installed on the Redback VM. Most students don’t need to do the install themselves, just know that it’s running on Docker, and you can log in to the dashboard to see alerts, logs, and security events.


   ## Reference
   https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html#single-node-stack
   

