---
sidebar_position: 5
---

:::info
**Document Creation:** 17 May 2025. **Last Edited:** 23 May 2025. **Authors:** Syed Mahmood Aleem Huzaifa.  
**Effective Date:** 23 May 2025. **Expiry Date:** 23 May 2026.
:::


### Overview 
Building on the successful integration and testing completed in Phase 3, this phase focuses on operationalising the **MISP enrichment pipeline within Wazuh**. The objective here is to fully automate the threat intelligence lookup process so that when an alert is generated on the Wazuh Manager, it is immediately enriched with contextual data from MISP, such as the threat category, attribute type, and IOC value—if a match is found. This enrichment process transforms basic security alerts into actionable intelligence, allowing analysts to better assess the severity and relevance of incidents in real time.


For users who are new and are just completing Phase 3 (i.e., the MISP instance has been deployed, the integration script has been tested using a known IOC such as 1.2.3.4, and successful enrichment was observed in logs), the next steps are about automating this enrichment so that it works without manual intervention. In Phase 3, enrichment was triggered deliberately using a test event. In Phase 4, this mechanism will be triggered by real system events matched by custom rules.

To begin this automation, users must ensure that the Wazuh Manager is configured to recognize and respond to events that warrant enrichment. This involves editing or creating custom detection rules under `/var/ossec/etc/rules/local_rules.xml` or `/var/ossec/etc/rules/custom_rules.xml`. These rules define the event patterns that will invoke the custom-misp script. For example, a rule might be written to detect repeated SSH failures or access attempts from suspicious IPs. Each such rule is assigned a unique rule_id, and it must correspond to one of the IDs defined in the `<integration>` block of the ossec.conf file. In your setup, rule IDs such as 100100, 100102, and 110000 already serve this function.

Once a matching rule is triggered by an event, Wazuh passes the alert to the custom-misp integration script. The script extracts relevant indicators, such as source IP addresses, and sends a search request to the MISP API. If MISP returns a match, the script formats the enrichment data (event ID, threat category, and attribute type) and sends it back to Wazuh using its internal socket mechanism. Wazuh then processes this enriched alert using another set of correlation rules, which assign additional metadata and may elevate the severity level based on the presence of a known threat.

For a new user, the next step after verifying MISP connectivity in Phase 3 is to simulate a real-world event that matches a predefined rule. For instance, the user can simulate an SSH login attempt from a known IOC IP address that has already been added to MISP. This generates a real alert from a Wazuh agent, which triggers the enrichment logic. The user can monitor this in real time using: ```sudo tail -f /var/ossec/logs/alerts/alerts.json```

The alert output will now include a `data.misp` section if a match was found, and may look like:
```
"misp": {
  "event_id": "241",
  "category": "Network activity",
  "type": "ip-dst",
  "value": "8.8.8.8"
}
```
![screenshot of misp alert](img\screenshotofmispalert.png)

Looking at the same screenshot as at the end of phase 3,  which confirmed that the `custom-misp.py` script successfully triggered a lookup and returned a positive response from the MISP threat intelligence platform, we now move into the automated correlation and alert enrichment process that marks the beginning of Phase 4.

At this point, Wazuh has received a structured response from MISP identifying the test IOC—in this case, the IP address 8.8.8.8—as a known indicator associated with a published threat event. The enrichment data returned by MISP includes crucial contextual fields such as the event ID (241), threat category (Network activity), attribute type (ip-dst), and the matching value itself. This data is programmatically appended to the original Wazuh alert and sent back through Wazuh’s internal processing pipeline.

As a result, the enriched alert is no longer simply a record of a local system event; it now contains actionable threat intelligence validated against an external authoritative source. Wazuh evaluates this enriched alert using custom detection rules defined in the local configuration. In this case, rule ID 100622 is specifically written to match alerts that include MISP enrichment fields. When the condition is met, the rule assigns a high severity level to the alert and categorises it under a specific group, such as misp_alert or threat_intel.

This transition marks the start of true automation. From this point onward, the system is capable of continuously monitoring inbound events, automatically correlating them with real-time threat intelligence from MISP, and escalating alerts based on confirmed matches - all without the need for manual review or scripting. This creates a continuous feedback loop in which Wazuh functions not just as a detection engine, but as an intelligence-aware analyst capable of filtering noise and surfacing high-confidence threats. The successful enrichment demonstrated in the previous screenshot confirms that this process is now occurring  automatically. Users can validate this visually by accessing the Wazuh Dashboard and searching for rule IDs such as 100622, or by filtering alerts using tags like misp_alert, threat_intel, or custom_correlated. Selecting any of these alerts reveals a detailed JSON view, where the embedded MISP context, including the event ID, category, type, and value, can be reviewed in full, verifying the seamless integration of external intelligence with local detection.


