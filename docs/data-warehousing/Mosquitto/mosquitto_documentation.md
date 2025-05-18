---
sidebar_position: 2
sidebar_label: Mosquitto MQTT Broker
---

**Last updated by:** RichardWhellum, **Last updated on:** 09/05/2025


**Last updated by:** RichardWhellum, **Last updated on:** 09/05/2025


# Mosquitto MQTT Broker

:::info
**Document Creation:** 6 May, 2025. **Last Edited:** 6 May, 2025. **Authors:** Richard Whellum.
<br></br> **Document Code:** DOC1. **Effective Date:** 6 May, 2025. **Expiry Date:** 6 May, 2026.
:::

## Overview

This document outlines the configuration, usage, and operational practices for the **Mosquitto MQTT Broker** deployed on the **Data Warehouse Ubuntu VM** (`10.137.0.149`).

**Eclipse Mosquitto** is a lightweight, open-source MQTT (Message Queuing Telemetry Transport) broker optimised for minimal network usage and ideal for IoT or lightweight messaging systems. It supports MQTT versions 3.1, 3.1.1, and 5.0.

---

## System Details

| Setting                | Value                                |
| ---------------------- | ------------------------------------ |
| **Host OS**            | Ubuntu                               |
| **Broker IP**          | `10.137.0.149`                       |
| **Port**               | `1883` (unencrypted, default)        |
| **Persistence**        | Enabled                              |
| **Logging**            | `/var/log/mosquitto/mosquitto.log`   |
| **Anonymous Access**   | Enabled (no restrictions configured) |
| **TLS/Authentication** | Not configured                       |


---

## Installation Summary

To install and enable the Mosquitto broker and client tools:

```bash
sudo apt update
sudo apt install -y mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

---

## Configuration

### Primary Config File

Path: `/etc/mosquitto/mosquitto.conf`

```conf
pid_file /var/run/mosquitto.pid

# Persistence
persistence true
persistence_location /var/lib/mosquitto/

# Logging
log_dest file /var/log/mosquitto/mosquitto.log
log_type all

# Include additional configs
include_dir /etc/mosquitto/conf.d
```

Common options:
| Option             | Description                                |
|--------------------|--------------------------------------------|
| `listener <port>`  | Set the port the broker listens on         |
| `allow_anonymous`  | Allow connections without username/password|
| `persistence true` | Enable message persistence                 |
| `log_dest stdout`  | Log output to stdout (useful for Docker)   |
| `password_file`    | File containing valid user credentials     |


### Key Parameters

- **Persistence** ensures messages and subscriptions survive broker restarts.
- **Logging** is set to capture all message and connection-related activity.
- `` allows modular configuration files (e.g., future access control or TLS settings).

---


## Logs & Monitoring

### View Log Output

```bash
sudo tail -f /var/log/mosquitto/mosquitto.log
```

### Common Log Entries

- Connection status
- Topic subscriptions
- Message publishing
- Errors or config issues


---

## Troubleshooting

| Problem                       | Suggested Fix                                                    |
| ----------------------------- | ---------------------------------------------------------------- |
| Port 1883 not open or refused | Confirm the service is active: `sudo systemctl status mosquitto` |
| Messages not received         | Verify topic names and client connectivity                       |
| Broker fails to start         | Check config file syntax and permissions in `conf.d/`            |
| Log file not updating         | Ensure write permissions for `/var/log/mosquitto/`               |

---

## File & Directory Summary

| Path                               | Description                      |
| ---------------------------------- | -------------------------------- |
| `/etc/mosquitto/mosquitto.conf`    | Main broker configuration        |
| `/etc/mosquitto/conf.d/`           | Directory for additional configs |
| `/var/log/mosquitto/mosquitto.log` | Primary log file                 |
| `/var/lib/mosquitto/`              | Persistence data location        |
