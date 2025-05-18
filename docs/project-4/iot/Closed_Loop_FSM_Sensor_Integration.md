---
sidebar_position: 14
---

**Last updated by:** Sohil Nagpal, **Last updated on:** 19/05/2024


**Last updated by:** Sohil Nagpal, **Last updated on:** 19/05/2024

# Research on Closed-Loop Systems and FSMs for Sensor Integration

:::info
*Author:* Sohil Nagpal
:::

## Introduction

This report explores the application of closed-loop systems and Finite State Machines (FSMs) to enhance the integration and functionality of multiple sensors—specifically heart rate monitors, accelerometers, and GPS—within our project. We discuss how these methods can lead to more accurate data collection and improved system performance.

## Understanding Closed-Loop Systems

Closed-loop systems, or feedback control systems, utilize feedback to control the state of a system based on its output. In the context of sensor integration, closed-loop systems can adjust the sensitivity or sampling rate of sensors based on real-time data, enhancing the system's adaptability and accuracy.

### Application in Sensor Integration

For instance, if the heart rate sensor detects an anomaly in readings, the system could automatically increase the sampling rate for more detailed data, while simultaneously adjusting the accelerometer to monitor for unusual movements, enhancing the detection of potential emergencies.

## Finite State Machines (FSMs) Overview

A Finite State Machine is a computational model consisting of a limited number of states. It's a powerful tool for managing complex logic in systems that need to handle multiple sensor inputs efficiently.

### FSMs in Our Project

In our sensor setup, an FSM could manage states such as:
- **Initialization**: Setting up sensor parameters and calibrating.
- **Data Collection**: Regular monitoring and data recording.
- **Anomaly Detection**: Identifying unusual readings and responding appropriately.
- **Error Handling**: Managing sensor errors or failures.
- **Power Saving**: Reducing power consumption when sensors are not needed.

## Implementing Closed-Loop Systems and FSMs

### Using Arduino Code from Previous Example

Let's enhance the Arduino setup to include basic FSM and closed-loop behavior. Below is a revised version of your sensor code that incorporates these concepts:

```cpp
#include "DFRobot_BloodOxygen_S.h"

// Define the I2C address for the MAX30102 sensor
#define I2C_ADDRESS 0x57
DFRobot_BloodOxygen_S_I2C MAX30102(&Wire, I2C_ADDRESS);

enum State { INIT, COLLECT_DATA, CHECK_DATA, ERROR };
State currentState = INIT;

void setup() {
  Serial.begin(115200);
}

void loop() {
  switch (currentState) {
    case INIT:
      if (MAX30102.begin() == true) {
        currentState = COLLECT_DATA;
        Serial.println("Sensor initialized.");
      } else {
        Serial.println("Sensor failed to initialize.");
        currentState = ERROR;
      }
      break;
    case COLLECT_DATA:
      MAX30102.sensorStartCollect();
      currentState = CHECK_DATA;
      break;
    case CHECK_DATA:
      if (checkSensorData()) {
        Serial.println("Data is within expected range.");
        delay(1000); // Data collection interval
      } else {
        Serial.println("Data out of range, adjusting parameters...");
        adjustSensorSettings();
      }
      break;
    case ERROR:
      handleSensorError();
      break;
  }
}

bool checkSensorData() {
  // Logic to check if data is within an expected range
  return true;
}

void adjustSensorSettings() {
  // Adjust settings based on data feedback
}

void handleSensorError() {
  // Handle errors and attempt to reset sensors
}
```

## Conclusion

Integrating closed-loop systems and FSMs with multiple sensors in our project allows for more dynamic and responsive management of sensor data. This approach not only improves the accuracy and reliability of the data collected but also enhances the system's ability to adapt to different conditions and detect anomalies more effectively.
