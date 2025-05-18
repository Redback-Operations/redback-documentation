---
sidebar_position: 1
sidebar_label: Dremio Guide
---

**Last updated by:** RichardWhellum, **Last updated on:** 09/05/2025


**Last updated by:** RichardWhellum, **Last updated on:** 09/05/2025


# Maintaining the structured Dremio solution

:::info
**Document Creation:** 21 September, 2024. **Last Edited:** 21 September, 2024. **Authors:** Kaleb.
<br></br> **Document Code:** DRE1. **Effective Date:** 21 September, 2024. **Expiry Date:** 21 September, 2025.
:::

### How the solution works
Think of the structured solution as a datalakehouse (Minio) which can store files of any type with Dremio layered over it as the interactable UI for doing sql queries on a sql table. They are linked through adding minio as a source for dremio to store and access the data. As of writing this documentation we have three buckets on minio though only project-2 and project-3 are connected to dremio. ![PHOTO OF DREMIO](img/dremio-ui.PNG) 

### How minio works

To create a new bucket simply go into minio and select the buckets tab, name it and press create. ![PHOTO OF CREATING BUCKET](img/minio-buckets.PNG)

To link it to dremio you'll need to go into minio again and create an access key and copy down the access key and secret key it gives you. ![PHOTO OF ACCESS KEY](img/minio-accesskey.PNG)

### How dremio works

Then go to dremio click add source. ![PHOTO OF BUTTON](img/add-dremio-source.PNG)

Then select amazon s3.

For the first tab of details simply enter any desired name for the source, the access and secret key you copied from the minio section and ensure encrypt connection is off. ![PHOTO OF DETAILS](img/source-page1.PNG)

Then for the advanced details tab specify the path of the bucket like below, it should just be /nameofbucketinminio and add three connection properties filling them out the same as seen below. ![PHOTO OF ADVANCED DETAILS](img/source-page2.PNG)

Then press save and it should add it.

### Creating tables in dremio

As of writing this documentation the method of converting and uploading data as a sql table is through this [script](https://github.com/Jesse-Rees/redback-data-warehouse/blob/Structured-Solution/Structured%20Dremio%20Solution/Script/pipeline.py) which is currently only uploaded to a forked repository of Redback Operation's github but should be merged soon in the directory: redback-data-warehouse/Structured Dremio Solution/Script/pipeline.py.

The script takes in a csv file and creates a sql table out of it in dremio. If you have access to dremio you can see the table and use the sql runner tab on the left to query it.

### How the flask api works
The flask api is a level of security and convenience on top of the dremio rest api to prevent malicous use of sql commands. It allows people connected to the deakin network through anyconnect VPN to query their data in dremio.

The code for the app and docker container running it can be found [here](https://github.com/Jesse-Rees/redback-data-warehouse/tree/Structured-Solution/Structured%20Dremio%20Solution/Flask-api), that link is the same fork as the script and should be added to the main branch soon in the same directory.

The guide on how to use the api as a data analyst will be uploaded alongside this one and should be found in the same folder labeled structured solution.
