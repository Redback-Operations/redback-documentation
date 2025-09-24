---
sidebar_position: 1
---

# BLE Auto Connecting Script

![image](../img/architecture/bike-architecture.png)

Script location: [scripts/ble-auto-connect/](https://github.com/Redback-Operations/redback-smartbike-iot/tree/main/scripts/ble-auto-connect)

This script was created to handle persistent BLE issues we had with the bike. Connecting to the bike was not consistent, with failed pairing on start up and even manually connecting using the `bluetoothctl` interface on the Raspberry Pi not working consistently. This script should resolve these issues by using `bluetoothctl` and `expect` script to act like a user and automatically resolve the BLE connection.

## Starting the Script

To start this script run the following command from the home directory: 

`bash iot/scripts/ble-auto-connect/ble_auto_connect.sh`

## Script Requirements

### Expect Installed

Ensure `expect` is installed using:

`sudo apt-get install expect`

### KICKR MAC Address

The KICKR's MAC address must be accurately stored in the hidden `.env` file, in the home directory, with the following format:

`... KICKR_MAC_ADDRESS="XX:XX:XX:XX:XX:XX" ...`

*To access the hidden environment file use `nano .env` in the home directory*

### Bike NOT on Standby

Ensure that the bike is not on standby: the BLE indicator light on the KICKR is blinking blue and not off

![image](../img/smartbike-photos/kickr-connected.jpg)

*KICKR BLE indicator light located above ANT+ indicator light*

If it is on standby rotate the pedals a few times.

## Expected Process Behaviour

The script follows a simple flow of commands reacting to expected outputs to terminal from `bluetoothctl` commands and writing input commands into the terminal.

### Once Started

Once the script has been started, it enters commands into the terminal interface like a user, waiting for expected output from commands and responding to resolve any issues. 

```
Agent registered
[bluetooth]# default-agent
Default agent request successful
[bluetooth]# connect d9:07:e8:1c:db:94
Attempting to connect to d9:07:e8:1c:db:94
[CHG] Device D9:07:E8:1C:DB:94 Connected: yes
Failed to connect: org.bluez.Error.Failed
[CHG] Device D9:07:E8:1C:DB:94 Connected: no
[bluetooth]# connect d9:07:e8:1c:db:94
Attempting to connect to d9:07:e8:1c:db:94
[CHG] Device D9:07:E8:1C:DB:94 Connected: yes
Connection successful
[Wahoo KICKR 58CB]# exit
```

**DO NOT** attempt to enter anything into command-line during this process - if you must, terminate the script using `Ctrl + C` before doing so.

### BLE Scanning

```
[CHG] Controller B8:27:EB:DB:48:17 Discovering: yes
[NEW] Device CB:81:82:06:8A:F8 HEADWIND AF28
[NEW] Device E4:8F:3B:BB:66:82 E4-8F-3B-BB-66-82
[NEW] Device F2:93:DE:57:0C:2C F2-93-DE-57-0C-2C
[CHG] Device D9:07:E8:1C:DB:94 RSSI: -45
[CHG] Device D9:07:E8:1C:DB:94 UUIDs: 00001818-0000-1000-8000-00805f9b34fb
[CHG] Device D9:07:E8:1C:DB:94 UUIDs: 00001826-0000-1000-8000-00805f9b34fb
[NEW] Device C1:44:45:FD:29:12 C1-44-45-FD-29-12
[NEW] Device 47:0B:B1:7F:C4:E6 47-0B-B1-7F-C4-E6
[NEW] Device D7:C1:4A:AF:BF:C1 D7-C1-4A-AF-BF-C1
```

If the KICKR has not been registered by `bluetoothctl` then the script will automatically initiate a scan for all local BLE devices yielding a spam of output like above. This output should only last a few seconds at most a minute.

### Script Completion

If a connection was successfully achieved, an output to the terminal should indicate so:

```
Connection established with bike via BLE
```

And the BLE indicator light on the KICKR should become solid:

![image](../img/smartbike-photos/kickr-connected.jpg)

### Script Failure

The above process should only take a few seconds to a minute but can fail for unknown reasons and enter into a loop. If this happens, use `Ctrl + C` to terminate the script and then restart both the bike & Pi, and re-run the script.

If this does not fix the issue then refer to the [BLEConnectivityFix](BLEConnectivityFix.md) document to connect manually.

## Future

Some improvements to the script are desireable and left for future team members to implement:

- Running the script on Pi start up using a daemon to fully automate the connection
- Running the script on script start up (`start_all.sh`) so that BLE connection is always resolved before other processes initialise
- Running the script in a background process so that it does not interfer with the command-line
- Forever looping the script so that it will reconnect if the connection drops for some reason
- Extend script to handle any future encountered issues
- Change the regex pattern used to match the KICKR MAC address to be more forgiving

## Resources

- `bluetoothctl` - https://manpages.debian.org/unstable/bluez/bluetoothctl.1.en.html
- `expect` introduction - https://phoenixnap.com/kb/linux-expect
- Reading files using `tcl` (the backbone of `expect`) - https://wiki.tcl-lang.org/page/How+do+I+read+and+write+files+in+Tcl
- Bash script & expect script located in [scripts/ble-auto-connect/](https://github.com/Redback-Operations/redback-smartbike-iot/tree/main/scripts/ble-auto-connect)
