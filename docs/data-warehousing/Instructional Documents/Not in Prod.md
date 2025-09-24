--- 
sidebar_position: 6
sidebar_label: Additional services
---

# Services not running in production

:::info
**Document Creation:** 22 September, 2024. **Last Edited:** 29 April, 2025. **Authors:** kghdxx, Jesse Rees, nouri-devv.
<br></br> **Document Code:** ONB6. **Effective Date:** 22 September 2024. **Expiry Date:** 29 April 2026.
:::

## Nessie 

Nessie is a metadata store that captures information about the files in Dremio and keeps it in case of corruption or for historical analysis.

Because the Nessie file in Dremio has the details of each file it can work as a data catalog to quickly sort and find information in a data model which was the original intention to include it in the Data Warehouse stack.

The Data Warehouse VM is running a Nessie instance, and the proof of concept has been performed successfully using sample data in Dremio, however at the time of writing there is no Nessie files being stored or utilised in the Data Warehouse Dremio instance.

  

## Spark Notebooks and the Virtual Machines

The Data Warehouse virtual machine is successfully running Apache Spark as part of the dockerfile.

By following the address: [http://10.137.0.149:8888/](http://10.137.0.149:8888/) this will open a window and start a new Jupyter notebook.

This notebook exists and is running in the virtual machine where Spark jobs can be configured and ran. This represents a functionality to code and run distributed Spark jobs within the virtual machine and has the advantage of being able to process large datasets using the Spark DAG scheduler and partitioning data with distributed computing. At the time of writing without large production datasets in the VM there isn't currently a need for this functionality yet.

![spark](./pictures/spark.png)
  
