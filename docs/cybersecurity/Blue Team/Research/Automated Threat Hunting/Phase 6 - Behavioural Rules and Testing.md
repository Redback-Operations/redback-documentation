---
sidebar_position: 7
---

:::info
**Document Creation:** 17 May 2025. **Last Edited:** 23 May 2025. **Authors:** Syed Mahmood Aleem Huzaifa.  
**Effective Date:** 23 May 2025. **Expiry Date:** 23 May 2026.
:::

### Overview 

Phase 6 introduces behavioural threat detection by leveraging custom Wazuh rules to identify suspicious activity based on system behaviour rather than static indicators. This phase covers the creation and testing of rules for detecting SSH brute-force attempts, suspicious PowerShell executions, and communication with known malicious IPs using Suricata and MISP integration. It also implements correlation logic that links behavioural events with threat intelligence to highlight high-confidence threats. Additionally, it introduces a MISP IOC hunting script for proactive threat detection and outlines techniques to suppress known benign noise to maintain alert quality and reduce false positives.

We now move into behavioural threat detection. Unlike static IOC matching, behavioural rules help us detect patterns of potentially malicious actions based on system activity. In this phase, we define custom Wazuh rules that monitor for suspicious behavior such as brute-force attempts, abnormal PowerShell execution, and network contact with known malicious IPs.

### Step 1: Detect SSH Brute-force Attempts

To detect brute-force SSH logins, begin by defining a custom rule that identifies repeated authentication failures. You can model this after the following rule from our setup:
```
<rule id="100101" level="10">
  <if_sid>5760</if_sid> <!-- SSHD: Too Many Wrong Passwords Entered -->
  <description>SSH Brute Force Attempt Detected (Custom Correlation)</description>
  <group>ssh,authentication_failed,custom</group>
</rule>
```

This rule should be placed inside your local_rules.xml file under a suitable group section such as local,syslog,sshd. The if_sid 5760 refers to a parent rule that already matches "Too many authentication failures" from /var/log/auth.log.

Once added, restart the Wazuh manager: ```sudo systemctl restart wazuh-manager```

### Step 2: Test the SSH Brute-force Rule

To simulate a brute-force attack, run the following command on the system monitored by Wazuh:
```for i in {1..7}; do ssh wronguser@localhost; done```

This creates failed SSH login attempts that Wazuh will log. You should observe a high-severity alert triggered by Rule ID 100101 in your Wazuh Dashboard or alerts.json.

### Step 3: Suspicious PowerShell Execution Detection

While our current configuration does not include PowerShell-specific detection, users can add the following rule to detect suspicious PowerShell commands like Invoke-Expression or Invoke-WebRequest:
```
<rule id="100200" level="12">
  <if_sid>18107</if_sid>
  <match>Invoke-Expression|Invoke-WebRequest</match>
  <description>Suspicious PowerShell execution detected</description>
  <group>windows,powershell,malicious_script</group>
</rule>
```

This goes under a new group or inside local_rules.xml, depending on your structure. Once configured, execute a known-bad PowerShell command on the Windows agent and verify alert generation.

### Step 4: Detect Malicious IP Communication via Suricata + MISP

To detect communication with known-malicious IPs, ensure that Suricata is configured on your monitored system and that Wazuh is parsing Suricata alerts. Then, implement a rule like this to trigger MISP enrichment for a known IP:
```
<rule id="110000" level="10">
  <if_sid>5716</if_sid>
  <srcip>8.8.8.8</srcip>
  <description>Trigger MISP Enrichment - SSH attempt from 8.8.8.8</description>
  <group>misp_integration</group>
</rule>
```
To test this, simulate a connection attempt from the malicious IP. You can fake a log entry like:
`echo "Failed password for invalid user misptest from 8.8.8.8" | sudo tee -a /var/log/auth.log`

This will activate the rule and trigger enrichment via the MISP .

Now that behavioural rules and enrichment are functioning, we define automatic correlation logic and proactive IOC hunting. These features enable Wazuh to reason about threats by linking separate events.

