---
sidebar_position: 1
title: Redback Data Warehouse - Complete Guide
---

# Welcome to the Redback Data Warehouse Complete Technical Guide

This document serves as a **comprehensive and current overview** of the Redback Operations Data Warehouse ecosystem. Whether you're a new team member, a project contributor, or just exploring how our infrastructure works — this guide will help you understand what services we run, why we run them, and how to use them.

This guide gives you the **big picture** — tying together MinIO, Dremio, the Streamlit File Upload System, Docker-based orchestration, and newer additions like Kafka, Airflow, and Restic — and will also contain reference links to all the individual service documentations in case there is a specific topic you need to explore in more detail.

If you ever feel stuck, reach out to the **Data Warehouse leadership** or your **mentor**. And if you spot anything missing or unclear, we encourage you to contribute!

Happy exploring !!


## The Virtual Machine (VM) – Core Infrastructure

The Redback Data Warehouse is hosted entirely on a dedicated **Deakin on-premises virtual machine** (VM), located within the university's infrastructure. This VM serves as the **central hub** for all data warehouse services and storage.

### Key Characteristics

- **Linux-based OS** (Ubuntu) maintained by Deakin IT
- **500GB local storage capacity**
- **No cloud capabilities** – all tools must be deployable on bare-metal
- **Docker-powered environment** – all services run in containers
- **Shared system** – used by multiple projects and users (cross-team)

### How the VM Powers the Warehouse

The VM hosts and runs all critical tools and services, including:

- MinIO (object storage)
- Dremio (query engine)
- MongoDB (NoSQL database)
- Streamlit File Upload Service
- Flask APIs
- Apache Airflow & Kafka (ETL & streaming)
- Spark, Elasticsearch, Postgres, and more

Each of these services runs in an isolated **Docker container**. This allows for flexible deployment, upgrades, and modular management — but comes with the caveat that **any restart or misconfiguration affects the shared production environment.**

>  VM operations require careful coordination. If you're unsure, check with a DW leader before restarting, modifying, or adding containers.


>  ⚠️**Important Warning – Shared VM Environment**
>
> The Redback Data Warehouse runs on a **shared production Virtual Machine (VM)** used by all teams. Any changes to services or containers affect everyone using the system.
>
> ⚠️ **Do NOT run destructive or high-impact commands** like `docker rm`, `docker volume rm`, or `docker-compose down` without first consulting the **Data Warehouse team lead** or your **mentor**.
>
> Such actions can:
> - Permanently delete project data or volumes
> - Break core infrastructure (MinIO, Dremio, Kafka, etc.)
> - Disrupt other projects that rely on running containers
>
>  Always coordinate changes or troubleshooting with team leadership. If unsure, ask first.

---

### VM Access Overview

Access is available to authorized users only via VPN + SSH:

1. Connect to Deakin VPN using Cisco AnyConnect
2. Access via terminal (`ssh yourusername@redback.it.deakin.edu.au`) or VSCode Remote SSH
3. Recommended: Create a personal working folder inside the VM and clone the GitHub repo

> Admins can create new VM users via `sudo adduser <username>`, but credentials must be shared securely.

---

### Docker Notes

- All services are listed via `docker ps`
- Restart core infrastructure with `docker compose up -d`

- **Persistent Volumes** are configured for critical tools like Dremio, MinIO, and Postgres to retain data even on restart

---

### Key Addresses

| Service                     | URL/Port                              |
|-----------------------------|------------------------------------   |
| VM SSH                      | `ssh <user>@redback.it.deakin.edu.au` |
| File Upload Service         | http://10.137.0.149:80/               |
| MinIO                       | http://10.137.0.149:9001/login        |
| Dremio                      | http://10.137.0.149:9047/             |
| MongoDB API                 | http://10.137.0.149:5003/documents    |
| Spark Jupyter Notebooks     | http://10.137.0.149:8888/             |
| Flask API (Downloads)       | http://10.137.0.149:5000/             |
| Kibana (Logs - if active)   | http://10.137.0.149:5601/             |

