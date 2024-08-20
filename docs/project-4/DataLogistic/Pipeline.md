# Deploying MongoDB and Kafka with Docker

This guide will help you set up a real-time data pipeline using MongoDB and Kafka with Docker on both Linux and Windows.

## Prerequisites

- Docker installed on your system
- Docker Compose installed
- Git installed (optional, for cloning repositories)

## Steps

### 1. Clone the Tutorial Repository

First, clone the tutorial repository that contains the necessary Docker configurations.

```bash
git clone https://github.com/mongodb-university/kafka-edu.git
cd kafka-edu/docs-examples/mongodb-kafka-base/
```

If you don't have Git installed, you can download the zip archive from the repository and extract it.


### 2. Start the Docker ContainersNavigate to the directory containing the Docker Compose file and start the containers.
- For Linux

```bash
cd kafka-edu/docs-examples/mongodb-kafka-base/
docker-compose -p mongo-kafka up -d --force-recreate
```

- For WindowsOpen PowerShell and navigate to the directory:

```bash
cd kafka-edu\docs-examples\mongodb-kafka-base\
docker-compose -p mongo-kafka up -d --force-recreate
```

### 3. Verify the SetupEnsure that the containers are running correctly.

```bash
docker ps
```
You should see containers for MongoDB, Kafka, Zookeeper, and other services running.

### 4. Configure Kafka ConnectorsYou can now configure Kafka connectors to read data from MongoDB and write it to a Kafka topic, or vice versa.

- Adding a Source Connector

```Json
Create a JSON file named source-connector.json with the following content:
{
  "name": "mongo-source-connector",
  "config": {
    "connector.class": "com.mongodb.kafka.connect.MongoSourceConnector",
    "connection.uri": "mongodb://mongo1:27017",
    "database": "your_database",
    "collection": "your_collection",
    "topic.prefix": "mongo."
  }
}
```

- Submit the connector configuration:

```bash
curl -X POST -H "Content-Type: application/json" --data @source-connector.json http://localhost:8083/connectors
```

- Adding a Sink ConnectorCreate a JSON file named sink-connector.json with the following content:

```Json
{
  "name": "mongo-sink-connector",
  "config": {
    "connector.class": "com.mongodb.kafka.connect.MongoSinkConnector",
    "connection.uri": "mongodb://mongo1:27017",
    "database": "your_database",
    "collection": "your_collection",
    "topics": "your_topic"
  }
}
```

- Submit the connector configuration:

```bash
curl -X POST -H "Content-Type: application/json" --data @sink-connector.json http://localhost:8083/connectors
```

### 5. Verify Data FlowTo verify that data is flowing correctly between MongoDB and Kafka, you can use the following commands:
- Check Kafka Topics
```bash
docker exec -it broker kafka-topics --list --bootstrap-server broker:9092
```

- Check MongoDB Collections
```bash
docker exec -it mongo1 mongo --eval "db.getCollectionNames()"
```


