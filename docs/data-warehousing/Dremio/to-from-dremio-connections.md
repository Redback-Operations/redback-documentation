---
sidebar_position: 6
sidebar_label: Adding Data Sources to Dremio
---

# **Adding Data Sources to Dremio (Community Edition)**
_(Docker-hosted setup)_
## **1. Introduction**
Dremio lets you connect to multiple heterogeneous data sources — relational databases, NoSQL stores, cloud/object storage, and file systems — and **query them using SQL without moving data**.
In this guide, you’ll learn how to:
*   Connect **PostgreSQL**, **MongoDB**, and **MinIO** (S3-compatible storage).
*   Understand every field in Dremio’s **Add Source** dialogs.
*   Enable **advanced options** for better performance and security.
*   Perform a **quick analysis** by uploading datasets and querying them instantly.
## **2. Prerequisites**
*   **Environment:** Dremio Community Edition running on **Docker**`docker ps | grep dremio
`Default Dremio UI: [http://redback.it.deakin.edu.au:9047](http://redback.it.deakin.edu.au:9047)
*   **Database Access:**
	*   PostgreSQL: hostname, port, database name, username, password.
	*   MongoDB: connection URI or host/port, username/password, replica set (if applicable).
	*   MinIO: endpoint URL, access key, secret key, and bucket permissions.
*   **Browser Access:** Use an **admin** account in Dremio UI.
*   **User Privileges:**
	*   PostgreSQL: **read-only** or **reporting role**.
	*   MongoDB: must allow running `dbStats`.
	*   MinIO: allow **read/write** on desired buckets.
## **3. Connecting PostgreSQL**
### **Step 1 — Navigate to Add Source**
*   Go to **Datasets** → **Sources** → **Add Source**.
*   Select **Databases** → **PostgreSQL**.
### **Step 2 — Fill General Fields**
|**Field**|**Description**|**Example Value**|
|---|---|---|
|**Source Name**|Friendly name for this source.|`postgres`|
|**Host**|PostgreSQL server hostname or IP.|`<postgresql_`_`container_`_`IP>`|
|**Port**|PostgreSQL port (default).|`5432`|
|**Database**|Database name to connect to.|`db`|
|**Username**|User with read permissions.|`dremio_user`|
|**Password**|Password for above user.|`mypassword`|
### **Step 3 — Configure Advanced Options**
Click **Advanced Options** and set:
|**Option**|**Purpose**|**Recommended Setting**|
|---|---|---|
|**Enable External Query**|Allows Dremio to push down full SQL queries to PostgreSQL instead of fetching all data first.|✅ Enable|
|**Encrypt Connection**|Use TLS for secure environments.|Enable if supported|
|**Fetch Size**|Controls number of rows per batch.|Default is fine unless tuning|
|**Enable Metadata Refresh**|Dremio will periodically refresh table/column metadata.|✅ Enable|
### **Step 4 — Save & Verify**
*   Click **Save**.
*   Go to **Datasets** → expand your new source → select a schema → preview a table.
*   Run a simple query in **SQL Runner**:`SELECT *
FROM "postgres_sales"."public"."orders"
FETCH FIRST 10 ROWS ONLY;
`
## **4. Connecting MongoDB**
### **Step 1 — Navigate to Add Source**
*   Go to **Datasets** → **Sources** → **Add Source**.
*   Choose **Databases** → **MongoDB**.
### **Step 2 — Fill General Fields**
|**Field**|**Description**|**Example Value**|
|---|---|---|
|**Source Name**|Friendly name for Mongo source.|`mongo_ops`|
|**Connection Type**|Choose between **Standalone**, **Replica Set**, or **SRV URI**.|`Standalone`|
|**Host(s)**|Hostnames/IPs of Mongo nodes.|`mongodb_container_IP`|
|**Port**|MongoDB port.|`27017`|
|**Authentication DB**|DB where user credentials are stored.|`admin`|
|**Username**|Mongo user with read permissions.|`dremio_reader`|
|**Password**|Password for above user.|`mypassword`|
|**Database(s)**|Optional — restrict to certain databases.|`db`|
### **Step 3 — Advanced Options**
|**Option**|**Purpose**|**Recommendation**|
|---|---|---|
|**Enable SSL/TLS**|Encrypt data in transit.|Enable if configured|
|**Replica Set**|Add if connecting to a Mongo replica cluster.|Enter replica set name|
|**Auth Mechanism**|Choose SCRAM-SHA-1, SCRAM-SHA-256, or LDAP if required.|Default: SCRAM|
|**Sampling**|Limit data fetched for schema detection.|Keep default unless schema is huge|
### **Step 4 — Save & Verify**
*   Click **Save**.
*   Expand **mongo_ops** in **Datasets** and open any collection.
*   Run a query:`SELECT _id, customerId, total
FROM "mongo_ops"."shopdb"."orders"
FETCH FIRST 10 ROWS ONLY;
`
> **Important:**User must have `dbStats` privileges; otherwise, Dremio cannot read schema details.
## **5. Connecting MinIO (S3-Compatible)**
### **Step 1 — Navigate to Add Source**
*   Go to **Datasets** → **Sources** → **Add Source**.
*   Choose **Object Storage** → **Amazon S3**.
### **Step 2 — Fill General Fields**
|**Field**|**Description**|**Example Value**|
|---|---|---|
|**Source Name**|Friendly name for MinIO source.|`minio_s3`|
|**AWS Access Key**|MinIO access key.|`minioadmin`|
|**AWS Secret Key**|MinIO secret key.|`minioadmin`|
|**Root Path**|Optional — restricts access to a specific bucket/path.|`sales-bucket`|
|**Connection Type**|Choose between **AWS Default** or **Custom Endpoint**.|Custom Endpoint|
|**Endpoint**|MinIO endpoint (URL).|`http://<minio_container_IP>:9000`|
### **Step 3 — Advanced Options**
|**Option**|**Purpose**|**Recommendation**|
|---|---|---|
|**Enable Compatibility Mode**|Required for S3-compatible services like MinIO.|✅ Enable|
|**Path-Style Access**|Ensures MinIO buckets resolve correctly.|✅ Set `fs.s3a.path.style.access=true`|
|**Encryption**|Use if MinIO buckets are encrypted.|Configure if applicable|
### **Step 4 — Save & Verify**
*   Click **Save**.
*   Browse **minio_s3** under **Datasets** → select your bucket → preview CSV/Parquet files.
*   Query example:`SELECT *
FROM "minio_s3"."sales-bucket"."olist_orders_dataset"
FETCH FIRST 10 ROWS ONLY;
`
## **6. Quick Analysis Workflow**
For instant dataset exploration:
### **Step 1 — Create a Space**
*   Go to **Datasets → Spaces → New Space**.
*   Example: `Quick_Analysis`.
### **Step 2 — Upload a Dataset**
*   Go to **Home** or your **Quick_Analysis** space.
*   Click **Upload File**.
*   Supported formats: CSV, JSON, Parquet, Excel.
*   Dremio automatically promotes uploaded files to datasets.
### **Step 3 — Start Querying**
```
SELECT *
FROM "@Quick_Analysis"."olist_customers_dataset"
FETCH FIRST 20 ROWS ONLY;
```
### **Step 4 — Save Cleaned Data**
*   Transform your query.
*   **Save As** → `Quick\_Analysis/Cleaned/olist\_customers_vds`.
## **7. Best Practices & Troubleshooting**
|**Area**|**Recommendation**|
|---|---|
|**Security**|Use TLS, least-privilege DB accounts, and avoid root users.|
|**Performance**|Enable external query pushdown and reflections.|
|**Organization**|Save curated datasets in **Spaces**, not **Home**.|
|**Troubleshooting**|Check MinIO compatibility mode, Mongo `dbStats` permissions, and PostgreSQL firewall rules.|

