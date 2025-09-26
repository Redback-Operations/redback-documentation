---
sidebar_position: 2
---

# Environment Variables

```bash
export MQTT_HOSTNAME=...
export MQTT_USERNAME=...
export MQTT_PASSWORD=...
export MQTT_PORT=...
export DEVICE_ID=...
export HEART_RATE_ADAPTER_NAME=...
export HEART_RATE_ALIAS_PREFIX=...
export CADENCE_ADAPTER_NAME=...
export CADENCE_ALIAS_PREFIX=...
export FAN_ADAPTER_NAME=...
export FAN_ALIAS_PREFIX=...
export KICKR_MAC_ADDRESS=...
```

*A partial and redacted sample of the `.env` file*

To make sensitive information accessible but not displayed on the public repo, a `.env` file has been created in the home directory of the Raspberry Pi. This file's variables can be loaded by `bash` scripts then either parsed by the loading `bash` script to a `python` or other program, or the program can access it directly from the environment variables.

## Variables

Some vairables of interest include:

| Variable | Description |
| ---- | ---- |
| `DEVICE_ID` | ID of the Smartbike - used in MQTT topics |
| `MQTT_HOSTNAME` | MQTT broker host address |
| `MQTT_PORT` | MQTT broker port |
| `MQTT_USERNAME` | Configured MQTT username |
| `MQTT_PASSWORD` | Configured MQTT password |
| `KICKR_MAC_ADDRESS` | **KICKR smart trainer** MAC address used by driver to connect via BLE |
| `HEART_RATE_ALIAS_PREFIX` | BLE advertised name of the **TICKR heart rate monitor** - used by driver to connect via BLE |
| `CADENCE_ALIAS_PREFIX` | BLE advertised name of the **Wahoo cadence sensor** - used by driver to connect via BLE |
| `FAN_ALIAS_PREFIX` | BLE advertised name of the **Wahoo headwind fan** - used by driver to connect via BLE |
| `HEART_RATE_ADAPTER_NAME` | Adapter address of the Raspberry Pi's **BLE adapter** - used by drivers to connect via BLE - the same value for `FAN_ADAPTER_NAME` & `CADENCE_ADAPTER_NAME` |

## Adding, Removing, & Editing Variables

To modify the `.env` file open the `.env` file in the home directory using `nano`:

```
nano .env
```

## Loading using `bash` script

To load the environment variables using a `bash` script add the following:

```bash
# at top of script
source ~/.env

...

# print value
echo $DEVICE_ID

# use as a string
echo "Smartbike ID: ${DEVICE_ID}"
```

## Passing to `python` using `bash` script

To parse the variable to a `python` program, the `python` program must include the `python` `shebang` at the top of the file and configure an `ArgumentParser` using the `argparse` module:

```python
#!/usr/bin/env python3

import os
from argparse import ArgumentParser

...

# initialise parser
parser = ArgumentParser()
parser.add_argument('--device_id', dest='device_id', type=str, help="Smartbike unique id", default=os.getenv('DEVICE_ID'))

# load parsed arguments
args = parser.parse_args()

...

# use argument
print(f'Smartbike ID: {args.device_id}')
```

To parse the variables from the `bash` script to the `python` program - indicate the variable and values when instigating the `python` program parsing the variables as `string`:

```bash
source ~/.env

...

python3 ~/iot/Drivers/my-driver/driver.py --device_id ${DEVICE_ID}
```

*Order of parsed named arguments does not matter.*

## Loading without parsing in `python`

To load the variables without parsing explicitly from the `bash` script. Load the variables normally in the `bash` script and instigate the `python` program:

```bash
source ~/.env

...

python3 ~/iot/Drivers/my-driver/driver.py
```

In the python program use the `os` module to load the environment variables directly:

```python
#!/usr/bin/env python3

import os

...

device_id = os.getenv('DEVICE_ID')
```

## Further Information

- More information on [argparse](https://docs.python.org/3/library/argparse.html)
- More information on [shebangs](https://en.wikipedia.org/wiki/Shebang_(Unix))
