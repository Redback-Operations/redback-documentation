
# Implementing HiveMQ and MQTT in Sensor Data Collection

## Introduction

This report explores the integration of HiveMQ and MQTT protocols in our project to facilitate efficient and reliable data communication. Focusing on the MAX30102 sensor setup, we explain how MQTT can be utilized to transmit sensor data, such as heart rate and oxygen saturation, over a network.

## Understanding MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol designed for low-bandwidth, high-latency or unreliable networks. It is ideal for IoT applications because it ensures data delivery with minimal bandwidth usage.

### Core Concepts
- **Publisher-Subscriber Model**: MQTT uses a pub-sub model where devices publish messages to topics, and clients subscribe to topics to receive messages.
- **Broker**: The central point of message distribution, handling the dissemination of all messages between publishers and subscribers. HiveMQ is a robust MQTT broker designed for enterprise-scale deployment.

## Role of HiveMQ

HiveMQ is an MQTT broker that enhances MQTT implementations with its high scalability, easy integration with enterprise systems, and robust security features. It facilitates the management of large-scale IoT applications and supports the seamless transmission of telemetry data.

## Implementing MQTT with Arduino

### Sensor Setup

The sensor setup remains the same as outlined in the previous guide. Here is a brief overview with additional MQTT implementation:

```cpp
#include "DFRobot_BloodOxygen_S.h"
#include <PubSubClient.h>  // MQTT client library

// Define the I2C address and create an instance of the sensor class
#define I2C_ADDRESS 0x57
DFRobot_BloodOxygen_S_I2C MAX30102(&Wire, I2C_ADDRESS);

// Setup MQTT parameters
const char* mqtt_server = "broker.hivemq.com";
const char* topic = "sensor/data";
const char* clientID = "unique_client_id";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "password");  // Connect to Wi-Fi
  client.setServer(mqtt_server, 1883);  // Connect to MQTT broker

  while (false == MAX30102.begin()) {
    Serial.println("init fail!");
    delay(1000);
  }
  Serial.println("init success!");
  Serial.println("start measuring...");
  MAX30102.sensorStartCollect();
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Collect data
  MAX30102.getHeartbeatSPO2();
  String payload = "SPO2 is: " + String(MAX30102._sHeartbeatSPO2.SPO2) + "%";
  Serial.println(payload);
  client.publish(topic, payload.c_str());

  delay(4000);
}

void reconnect() {
  // Reconnect to the MQTT broker
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect(clientID)) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}
```

### Python Script for Monitoring (Subscriber)

The Python script acts as a subscriber, receiving data published to the MQTT topic.

```python
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensor/data")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
```

## Conclusion

The integration of HiveMQ and MQTT into our sensor data collection project allows for robust, scalable, and efficient data communication. This setup ensures real-time data monitoring across different platforms, enhancing the capabilities of IoT applications in health monitoring.
