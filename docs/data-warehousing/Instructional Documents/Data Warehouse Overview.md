--- 
sidebar_position: 2
sidebar_label: Data Warehouse Overview
---

# Data Warehouse Administration

:::info
**Document Creation:** 22 September, 2024. **Last Edited:** 29 April, 2025. **Authors:** kghdxx, Jesse Rees, nouri-devv.
<br></br> **Document Code:** ONB1. **Effective Date:** 22 September 2024. **Expiry Date:** 29 April 2026.
:::

The Data Warehouse in Redback Operations exists to serve the company by providing storage and Data Warehouse solutions to the associated Projects in Redback Operations.
It has been the goal of Data Warehouse to provide multiple options and satellite services that accompany our overall aim to enhance the data quality, ease-of-access and governance of Redback Operations.

This document contains information on the different parts of the Data Warehouse and brief explanations on how they work. It does not expand on the individual 'Data Warehouse Solutions' which all have their own documentation. Instead, this document outlines how to use the tools of the Data Warehouse project from an administrator's perspective.

Data Warehouse has three 'Data Warehouse Solutions' that can facilitate company data.

- The File Upload Service
This is based in a streamlit app, it can take data and store it in a folder on the VM the files can be viewed in a separate tab, downloaded from the VM and replaced.
It has built-in preprocessing for data clean-up and Machine learning specific pre-processing for .csv files. located here: [File Upload Service](http://10.137.0.149:80/)

- The Structured Dremio Solution
The Dremio solution takes structured data (flat files, .csv .xlsx) and stores them on the virtual machine in a MinIO object store. From here the data is connected to the Dremio user interface where tables can be created from SQL commands.
The data can be access out through the UI or through a Flask API that connects to Dremio and can retrive data based on SQL statements in the API request. Located here: [Dremio](http://10.137.0.149:9047/) with documentation here: [Structured Solution Documentation](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Data%20Lakehouse/Managing-the-structured-solution)

- The Semi-structured MongoDB solution
The MongoDB solution takes semi-structured data in the form of .json files from Redback projects and parses them into the MongoDB database that runs on the virtual machine. The data is able to be accessed back out through either an API or the MongoDB Atlas user interface. The MongoDB solution is also a source of data for the Dremio UI and can be queried there also.
[MongoDB API](http://10.137.0.149:5003/documents)
 

A main part and fundamental aspect of the Data Warehouse is its storage base which is a Deakin Virtual Machine. 

### Credentials and Admin Users

There are many credentials for each tool or software associated with the Data Warehouse.

There is a list of credentials that is maintained by the **Data Warehouse leader & Mentor** will also have access and if appropriate, will be able to grant access to new users.

There is not nor should there be credentials in plain text for Data Warehouse files.


## Further Services

### Data Provenance Pipeline

A key part of the infrastructure introduced in T3 of 2024 was the provenance pipeline with the purpose of tracking and storing historical meta data about all changes that occur in the system including data upload, transformation, access, deletion, etc.

The key aspects of the pipeline are the ELK stack (elasticsearch, logstash, kibana) and a postgres database acting as a provenance store.

### Logstash 

Logstash is a tool for parsing data of various schemas and formats and directing them to another source, it is running on port 5044 though is only access through code.

### Elasticsearch 

Elasticsearch is the storage and querying tool for logs and has its own external volume and the raw json storage can be accessed through the below ports.

See indexes: [http://10.137.0.149:9200/_cat/indices?v](http://10.137.0.149:9200/_cat/indices?v)

Query minio logs: [http://10.137.0.149:9200/minio-*/_search?pretty/](http://10.137.0.149:9200/minio-*/_search?pretty/)

Query file upload service logs: [http://10.137.0.149:9200/upload-service-*/_search?pretty](http://10.137.0.149:9200/upload-service-*/_search?pretty)

### Postgres

Postgres is the provenance store and must be accessed after terminal ssh into the VM using this command:

```sh
docker exec -it postgres psql -U <username> -d <database-name>
```

### Kibana

Kibana is a tool for visualizing the logs stored in elasticsearch. Whilst it is connected to elasticsearch and operational, no dashboards have been created as of yet.

Kibana: [http://10.137.0.149:5601](http://10.137.0.149:5601)
  


