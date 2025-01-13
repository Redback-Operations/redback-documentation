import json
from paho.mqtt.client import Client
from pymongo import MongoClient

# MongoDB configuration
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["mqtt_data"]
collection = db["messages"]

# MQTT configuration
MQTT_BROKER = "localhost"  # Replace with your MQTT broker address
MQTT_PORT = 1883           # Default MQTT port
MQTT_TOPIC = "bike/#"      # Subscribe to all topics in the "bike/" hierarchy

#bike/{DEVICE_ID}/[topic name]/[sub-topic] NAMING CONVENTION

# Listing of specific topics to subscribe to as per the naming conventions
# meaning of these topics and subtopics is already in the documentation in regards to project 1.
MQTT_TOPICS = [
    "Bike1/000001/incline/control",
    "Bike1/000001/incline/report",
    "Bike1/000001/incline/status",
    "Bike1/000001/resistance/control",
    "Bike1/000001/resistance/report",
    "Bike1/000001/resistance/status",
    "Bike1/000001/fan/status",
    "Bike1/000001/fan/report",
    "Bike1/000001/fan/control",
    "Bike2/000002/speed/control",
    "Bike2/000002/speed/report",
    "Bike2/000002/speed/status",
    "Bike2/000002/power/control",
    "Bike2/000002/power/report",
    "Bike2/000002/power/status",
    "Bike2/000002/heartrate/status",
    "Bike2/000002/heartrate/report",
    "Bike2/000002/heartrate/control",
    "Bike1/000001/cadence/control",
    "Bike2/000002/cadence/report",
    "Bike1/000001/cadence/status",
]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        # Decode the MQTT message
        payload = msg.payload.decode("utf-8")
        topic = msg.topic

        # Convert payload to JSON 
        try:
            data = json.loads(payload)
        except json.JSONDecodeError:
            data = {"raw_data": payload}

        # Add topic and timestamp
        message = {
            "topic": topic,
            "data": data,
        }

        # Insert into MongoDB
        collection.insert_one(message)
        print(f"Saved to MongoDB: {message}")

    except Exception as e:
        print(f"Error processing message: {e}")

def main():
    # Initialize MQTT client
    mqtt_client = Client()

    # Set MQTT event callbacks
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    # Connect to the MQTT broker
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)

    # Start the MQTT client loop
    mqtt_client.loop_forever()

if __name__ == "__main__":
    main()
