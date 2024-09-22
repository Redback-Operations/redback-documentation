---
sidebar_position: 3
---

# Redback - MQTT Temperature Plugin in Nagios 

:::important

**Yuhan Bulathsinhalage**  
**Date:** 21/09/2024

:::

# Guide to Setting Up MQTT Temperature Plugin in Nagios

This guide will help you integrate and configure an MQTT temperature plugin in Nagios for real-time monitoring of IoT temperature sensors.

## Step 1: Install Required Dependencies

Before configuring the plugin, ensure that all dependencies are installed on your Nagios server. The MQTT plugin may require Python or other libraries. You can install these dependencies by running the following command:

```bash
sudo apt-get install python3 python3-pip
pip3 install paho-mqtt
```

## Step 2: Configure `commands.cfg`

You will need to define the command for the MQTT temperature plugin in the `commands.cfg` file.

1. Open the `commands.cfg` file:
   ```bash
   sudo nano /usr/local/nagios/etc/objects/commands.cfg
   ```

2. Add the following command definition to the file:
   ```bash
   define command {
      command_name check-mqtt_temperature
      command_line /usr/local/nagios/libexec/check-mqtt_temperature.py -H $ARG1$ -t $ARG2$
   }
   ```

   This defines the custom command that Nagios will use to check the temperature data from the MQTT broker. Save and exit the file.

## Step 3: Configure `localhost.cfg`

Next, configure the service in the `localhost.cfg` file to enable monitoring using the temperature plugin.

1. Open the `localhost.cfg` file:
   ```bash
   sudo nano /usr/local/nagios/etc/objects/localhost.cfg
   ```

2. Add the following service definition for the MQTT temperature plugin:
   ```bash
   define service {
      use                   generic-service
      host_name             localhost
      service_description   MQTT Temperature Check
      check_command         check-mqtt_temperature!10.137.0.149!iot/device/temperature
      check_interval        1
      retry_interval        1
      contacts              nagiosadmin
      notifications_enabled 1
      notification_options  w,u,c,r
      notification_interval 60
      notification_period   24x7
   }
   ```

   This service will run the MQTT temperature check every minute and notify the admin via email if abnormal conditions are detected.

## Step 4: Configure Alerts and Notifications

To ensure email notifications are sent when a temperature threshold is crossed, configure the email alerts in Nagios.

1. Install the necessary mail utilities:
   ```bash
   sudo apt-get install mailutils
   ```

2. Configure the contact group and contact information:

   Open the `contacts.cfg` file:
   ```bash
   sudo nano /usr/local/nagios/etc/objects/contacts.cfg
   ```

3. Add the following contact information:
   ```bash
   define contact {
      contact_name            nagiosadmin
      alias                   Nagios Admin
      email                   youremail@email.com
   }

   define contactgroup {
      contactgroup_name       admins
      alias                   Nagios Administrators
      members                 nagiosadmin
   }
   ```

   This configuration defines the recipient for the notification emails.

## Step 5: Test Notifications

To verify that email notifications are functioning correctly, manually trigger an alert by simulating an abnormal condition, such as stopping the MQTT service or setting an unrealistic temperature value. Nagios will detect the condition and send an email to the configured address. 

Check your email inbox to confirm that the alert was received. You should see a message similar to this:

![Email notification](img\email.png)

**Figure 1: Test E-mail**

## Step 6: Restart Nagios

After configuring all necessary files, restart the Nagios service to apply the changes.

```bash
sudo systemctl restart nagios
```

---

This completes the setup of the MQTT temperature monitoring plugin in Nagios. You can now monitor IoT device temperatures and receive alerts when abnormal conditions are detected.




