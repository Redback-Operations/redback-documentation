---
sidebar_position: 1
---

# Proposal for the utilization of Microsoft Azure as the cloud platform of choice for Redback Operations
GCP -> Azure changes

:::info
**Document Creation:** 6 December, 2023. **Last Edited:** 8 December, 2023. **Authors:** Joel Daniel.
<br></br>**Effective Date:** 8 December, 2023. **Expiry Date:** 8 December, 2024.
:::

##  Purpose and Scope of the Proposal

The purpose of this proposal is to recommend the company to convert their choice of cloud 
operations and platform from Google Cloud to Microsoft Azure. The proposal will cover only 
Azure and Google Cloud and not consider any other cloud platforms.

## What is Microsoft Azure?

Microsoft Azure is a cloud services platform provided by Microsoft, which allows 
organizations to utilize services in the cloud to carry out a variety of organizational activities 
from custom activities such as specific machines for software development and research to 
even leveraging identity and access management services for carrying out active directory 
operations, whether it be fully in the cloud or hybrid or even through private on-site 
options.

## What is Google Cloud?

Google Cloud is a cloud service platform provided by Google, which operates on providing 
customer friendly prices while also giving a plethora of services from compute capabilities to 
administrative and security capabilities.

## Azure Virtual Machines vs Google Compute Instances

Both Azure and Google sport a large variety of predefined VMs for many operating systems, 
with their offerings categorized based on performance, machine specs and usage purpose, 
with billings being done on a pay-as-you-go basis. However Google Cloud does provide 
custom virtual machines (hardware specifics) to cater for extremely specific scenarios while 
maintaining very little pricing changes in comparison to Azure which lacks the flexibility 

(https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type). 

##Azure Cloud Regional Areas vs Google Cloud Zonal Areas
Azure and Google Cloud each sport various datacenters across the globe, with atleast one 
datacenter in New South Wales and Victoria. These allow for creating geographic zones, 
which ensure that the instances created are in the closest physical location hosting the 
cloud capabilities in order to ensure low latency and little to no delays for the customer.

- Backups of the instances may be spread across globally based on Azure and Google 
Cloud backup policies or stored completely in a different region.

- Offerings of available resources on the cloud will vary from region to region.

### Azure Cloud Geographies

https://azure.microsoft.com/en-gb/explore/global-infrastructure/geographies/#geographies

![Azure Regions](img\azure-regions.jpg)

### Google Cloud Locations

https://cloud.google.com/about/locations#asia-pacific

![Azure Google Regions](img\azure-google-regions.jpg)

Comparing Australian regions alongside regional offerings, the Sydney regions for both 
platforms offer the largest catalogue of products. Melbourne will be the recommended 
region as its offerings contain all the products required for Redback Operations.


## Pricing of Azure and Google Cloud

### Pay-As-You-Go (PAYG)

Google Cloud was comparatively cheaper than Azure on almost all instance types. 
Azure generally offers a flat rate for PAYG billing, but Google Cloud utilizes a discount 
scaling method that increases the discount after a certain rate of usage, making 
Google Cloud an economical option for general purposes.

![Azure PAYG](img\azure-payg.jpg)

### Reserved Instances/Committed Use

Both platforms also offer alternatives called ‘Reserved Instances’ and ‘Committed Use’ 
by Azure and Google Cloud respectively. For long term or dedicated cloud usage, these 
alternatives are far cheaper since a fixed resource is set (regardless of how much of 
the resource is used, while allowing for consumption beyond the fixed resource), 
further ensuring that scaling lag or minute slowdowns/delays are not experienced. In 
these alternatives, Azure was cheaper across all instance types against Google Cloud.

![Azure PAYG Uses](img\azure-payg-uses.jpg)

## Recommendation

As seen in Trimester 3 2023, access for Google Cloud was vital for several projects, 
especially ones relying on data analytics and big data. While the projects were able to 
temporarily pivot and carry out their activities on local machines, the lack of Google Cloud 
access prevented projects from continuing (and possibly completing) activities planned in T2  2023. Deakin’s IT infrastructure together with identity management allowing for ease of 
access to Azure will make it easier for the company leadership responsible for access to 
grant it per project (via resource groups) to students.

###  Pros

- Students can simply sign in to Azure using their Deakin IDs in comparison to 
Google Cloud which requires students to create a google cloud (using the Deakin 
ID).

- Company board can own a tenant and split members into their relevant project 
user groups (assigned membership), which can then be assigned their very own 
resource groups to control resource creation and billing at a granular level.

  - Since Deakin already owns the Deakin University tenant, it can be requested 
to create a specified group (or a separate tenant for Redback Operations if 
feasible) for the company with the company board having user 
administrator/group administrator permissions.

- Created resources (including instances with inbuilt software for projects) can be 
saved as templates for later use over trimesters.

###  Cons

- Due to the nature of the trimester activities and the companies, the Pay-As-You-Go model will have to be implemented over the Reserved Instances, in which 
Azure costs slightly more than Google Cloud (taking standard compute 
instances).

### Rough Estimate of cost company will use

- Assuming five instances (one per current project) with 100GB of persistent disk 
storage, we get an approximate cost of 1150 AUD per month on Google Cloud.


![Azure Google Pricing](img\azure-google-pricing.jpg)

- Assuming the same with Azure (alongside a 1-year discount plan of 20%), we get 
an approximate cost of 1204 AUD per month.

![Azure Pricing](img\azure-pricing.jpg)

Despite the slight cost increase Azure will have over Google Cloud, the increase justifies the 
various efficiencies and ease of use the company will get from quick sign ins to access 
provisioning and resource control, which would make Azure a far more viable option than 
Google Cloud.
