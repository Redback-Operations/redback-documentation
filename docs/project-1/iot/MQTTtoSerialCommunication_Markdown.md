---
sidebar_position: 2
---
# Moving from Wireless MQTT connection to Serial

:::danger[Important!]

The VR headset does not have serial support and hence the following cannot be implemented.

:::

To switch from MQTT to serial communication for handling the button presses, you will need to modify your setup to use a serial connection (e.g., USB serial) instead of MQTT. Additionally, you will need a way to dynamically detect the serial port used by your device.



Here's how you can achieve this:

Steps to Implement Serial Communication

a)   	Identify Available Serial Ports: Use the <code>serial.tools.list_ports</code> module to dynamically identify available serial ports.

b)  	Setup Serial Communication: Initialize the serial connection and read button states through the serial port.



## Code Example

Here is an example Python script that replaces MQTT with serial communication. This script will dynamically find the correct serial port and read the button states from the Raspberry Pi.



## Required Libraries

First, make sure you have the <code>pyserial</code> library installed:

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/09fe7719-cc10-41e3-8674-450f836c03cd)
![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/a903afd6-c83a-49e6-a699-636404ee7479)



## Explanation of the Code

a)   	GPIO Setup: Same as before, configuring pins 11 and 12 as inputs for the right and left turn buttons, respectively.

b)  	Serial Port Detection: The <code>find_serial_port</code> function scans all available serial ports and returns the one that is suitable (e.g., containing "USB" or "ACM" in the description). Adjust this logic based on your specific device's identifiers.

c)   	Serial Communication: The <code>ButtonTest</code> function now sends button states over the serial connection instead of MQTT. The serial connection is established with the detected port using a baud rate of 9600 (adjustable as needed).

d)  	Main Loop: Continuously calls the <code>ButtonTest</code> function every second to check the button states and send updates via the serial connection.



## Handling Serial Port Changes

If the serial port changes, the script will dynamically detect the correct port at startup. Ensure that your VR game or receiving system is set up to handle incoming data over the serial connection.

This setup should provide a seamless transition from MQTT to serial communication, with dynamic port detection to handle different connection scenarios.

Below are detailed steps to implement serial communication for handling button presses in your smart bike project. This section will guide you through setting up serial communication, identifying available serial ports dynamically, and replacing MQTT with serial data transmission.



## Steps to Implement Serial Communication

a)   	Install Required Libraries

Before starting, ensure you have the necessary libraries installed. You'll need <code>pyserial</code> for serial communication. Install it using pip:

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/33ca3efe-5bf4-44d2-808a-d53deded8ee3)


b)  	Configure GPIO for Button Inputs

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/a569796b-52a8-427a-b5c6-84a695a7ca81)

Set up the GPIO pins on your Raspberry Pi to read the states of the buttons. Configure pins 11 and 12 as inputs for the right and left turn buttons, respectively.

c)   	Identify Available Serial Ports Dynamically


To make your system robust and flexible, it's important to dynamically identify the serial port that the Raspberry Pi will use to communicate with the VR game. This way, you won't have to manually specify the port each time it changes.

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/c8874062-0af1-44c3-aa4c-7df379ea4e8d)


In this function, <code>serial.tools.list_ports.comports()</code> lists all available serial ports. The function checks each port description for identifiers such as "USB" or "ACM". If a suitable port is found, it returns the port name (e.g., <code>/dev/ttyUSB0</code>).



d)  	Setup Serial Communication

Initialize the serial connection using the port identified in the previous step. Set an appropriate baud rate (e.g., 9600).

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/aecf62b4-363a-4aae-ba3c-ca541aa51e7c)


e)  	Replace MQTT with Serial Communication

Modify the button state checking function to send data over the serial connection instead of publishing to MQTT topics.

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/e881f0a6-7689-446b-8bbc-c498b1267dd1)


In this function, <code>serial_conn.write</code> sends the button states (<code>RIGHT</code>, <code>R_LOW</code>, <code>LEFT</code>, <code>L_LOW</code>) as byte strings over the serial connection.



