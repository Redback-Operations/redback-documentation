---
sidebar_position: 3
---

# MQTT Client

The Smartbike uses MQTT for external communication - between itself and applications. 

## Paho-MQTT

The `paho-mqtt` library, based on the [Eclipse Mosquitto](https://eclipse.dev/paho/index.php?page=clients/python/index.php) MQTT broker, is used for MQTT functionality.

### Installation

To install the library run the follow command

`pip install paho-mqtt`

### Library Documentation & Source Code

To find out more about `paho-mqtt` view the [documentation](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html) or [source code](https://github.com/eclipse/paho.mqtt.python).

## MQTTClient

To simplify and standardise using MQTT, a paho based client-class (`MQTTClient`) has been implemented in `Drivers/lib/mqtt_client.py` and should be used in all drivers and programs using MQTT.

```Python
from lib.mqtt_client import *

...

# define credentials and broker details
broker_address = 'example_address'
username = 'ExampleUsername'
password = 'Ex@mpLeP@Ssw0rd'
port = 1883

# Create & setup client
client = MQTTClient(broker_address, username, password, port)
client.setup_mqtt_client()

# Subscribe to topics
client.subscribe('example/1')

...

# Publish on some event
def my_event():
    payload = json.dumps( { ... } )
    client.publish('example/2', payload)

...

# start the client
client.loop_start()

```

### Import & Create Client

Import the client-class from `Drivers/lib/`, create a client-object, and setup the connection to the broker using:

```Python
from lib.mqtt_client import *

...
broker_address = 'example_address'
username = 'ExampleUsername'
password = 'Ex@mpLeP@Ssw0rd'
port = 1883

client = MQTTClient(broker_address, username, password, port)
client.setup_mqtt_client()
```

`MQTTClient(broker_address: str, username: str, password: str, port: int=1883)`

| **Parameter** | Type | Description | *example* |
| ---- | ---- | ---- | ---- |
| `broker_address` | *string* | MQTT broker host address | *mqtt.example.address* |
| `username` | *string* | Configured account username | *ExampleUsername* |
| `password` | *string* | Configured account password | *Ex@mpLeP@Ssw0rd* |
| `port` | *integer* | Port of the MQTT broker [default `1883`] | *`1883`, `8883`, ...* |

### Subscribing to Topic

Subscribing to a topic in MQTT will have your client receive all messages published to that topic. When a message is received it will trigger the `client.on_message()` method.

```Python
client.subscribe('example/1')
```

`client.subscribe(topic_name: str)`

| **Paramater** | Type | Description | *example* |
| ---- | ---- | ---- | ---- |
| `topic_name` | *string* | Topic to subscribe to | *bike/000001/speed/report* |

### Publish to Topic

Publishing to a topic in MQTT will send the `payload` to all clients subscribed to that topic.

```Python
payload = json.dumps( { ... } )
client.publish('example/2', payload)
```

`publish(topic_name: str, payload: any)`

| **Paramater** | Type | Description | *example* |
| ---- | ---- | ---- | ---- |
| `topic_name` | *string* | Topic to publish to | *bike/000001/incline/control* |
| `payload` | *any* | Message to send - *it does not need to be a JSON but it is good practice.* | `{ 'incline' : 19, 'ts' : 1722834170.603658 }`, `'Hello World!'`, `[True, False]`, `-10`, *etc.* |

### on_message

To do something when a message is received by a subscribed topic, the client-class needs to be sub-classed to extend its `client.on_message()` method.

```Python
class MyChildClient(MQTTClient):
    def __init__(self, broker_address, username, password, device):
        super().__init__(broker_address, username, password)
        self.device = device

    def on_message(self, client, userdata, msg):
        super().on_message(client,userdata, msg)
        self.device.on_message(msg)
```

The topic-of-origin (`msg.topic`) of the message should be checked if subscribing to more than one topic. The message then needs to be decoded and converted into its expected data structure.

```Python
class Device:

    ...

    def on_message(self, msg):

        # check msg topic of origin
        if self.device_topic != msg.topic: return

        # decode the payload
        decoded_payload = str(msg.payload, 'utf-8')

        # convert to expected data structure
        dict_payload = json.loads(decoded_payload)

        # use payload values
        ...
```

`client.on_message(client, userdata, msg)`

Refer to `paho-mqtt` [documentation](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html) for more information.

### loop_forever & loop_start

Before being able to publish and receive messages the client loop must first be started using one or two methods:

```Python
client.start_loop()
```

Will start the client loop in a separate thread allowing continued procedure of execution.

```Python
client.loop_forever()
```

Will start the client loop in a blocking function preventing further execution of code.

These loops will attempt to reconnect if the connection is lost but will also timeout if unable to reconnect.

## Further Information

For more information on `paho-mqtt`:

- See the [documentation](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html).
- See the [source code](https://github.com/eclipse/paho.mqtt.python).

For our MQTT client-class & topics:

- [Client-class code](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/lib/mqtt_client.py)
- [Topics](MQTT-Topics.md)