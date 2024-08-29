---
sidebar_position: 1
---
 # How to fix Bluetooth Connectivity for Raspberry Pi with Wahoo device connection?

Due to the volatility of BLE connection, while running the script to have the Raspberry Pi send data to the cloud, you might have encountered the following message:

[MAC ADDRESS] Connected

[MAC ADDRESS] Disconnected

While research is being done to move to a serial connection, I have created a way through which the Wahoo device will stay connected to the Raspberry after which the script can be ran for testing and showcases.

Here are the steps to follow:

1) Open a terminal in the Raspberry Pi.


1) Ensure the Pi’s Bluetooth is switched on.
1) Type ‘sudo bluetoothctl’. It has already been installed in Bike 1’s Raspberry Pi.

1) Type in ‘agent on’, then ‘default-agent’ to enable device scanning and connections.
1) As the device is already connected, you can type connect [MAC ADDRESS OF DEVICE]\*.
1) In case of the device being unpaired with the Pi, type in ‘pair [MAC ADDRESS OF DEVICE]\*.
1) Run your script and the Bluetooth connectivity will stay on throughout the script being ran.

\*Check the constants.py file in the lib file from the [redback-smartbike-iot](https://github.com/Redback-Operations/redback-smartbike-iot) repository.
