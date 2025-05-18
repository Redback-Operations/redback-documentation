---
sidebar_position: 4
---

**Last updated by:** KasparByrne, **Last updated on:** 23/09/2024


**Last updated by:** KasparByrne, **Last updated on:** 23/09/2024


# MQTT Topics

The Smartbike relies on MQTT for external communication with applications like the VR game and mobile app. All topics follow the following naming convention:

:::danger[Important!]

Old drivers only partially follow this convention. All driver code that will continue to be used should be updated to follow this convention. Any application planning to interface with the Smartbike should follow this convention.

:::

`bike/{DEVICE_ID}/[topic name]/[sub-topic]`

* `{DEVICE_ID}`     being replaced with the Smartbike's ID - this should be done by the program depending on the bike it is interacting with.
* `[topic name]`    being the name of the topic.
* `[sub-topic]`     being the relevant sub-topic for the application of the topic (more about sub-topics below).

## Device IDs

As the Smartbike is still in a prototyping phase and there are only two of them, the device ids of the Smartbikes are below:

| Smartbike | ID |
| ---- | ---- |
| Bike 1 | 000001 |
| Bike 2 | 000002 |

## Sub-Topics

Sub-topics define the direction and type of data being published:

| Sub-topic | Direction of Communication | Type of Data |
| ---- | ---- | ---- |
| `control` | Bike ← App | Actuating |
| `report` | Bike → App | Sensing |
| `status` | Bike ↔ App | Error/Status |

:::danger[Important!]

The `status` sub-topic is not yet implemented in any drivers or applications.

:::

## Topics

*Refer to driver's documentation for implemented topic details*

All implemented topics are split into two categories: actuating and sensing. 

Actuating topics may not have a `report` sub-topic, and if they do, it may only report meta data such as accepted values.

Sensing topics may not have a `control` sub-topic.

| Topic | Description |
| ---- | ---- |
| `incline` | Control KICKR Climb incline |
| `resistance` | Control KICKR smart trainer pedal resistance |
| `fan` | Control the Wahoo Headwind Fan power |
| `speed` | Read the m/s speed value of the KICKR smart trainer |
| `cadence` | Read the RPM cadence value of the KICKR smart trainer |
| `power` | Read the Wattage power value of the KICKR smart trainer |
| `heartrate` | Read the BPM of the TICKR heart rate monitor |

## Payload Structure

*Refer to driver's documentation for expected payload structure.*

Data published to topics, either by the Smartbike or an application, should follow a predictable JSON structure, including:

- The values of interest with appropriately named keys
- A timestamp for time-of-publication
- Any useful descriptive metadata

*Example - `cadence/report` publish:*

```JSON
{
    "value": 6.0, 
    "unitName": "RPM", 
    "timestamp": 1722834169.6118855, 
    "metadata": {
        "deviceName": "bike000001"
        }
}
```

## Example Topics

`bike/000001/incline/control` will change the incline of the KICKR Climb when valid values are published to it.

`bike/000001/speed/report` will forward speed value updates from the Smartbike if subscribed to.

## Further Information

See our [MQTT client-class](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/lib/mqtt_client.py).

View implemented topics in the drivers' code:

- [KICKR Smart Trainer & Climb](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/kickr_climb_and_smart_trainer/wahoo_device.py)
- [Wahoo Headwin Fan](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/fan/fan.py)
- [TICKR Heart Rate Monitor](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/heart_rate_sensor/heartrate.py)
- [Wahoo Cadence Sensor](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/cadence_sensor/cadence.py)
- [Button Driver](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/button_control/button_control.py)