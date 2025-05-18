---
sidebar_position: 4
---

**Last updated by:** KasparByrne, **Last updated on:** 25/09/2024


**Last updated by:** KasparByrne, **Last updated on:** 25/09/2024


# Heart Rate Sensor

The heart_rate_sensor driver drives the TICKR heart rate monitor, pulling heart rate data from the TICKR.

## GATT Device

The driver is primarily driven by a `gatt.Device` object which connects and reads data from the TICKR heart rate monitor through its characteristics.

| Service/Characteristic | UUID | Purpose |
| ---- | ---- | ---- |
| `heart_rate_service` | ending-`180d` | Holds the `heart_rate_measurement_characteristic` characteristic |
| `heart_rate_measurement_characteristic` | ending-`2a37` | Readable characteristic which holds the measured heart rate data |

*UUIDs can be matched to their characteristic/service using the following two Bluetooth SIG documents:*

- *[Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/)*
- *[Fitness Machine Service 1.0](https://www.bluetooth.com/specifications/specs/fitness-machine-service-1-0/)*

## Extracting Heart Rate Data

Notification is enabled for the `heart_rate_measurement_characteristic` characteristic and so when it updates the `characteristic_value_updated` method is called with the new heart rate data.

The heart rate data is stored in a series of bytes with a preceding flag byte to indicate the format of the data and what data is present.

**Flags**

| Bit Position | Meaning |
| ---- | ---- |
| 0 | set if the heart rate is 16 bit (otherwise 8 bit) |
| 1 | set if contact is detected (only valid if bit 2 is also set) |
| 2 | set if contact status is reported |
| 3 | set if energy expenditure is reported |
| 4 | set if rr interval is reported |
| 5-7 | reserved for future use (ignored) |

**Measurements**

- Heart rate (beats per minute) [uint8, or uint16 if flags Bit 0 is set]
- Energy (kJ) [uint16, only present if flags Bit 3 is set]
- RR Interval (1/1024 seconds) [Remaining bytes until end of packet, only present if flags bit 4 is set]

## MQTT Topics

Heart rate data is published to the following topic:

`bike/{DEVICE_ID}/heartrate`

*This should be changed to conform to the [MQTT Topics](../MQTT-Topics.md) documents convention:*

`bike/{DEVICE_ID}/heartrate/report`

## Driver Location

[Drivers/heart_rate_sensor/heartrate.py](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/heart_rate_sensor/heartrate.py)