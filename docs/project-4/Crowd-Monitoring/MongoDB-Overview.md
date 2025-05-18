---
sidebar_position: 2
---

**Last updated by:** Vincent Tran, **Last updated on:** 22/08/2024


**Last updated by:** Vincent Tran, **Last updated on:** 22/08/2024


# MongoDB

## Introduction

MongoDB, a NoSQL database management platform, is utilized in this project to store crowd monitoring data. Given the current focus on tracking crowds and analyzing movement trends, MongoDB is a suitable choice due to its schemaless and non-relational properties, which offer flexibility in handling diverse data types. However, as the project scales and becomes more complex with additional components, transitioning to a standard SQL database may be considered to accommodate the need for more structured data management.

## Installation

To establish a database on MongoDB, you can easily create the database and clusters by following the instructions provided on the MongoDB website. For cluster configuration, the team will use the free-tier option, which includes 512 MB of storage.

When connecting to MongoDB, it's important to select the appropriate driver and version to ensure you receive the correct instructions, as shown in the image below.

![MongoDB Setup](img\MongoDBConnect.png)

To install the MongoDB driver on your local machine, follow the command line instructions provided below.

```python
python -m pip install "pymongo[srv]"
```

## Data Recording
The below block has the function of connecting to the MongoDB driver.
It would directly access to the CrowdTracking database and Crowd collection

```python
from pymongo import MongoClient

client = MongoClient('mongo+srv:// ')
db = client["CrowTracking"]
collection = db["Crowd"]
```
In regard to real-time crowd monitoring there would be two main approachs. 
```python
now = datetime.now()
data = {            
    "frame_id": frame_id,
    "timestamp": now.strftime("%d/%m/%Y %H:%M:%S"),
    "total_persons": len(boxes)
}
collection.insert_one(data)
```
This code would record the captured data based on every round of loop. The advantage of this approach is that the data would be imported into MongoDB in every frame ID. However, as the recursion os executed hastely, YOLO could process mutiple of frames in a second leading to the burdern of storage.

```python
if current_time - last_update_time < update_interval:
    now = datetime.now()
    data = {
        "frame_id": frame_id,
        "timestamp": now.strftime("%d/%m/%Y %H:%M:%S"),
        "total_persons": len(boxes)
    }
    collection.insert_one(data)
    last_update_time = current_time
```
With the above code, by setting up a variable for interval time, we can easily adjust this variable to update the recorded data on MongoDB in every second, minute or hour.

## Results
![MongoDB Live Data](img\live_data.png)