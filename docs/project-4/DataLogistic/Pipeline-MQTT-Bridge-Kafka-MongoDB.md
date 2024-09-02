# Setting Up MQTT, Kafka, and MongoDB on Windows and Linux Using Docker

## Prerequisites
- Docker installed on your system. You can download it from Docker's official website.

## Table of Contents
1. MQTT
    - Windows
    - Linux
2. Kafka
    - Windows
    - Linux
3. MongoDB
    - Windows
    - Linux

## MQTT

### MQTT on Windows

1. **Pull the Eclipse Mosquitto Docker Image:**
    ```sh
    docker pull eclipse-mosquitto
    ```

2. **Run the Mosquitto Container:**
    ```sh
    docker run -d --name mosquitto -p 1883:1883 -p 9001:9001 eclipse-mosquitto
    ```

3. **Verify the Installation:**
    - Open a terminal and run:
    ```sh
    docker ps
    ```
    - You should see the Mosquitto container running.

### MQTT on Linux

1. **Pull the Eclipse Mosquitto Docker Image:**
    ```sh
    sudo docker pull eclipse-mosquitto
    ```

2. **Run the Mosquitto Container:**
    ```sh
    sudo docker run -d --name mosquitto -p 1883:1883 -p 9001:9001 eclipse-mosquitto
    ```

3. **Verify the Installation:**
    - Open a terminal and run:
    ```sh
    sudo docker ps
    ```
    - You should see the Mosquitto container running.

## Kafka

### Kafka on Windows

1. **Pull the Confluent Kafka Docker Image:**
    ```sh
    docker pull confluentinc/cp-kafka
    ```

2. **Run the Kafka Container:**
    ```sh
    docker run -d --name zookeeper -p 2181:2181 confluentinc/cp-zookeeper
    docker run -d --name kafka -p 9092:9092 --link zookeeper:zookeeper confluentinc/cp-kafka
    ```

3. **Verify the Installation:**
    - Open a terminal and run:
    ```sh
    docker ps
    ```
    - You should see the Kafka and Zookeeper containers running.

### Kafka on Linux

1. **Pull the Confluent Kafka Docker Image:**
    ```sh
    sudo docker pull confluentinc/cp-kafka
    ```

2. **Run the Kafka Container:**
    ```sh
    sudo docker run -d --name zookeeper -p 2181:2181 confluentinc/cp-zookeeper
    sudo docker run -d --name kafka -p 9092:9092 --link zookeeper:zookeeper confluentinc/cp-kafka
    ```

3. **Verify the Installation:**
    - Open a terminal and run:
    ```sh
    sudo docker ps
    ```
    - You should see the Kafka and Zookeeper containers running.

## MongoDB

### MongoDB on Windows

1. **Pull the MongoDB Docker Image:**
    ```sh
    docker pull mongo
    ```

2. **Run the MongoDB Container:**
    ```sh
    docker run -d --name mongodb -p 27017:27017 mongo
    ```

3. **Verify the Installation:**
    - Open a terminal and run:
    ```sh
    docker ps
    ```
    - You should see the MongoDB container running.

### MongoDB on Linux

1. **Pull the MongoDB Docker Image:**
    ```sh
    sudo docker pull mongo
    ```

2. **Run the MongoDB Container:**
    ```sh
    sudo docker run -d --name mongodb -p 27017:27017 mongo
    ```

3. **Verify the Installation:**
    - Open a terminal and run:
    ```sh
    sudo docker ps
    ```
    - You should see the MongoDB container running.


### Connect MQTT and Kafka:
1. Run the Mosquitto (MQTT) Container:

    ``docker run -d --name mosquitto -p 1883:1883 -p 9001:9001 eclipse-mosquitto``

2. Run the Zookeeper and Kafka Containers:

    ``docker run -d --name zookeeper -p 2181:2181 confluentinc/cp-zookeeper``
    ``docker run -d --name kafka -p 9092:9092 --link zookeeper:zookeeper confluentinc/cp-kafka``

3. Set Up the MQTT-Kafka Bridge:
    - Use a tool like Kafka Connect with the MQTT connector to bridge MQTT and Kafka.
    - Pull the Kafka Connect image:

        ``docker pull confluentinc/cp-kafka-connect``

    - Run the Kafka Connect container:

        ``docker run -d --name kafka-connect -p 8083:8083 --link kafka:kafka --link zookeeper:zookeeper confluentinc/cp-kafka-connect``

4. Configure the MQTT Source Connector:
    - Create a configuration file mqtt-source-connector.json with the following content:

    ```Json
    {
    "name": "mqtt-source-connector",
    "config": {
        "connector.class": "io.confluent.connect.mqtt.MqttSourceConnector",
        "tasks.max": "1",
        "mqtt.server.uri": "tcp://mosquitto:1883",
        "mqtt.topics": "your-mqtt-topic",
        "kafka.topic": "your-kafka-topic",
        "value.converter": "org.apache.kafka.connect.converters.ByteArrayConverter"
    }
    }
    ```

    - Deploy the connector:

        ``curl -X POST -H "Content-Type: application/json" --data @mqtt-source-connector.json http://localhost:8083/connectors``

5. Set Up Rules and Conditions:
    - You can use Kafka Streams or KSQL to process the data and apply rules based on the device's processing capability, message subject, source device type, data importance, etc.
    - Example KSQL query to filter important messages:

        ``CREATE STREAM important_messages AS SELECT * FROM your_kafka_topic WHERE importance = 'high';``


## Conclusion
By following these steps, you should have MQTT, Kafka, and MongoDB running on your Windows or Linux system using Docker. If you encounter any issues, make sure Docker is properly installed and running on your system. 
You can also set up an MQTT-Kafka bridge and configure it to handle data based on various conditions.