---

> See full access steps and Docker commands in the [VM Access Guide (ONB2)](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Instructional%20Documents/VM%20Guide)


## Background – Requirements Gathering Summary

Before building the Redback Data Warehouse infrastructure, a structured **requirements gathering process** was conducted through stakeholder meetings and surveys. The goal was to understand project-level and company-wide needs and evaluate suitable Data Lakehouse solutions.

### Key Pain Points Identified:
- No centralized platform for storing and accessing company-wide data.
- Frequent issues with updating datasets (manual Git workflows).
- Need for **supporting both structured and unstructured data**.
- Budget constraints and student turnover requiring low-code, easy-to-learn tools.
- Licensing issues tied to individual users — not scalable for rotating student teams.

### Key Requirements Defined:
- Must scale to accommodate multiple projects.
- Supports CSV, JSON, media, and other object formats.
- Low technical entry barrier (GUI, minimal setup).
- Free/open-source or trial-based licensing preferred.
- Centralized data access and governance.

Based on these, tools like **MinIO, Dremio, MongoDB, and Apache Airflow** were selected and tested.

> [View Full Requirements Document](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Data%20Lakehouse/Data%20Warehouse%20Requirements)


## Data Architecture & Platform Rationale

Redback Operations adopted a **Data Lakehouse architecture** in Trimester 1, 2024, after operating without a centralized data platform. Initial requirements were gathered through interviews and surveys with project and company leaders, which led to a focus on open-source, scalable, and VM-compatible technologies.

Since then, the platform has grown significantly and now supports real-time pipelines, orchestration tools, automated backups, and enhanced governance layers — all running on a shared Dockerized VM environment.

---

### Why a Data Lakehouse?

A Data Lakehouse combines the flexibility of a Data Lake with the governance features of a Data Warehouse. This hybrid design supports:

- Native file/object storage (CSV, JSON, images, etc.)
- SQL-compatible querying (via Dremio)
- Versioning and rollback (via Apache Iceberg + Nessie)
- Cost-effective, on-premises deployment on the Deakin VM
- Centralization for collaboration across rotating student teams

---

### Tools Currently in Use (T1 2025)


| Tool / Service                 | Role in Ecosystem                                                                    |
|--------------------------------|--------------------------------------------------------------------------------------|
| **Dremio**                     | SQL query engine + GUI frontend for browsing and querying data                       |
| **MinIO**                      | S3-compatible object storage backend for both raw (Bronze) and cleaned (Silver) data |
| **Streamlit App**              | Upload interface for data files with optional preprocessing                        |
| **MongoDB**                    | JSON storage for semi-structured data used by various projects                       |
| **PostgreSQL**                 | Provenance metadata store (used in ELK pipelines)                                    |
| **Apache Iceberg**             | ACID-compliant table format for versioned datasets in Dremio                         |
| **Nessie**                     | Metadata catalog and rollback manager for Dremio (experimental stage)                |
| **Flask API**                  | Enables safe, secure data querying and file downloads via HTTP                       |
| **Kafka**                      | Message broker used for real-time pipelines (e.g., Project 4 image ingestion)        |
| **Apache Airflow**             | Orchestrates processing pipelines triggered by Kafka or scheduled jobs               |
| **FastAPI**                    | API layer connecting frontend uploads to backend workflows (Kafka + Airflow)         |
| **Docker**                     | Container orchestration for all services running on the shared production VM         |
| **Restic**                     | Docker-based backup solution for key volumes and containers                          |
| **Spark Notebooks**            | Jupyter + Spark environment (available, but not in active use)                       |
| **ClamAV**                     | Virus scanner container for uploaded files (currently experimental)                  |
| **Wazuh**                      | Security monitoring suite (shared with Cybersecurity team on VM)                     | 
| **Elasticsearch**               | Indexes logs from all tools (provenance)                                             |
| **Logstash**                   | Pipeline to parse & forward logs                                                     |
| **Kibana**                     | Log dashboard/visualisation tool (not active)                                        |
| **PostgreSQL (Provenance)**    | Structured storage of event logs                                                     |
| **Restic**                     | Docker volume backup system                                                          |

