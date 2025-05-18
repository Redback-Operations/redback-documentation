--- 
sidebar_position: 4
sidebar_label: Dremio Guide
---

**Last updated by:** RichardWhellum, **Last updated on:** 09/05/2025


**Last updated by:** RichardWhellum, **Last updated on:** 09/05/2025


# How to Use Dremio

:::info
**Document Creation:** 22 September, 2024. **Last Edited:** 29 April, 2025. **Authors:** kghdxx, Jesse Rees, nouri-devv.
<br></br> **Document Code:** ONB4. **Effective Date:** 22 September 2024. **Expiry Date:** 29 April 2026.
:::

## Why Dremio?

Dremio in the Data Warehouse is the GUI for table storage. It accesses data from the Data Warehouse sources of MinIO and Mongo DB.

  

Dremio was decided upon after a series of redback requirements gathering tasks where it was considered cost-effective (free) and would allow for storage from different data sources, with the SQL functionality and GUI making it a smaller learning curve than other FOSS that were mostly terminal based.

  

### How To Add A Source in Dremio

There are a few steps to adding a source in Dremio.

(For this example we will add a MinIO bucket as a source)

  

1. Add source

Use the 'Add source' button on the user interface

2. Enter Credentials

Enter Credentials according to the source.

![Addingasource1](./pictures/Addingasource1.png)

3. Go to 'Advanced Options' and tick 'enable compatibility mode'

![Addingasource2](./pictures/Addingasource2.png)

  

At this point, 'save' and the source should appear in the object storage list quickly.

  
  

### Adding a Table in Dremio with SQL

Dremio allows for creating tables or 'views' with T-SQL. What this means is with the SQL language it's possible to modify the source data to a more meaningful state depending on the data analysis purpose.

  

Once a source has been added. Enter the SQL interface on the left side of the GUI. This will bring up a text box that SQL commands can be written in and executed from. Resulting in a modified table that can be accessed downstream.

![Dremio3](./pictures/Dremio3.png)

  

Dremio also has the capability of storing files in Iceberg or **Parquet** format allowing for time-series versions of the same file and their metadata, which would aid in recording historical versions of the same files.

#### SQL Endpoint

Alternatively, Dremio offers a SQL endpoint that through code you can query the source data through Dremio with SQL statements.

  

See the documentation of [Dremio API ](https://redback-operations.github.io/redback-documentation/docs/data-warehousing/Data%20Lakehouse/Dremio-API(For%20data%20analysts)) also located in the Data warehouse documentation for a detailed explanation.


