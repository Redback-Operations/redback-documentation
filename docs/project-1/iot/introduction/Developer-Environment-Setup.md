---
sidebar_position: 3
---

# Developer Environment Setup

Working with the Smartbike requires a few extra tools compared to working on applications like the VR game.

## General Needs

You still require general things like:

- IDE of your choice.
- [GitHub Desktop app](https://desktop.github.com/download/) or [GitHub CLI](https://cli.github.com) or equivalent.

## Project Repositories

Fork the Redback Operation repositories, and bookmark both the original and personal-forks for ease of access.

- [IoT Repo](https://github.com/Redback-Operations/redback-smartbike-iot)
- [Documentation Repo](https://github.com/Redback-Operations/redback-documentation)
- [VR repo](https://github.com/Redback-Operations/redback-smartbike-iot)

Clone the repositories to your PC to be ready for development.

## Tools for the Smartbike & Raspberry Pi

To ease development on the Raspberry Pi it is recommended to prepare the following tools to assist in development:

- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) or equivalent - for accessing the Raspberry Pi.
- [FileZilla](https://filezilla-project.org/download.php?type=client) or [WinSCP](https://winscp.net/eng/download.php) or equivalent FTP application - for transfering files between your development environment and the Raspberry Pi.
- Install dependencies such as Python's [gatt library](https://pypi.org/project/gatt/) and [paho MQTT](https://pypi.org/project/paho-mqtt/) - for hints during development.

## Personal Mobile Hotspot

The Raspberry Pi currently (T2 2024) connects to the internet through connecting to someone's personal mobile hotspot on their phone. As long as you have the same SSID and password setup it will be able to connect. **Reach out to your project lead (or if you are the lead read the handover document) for the SSID and password to set.**

## Ready to Start

Ask your project lead for tasks to get started on or...

- See the Planner on Teams for tasks (it is like Trello).
- [Delve into the code](https://github.com/Redback-Operations/redback-smartbike-iot)