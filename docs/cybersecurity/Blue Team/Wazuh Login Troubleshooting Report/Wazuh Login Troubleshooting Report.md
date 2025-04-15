

# Wazuh Login Troubleshooting Report

**Author:** Elvis Ifeanyi Nwosu  
**Date:** April 8, 2025  
**System:** Wazuhs Full Stack Deployment (Manager, Indexer, Dashboard) on Local VM



## Summary

This report documents the troubleshooting process undertaken to resolve login issues encountered while accessing the Wazuh Dashboard after full stack deployment. The process involved validating service statuses, resetting credentials, fixing permission issues, and regenerating SSL certificates.



## Issue Summary

Following deployment of the Wazuh manager, indexer, and dashboard, login attempts to the Wazuh web interface failed. The failure was accompanied by:

- Credential mismatch errors.  
- Permission-denied issues when updating the keystore.  
- SSL file not found (`dashboard-key.pem`) error.



## Root Cause Analysis

### 1. **Credential Errors**
- Default login credentials (`admin/admin`) were not accepted.  
- Manual user creation and password reset did not resolve the issue immediately.

### 2. **Keystore Permission Denied**
- Attempt to update the `opensearch-dashboards-keystore` failed due to lack of root privileges.

### 3. **Missing SSL Certificate**
- Wazuh dashboard failed to start due to missing `/etc/wazuh-dashboard/certs/dashboard-key.pem`.



## Troubleshooting Steps

### Step 1: Verified Service Status

```bash
sudo systemctl status wazuh-manager
sudo systemctl status wazuh-dashboard
sudo systemctl status wazuh-indexer
```

 Confirmed manager was active but Dashboard and indexer failed.

**Screenshot of Service Status wazuh-dashboard:**  
![Service Status wazuh-dashboard](Img\image-4.png)

**Screenshot of Service Status wazuh-indexer:**
![Service Status wazuh-indexer](Img\image-2.png)

**Screenshot of Service Status wazuh-manager:**
![Service Status wazuh-manager](Img\image-3.png)

### Step 2: Reset Credentials

```bash
sudo /usr/share/wazuh-indexer/plugins/opensearch-security/tools/wazuh-passwords-tool.sh --change-all
```

Successfully reset passwords for users including `kibanaserver`.

**Screenshot of new passwords:** 

![Password Reset Output](Img\image.png)


### Step 3: Updated Keystore

```bash
echo '<new-password>' | /usr/share/wazuh-dashboard/bin/opensearch-dashboards-keystore --allow-root add -f --stdin opensearch.password
```

Note: Initial attempts failed due to insufficient permissions. Switching to root user (`sudo -i`) resolved the issue.




### Step 4: Regenerated Missing SSL Files

```bash
sudo mkdir -p /etc/wazuh-dashboard/certs
sudo openssl genrsa -out /etc/wazuh-dashboard/certs/dashboard-key.pem 2048
sudo openssl req -new -key /etc/wazuh-dashboard/certs/dashboard-key.pem -out /etc/wazuh-dashboard/certs/dashboard.csr
sudo openssl x509 -req -in /etc/wazuh-dashboard/certs/dashboard.csr -signkey /etc/wazuh-dashboard/certs/dashboard-key.pem -out /etc/wazuh-dashboard/certs/dashboard-cert.pem -days 365
```

 Successfully created private key and certificate.

**Screenshot of regenerated dashboard certs:**  
![regenerated dashboard certificates](Img\image-5.png)



### Step 5: Adjusted Permissions

```bash
sudo chown -R wazuh:wazuh /etc/wazuh-dashboard/certs
sudo chmod 600 /etc/wazuh-dashboard/certs/dashboard-key.pem
```

 Ensured proper access rights for dashboard service.

**Screenshots of access permisssions**
![Access rights permissions](Img\image-6.png)

### Step 6: Restarted Services

```bash
sudo systemctl restart wazuh-indexer
sudo systemctl restart wazuh-dashboard
sudo systemctl restart wazuh-manager
```

 Confirmed all services started successfully and dashboard became accessible.

**Screenshot dashboard access prompt:**  
![Dashboard Access](Img\image-7.png)



#### Outcome

The login issue was resolved by addressing password mismatches, updating the keystore securely, and regenerating SSL certificates with appropriate permissions. Dashboard is now accessible with updated credentials.








#### Appendix

- **Logs:** `/var/ossec/logs/ossec.log`, `journalctl -xeu wazuh-dashboard.service`  
- **Config files:** `/etc/wazuh-dashboard/opensearch_dashboards.yml`, `authentication.json`  
- **Tools used:** OpenSSL, systemctl, wazuh-passwords-tool





