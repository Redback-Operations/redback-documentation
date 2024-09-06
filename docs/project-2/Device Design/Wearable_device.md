---
sidebar_position: 1
---

# Wearable IoT device for the Elderly

![Block Diagram of the Smart watch and its components](img/IoTWearableBlock.drawio.png)

This page and its children document the design and implementation of the hardware for Redback-Operations Smart Watch Project.

We're eagerly seeking a name and branding for it with the shortlist of:
- Safeguardia
- Elli
- Readbackaware
- Awarewear
- Lachesis


# Background/Objective

The smartwatch aspect of this project will be the primary physical interface between our users and the work that has been conducted between each of our project teams. It is a bespoke design to facilitate the capture of data of interest to our Predictive Modelling and Analytics teams while also designed with the aim of providing a feature set that will encourage our users to actively engage with the device. 

When designing the hardware we've had to balance the considerations between our data team and our end user. These considerations have included the physical interface of the device, where we've noted that the elderly tend to be averse to touch interfaces and have opted for our primary navigation to be tactile and mechanical using buttons and a wheel. The implemented sensor array has been selected primarily based on the requirements of the data analytics teams and with consideration to data that may be useful to them that isn't necessarily available on existing smart watches. 




# Getting Started

In the interest of making this as accessible to the developer as it is to the user, we have opted to base our device on the [Arduino Nano IoT 33](https://store-usa.arduino.cc/products/arduino-nano-33-iot). This means that all one needs to start developing for the project is the Arduino IDE or a compatible tool-chain.

The Arduino IDE is available [here](https://www.arduino.cc/en/software) with binaries for Windows 10+, macOS (intel / apple) and Linux (appimage but its available in many package repos and can be compiled from source). 

Going forward we will be migrating development to [PlatformIO](https://platformio.org/), A platform anogstic development environment for microcontrollers with extensions in a number of IDE's and text editors. 

With a way to work on the codebase now installed and configured, you may find the device software under 
`./Codebase/Complete_Code/`. \
At present this is a monolithic file containing the entire firmware for the device but in future we will be modularizing it for ease of maintenance. 

:::warning
Please ensure that any API keys in use are added to `secrets.h` and add that file to your .gitignore
:::

Work on the PCB has been conducted in [Altium Designer](https://www.altium.com/altium-designer) however the files can be imported into KiCAD. 

# Prerequisites

The libraries in use are mostly available within the Arduino Library Manager and are drivers for the sensors and display module. Please make sure that you have them enabled / installed. 

- [SPI.h - Built into Arduino.](https://www.arduino.cc/reference/en/language/functions/communication/spi/)
  - Enables communication with the Serial Peripheral Interface Protocol.

- [WiFiNINA.h - Available through the Library Manager and on github.](https://github.com/arduino-libraries/WiFiNINA)
  - Allows using the WiFiNINA module to perform wireless tasks.

- [Adafruit_Sensor.h - Available through the Library Manager and on github.](https://github.com/adafruit/Adafruit_Sensor)
  - Prerequisite Framework for other Adafruit Libraries.

- [DHT.h - Available through the Library Manager and on github.](https://github.com/adafruit/DHT-sensor-library)
  - Library for the DHT humidity / temperature sensor family. (Deprecated in the Mk2)

- [Adafruit_GFX.h - Available through the Library Manager and on github.](https://github.com/adafruit/Adafruit-GFX-Library)
  - Core graphics library for Adafruit displays. 

- [Adafruit_SSD1306.h - Available through the Library Manager and on github.](https://github.com/adafruit/Adafruit_SSD1306)
  - Monochrome OLED display used in the initial prototype (Deprecated in the Mk2).

- [Wire.h - Available through the Library Manager.](https://www.arduino.cc/reference/en/language/functions/communication/wire/)
  - Enables communication with the I2C protocol.

- [Adafruit_BME680.h - Available through the Library Manager and on github.](https://github.com/adafruit/Adafruit_BME680)
  - Library for the Temperature, Pressure, Humidity and Gas Sensor.

- [Arduino_LSM6DS3.h - Available through the Library Manager.](https://www.arduino.cc/reference/en/libraries/arduino_lsm6ds3/)
  - Library for the Nano IoT 33's Inbuilt Accelerometer, Gryoscope and Temperature Sensor. 

- [RTCZero.h - Available through the Library Manager.](https://www.arduino.cc/reference/en/libraries/rtczero/)
  - Permits RTC functions.

- [WiFiUdp.h - Available through the Library Manager.](https://www.arduino.cc/reference/en/libraries/wifi/wifiudp/)
  - Library for UDP packet Tx / Rx.

- [DFRobot_MAX30102.h - Must be downloaded and installed from the official repo.](https://github.com/DFRobot/DFRobot_MAX30102)
  - Library for the Heart-Rate and Oximeter Sensor.
  - To Install, download the library from the repo and save in your \Arduino\libraries directory.

- [ThingSpeak.h - Available through the Library Manager and on github.](https://github.com/mathworks/thingspeak-arduino)
  - Communications library for writing to the ThingSpeak API endpoints. This will probably be deprecated in the future due to the limited fields avaialable.



# Installation

A fresh from the fab Mk2 PCB will require the burning of a bootloader before it can be used with the Arduino IDE.\
The easiest way is to use another arduino acting as an ISP programmer. \
This is easy but might be a bit scary your first time because fair warning, if you do it wrong you can brick the board.\
But trust me, read the steps twice and then follow them step by step and she'll be right, you got this. \
The official walkthrough is available [here](https://support.arduino.cc/hc/en-us/articles/8991429732124-Burn-the-bootloader-on-Arduino-Nano-33-IoT).

# Folder Structure

The folder structure compartmentalizes the three aspects of our hardware repository, 
- CAD_Designs
    - Contain the designs for our case and custom PCB
- Codebase
    - Contains the functioning code in [Complete Code](https://github.com/Redback-Operations/Elderly_Wearable_Tech/tree/main/IoT_Wearable/Codebase/Complete_Code) as well as experiments, examples and archived efforts in their respective folders.
- Documentation
    - Contains written and visual deliverables, research notes, datasheets and guides. More yet to come. 
```
.
├── CAD_Designs
│   ├── Case
│   └── PCB
├── Codebase
│   ├── Archive
│   ├── Complete_Code
│   ├── Example_Code
│   └── Experiments
└── Documentation
    ├── DataSheets
    ├── Figures
    ├── ReleaseForms
    └── Videos

```

# Project Status

Presently, we are constructing the first iteration to fit an actual wristwatch form factor. A number of components have been changed or removed and the rest are in the process of being integrated into a custom PCB based on the Arduino Nano IoT 33. Once this prototype has been ordered, work on the project will snowball as we work to programmatically integrate everything into a new firmware for the device as well as building out a case. 

# Future Considerations

We've reached the limit of the Arduino IoT Nano 33's avaliable I/O and so any further additions will require either consolidation or migration to a new base Microcontroller. We are working to refactor the codebase such that it isn't monolithic. Based on testing with the new device it might be worth considering a larger screen but that determination has been set aside for later 

# Compliance and Safety
As this is a data collection platform targeting health data in particular, it is **paramount** that any subjects who have their data captured provide informed consent to the data capture. 
Please make use of the consent forms located under `Documentation/ReleaseForms` if using on someone not directly involved with development. 

It was mentioned above however it bares repeating: \
Credentials and Secrets such as API_Keys are scraped from public repos **constantly**.\
 Please make use of the secrets.h file for WiFi credentials, user accounts and API keys and add it to your `.gitignore`.\
Failure to do so will be grumbled at and subsequently mocked. 

## License

The Hardware of this project is bound under the terms of a [Creative Commons Noncommercial Sharealike 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) inherited from the Arduino Nano 33 IoT it is based on.\
The software is bound under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).\
The Datasheets are the property of their relevant authors and are only provided here for reference. 
Written Artefacts, reports and visual media are tbd

