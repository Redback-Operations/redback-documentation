---
sidebar_position: 5
---

# GATT Code

![bike-architecture](../img/architecture/bike-architecture.png)

The Smartbike relies on BLE's GATT protocol for internal communication (between the Smartbike's components & Raspberry Pi). A `gatt` python library is used to drive this communication between the Raspberry Pi and the Smartbike's components.

## Installion of `gatt` library

To install run the following `pip` command:

```
pip install gatt
```

## Classes

The `gatt` library provides two classes which together manage and connect to BLE GATT enabled devices: `DeviceManager` & `Device`.

### DeviceManager

This class discovers and manages BLE devices.

To initialise a `DeviceManager` pass it the BLE adapter address:

```Python
manager = gatt.DeviceManager(adapter_name='hci0')
```

To run the `DeviceManager` call `DeviceManager.run()`:

```Python

```

### Device

...

### Service

...

### Characteristic

...

## Updated `gatt` library

...

### Descriptor

...

## Further Information

- For more information on [GATT protocol](../technical-background-information/GATT.md)
- For the `gatt` library's [source code](https://github.com/getsenic/gatt-python/blob/master/gatt/gatt_linux.py)
- For the `gatt` library's [documentation](https://github.com/getsenic/gatt-python/blob/master/README.md)
- For the updated `gatt` library [Drivers/lib/gatt/gatt_linux.py](https://github.com/Redback-Operations/redback-smartbike-iot/tree/main/Drivers/lib/gatt/gatt_linux.py)