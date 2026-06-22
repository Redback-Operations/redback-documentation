---
sidebar_position: 6
sidebar_label: Dremio default API
---

# Beginner’s Guide to Dremio 25.x REST APIs

## 1. Introduction

Dremio is a modern data lakehouse platform designed to make it easier to access, query, and analyze data from multiple sources without heavy ETL pipelines. While many users interact with Dremio through its **user interface** or tools like **DBeaver** or **BI dashboards**, it also exposes a powerful **REST API**.

The REST API allows developers, analysts, and system administrators to **automate tasks**, **integrate Dremio with other systems**, and **query metadata** about datasets, sources, and jobs programmatically.

In this guide, we will walk through Dremio’s most important APIs using practical examples tested against Dremio **25.x**. Each section explains **what the endpoint does**, **how to call it with curl**, **sample responses**, and **common pitfalls**.

By the end, you’ll be able to:

* Authenticate against the Dremio API.
* Discover sources and datasets.
* Run SQL queries programmatically.
* Retrieve job results and dataset metadata.
* Explore reflections and catalog objects.
* Troubleshoot common issues.

This guide is **beginner friendly**, assumes you know a little about curl and JSON, but no prior Dremio API knowledge.



## 2. Authentication

All Dremio APIs are protected. To use them, you need a **token** in your HTTP `Authorization` header. There are **two ways** to get this token:

1. **Login API (`/apiv2/login`)** – authenticate with your username and password. This returns a temporary bearer token that usually expires in \~30 hours.
2. **Personal Access Token (PAT)** – generated once from the Dremio UI. PATs are better for automation and scripts, since they don’t expire as quickly.

### 2.1 Login with Username/Password

Request:

```bash
curl --location --request POST "http://redback.it.deakin.edu.au:9047/apiv2/login" \
  --header "Content-Type: application/json" \
  --data '{
    "userName": "jrees",
    "password": "your_password_here"
  }'
```

Response (example):

```json
{
  "token": "a9pu7d0aimhflnjp0fnnmuq4f0",
  "userName": "jrees",
  "firstName": "John",
  "lastName": "Rees",
  "expires": 1737500000000,
  "userId": "user_id"
}
```

* **token** → This is your bearer token. Copy it, you’ll use it in all subsequent requests.
* **expires** → A Unix timestamp when the token expires.
* **userId** → Useful if you need to query jobs or permissions related to this user.

Use the token in the `Authorization` header:

```
Authorization: Bearer a9pu7d0aimhflnjp0fnnmuq4f0
```

### 2.2 Using Personal Access Tokens (PAT)

PATs are generated in the Dremio UI under **User Settings > Personal Access Tokens**. Once created, the API usage looks like this:

```bash
curl --location --request GET "http://<hostname>:<port>/api/v3/catalog" \
  --header "Authorization: Bearer <your_pat_here>"
```

This is often preferred in production or CI/CD pipelines because you don’t want to embed your password in scripts.



## 3. Exploring Sources

**Sources** in Dremio are external systems connected to your Dremio environment (e.g., PostgreSQL, S3, ADLS, Hive, etc.). You can query them, create virtual datasets from them, and manage them via the API.

### 3.1 List All Sources

```bash
curl --location --request GET "http://redback.it.deakin.edu.au:9047/api/v3/source" \
  --header "Authorization: Bearer a9pu7d0aimhflnjp0fnnmuq4f0"
```

Response (simplified):

```json
{
  "data": [
    {
      "id": "Analytics",
      "type": "source",
      "config": {
        "name": "Analytics",
        "type": "POSTGRES",
        "host": "analytics-db.redback.it.deakin.edu.au",
        "port": 5432
      }
    },
    {
      "id": "S3_Store",
      "type": "source",
      "config": {
        "name": "S3_Store",
        "type": "S3",
        "accessKey": "****",
        "propertyList": []
      }
    }
  ]
}
```

Notice:

* Each source has an **id** and **config**.
* The `Analytics` source here is a PostgreSQL database.
* You can later query datasets inside `Analytics` like `Analytics.bronze_afl_players`.



## 4. Running SQL Queries

One of the most powerful features of Dremio is running SQL queries through its REST API.

### 4.1 Submitting a SQL Query

```bash
curl --location --request POST "http://redback.it.deakin.edu.au:9047/api/v3/sql" \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer $TOKEN" \
  --data '{
    "sql": "SELECT * FROM Analytics.\"bronze_afl_players\" LIMIT 5"
  }'
```

Response:

```json
{
  "id": "job_id",
  "rowCount": 5,
  "columns": [
    {"name": "player_id", "type": "INTEGER"},
    {"name": "name", "type": "VARCHAR"},
    {"name": "team", "type": "VARCHAR"}
  ],
  "rows": [
    [101, "John Smith", "Geelong"],
    [102, "James Doe", "Sydney"],
    [103, "Michael Lee", "Collingwood"],
    [104, "Andrew Chen", "Brisbane"],
    [105, "Sam Brown", "Melbourne"]
  ]
}
```

Explanation:

* `id` → Job ID. Every SQL execution creates a job, which you can later check for status or cancel.
* `rowCount` → Number of rows returned.
* `columns` → Schema of the dataset.
* `rows` → The actual data (first N rows).

### 4.2 Using Jobs API for Large Queries

If your SQL query is large, instead of immediately returning rows, Dremio will respond with a **job ID**. You can then poll the job status:

```bash
curl --location "http://<hostname>:<port>/api/v3/job/{job_id}" \
  --header "Authorization: Bearer <your_token>"
```

