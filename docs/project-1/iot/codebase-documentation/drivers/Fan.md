---
sidebar_position: 3
---

# Fan Driver

:::danger[Important!]

The fan driver code is quiet rough and requires a major rewrite. Relevant characteristics & services were not documented and it is unclear what characteristics do what. The flow control is basically *try again and hope*.

:::

The fan driver code drives the Wahoo Headwind Fan, controlling its blowing force.

## GATT Device

The driver is primarily driven by a `gatt.Device` object which connects to the Fan and then writes to the relevant characteristics.

| Service/Characteristic | UUID | Purpose |
| ---- | ---- | ---- |
| `enable_service` | ending-`ee01` | Holds the `enable_characteristic` |
| `enable_characteristic` | ending-`e002` | Likely the FTMS control point of the Headwind Fan - an array of bytes is written to it with a comment indicating that it is to request writing permissions |
| `fan_service` | ending-`ee0c` | Holds the `fan_characteristic` |
| `fan_characteristic` | ending-`e038` | Likely the custom fan control point - two arrays of bytes are written to it with comments indicating that they are to turn the fan on and to write a new blowing force |

*UUIDs can be matched to their characteristic/service using the following two Bluetooth SIG documents:*

- *[Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/)*
- *[Fitness Machine Service 1.0](https://www.bluetooth.com/specifications/specs/fitness-machine-service-1-0/)*

*No proper flow control is implemented instead values are rewritten multiple times with the hope that they will be successfully written.*

## MQTT Topics

The implemented MQTT topic is the KICKR smart trainer's speed publishing topic:

`bike/{DEVICE_ID}/speed`

*This should be changed to conform to the [MQTT Topics](../MQTT-Topics.md) documents convention:*

`bike/{DEVICE_ID}/fan/control`

## Speed Value Binning

The blow force of the Headwind Fan is a percentage between 0 and 100.

The current fan driver implementation bins speed values into 6 bins.

| Bin Range | Blow Force |
| ---- | ---- |
| 0 | 0% |
| 0 - 4 | 20% |
| 4 - 8 | 40% |
| 8 - 12 | 60% |
| 12 - 16 | 80% |
| >16 | 100% |

:::danger[Important!]

It is better to let application developers decide how they want the fan's power to be controlled. Forcing a relationship between speed and fan force, in addition to forcing a set number of steps in blow force, is bad.

:::

## Driver Location

[Drivers/fan/fan.py](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/fan/fan.py)
