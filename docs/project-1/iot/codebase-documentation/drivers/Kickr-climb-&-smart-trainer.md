---
sidebar_position: 2
---

**Last updated by:** KasparByrne, **Last updated on:** 25/09/2024


**Last updated by:** KasparByrne, **Last updated on:** 25/09/2024


# KICKR Climb & Smart Trainer

:::danger[Important!]

These Bluetooth SIG documents offer greater insight into how this driver works then I can:

- [Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/)
- [Fitness Machine Service 1.0](https://www.bluetooth.com/specifications/specs/fitness-machine-service-1-0/)

:::

The KICKR's driver has three different functions - compared to the one function all other drivers have:

1. Read speed, cadence & power data
2. Control incline
3. Control resistance

## Data Reading

Data reading is achieved by enabling notification on the `indoor_bike_data` characteristic with UUID ([INDOOR_BIKE_DATA_UUID](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/lib/constants.py#L28)). Once notification is enabled, when the characteristic updates the `characteristic_value_updated` method is called with the new `value` and the `process_indoor_bike_data` method is called to process the new data.

The data processing is complex and the linked Bluetooth SIG documents should be investigated to understand how it works.

## Incline Control

*As a quick note: the incline control does not follow the standards defined by Bluetooth SIG.*

A new incline value can be set by writing to the `custom_incline_characteristic` characteristic - [UUID](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/lib/constants.py#L77).

The value must be between -10 and 19, and converted to a byte array using the [`convert_incline_to_op_value` BLE helper function](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/lib/ble_helper.py#L32). The value must also be paired with the [`INCLINE_CONTROL_OP_CODE` OP code](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/lib/constants.py#L81).

The `custom_control_point_set_target_inclination` method can be passed the integer value to set the new incline.

## Resistance Control

A new resistance value can be set by writing to the `ftms_control_point` characteristic - [UUID](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/lib/constants.py#L22).

The value must be an integer between 0 and 100 - representing a percentage - and converted to a byte array. It must be paired with the [`FTMS_SET_TARGET_RESISTANCE_LEVEL` OP code](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/lib/constants.py#L56).

The `ftms_set_target_resistance_level` method can be passed the integer value to set the new resistance.

## MQTT Topics

Subscribed topics messages are processed by the [custom MQTT client](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/kickr_climb_and_smart_trainer/mqtt_custom_client.py). 

### Data Topics

| Topic | Data |
| ---- | ---- |
| `bike/{DEVICE_ID}/speed` | Speed data |
| `bike/{DEVICE_ID/cadence` | Cadence data |
| `bike/{DEVICE_ID}/power` | Power data |

*This should be changed to conform to the [MQTT Topics](../MQTT-Topics.md) documents convention:*

- `bike/{DEVICE_ID}/speed/report`
- `bike/{DEVICE_ID/cadence/report`
- `bike/{DEVICE_ID}/power/report`

### Incline Topic

The incline is controlled using the topic:

`bike/{DEVICE_ID}/incline`

With the package expected to be only an integer.

*This should be changed to conform to the [MQTT Topics](../MQTT-Topics.md) documents convention:*

`bike/{DEVICE_ID}/incline/control`

### Resistance Topic

The resistance is controlled using the topic:

`bike/{DEVICE_ID}/resistance`

With the package expected to be only an integer.

*This should be changed to conform to the [MQTT Topics](../MQTT-Topics.md) documents convention:*

`bike/{DEVICE_ID}/resistance/control`

## MQTT Payload

The data (speed, cadence, power) payload follows a JSON structure:

```
{
    'value' : [cadence | speed | power]
    'unitName' : [a unit metric relevent to the data type]
    'timestamp' : [the time at publish]
    'metadata' : {
        'deviceName' : [some identifier of the publishing device]
    }
}
```

## Driver Location

This driver has two parts:
- Core driver code - [Drivers/kickr_climb_and_smart_trainer/wahoo_device.py](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/kickr_climb_and_smart_trainer/wahoo_device.py)
- Driver starter - [Drivers/kickr_climb_and_smart_trainer/incline_and_resistance_control.py](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/kickr_climb_and_smart_trainer/incline_and_resistance_control.py)

### An Alternative Driver

Two alternative driver `wahoo_controller.py` and `smartbike.py` were developed to implement many of the above requirements. `wahoo_controller.py` works and has a starter `wahoo_controller_starter.py`. `smartbike.py` is an extension of `wahoo_controller.py` to cover all drivers but was developed late and is not functional (I would not recommand using it).

:::danger[Important!]

The VR game's incline control was developed to use the improved incline control payload used by the `wahoo_controller.py` driver. You should use the `wahoo_controller.py` driver over the `kickr_climb_and_smart_trainer` driver.

:::

Location - [Drivers/smartbike_driver/smartbike/](https://github.com/Redback-Operations/redback-smartbike-iot/tree/main/Drivers/smartbike)