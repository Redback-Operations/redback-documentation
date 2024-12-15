---
sidebar_position: 1
---

# Button Control

:::danger[Important!]

The HiveMQ broker has a limit on how often it can be published to. As a result, button publishes can be denied if they are too quick or obstructured by other publishing traffic. The alternative driver for temporary demonstration purposes `DEMO_button_control.py` is less susceptible to this but it is not a solution.

:::

The `button_control` driver drives buttons added to the Smartbike and attached to the Raspberry Pi's GPIO pins.

## Button class

The `Button` class can be used to quickly create new buttons which will read input from a passed pin and publish when the pin is pressed or released. The class functions based on events from the GPIO board.

| Parameter | Type | Description |
| ---- | ---- | ---- |
| `pin` | `int` | The `GPIO` pin the button is connected to |
| `name` | `str` | An identifying name used in logging and to identify in the publishing payload |
| `client` | `MQTTClient` | the standardised MQTT client |

## MQTT Topics

The default MQTT topic used in this driver is:

`bike/{DEVICE_ID}/button/report`

All button presses and releases will be published to this topic.

## MQTT Payload

The published payload on each press and release uses this a `JSON` structure:

```
{
    'button' : [button name]
    'state' : [1 for pressed] | [0 for released]
    'timestamp' : [time of publish]
}
```

## Driver Location

To see the `button_control` driver code:

[Drivers/button_control/button_control.py](https://github.com/Redback-Operations/redback-smartbike-iot/blob/main/Drivers/button_control/button_control.py)