Response (example):

```json
{
  "id": "{job_id}",
  "state": "COMPLETED",
  "user": "jrees",
  "startedAt": 1737488000000,
  "endedAt": 1737488010000,
  "rowCount": 12000
}
```

If state is `RUNNING`, keep polling. Once `COMPLETED`, you can fetch results.



## 5. Working with Datasets

Datasets are tables, views, or virtual datasets defined in Dremio. After you query data or create a dataset, you can fetch its metadata or reflection recommendations.

### 5.1 Get Dataset Details

```bash
curl --location --request GET "http://redback.it.deakin.edu.au:9047/api/v3/dataset/{job_id}" \
  --header "Authorization: Bearer {token}"
```

Response (example):

```json
{
  "id": "{job_id}",
  "path": ["Analytics", "bronze_afl_players"],
  "type": "PHYSICAL_DATASET",
  "fields": [
    {"name": "player_id", "type": "INTEGER"},
    {"name": "name", "type": "VARCHAR"},
    {"name": "team", "type": "VARCHAR"}
  ],
  "createdAt": 1737400000000,
  "format": "PARQUET"
}
```

### 5.2 Reflection Recommendations

Dremio can recommend **Reflections** (materialized views) to speed up queries. To get them:

```bash
curl --location --request GET "http://redback.it.deakin.edu.au:9047/api/v3/dataset/`{job_id}`/reflection/recommendation/RAW/" \
  --header "Authorization: Bearer a9pu7d0aimhflnjp0fnnmuq4f0"
```

Response:

```json
{
  "recommendations": [
    {
      "type": "RAW",
      "fields": ["player_id", "team"],
      "estimatedSize": "10 MB"
    }
  ]
}
```



## 6. Catalog API

The catalog is a unified view of all objects: spaces, sources, folders, datasets, and views.

### 6.1 Get Entire Catalog

```bash
curl --location --request GET "http://redback.it.deakin.edu.au:9047/api/v3/catalog" \
  --header "Authorization: Bearer $TOKEN"
```

Response (simplified):

```json
{
  "data": [
    {
      "id": "Analytics",
      "path": ["Analytics"],
      "type": "SOURCE"
    },
    {
      "id": "Analytics.bronze_afl_players",
      "path": ["Analytics", "bronze_afl_players"],
      "type": "PHYSICAL_DATASET"
    },
    {
      "id": "Spaces",
      "path": ["Spaces"],
      "type": "SPACE"
    }
  ]
}
```

### 6.2 Search Catalog

You can search for objects:

```bash
curl "http://<hostname>:<port>/api/v3/catalog/by-path/Analytics/bronze_afl_players" \
  --header "Authorization: Bearer <your_token>"
```

Response:

```json
{
  "id": ".....",
  "type": "PHYSICAL_DATASET",
  "path": ["Analytics", "bronze_afl_players"]
}
```



## 7. Other Useful APIs

### 7.1 Jobs

* **GET /api/v3/job/`{job_id}`** → check job status.
* **DELETE /api/v3/job/`{job_id}`** → cancel a running job.

### 7.2 Reflections

* **GET /api/v3/reflection** → list reflections.
* **POST /api/v3/reflection** → create a reflection.
* **DELETE /api/v3/reflection/`{job_id}`** → delete.

### 7.3 Scripts

Dremio allows saving reusable SQL scripts:

* **GET /api/v3/scripts** → list scripts.
* **POST /api/v3/scripts** → create.



## 8. Common Errors and Troubleshooting

* **401 Unauthorized** → Token missing or expired. Get a new one with `/apiv2/login`.
* **403 Forbidden** → User lacks permission. Check dataset/source permissions.
* **404 Not Found** → Dataset or source doesn’t exist. Double-check path (`Analytics.table_name`).
* **500 Server Error** → Internal error. Sometimes caused by bad SQL or cluster overload.

Tip: Always test your SQL in the Dremio UI first before running it in the API.



## 9. Full Example Workflow

Here’s how a beginner might chain everything together.

```bash
# Step 1: Login
TOKEN=$(curl -s -X POST "http://redback.it.deakin.edu.au:9047/apiv2/login" \
  -H "Content-Type: application/json" \
  -d '{"userName":"jrees","password":"your_password"}' \
  | jq -r '.token')

# Step 2: List sources
curl -s -X GET "http://redback.it.deakin.edu.au:9047/api/v3/source" \
  -H "Authorization: Bearer $TOKEN"

# Step 3: Run a SQL query
JOB=$(curl -s -X POST "http://redback.it.deakin.edu.au:9047/api/v3/sql" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"sql":"SELECT * FROM Analytics.\"bronze_afl_players\" LIMIT 10"}' \
  | jq -r '.id')

# Step 4: Check job status
curl -s "http://redback.it.deakin.edu.au:9047/api/v3/job/$JOB" \
  -H "Authorization: Bearer $TOKEN"
```



## 10. Conclusion

The Dremio REST API opens up automation possibilities far beyond the GUI. You can:

* Automate ingestion and dataset discovery.
* Run scheduled SQL queries.
* Integrate with CI/CD for testing data pipelines.
* Manage reflections and accelerate performance.

As you get more comfortable, check out:

* [Dremio API Reference 25.x](https://docs.dremio.com/25.x/reference/api/)
* [Jobs API](https://docs.dremio.com/25.x/reference/api/jobs/)
* [Reflections API](https://docs.dremio.com/25.x/reference/api/reflections/)