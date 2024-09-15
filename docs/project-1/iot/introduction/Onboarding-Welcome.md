---
sidebar_position: 1
---

# Onboarding Welcome

[Insert project image here]

**Project 1 - Smartbike VR**, combines our physical Smartbike with our self-developed applications to enhance exercise through gamification and technology. Project 1 is split into three teams:

* **VR Team** - responsible for development of the **VR game**.
* **IoT Team** - responsible for the Smartbike and any other IoT requirements.
* **Mobile Team** - responsible for the development of the **mobile app**.

## IoT Mission

The IoT team is primarily focused on the development of the Smartbike, aiming to develop a robust interface which will allow our other applications, such as the VR game and mobile app, to appropriately and consistently interact with the Smartbike system. This includes enabling applications to read and write to characteristics on the Smartbike, identify the operational status of the Smartbike, and to do this with acceptable latency.

As to achieve these goals, several project principals should be followed:

1. **Collaborate and communicate** with other teams to identify IoT functional requirements.

2. Solutions should follow a **blackbox design** - where deep technical knowledge is not required to interact with the Smartbike.

3. Solutions should **maximise freedom of control and minimize obfuscation**, selecting to allow application developers to decide on IoT requirements at the application level - *Provide more control and data than is necessary*.

4. **Test & Document** before completing tasks.

## System Architecture

[Insert diagram of system architecture here]

The Smartbike does not exist in a vacuum, it requires a variety of other systems to operate. The Smartbike itself, is made up by a **Wahoo Indoor Exercise Bike** and a connected **Raspberry Pi**. The Smartbike communicates *internally* using the **BLE GATT** protocol.

To interact with other applications, the Smartbike relies on **MQTT** for *external* communication. The MQTT broker is stored on a **virtual machine (VM)** run on the Burwood campus which requires connection to *Eduroam*.

:::danger[Important!]

Currently, we **do not** use the **VM**'s broker. Instead, a **public MQTT broker** is used and the Raspberry Pi is connected to the internet through **personal mobile hotspots**, rather than Deakin's Eduroam. This is done for when the bike must be moved for demonstration purposes.

:::

Applications can then interface with the Smartbike by *subscribing* and *publishing* to its MQTT topics.

A **database**, also stored on the **VM**, has been established for storing any data which we may wish to keep from the Smartbike: workout session data, exercise metrics, etc.

# What Next?

Follow the rest of the introduction, explore the existing codebase, or learn some of the technical background needed for working with the Smartbike. 

1. [Smartbike Introduction](Smartbike-Introduction)

2. [Developer Environment Setup](Developer-Environment-Setup)

3. **Know the code:**

    - [Technical Background Information](../technical-background-information)

    - [Codebase Documentation](../codebase-documentation)

