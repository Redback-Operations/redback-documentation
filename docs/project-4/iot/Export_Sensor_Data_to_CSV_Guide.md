---
sidebar_position: 12
---
# Guide to Exporting Sensor Data from Serial Monitor to CSV

:::info
*Author:* Sohil Nagpal
:::

## Introduction

This guide provides step-by-step instructions on how to collect data from the MAX30102 sensor using an Arduino and export this data to a CSV file through the serial monitor. This process is essential for further analysis and visualization of the sensor data.

## Arduino Setup

### Sensor Code

Below is the Arduino code required to initialize the MAX30102 sensor and send its data (heart rate and oxygen saturation) to the serial monitor.

```cpp
#include "DFRobot_BloodOxygen_S.h"

// Define the I2C address for the MAX30102 sensor
#define I2C_ADDRESS 0x57

// Create an instance of the DFRobot_BloodOxygen_S_I2C class for I2C communication
DFRobot_BloodOxygen_S_I2C MAX30102(&Wire, I2C_ADDRESS);

void setup() {
  // Initialize serial communication at a baud rate of 115200
  Serial.begin(115200);

  // Attempt to initialize the MAX30102 sensor
  while (false == MAX30102.begin()) {
    Serial.println("init fail!");
    delay(1000);
  }

  Serial.println("init success!");
  Serial.println("start measuring...");
  MAX30102.sensorStartCollect();
}

void loop() {
  // Retrieve the heartbeat and SPO2 data from the sensor
  MAX30102.getHeartbeatSPO2();
  
  // Print the SPO2 value to the serial monitor
  Serial.print("SPO2 is : ");
  Serial.print(MAX30102._sHeartbeatSPO2.SPO2);
  Serial.println("%");

  // The sensor updates the data every 4 seconds, so delay for 4 seconds before the next read
  delay(4000);
}
```

## Python Script for Data Collection

### Setup and Execution

Here's a Python script that sets up a serial connection to read the data from the serial port and saves it to a CSV file for later analysis.

```python
# Save this as collect_data.py

import serial
import time

# Setup your serial port and baud rate. Replace '/dev/tty.usbmodemXXXX' with your actual device port
serial_port = '/dev/tty.usbmodemXXXX'
baud_rate = 115200

try:
    ser = serial.Serial(serial_port, baud_rate)
    time.sleep(2)  # Allow time for serial connection to initialize
    print("Connected to Arduino. Collecting data...")

    with open("output.csv", "w") as file:
        while True:
            data = ser.readline().decode().strip()  # read data from serial and decode it
            file.write(data + "\n")  # write data to CSV file
            print(data)  # print data to console

except serial.SerialException:
    print(f"Failed to connect on {serial_port}")
except KeyboardInterrupt:
    print("Interrupted by user, stopping data collection.")
finally:
    ser.close()  # Ensure serial connection is closed on exit
```

## Conclusion

This guide provides a comprehensive method to capture sensor data from the MAX30102 and export it to a CSV file using Arduino and Python. This setup is ideal for those who need to collect and analyze physiological data for health monitoring or research purposes.
