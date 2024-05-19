---
sidebar_position: 4
---

# Heart rate initializing documentation

Documentation Guide to Using Wahoo TICKR Heart Rate Sensor with Arduino Nano 33 IoT

:::info
Author: Mayank Sharma
:::




# In-Depth Guide to Using Wahoo TICKR Heart Rate Sensor with Arduino Nano 33 IoT

## Overview
This comprehensive guide aims to help junior students understand how to use the Wahoo TICKR heart rate sensor with the Arduino Nano 33 IoT. The objective is to connect the sensor, read the heart rate data, and display it using the Arduino IDE and the BLE (Bluetooth Low Energy) library.

## 1. Materials Needed
### 1. Wahoo TICKR Heart Rate Sensor
- **Description**: The Wahoo TICKR is a wearable sensor that measures your heart rate and transmits the data wirelessly via Bluetooth. It is typically worn on the chest and can be used during various physical activities to monitor heart rate in real-time.
- **Key Features**: Accurate heart rate monitoring, Bluetooth and ANT+ connectivity, long battery life.
- **Setup**: Attach the sensor to the provided chest strap, ensuring the electrodes are in contact with your skin. Secure the strap snugly around your chest.

### 2. Arduino Nano 33 IoT
- **Description**: This is a compact microcontroller board with built-in Bluetooth Low Energy (BLE) capabilities. It is designed for IoT (Internet of Things) projects, making it ideal for connecting to sensors and other BLE devices.
- **Key Features**: ARM Cortex-M0+ processor, built-in Wi-Fi and BLE, 48 MHz clock speed, 256 KB flash memory.
- **Setup**: Familiarize yourself with the board layout, including the micro-USB port, power pins, digital I/O pins, and the onboard LED.

### 3. USB Cable for Arduino Nano 33 IoT
- **Description**: A USB cable is required to connect the Arduino Nano 33 IoT to your computer for programming and power supply. It typically uses a micro-USB or USB-C connector, depending on the version of the board.
- **Setup**: Ensure you have the appropriate cable type for your board and connect it to a USB port on your computer.