f)        Implement the Main Loop

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/e34a4847-a13f-45ec-b176-379d032b939f)


In the main part of your script, use a loop to continuously read the button states and send updates via the serial connection. Ensure proper cleanup and error handling.



g) Ensure Proper Resource Management

·   	Error Handling: The <code>try</code> block ensures that any exceptions (e.g., no serial port found) are caught and handled gracefully.

·   	Cleanup: The <code>except KeyboardInterrupt</code> block ensures that GPIO pins are cleaned up and the serial connection is closed when the script is interrupted (e.g., by pressing Ctrl+C).



By following these steps, you transition your button handling from MQTT to serial communication, making the system adaptable to different port configurations. The key steps include configuring GPIO pins, dynamically identifying serial ports, setting up the serial connection, and sending button states over this connection. This approach enhances flexibility and robustness in your smart bike project, ensuring smooth integration with the VR game.


Handling serial port changes dynamically is crucial for ensuring that your system can adapt to different hardware configurations and connection scenarios. Here's a detailed explanation on how to handle serial port changes effectively:



Handling Serial Port Changes: When dealing with serial communication, it's common to encounter scenarios where the serial port name or connection changes. This could happen if you plug the device into a different USB port, use a different computer, or if the operating system assigns a different port name. To manage these changes gracefully, follow these steps:



a)   	Dynamic Serial Port Detection

Instead of hardcoding the serial port name, use a method to dynamically detect the available serial ports and select the correct one based on specific criteria.

Code Example for Dynamic Port Detection:

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/aa90282e-1143-4800-b106-0fdb95f29502)

In this function:

·   	<code>serial.tools.list_ports.comports()</code> provides a list of all available serial ports.

·   	The function iterates through the list, checking each port’s description or device name for keywords like "USB" or "ACM", which are typically associated with USB serial devices.

·   	If a matching port is found, the function returns the port name (e.g., <code>/dev/ttyUSB0</code> or <code>COM3</code>).

·   	If no matching port is found, an exception is raised.





b)  	Initialize Serial Communication

Use the detected serial port to establish a serial connection. This ensures that your application connects to the correct port, regardless of changes.



Code Example for Serial Initialization:

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/6bf53f94-7393-4e18-9ad7-f98dcdc1ce05)

In this example:

·   	The <code>find_serial_port()</code> function is called to get the correct serial port.

·   	<code>serial.Serial</code> is used to open a connection to the detected port with a specified baud rate and timeout.

·   	If an exception occurs (e.g., no suitable port found), it is caught and printed.




c)   	Continuous Monitoring and Error Handling

In the main loop of your application, monitor the button states and handle any exceptions that may occur during serial communication. This ensures that your application can recover gracefully from errors such as disconnection or port changes.



##Code Example for Main Loop with Error Handling:

![image](https://github.com/KrishnPrayag/redback-documentation/assets/127953518/8cff291f-3819-4c45-a6d3-629ac65f4423)


In this example:

·   	The main loop continuously calls <code>ButtonTest</code> to read button states and send them over the serial connection.

·   	If a <code>serial.SerialException</code> occurs (e.g., due to disconnection), it is caught, and the script attempts to reinitialize the serial connection by finding the port again and reopening it.

·   	The outer <code>try</code> block handles general exceptions, ensuring that any other errors are caught and handled gracefully.

·   	The <code>KeyboardInterrupt</code> exception ensures that the GPIO pins are cleaned up and the serial connection is closed when the script is interrupted.



Handling serial port changes dynamically involves:

·   	Dynamic Port Detection: Using <code>serial.tools.list_ports</code> to list and identify available serial ports based on specific criteria (e.g., containing "USB" or "ACM").

·   	Robust Initialization: Establishing the serial connection using the detected port and handling exceptions to ensure the connection can be reestablished if it changes.

·   	Continuous Monitoring and Error Handling: Implementing error handling in the main loop to detect and recover from serial communication errors, such as disconnections.

This approach ensures that your system remains flexible and resilient to changes in the serial port configuration, providing a seamless user experience.