### Step 5: Correlate Behaviour and Threat Intel

We define a high-severity correlation rule that detects when a failed login (a behaviour) and a threat intel match (from MISP) share the same IP. Use this rule from our configuration:
```
<rule id="110005" level="15">
  <if_sid>100100</if_sid> <!-- SSH Failed Login -->
  <field name="data.srcip">8.8.8.8</field> <!-- IOC IP from MISP -->
  <description>SSH failed login from known IOC (MISP hit)</description>
  <group>bruteforce,threat_intel,custom_correlated</group>
</rule>
```

Before this works, ensure you have the base detection rule:
```
<rule id="100100" level="7">
  <if_sid>5710</if_sid>
  <description>Detected an SSH failed login attempt</description>
</rule>
```

This creates a chain: Rule 100100 fires for login failures, and 110005 correlates that event with the known malicious IP (provided by MISP). Replace the IP 8.8.8.8 with one from your actual MISP indicators.

Local rules would contains a structured collection of custom Wazuh rules tailored to enhance the detection, correlation, and enrichment capabilities of the threat monitoring setup used in this project. The rules are organized into logical groups, each serving a specific detection purpose.

The local,syslog,sshd group defines rules that identify SSH login failures, brute-force attacks, and test patterns. These rules are crucial for detecting suspicious authentication behavior on monitored systems. The misp group includes rules that process and respond to events generated from MISP threat intelligence, such as matching IoCs, API errors, and debug events. These ensure that threat intelligence enrichment is actively monitored and operational. The custom-misp group implements advanced correlation logic by combining behavioral detections, like failed SSH logins, with confirmed threat data from MISP. It also includes rules that simulate or respond to test cases used during validation.

Together, these rules significantly strengthen the project’s objective of building an automated threat detection and response pipeline. They allow Wazuh to go beyond basic log parsing by linking real-time system activity with external threat intelligence sources. This enables the detection engine to generate high-confidence alerts, reduce false positives, and deliver actionable insights, ultimately improving the responsiveness and accuracy of the security operations environment.

### Step 6: Configure a MISP IOC Hunting Script

To automate daily threat hunting, create a script that queries MISP:

```
#!/bin/bash
curl -X GET -H "Authorization: <API_KEY>" https://<misp_ip>/attributes/restSearch
```

Replace `<API_KEY>` with your MISP user’s API key, and `<misp_ip>` with the address of your MISP instance. Place this script in /usr/local/bin/ioc_hunt.sh and make it executable:
```chmod +x /usr/local/bin/ioc_hunt.sh```

You can now run this script manually whenever you want to perform an on-demand threat intelligence sweep from MISP. This enables you to fetch current indicators without depending solely on real-time alert triggers. The output can be parsed, logged, or integrated with local detection rules based on your workflow.

### Step 7 - Suppress Known Benign Noise

To avoid alert fatigue and false positives, Wazuh allows you to suppress alerts from known, trusted sources. This is especially useful in lab or internal environments where systems like monitoring agents, load balancers, or patch managers may repeatedly trigger low-priority events.

For instance, if a trusted internal IP such as 192.168.0.1 frequently generates SSH login attempts for monitoring purposes, you can suppress those by adding the following directive inside your custom rule block:
```
<ignore>192.168.0.1</ignore>
This tells Wazuh to completely ignore alerts from that IP. Alternatively, you can tune the detection rule itself by increasing the frequency or reducing the level, like so:
<rule id="100101" level="5">
  <if_sid>5760</if_sid>
  <description>SSH brute force attempt with lower severity</description>
  <frequency>10</frequency>
  <timeframe>60</timeframe>
</rule>
```

This configuration raises the threshold for triggering the rule and lowers its alert level, helping filter out non-malicious but repetitive behavior. These techniques are essential in real-world deployments to reduce noise, focus analyst attention, and maintain a high signal-to-noise ratio in the SIEM.

With noise suppression and enrichment functioning, your Wazuh-based threat detection pipeline becomes significantly more efficient, contextual, and actionable.