> All services are deployed on a shared Linux-based VM (`redback.it.deakin.edu.au`) using Docker. Admin rights and service restarts should be handled with care.

---

### Medallion Architecture

Redback follows the Medallion Lakehouse model — a layered storage strategy:

- **Bronze Layer**: Raw, unprocessed source data. Not user-editable.
- **Silver Layer**: Cleaned and transformed data. Stored in Iceberg format for versioning.
- **Gold Layer**: Final, analysis-ready data with specific aggregations or scopes.

Folder layout follows:  
`/project_name/YYYY/tX_task_name/student_ID (optional)`

This standard helps with both governance and future orchestration.

---

### Typical Data Flow

1. **Upload** data via Streamlit (or direct upload to MinIO)
2. **Store** in Bronze bucket (raw layer)
3. **ETL pipeline** processes file into Silver bucket (cleaned layer)
4. **Register/query** data using Dremio (optionally build Gold tables/views)
5. **(Optional)**: Use Airflow/Kafka for automated workflows

> [View full Data Architecture](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Data%20Lakehouse/Data%20Architecture)

---

## MinIO – Object Storage Backbone of the Data Warehouse

MinIO is the core object storage system used in the Redback Data Warehouse infrastructure. It functions similarly to AWS S3, allowing users to store and retrieve files through programmatic APIs or a friendly web-based GUI. It plays a **central role in storing raw and processed datasets**, especially CSV, TXT, JSON, XLSX files used in the File Upload Service and downstream tools like Dremio.

### Accessing MinIO

- **URL:** `http://10.137.0.149:9000`
- **Admin Portal:** `http://10.137.0.149:9001`
- **Credentials:** Not included here; contact the DW Team Leader or Mentor for access.

Once logged in, users will see a UI displaying MinIO "buckets" — essentially folders for storing categorized files.

> **Default Bucket for Uploads:** `dw-bronze-bucket`  
> Files uploaded via the Streamlit File Upload App are saved here before preprocessing or ETL.

### Bucket Structure

MinIO separates data into **Bronze** and **Silver** tiers:
- **Bronze Bucket:** Stores raw, unprocessed uploads.
- **Silver Bucket:** Stores cleaned, preprocessed files after ETL transformations.

This clean separation supports better **data governance** and makes it easy for tools like Dremio to distinguish between staging and production data.

| Bucket Name        | Purpose                                |
|--------------------|----------------------------------------|
| `dw-bronze-bucket` | Raw files uploaded via UI or manually  |
| `dw-silver-bucket` | Cleaned/preprocessed data from ETL     |

---

### How to Use MinIO – GUI vs Code