### 4. Arduino IDE installed on your computer
- **Description**: The Arduino Integrated Development Environment (IDE) is a software application used to write, upload, and debug code on Arduino boards. It supports a wide range of Arduino boards and provides an easy-to-use interface for programming.
- **Key Features**: Code editor, built-in libraries, board manager, serial monitor.
- **Setup**: Ensure you have the latest version of the Arduino IDE installed. You can download it from the [Arduino official website](https://www.arduino.cc/en/software).

## 2. Wahoo TICKR LED Indicators
Understanding the LED indicators on the Wahoo TICKR sensor is crucial for troubleshooting and confirming the sensor's status:

- **Red and Blue lights blink together**: Indicates that the sensor is powered on and ready to use.
  - **Troubleshooting**: If the lights do not blink together when the sensor is turned on, check the battery or ensure the sensor is properly attached to the chest strap.

- **Blue light blinks continuously**: The sensor is actively searching for a heart rate. This usually occurs when the sensor is not properly attached to the body or if it is having trouble detecting a pulse.
  - **Troubleshooting**: Ensure the sensor is snugly attached and the electrodes are in contact with your skin. Moistening the electrodes slightly can help improve contact.

- **Blue and Red lights blink alternately**: The sensor is successfully detecting and transmitting heart rate data. This is the normal operating mode when the sensor is properly attached and functioning correctly.
  - **Troubleshooting**: If you do not see this pattern during use, recheck the sensor attachment and ensure it is within the transmission range of the receiving device.

## 3. Step-by-Step Instructions

### 1. Setting Up Arduino IDE
#### a. Install Arduino IDE
##### Download and Install
- **Windows**: After downloading the installer, run the executable file and follow the on-screen instructions to complete the installation.
  - **Steps**:
    - Download the installer.
    - Double-click the downloaded file.
    - Follow the installation wizard, accepting the default options.
    - Click 'Install' and wait for the process to complete.

- **MacOS**: Open the downloaded file and drag the Arduino application to your Applications folder. Double-click the application to launch it.
  - **Steps**:
    - Download the disk image (.dmg) file.
    - Open the disk image and drag the Arduino IDE icon to the Applications folder.
    - Launch the Arduino IDE from the Applications folder.

- **Linux**: Extract the downloaded tar.gz file and run the install.sh script in a terminal. You may need to provide administrative permissions.
  - **Steps**:
    - Download the tar.gz file.
    - Open a terminal and navigate to the download directory.
    - Extract the file using `tar -xvf filename.tar.gz`.
    - Run the installation script using `./install.sh`.

##### Verify Installation
Once installed, open the Arduino IDE. You should see the main window with options to create a new sketch, open existing ones, and access the library manager. Ensure there are no error messages upon startup.
- **Steps**:
  - Launch the Arduino IDE.
  - Verify that the IDE opens without error messages.
  - Check the menus and toolbars to ensure all options are available.

#### b. Install ArduinoBLE Library
##### Open Arduino IDE
Launch the Arduino IDE on your computer.

##### Library Manager
Navigate to `Sketch > Include Library > Manage Libraries`. This will open the Library Manager window where you can search for and install additional libraries.
- **Steps**:
  - Click on `Sketch` in the menu bar.
  - Select `Include Library`.
  - Click on `Manage Libraries`.

##### Search and Install
In the Library Manager, type `ArduinoBLE` in the search bar. Locate the `ArduinoBLE` library in the search results and click the `Install` button.
- **Steps**:
  - Type `ArduinoBLE` in the search bar.
  - Find the library in the list and click `Install`.
  - Wait for the installation to complete.

##### Usage
This library provides essential functions for BLE operations on the Arduino Nano 33 IoT, including scanning for devices, connecting, and communicating with BLE peripherals.

### 4. Initializing BLE on Arduino Nano 33 IoT
To use the BLE capabilities of the Arduino Nano 33 IoT, you need to initialize the BLE module.

#### a. Begin BLE Service
##### Initialization
Start by initializing the BLE service in your Arduino sketch. This sets up the BLE module to begin communication. Use a function to initialize the BLE hardware and check if the initialization is successful. If not, print an error message to the Serial Monitor and halt the program.
- **Steps**:
  - Call a function to initialize the BLE module, such as `BLE.begin()`.
  - Check the return value of the initialization function.
  - If initialization fails, use `Serial.print` to display an error message and stop further execution.

#### b. Scan for Heart Rate Service
##### UUID Scanning
Configure the BLE module to scan specifically for devices that advertise the Heart Rate service, identified by the UUID "180D". Use a function to start scanning for BLE devices with the Heart Rate service UUID. This helps to quickly identify the Wahoo TICKR among other BLE devices in the vicinity.
- **Steps**:
  - Use a scanning function to look for devices with the UUID "180D".
  - Monitor the scanning process to ensure the target device is detected.
  - Print messages to the Serial Monitor to indicate the scanning status.

### 5. Connecting to Wahoo TICKR
After initializing the BLE module, the next step is to establish a connection with the Wahoo TICKR heart rate sensor.

#### a. Scan and Detect Device
##### Continuous Scanning
Continuously scan for BLE devices within range using a loop. Use a loop to check for nearby BLE devices and identify the Wahoo TICKR by its local name.
- **Steps**:
  - Implement a loop that repeatedly scans for BLE devices.
  - Use a function to retrieve detected devices.
  - Compare each device's local name to identify the Wahoo TICKR.

##### Device Identification
Ensure that the detected device is the Wahoo TICKR by comparing its local name. This prevents connecting to the wrong device. Retrieve the local name of the BLE device and compare it with the expected name.
- **Steps**:
  - Retrieve the local name of each detected device using a function like `peripheral.localName()`.
  - Compare the retrieved name with the expected name, such as "TICKR 0A5B".
  - Print messages to the Serial Monitor to indicate if the target device is found.

#### b. Establish Connection
##### Stop Scanning
Once the Wahoo TICKR is detected, stop scanning to conserve power and processing resources. Use a function to stop the BLE scanning process.
- **Steps**:
  - Call a function to stop scanning, such as `BLE.stopScan()`.
  - Confirm that scanning has stopped by printing a message to the Serial Monitor.

##### Attempt Connection
Try to establish a connection with the Wahoo TICKR. Use a function to connect to the detected BLE device and handle connection success or failure.
- **Steps**:
  - Call a function to connect to the device, such as `peripheral.connect()`.
  - Check the connection status and print messages to the Serial Monitor to indicate success or failure.
  - If the connection fails, retry the connection or notify the user of the issue.

### 6. Discovering Services and Characteristics
Upon establishing a connection with the Wahoo TICKR, discover its services and characteristics to access the heart rate data.

#### a. Discover Attributes
##### Service Discovery
Discover the services provided by the Wahoo TICKR. Use a function to discover all attributes (services and characteristics) provided by the connected device.
- **Steps**:
  - Call a function to discover attributes, such as `peripheral.discoverAttributes()`.
  - Confirm the discovery process by printing messages to the Serial Monitor.

##### Characteristic Discovery
Identify the characteristic for heart rate measurement within the Heart Rate service (UUID "2A37"). Retrieve the Heart Rate service and its characteristics using the appropriate functions.
- **Steps**:
  - Retrieve the Heart Rate service using a function, such as `peripheral.service("180D")`.
  - Within the service, retrieve the heart rate characteristic using a function, such as `service.characteristic("2A37")`.
  - Print messages to the Serial Monitor to confirm the discovery of the heart rate characteristic.

#### b. Subscribe to Heart Rate Characteristic
##### Subscription
Subscribe to the heart rate characteristic to start receiving data updates. Use a function to subscribe to notifications for the heart rate characteristic.
- **Steps**:
  - Call a function to subscribe to the characteristic, such as `characteristic.subscribe()`.
  - Confirm the subscription by printing messages to the Serial Monitor.
  - Ensure that the Arduino is set to receive notifications when the heart rate data is updated.

### 7. Reading and Displaying Heart Rate Data
With the subscription in place, the Arduino can start receiving and processing heart rate data from the Wahoo TICKR.

#### a. Poll for Data Updates
##### Polling
Continuously poll the BLE characteristic for new data. Use a loop to call functions that process BLE events and check for updates in the heart rate characteristic.
- **Steps**:
  - Implement a loop that regularly calls a function to process BLE events, such as `BLE.poll()`.
  - Within the loop, check if the heart rate characteristic has been updated using a function, such as `characteristic.valueUpdated()`.
  - Print messages to the Serial Monitor to indicate when new data is received.

#### b. Extract and Print Heart Rate
##### Data Extraction
Extract the heart rate value from the received data. Use a function to retrieve the current value of the heart rate characteristic and process the data to extract the heart rate value.
- **Steps**:
  - Call a function to get the current value of the characteristic, such as `characteristic.value()`.
  - Extract the heart rate value from the data array. The heart rate value is typically located at a specific index.
  - Convert the extracted value to a human-readable format.

##### Display Data
Print the heart rate value to the Serial Monitor. Use `Serial.print` and `Serial.println` functions to display the heart rate data in the Serial Monitor.
- **Steps**:
  - Use `Serial.print` to display the heart rate value.
  - Use `Serial.println` to print the value with a new line.
  - Ensure the Serial Monitor baud rate is set to 9600 for proper communication.

### 8. Uploading the Code and Monitoring Output
To execute the program and view the heart rate data:

#### a. Connect Arduino to Computer
##### USB Connection
Use a USB cable to connect your Arduino Nano 33 IoT to your computer.
- **Steps**:
  - Ensure the correct cable type (micro-USB or USB-C) is used.
  - Connect one end of the cable to the Arduino and the other end to a USB port on your computer.
  - Verify that the Arduino is powered on and recognized by the computer.

#### b. Select Board and Port
##### Board Selection
In the Arduino IDE, go to `Tools > Board` and select `Arduino Nano 33 IoT`.
- **Steps**:
  - Click on `Tools` in the menu bar.
  - Select `Board`.
  - Choose `Arduino Nano 33 IoT` from the list.

##### Port Selection
Select the appropriate port under `Tools > Port`. The correct port usually corresponds to the one associated with the connected Arduino.
- **Steps**:
  - Click on `Tools` in the menu bar.
  - Select `Port`.
  - Choose the port that corresponds to your Arduino Nano 33 IoT (e.g., COM3 on Windows or /dev/ttyUSB0 on Linux).

#### c. Upload the Program
##### Upload
Click the upload button in the Arduino IDE to transfer the code to the Arduino. The status bar will confirm when the upload is complete.
- **Steps**:
  - Click the upload button (right-pointing arrow) in the Arduino IDE toolbar.
  - Wait for the status bar to indicate that the upload is complete.
  - Monitor any error messages during the upload process and resolve them if necessary.

#### d. Open Serial Monitor
##### Serial Monitor
Open the Serial Monitor from `Tools > Serial Monitor` to view the heart rate data. Ensure the baud rate is set to 9600. The heart rate data will be displayed in real-time.
- **Steps**:
  - Click on `Tools` in the menu bar.
  - Select `Serial Monitor`.
  - Set the baud rate to 9600 in the Serial Monitor window.
  - Observe the heart rate data being printed in real-time.

## 9. Accessing the Code on GitHub
To access the complete code used in this guide, visit the following GitHub repository: [Heart Rate Sensor Code](https://github.com/Redback-Operations/redback-orion/blob/main/IOT_HRS/heart_rate_sensor_2/heart_rate_sensor_2.ino)

## Troubleshooting Tips
### BLE Initialization Failure
#### Check Power Supply
Ensure the Arduino Nano 33 IoT is properly powered via USB.
- **Explanation**: Inadequate power supply can cause initialization failures. Ensure the USB connection is secure and the power source is stable.
- **Steps**:
  - Verify that the USB cable is properly connected to both the Arduino and the computer.
  - Ensure the computer's USB port is functioning correctly.

#### Reinstall Library
Try reinstalling the ArduinoBLE library if initialization continues to fail.
- **Explanation**: A corrupted or outdated library can cause issues. Reinstalling ensures you have the latest and correct version.
- **Steps**:
  - Open the Library Manager in the Arduino IDE.
  - Locate the ArduinoBLE library and uninstall it.
  - Reinstall the library and restart the Arduino IDE.

### Device Not Found
#### Ensure Sensor is On
The Wahoo TICKR must be turned on and within range for the Arduino to detect it.
- **Explanation**: The sensor should be active and in pairing mode. Check the LED indicators to confirm its status.
- **Steps**:
  - Check that the sensor is powered on and the LED indicators are blinking as expected.
  - Ensure the sensor is within the Bluetooth range of the Arduino.

#### Minimize Interference
Reduce other Bluetooth devices to minimize interference during scanning.
- **Explanation**: Multiple active Bluetooth devices can cause signal interference, making it difficult to detect the sensor.
- **Steps**:
  - Turn off other nearby Bluetooth devices or move them away from the Arduino and sensor.
  - Retry the scanning process in a less congested environment.

### Connection Issues
#### Restart Devices
Restart both the Wahoo TICKR and Arduino Nano 33 IoT to reset connections.
- **Explanation**: Sometimes, restarting the devices can resolve temporary connection issues caused by software glitches.
- **Steps**:
  - Turn off the Wahoo TICKR, wait for a few seconds, and then turn it back on.
  - Disconnect and reconnect the Arduino Nano 33 IoT from the computer.
  - Retry the connection process.

## Video Tutorial
For a video tutorial, watch [this YouTube video](https://youtu.be/X6fjwMR9INM).
