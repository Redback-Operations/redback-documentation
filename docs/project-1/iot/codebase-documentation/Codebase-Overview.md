---
sidebar_position: 1
---

**Last updated by:** KasparByrne, **Last updated on:** 24/09/2024


**Last updated by:** KasparByrne, **Last updated on:** 24/09/2024


# Codebase Overview

```
├── Archive
├── Drivers
│   ├── button_control
│   │   └── button_control.py
│   ├── kickr_climb_and_smart_trainer
│   │   ├── wahoo_device.py
│   │   └── incline_and_resistance_control.py
│   ├── fan
│   │   └── fan.py
│   └── heart_rate_sensor
│       └── heartrate.py
└── scripts
    ├── start_all.sh
    ├── start_ ... .sh
    └── ble-auto-connect
        ├── ble_auto_connect.sh
        └── ble_auto_connect.exp
```

**Repository: [redback-smartbike-iot](https://github.com/Redback-Operations/redback-smartbike-iot)**

The IoT repository is only split across three directories:

1. `Archive` contains old and retired code, research, and documentation.
2. `Drivers` contains currently used driver code.
3. `scripts` contains bash scripts used to run driver code.

## Dependencies

Several dependencies are used by the drivers:

- `paho-mqtt` is used for MQTT functionality
- `gatt` library is used for GATT functionality

`Drivers/lib/` directory contains our in-house library/common code - including:

- `constants.py` for constants used across drivers such as MQTT example topics, upper and lower bounds for valid value ranges, etc.
- `mqtt_client.py` which contains our standard mqtt client which should be used by all drivers.
- `ble_helper.py` which is used by drivers to match UUIDs of characteristics & services and convert values to their OP codes.
- `gatt/` directory which contains the `gatt_linux.py` updated `gatt` library used by some drivers.

Both the in-house and external dependencies help to standardise and streamline code.

## scripts

The `scripts` directory holds our `bash` scripts for running driver code. 

The `start_all.sh` script is the primary Smartbike process script which starts all relevant drivers.

### ble-auto-connect

`ble-auto-connect/` sub-directory contains the `ble_auto_connect` script: it is made up of a `bash` script and `expect` script. To find out more about the `ble_auto_connect` script see the [documentation](../ble-connectivity/BLE-Auto-Connect-Script.md).

## Drivers

Drivers drive the functionality of the Smartbike. They connect, control and read values from a specific Smartbike component. Multiple drivers are used to drive the whole Smartbike.

### button_control

`button_control.py` drives the turning button code and any other buttons.

### kickr_climb_and_smart_trainer

`wahoo_device.py` drives the **KICKR Climb**'s incline control and **KICKR smart trainer**'s resistance control. It also reads the `speed`, `cadence` and `power` values from the KICKR smart trainer.

`incline_and_resistance_control.py` is the starter for the `wahoo_device.py` driver. It takes arguments from the starting script and reads loaded environment variable values.

### fan

`fan.py` drives the **Wahoo Headwind Blueooth Fan**, connecting to and controlling the fan's blowing force.

### heart_rate_sensor

`heartrate.py` drives the **TICKR heart rate monitor**, connecting to and read & publishing the heart rate data from the TICKR.

## Archive

The `Archive` directory holds old and retired code. This includes retired drivers (mostly predefined workout "routines" for the Smartbike), code for remotely connecting to and controlling the Raspberry Pi, a very different and old version of the VR game. It also holds old documentation and research.