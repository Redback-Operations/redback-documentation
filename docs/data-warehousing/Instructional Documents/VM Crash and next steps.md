---
sidebar_position: 50
---

#  After-Action Report: Data Warehouse Crash and Recovery (April 2025)

##  Summary

This document outlines the events, diagnosis, response, and lessons learned from a critical incident involving the Redback Data Warehouse (DW) VM, where all containers went down and the system became unresponsive due to a combination of user error and a rogue service (Suricata) flooding the disk.

This report serves both as documentation of leadership and technical response, and as a **reference for future team members** on how to handle similar VM-level issues.

---

##  Incident Overview

* **Date of Incident:** 15 April 2025
* **VM Services Affected:** All core DW services (MinIO, Dremio, File Upload Service, Postgres, etc.)
* **Initial Trigger:** Accidental execution of `docker rm -f dremio minioserver` followed by `docker compose up -d` by a teammate
* **Result:** Containers restarted incorrectly, data volumes not attached, and later VM became completely unresponsive due to full disk

---

##  Timeline & Root Cause Analysis

###  Phase 1: User Error

* A teammate mistakenly believed they were working in an isolated environment and ran the following command:

  ```bash
  docker rm -f dremio minioserver
  docker compose up -d
  ```
* Unfortunately, the wrong Docker Compose file (from the Streamlit file upload app) was used, which does **not map to the correct persistent volumes**.
* As a result, the new containers started without links to the historical data — making it appear as if data had been lost.

###  Phase 2: Leadership Response

* As the DW leader, I called my mentor Ben Stephens immediately, recognizing the severity of the incident.
* Ben advised checking whether volumes still existed — they did.
* We concluded that the data wasn't lost but rather the current containers weren’t mapped correctly.
* I attempted to locate and run the correct Docker Compose setup but couldn’t find the core DW folder.

###  Phase 3: Secondary Failure - Disk Full

* While troubleshooting with Sumit (another team lead with data engineering experience), we found:

  ```bash
  docker compose up -d
  => Error: no space left on device
  ```
* VM disk usage was at 100%, preventing any container restarts.
* Ben later found the root cause: **Suricata service had created 379GB of logs**, overwhelming the system.

###  Phase 4: Mentor Resolution

* Ben:

  * Disabled Suricata using `systemctl`
  * Removed excess logs and files (including 2GB initially without success)
  * Eventually recovered \~400GB of space
  * Confirmed it was safe to bring the DW stack back online

###  Phase 5: My Recovery Actions

* I searched for the `.env` file required to run the core DW `docker-compose.yml`.
* Located it in the **previous team leader’s directory**.
* Once `.env` was in place, I ran:

  ```bash
  docker compose --env-file .env up -d
  ```
* All containers restarted successfully, data volumes were reattached, and **DW was fully operational again**.

---

##  Lessons Learned

###  Technical

* **Containers in Docker are not user-isolated by default.**

  * Running `docker rm` on shared containers can affect everyone.
* **Volumes are persistent only if correctly mapped.**

  * Wrong compose file = containers without data.
* **Disk usage alerts/log rotation for system services** should be monitored — rogue services like Suricata can crash unrelated environments.

###  Team & Leadership

* Immediate escalation helped avoid damage.
* Involving experienced teammates (e.g., Sumit) accelerated recovery.
* Calm triage under pressure prevented further accidental damage.
* Mentor involvement at the right moment solved a system-level issue.

---

##  Recommendations

###  Technical Safeguards

* Use **container labels/namespaces** or Docker Compose project names to logically separate projects.
* Establish a **read-only directory for critical compose files** to prevent accidental edits or usage.
* Set up **disk usage monitoring** with alerts for system-wide usage > 80%.

###  Training & Awareness

* Onboard all users with a clear understanding of:

  * **Shared nature of the VM**
  * **Which Docker Compose files to use**
  * **Where persistent volumes are declared and mounted**
* Create a guide on **"How to safely run Docker containers in the DW VM"**

###  Preventive Measures

To proactively warn all users about the shared nature of the environment, a system-wide login message was added using the VM’s dynamic MOTD (Message of the Day) system. This banner appears every time a user logs in via SSH and highlights the risk of running destructive Docker commands like `docker rm -f`. This aims to prevent accidental container deletion and reinforces the importance of checking with the Data Warehouse leader before making changes.

* Added a disclaimer to critical command guides like:

  ```bash
  DO NOT run `docker rm -f` on shared containers unless confirmed with mentor or DW lead.
  ```

---

##  Conclusion

This incident highlighted the importance of:

* Good communication
* Team collaboration
* Calm leadership
* Technical clarity and documentation

Despite being outside my technical comfort zone, I led the response by:

* Immediately escalating to our mentor
* Bringing in experienced help
* Coordinating a recovery plan
* Taking ownership of getting DW back online

This documentation ensures that future leaders and contributors **do not repeat the same mistakes** and can follow a clear recovery path if a similar issue arises again.

---

*Document prepared by Daezel Goyal, Data Warehouse Leader – Redback Operations, May 2025*