#### GUI Access (User-Friendly Option)
1. Navigate to [MinIO Admin Portal](http://10.137.0.149:9001)
2. Login using your assigned credentials.
3. Browse, upload, delete, or organize files within project-specific folders.
4. You can also generate new Access Keys and Secret Keys for programmatic use.

#### Programmatic Access (Recommended for Scripts)
MinIO can be accessed using the official Python SDK (`minio`), behaving like AWS S3.

```python
from minio import Minio
import os

client = Minio(
    "10.137.0.149:9000",
    access_key=os.getenv("AWS_ACCESS_KEY"),
    secret_key=os.getenv("AWS_SECRET_KEY"),
    secure=False
)

```

>[click here to view minio guide](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Instructional%20Documents/MinIO%20Guide)



## Dremio – Interactive SQL Engine & Lakehouse UI

Dremio is the **query engine and interactive layer** for the Redback Data Warehouse. It connects to data stored in MinIO and MongoDB, allowing users to create virtual SQL tables and run queries directly from a browser or code interface.

Unlike traditional database engines, Dremio reads directly from **object storage** (MinIO), and allows teams to build **virtual tables** ("views") on top of raw data — without duplication. Its graphical interface and SQL endpoint make it easy to use for both analysts and developers.

---

### Why Dremio?

- **Cost-effective**: Free and open-source.
- **User-friendly**: Comes with a full GUI and SQL editor.
- **Multi-source capable**: Can query data from MinIO, MongoDB, PostgreSQL, and more.
- **Time-travel support**: Enables data versioning with formats like Apache Iceberg and Parquet.
- **Safe query execution**: Uses a proxy Flask API to limit risky SQL commands.

---

### Accessing Dremio

- **Dremio Web UI**: `http://10.137.0.149:9047`
- **Flask SQL API**: `http://10.137.0.149:5001/dremio_query`
- **Access**: VPN required (Cisco AnyConnect)  
  Login credentials are provided by the Data Warehouse team leader or mentor.

---

### Connecting MinIO to Dremio (Source Setup)

1. In the Dremio UI, click **“Add Source”**.
2. Select **Amazon S3** as the source type.
3. Use the **Access Key** and **Secret Key** from MinIO to authenticate.
4. In **Advanced Options**:
   - Tick `Enable Compatibility Mode`
   - Provide the bucket path (e.g., `/project-2`)
   - Add required connection properties.
5. Click **Save**.

Once saved, the MinIO bucket will be visible as a data source within Dremio’s **“Sources”** tab.

---

### Creating Tables in Dremio (Two Ways)

#### Option 1: Using SQL Editor in GUI

- Navigate to the SQL tab in Dremio.
- Write a SQL `SELECT`, `JOIN`, or `CREATE VIEW` statement.
- Save the view as a virtual table to use in future queries.

#### Option 2: Scripted Pipeline

A Python script (`pipeline.py`) exists in the Redback repository (currently in a forked branch) which:
- Takes a CSV file from MinIO
- Automatically creates a Dremio SQL view
- Registers it for downstream queries

> This automates ingestion + query registration for power users and is expected to be merged soon into the official repo.

---

### Using Flask API to Query Dremio via Code

Redback also provides a **Flask API interface** that lets users query Dremio securely using only `SELECT` statements.

Here’s an example Jupyter notebook workflow:

```python
import requests
import json
import pandas as pd

api_url = "http://10.137.0.149:5001/dremio_query"
headers = { "Content-Type": "application/json" }

sql_query = {
    "sql": "SELECT * FROM \"project-3\".\"extended_activities\" LIMIT 10;"
}

response = requests.post(api_url, headers=headers, data=json.dumps(sql_query))
result = response.json()

df = pd.DataFrame(result['rows'])
display(df)
```

> [click here to view dremio guide](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Instructional%20Documents/Dremio%20Guide)

> [Other useful documents - maintaining structured dremio solution](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Dremio/Managing-the-structured-solution)

> [other useful documents - how to access stored data in dremio](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Dremio/Dremio-API)

## Streamlit File Upload Service – Uploading & Managing Files in the DW

The **File Upload Service (FUS)** is a web-based interface built using Streamlit. It allows users to upload CSV files to the Data Warehouse in a structured and governed way. Uploaded files are stored in **MinIO buckets** under project-specific folders and optionally processed before storage.

This service is especially useful for team members who need a simple way to upload, clean, and manage datasets without directly interacting with the VM or MinIO backend.

---

### Accessing the File Upload Interface

The Streamlit app is hosted on the Redback Data Warehouse Virtual Machine.

- **URL**: `http://10.137.0.149/` (default root port (80))
- **VPN Required**: Connect using Cisco AnyConnect to access the internal network.
- **Authentication**: Once VPN is active, no additional login is required for the app.

---

### How to Upload a File

1. **Select Your Project**
   - Choose the project folder where your file will be stored (e.g., `project-1`, `project-3`).

2. **Upload File**
   - Drag and drop a file or browse for one. 
   - At the time of writing, the file formats supported by file upload service are - CSV, TXT, JSON, XLSX

3. **Choose Preprocessing (Optional)**
   - **None**: File is uploaded as-is.
   - **Data Clean-Up**: Removes empty columns, duplicate rows, standardizes format.
   - **Machine Learning Prep**: Scales numeric features, handles missing values, optimizes for ML tasks.

4. **Filename Options**
   - By default, a **prefix** and **timestamp suffix** are added (recommended for governance).
   - Unticking the box allows you to overwrite an existing file by using the same filename.

5. **Submit Upload**
   - Click the **Upload to Data Warehouse** button.
   - A success or error message will appear.

> Uploaded files are stored in the `dw-bronze-bucket` in MinIO. If preprocessing is applied, the cleaned version is saved in the `dw-silver-bucket`.

---

### What about ETL?

- ETL is a separate trigger, not automatically tied to upload.
- In most cases, ETL also reads from dw-bronze-bucket, transforms the data, and may overwrite or add new files to Silver — depending on the pipeline setup.
- If preprocessing wasn't selected during upload, then Silver won't have that file until ETL moves it there.

### Behind the Scenes: What Happens After Upload?

- Uploaded file → stored in **MinIO** under selected project folder.
- If preprocessing is selected:
  - A Python script processes the file using **Pandas**.
  - Resulting cleaned file is uploaded to `dw-silver-bucket`.
  - Metadata is appended (e.g., extract date, unique ID).

---

### Downloading Files

#### Option A: Programmatic Access via Flask API

You can retrieve files from the VM using the Flask API:

**Example – Using Python:**
```python
import requests

url = "http://10.137.0.149:5000/download-file"
params = {
    "bucket": "dw-bucket-bronze",
    "filename": "project3/testdocument_20240921.csv"
}

response = requests.get(url, params=params)
with open("downloaded_file.csv", "wb") as f:
    f.write(response.content)
```

We are showing the **Bronze bucket** here, but it works exactly the same for Silver too — just change the bucket name.

---

#### Option B: Using `curl` in Terminal

```bash
curl -o file.csv "http://10.137.0.149:5000/download-file?bucket=dw-bucket-bronze&filename=project3/testdocument_20240921.csv"
```

---

#### Option C: Download via the Streamlit UI

1. Go to: `http://10.137.0.149/`
2. Select the appropriate tab:

   * **View Original Files** (Bronze bucket)
   * **View Pre-Processed Files** (Silver bucket)
3. Choose the relevant project from the dropdown.
4. Select a file and click **Download**.

When you click the download button, the app shows the corresponding Flask API URL used under the hood.

#### Option D: Download directly from backend (Minio)

1. Navigate to correct folder/file and manually download file.

> [click here to view file upload service guide](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Instructional%20Documents/How%20To%20Access%20The%20File%20Upload%20Service)

> [streamlit setup documentation] (https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Streamlit%20tutorial/streamlit_tutorial)  - In case you need to work on implementing some upgrades in the existing file upload service or due something of your own using streamlit, this guide will be handy


## Other Available Services (Not in Full Production)

The following services are deployed on the VM but are not currently in active production use. They may be utilized in future phases or specialized projects.

- **Project Nessie**  
  A metadata store integrated with Dremio. Enables version control and historical tracking of datasets. Proof of concept complete, but not actively used yet.  

- **Apache Spark (Jupyter Notebooks)**  
  Jupyter environment running on the VM at `http://10.137.0.149:8888/`. Supports distributed Spark jobs for large-scale data processing. Currently idle due to lack of large production datasets.  

> [click here to view documentation on additional services](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Instructional%20Documents/Not%20in%20Prod)

##  MongoDB Connection Service

MongoDB is used within the Data Warehouse for storing **semi-structured data**, such as `.json` documents. To make this easier for teams to use, a dedicated **web server/API** has been set up that interacts with MongoDB using RESTful endpoints.

### Setup Overview (Admin/Dev Use)

- Repository: `redback-data-warehouse/MongoDB Connection`
- Services are containerized using **Docker Compose**
- `.env` file must include:
  - `MONGO_URI`
  - `DB_NAME`
  - `COLLECTION_NAME`
- Run with:  
  ```bash
  docker-compose up --build

> [click here to view detailed guide on MongoDB](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/MongoDb%20Connection/mongodbconnection)

## Mosquitto MQTT Broker (IoT Messaging)

The Data Warehouse VM hosts a lightweight **Mosquitto MQTT Broker**, primarily for **real-time messaging** and **IoT simulation use cases**.

### What is MQTT?

MQTT (Message Queuing Telemetry Transport) is a lightweight protocol ideal for low-overhead, publish/subscribe-based communication. It’s commonly used in IoT environments or systems requiring fast, low-bandwidth updates.

---

### Key Details

- **Broker IP**: `10.137.0.149`
- **Port**: `1883` (default, unencrypted)
- **Anonymous Access**: Enabled  
- **Persistence**: Enabled (messages survive broker restarts)
- **Logs**: `/var/log/mosquitto/mosquitto.log`

---

### Setup Notes

Installed via:
```bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

> [Click here to view guide on Mosquitto MQTT](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Mosquitto/mosquitto_documentation)

## Restic-Docker Backup System

The Data Warehouse includes an automated backup system using **Restic** — a secure, open-source tool for backing up Docker volumes on the VM.

### Purpose

This system ensures that critical services like **MinIO**, **PostgreSQL**, **Dremio**, and **Elasticsearch** are backed up regularly. If a container crashes or data is accidentally lost, snapshots allow for fast recovery.

---

### What Gets Backed Up?

Restic monitors and stores snapshots of the following Docker volumes:

- `data-lakehouse_minio-data`
- `data-lakehouse_minio-config`
- `fileuploadservice_dremio-data`
- `dp-postgres-data`
- `dp-es-data` *(Elasticsearch)*
- `dp-logstash-data`

> All these volumes are tied to key components of the data platform (storage, search, provenance, etc.).

### Setup Overview (Admin Use Only)

To deploy the Restic backup system:

1. **Clone the repo** and navigate to the Restic directory:

   ```bash
   git clone https://github.com/Redback-Operations/redback-data-warehouse.git
   cd restic
   ```

2. **Create required volumes** *(if not already present)*:

   * `data-lakehouse_minio-data`
   * `fileuploadservice_dremio-data`
   * `dp-postgres-data`, etc.

3. **Add your Restic password** to `restic-password.txt`

4. **Start the service**:

   ```bash
   chmod +x scripts/backup.sh
   docker-compose up -d
   ```

5. **Check logs or restore snapshots** using:

   ```bash
   docker exec -it restic-backup sh
   restic snapshots
   ```


> For complete instructions, including customisation and snapshot restoration, refer to the [Restic Full Guide](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Restic/)


## Kafka + Airflow Stack

A Kafka-based real-time pipeline is now operational on the VM, originally developed for Project 4. This stack integrates **FastAPI**, **Kafka**, and **Airflow**, and it's designed to support **event-driven workflows** and **automated DAG triggering**.

>  This system is not limited to images — it can be adapted to trigger workflows from **any kind of file upload, sensor input, log event, or status change**.

---

### Core Use Case Pattern

```text
User Uploads File/Trigger Event
        ↓
FastAPI → Kafka Producer
        ↓
Kafka Topic (event ingestion)
        ↓
Airflow DAG triggered via API
        ↓
Kafka Topic (result or signal)
        ↓
FastAPI Kafka Consumer → Result returned/logged

```

### Common Use Cases for Other Teams

Here are examples of how teams across Redback can reuse this system without setting up Kafka/Airflow from scratch:

#### Data Cleaning Pipelines
Upload a data file through a Streamlit or FastAPI form → send to a Kafka topic → trigger Airflow DAG that:
- Cleans null values
- Validates schema
- Pushes cleaned data to the Silver bucket in MinIO

#### ML Inference on Upload
Send image/audio/text files via Kafka → trigger Airflow DAG to:
- Run object detection, classification, or sentiment analysis
- Store results back into MongoDB or Dremio
- Notify user via FastAPI return or log entry

#### Data Cataloging or Metadata Extraction
Trigger a DAG when a new file is added to MinIO that:
- Reads basic metadata (rows, columns, types)
- Tags the file or stores metadata in PostgreSQL
- Optionally emails or posts a summary to Teams/Slack

#### Real-Time Dashboard Updating
Send sensor data or user entries via Kafka → DAG aggregates & stores latest stats → Dashboards pull new numbers without delay

---

### How to Reuse This Pipeline

You don’t need to build a new Kafka setup. Just follow these steps:

#### Step 1: Create a Kafka Topic (Optional)
Ask the DW team to help create a new topic (e.g., `project5-cleaning-topic`) or reuse an existing one.

#### Step 2: Write Your Airflow DAG
Your DAG should:
- Listen for an incoming trigger (e.g., a filename, ID, or metadata)
- Fetch the related file or data
- Perform the required task (cleaning, prediction, merging, etc.)
- Optionally publish back to Kafka or save to a storage system

*Example DAG trigger:*
```python
@dag(schedule_interval=None)
def clean_csv_on_trigger():
    # Pulls file info from Kafka or API
    # Runs cleaning steps
    # Stores clean file to MinIO Silver bucket

```

> documentation on this currently Work in progress. For now, this is the link of repository which contains the readme file and other information [Kafka and airflow stack](https://github.com/sumituiet/kafka_python/blob/main/README.md)

Sure! Here's the updated version of the **Data Warehouse Administration** section in clean Markdown:


## Administrative Services Overview

Beyond the core upload and query systems, the Redback Data Warehouse includes several **under-the-hood services** for tracking, recovery, and observability — mostly handled by the admin or DW lead.

### Data Provenance Pipeline

A provenance pipeline was introduced to **track system-level changes** across services — including uploads, deletions, access logs, and transformations.

It uses the **ELK Stack** (Elasticsearch, Logstash, Kibana) with **PostgreSQL** as a central provenance store.

* **Elasticsearch**: Stores logs as JSON, searchable via:

  * [MinIO Logs](http://10.137.0.149:9200/minio-*/_search?pretty/)
  * [Upload Logs](http://10.137.0.149:9200/upload-service-*/_search?pretty/)
* **Logstash**: Parses logs and forwards them to Elasticsearch.
* **Kibana**: Optional frontend for dashboarding. Available at `http://10.137.0.149:5601`
* **PostgreSQL**: Long-term metadata store; access it using:

  ```bash
  docker exec -it postgres psql -U <username> -d <database-name>
  ```

> Note: No dashboards have been set up in Kibana yet, but the stack is running and can be extended.

> [click here to view detailed information on this](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Instructional%20Documents/Data%20Warehouse%20Overview)

---

## Final Notes

This guide has aimed to provide a **complete and current overview** of the Redback Data Warehouse ecosystem — from data ingestion and processing to storage, querying, and backup. Whether you're a new contributor or a returning team member, this documentation should help you navigate the platform, understand the role of each component, and collaborate more effectively across teams.

As the platform evolves, so will this guide. If you notice missing pieces or have improvements to suggest, please contribute or notify the current Data Warehouse lead. Let’s keep building better data infrastructure — together. 

---

*version 1 - Document prepared by Daezel Goyal, Data Warehouse Leader – Redback Operations, May 2025*


