**ModSecurity CRS Rule Analysis and Classification Report**

**Document Classification: Internal Use Only – Redback Operations**  
**Distribution: Restricted to Blue Team and Security Team Members**

**1\. Introduction**

Modern web applications are continuously exposed to a wide range of automated and targeted cyber threats, including injection attacks, remote code execution attempts, and reconnaissance scanning. To defend against such threats, organisations deploy Web Application Firewalls (WAFs) that provide real-time inspection and filtering of HTTP traffic. One of the most widely adopted open-source WAF solutions is ModSecurity, which operates by applying predefined and custom security rules to incoming requests.

A key component of ModSecurity is the OWASP Core Rule Set (CRS), a comprehensive collection of generic attack detection rules developed and maintained by the Open Web Application Security Project (OWASP). The CRS is designed to identify and mitigate common web-based attacks such as SQL injection (SQLi), Cross-Site Scripting (XSS), Local File Inclusion (LFI), and Remote Code Execution (RCE), using a rule-based anomaly scoring system. Each rule is assigned a unique identifier (Rule ID) and contributes to an overall anomaly score that determines whether a request should be allowed, logged, or blocked. While the CRS provides strong baseline protection, its generic nature often results in high volumes of alerts, particularly in environments exposed to automated scanning tools and internet-wide reconnaissance activity.

This can lead to log noise, where large numbers of benign or non-actionable alerts obscure meaningful security events. As a result, effective WAF operation requires not only deployment but also continuous analysis, validation, and tuning of CRS rules.

This documentation focuses on the systematic analysis of CRS rule triggers observed within the Redback Operations environment. The primary objective is to map Rule IDs to their corresponding attack categories, understand the behaviour and intent of detected traffic, and distinguish between genuine threats and benign automated activity. Special attention is given to repeated high-frequency alerts associated with /cgi-bin/\* endpoints, which were identified as a significant source of log noise.

Through this analysis, the document aims to:

*   Provide clear visibility into how CRS rules function in a real-world environment
*   Identify dominant attack patterns and their underlying causes
*   Evaluate the effectiveness of the current WAF configuration
*   Support informed decision-making for safe and targeted rule tuning

Ultimately, this work contributes to improving the signal-to-noise ratio in WAF logging, ensuring that security teams can focus on actionable threats while maintaining robust protection against real-world attacks.

**Security Note:**  
This report contains security analysis and findings related to Web Application Firewall (WAF) behaviour. All sensitive information such as real IP addresses, domain names, authentication tokens, or internal infrastructure details must not be committed to the repository. Any such data must be anonymised or redacted before documentation or sharing.

**2\. Environment Overview**

The analysis was conducted within the Redback Operations infrastructure, which is designed to simulate a real-world enterprise environment with multiple interconnected services. The system architecture incorporates a reverse proxy layer, containerised applications, and centralised security monitoring, providing a practical setting for evaluating Web Application Firewall (WAF) behaviour under realistic conditions.

At the core of the web security layer is an Nginx-based reverse proxy integrated with ModSecurity. This proxy is deployed as a container (nginx.modsecurity) and is responsible for handling inbound HTTP/HTTPS traffic, enforcing security rules, and routing requests to backend services. ModSecurity operates in conjunction with the OWASP Core Rule Set, which provides a predefined set of detection rules for identifying malicious or anomalous requests.

The environment is built using Docker, where multiple services including application backends, monitoring tools, and supporting infrastructure are deployed as isolated containers. The reverse proxy serves as the primary entry point, ensuring that all external traffic is inspected before reaching internal services. This architecture enables effective traffic filtering, logging, and enforcement of security policies at a centralised point.

For this analysis, ModSecurity logs were obtained directly from the container using Docker logging mechanisms. These logs capture detailed information about each triggered rule, including Rule IDs, request URIs, client IP addresses, and anomaly scores. To facilitate structured analysis, a custom Python-based log processing pipeline was used to extract, aggregate, and summarise this data into multiple formats, including Markdown reports, CSV files, and JSON datasets.

The scope of the analysis focused on recent log data collected over defined time windows (typically 24 hours), with additional comparisons across multiple days to identify recurring patterns. Key metrics examined include:

*   Total number of WAF alerts (rule hits)
*   Frequency distribution of Rule IDs
*   Unique request URIs and endpoints
*   Client IP activity and concentration
*   Transaction-level behaviour and repetition

The environment also supports auxiliary security tooling, such as Wazuh for vulnerability detection and monitoring, which complements the WAF by providing broader visibility into system-level events. However, this document primarily concentrates on ModSecurity and CRS rule behaviour within the web traffic layer.

Overall, this controlled yet realistic environment enables a comprehensive evaluation of WAF performance, highlighting both its effectiveness in detecting threats and the challenges associated with managing high volumes of log data generated by automated scanning activity.

**3\. Methodology**

A structured and systematic approach was followed to analyse ModSecurity logs, map CRS rule behaviour, and identify sources of log noise within the environment. The methodology combines log extraction, rule mapping, behavioural analysis, and validation techniques to ensure accurate interpretation of security events.

**3.0 Data Handling and Anonymisation**

All log data used in this analysis has been reviewed to ensure that no sensitive or identifiable information is exposed. Where applicable, IP addresses, hostnames, and environment-specific identifiers have been anonymised (e.g., replaced with x.x.x.x or generic placeholders).

This ensures compliance with secure documentation practices while maintaining the integrity of the analysis.

**3.1 Log Collection and Extraction**

ModSecurity alert logs were collected directly from the reverse proxy container using Docker logging commands. The following approach was used:

*   Extract logs from the nginx.modsecurity container
*   Filter relevant entries containing ModSecurity alerts and request details
*   Focus on recent activity using defined time windows (e.g., last 24 hours)

This ensured that the dataset represented current system behaviour while remaining manageable for analysis.

**3.2 Data Processing and Report Generation**

To enable structured analysis, a custom log processing pipeline was utilised. The pipeline performed the following tasks:

*   Parsed raw log entries to extract:
    *   Rule IDs
    *   Request URIs
    *   Client IP addresses
    *   Transaction identifiers
*   Aggregated rule frequency counts
*   Identified top triggering rules and endpoints
*   Generated outputs in:
    *   Markdown reports (for human-readable summaries)
    *   CSV files (for quantitative analysis)
    *   JSON files (for structured data processing)

This step transformed unstructured logs into meaningful datasets that could be systematically analysed.

**3.3 Rule Mapping and Classification**

Each observed Rule ID was mapped to its corresponding rule definition within the OWASP Core Rule Set. This was achieved by:

*   Extracting rule definitions from CRS configuration files inside the container
*   Identifying:
    *   Rule messages (msg)
    *   Tags (tag) indicating attack categories
    *   Associated CRS rule files

Based on this mapping, rules were categorised into attack types such as:

*   Scanner Detection
*   Protocol Enforcement
*   Local File Inclusion (LFI)
*   Remote Code Execution (RCE)
*   Cross-Site Scripting (XSS)
*   SQL Injection (SQLi)
*   Anomaly Scoring / Blocking Evaluation

This classification enabled a deeper understanding of the nature of detected traffic.

**3.4 Behavioural Analysis of Traffic Patterns**

To distinguish between legitimate activity and noise, multiple behavioural indicators were analysed:

*   **Frequency Analysis:**  
    Identification of high-frequency Rule IDs contributing to the majority of alerts
*   **Endpoint Analysis:**  
    Detection of repeatedly accessed URIs, particularly /cgi-bin/\* paths
*   **Client IP Analysis:**  
    Observation that a single or small number of IPs generated a large proportion of alerts
*   **Pattern Consistency:**  
    Verification that the same endpoints and rules appeared consistently across multiple days
*   **Request Characteristics:**  
    Examination of request payloads for known attack signatures (e.g., ../, /etc/passwd, command injection patterns)

These indicators were used to identify automated scanning behaviour and differentiate it from legitimate user activity.

**3.5 Validation of Application Relevance**

To ensure accurate classification of false positives, additional validation steps were performed:

*   Checked Nginx configuration to verify whether /cgi-bin/\* endpoints were routed to any backend service
*   Tested selected endpoints using HTTP requests (e.g., curl)
*   Confirmed that these endpoints consistently returned error responses (e.g., 404 Not Found)
*   Verified absence of /cgi-bin references within application routing configurations

This confirmed that the observed requests were targeting non-existent endpoints and were not part of legitimate application functionality.

**3.6 Multi-Day Log Comparison**

To strengthen the analysis, log data from multiple days was compared to identify recurring patterns. This included:

*   Comparing rule frequency distributions across reports
*   Verifying consistency in triggering endpoints
*   Confirming repeated activity from similar client IP ranges

This step provided strong evidence that the observed behaviour was persistent and automated rather than isolated incidents.

**3.7 Tuning and Validation Approach**

A controlled tuning strategy was applied to reduce log noise while maintaining security coverage. The approach included:

*   Implementing scoped ModSecurity rules targeting specific patterns (e.g., /cgi-bin/\*)
*   Avoiding global rule disabling to prevent weakening protection
*   Applying logging suppression techniques (nolog) rather than removing detection logic
*   Monitoring changes in alert volume after tuning
*   Validating that no legitimate application traffic was affected

The effectiveness of tuning was evaluated by comparing alert metrics before and after implementation.

**3.8 Key Objective of Methodology**

The overall objective of this methodology was to:

*   Accurately interpret WAF alerts
*   Identify dominant sources of log noise
*   Validate whether alerts represent real threats or benign activity
*   Enable safe and targeted optimisation of CRS rules

This structured approach ensures that tuning decisions are evidence-based and do not compromise the security posture of the system.

**4\. CRS Rule Categorization Overview**

The analysis of ModSecurity logs revealed that a diverse set of rules from the OWASP Core Rule Set were triggered during the observation period. These rules span multiple security categories, each designed to detect specific types of web-based attacks or anomalous behaviour.

To provide clarity and structure, the identified Rule IDs were grouped into logical categories based on their associated CRS rule files, tags, and detection purpose. This categorisation enables a clearer understanding of the nature of incoming traffic and helps distinguish between genuine attack attempts and non-actionable noise.

**4.1 Summary of Rule Categories**

| Category | CRS Rule Range / Files | Description |
| --- | --- | --- |
| Scanner Detection | REQUEST-913 | Identifies automated scanning tools based on User-Agent and behaviour |
| Protocol Enforcement | REQUEST-920 | Detects malformed or non-compliant HTTP requests |
| Local File Inclusion (LFI) | REQUEST-930 | Identifies attempts to access sensitive files (e.g., /etc/passwd) |
| Remote Code Execution (RCE) | REQUEST-932 | Detects command injection and execution attempts |
| PHP Injection | REQUEST-933 | Identifies PHP-specific injection patterns |
| Cross-Site Scripting (XSS) | REQUEST-941 | Detects malicious scripts injected into requests |
| SQL Injection (SQLi) | REQUEST-944 | Identifies database query manipulation attempts |
| Blocking Evaluation | REQUEST-949 | Calculates anomaly score and determines whether to block requests |

**4.2 Interpretation of Categories in Context**

**Scanner Detection (REQUEST-913)  
**Rules in this category identify known scanning tools through patterns such as User-Agent strings. In the observed logs, these rules were frequently triggered by requests associated with automated tools, indicating widespread reconnaissance activity targeting the system.

**Protocol Enforcement (REQUEST-920)**

These rules enforce compliance with HTTP standards by detecting malformed or suspicious requests. High activity in this category typically indicates automated tools sending irregular or incomplete requests, rather than legitimate user traffic.

**Local File Inclusion – LFI (REQUEST-930)**

LFI rules detect attempts to access sensitive files through path traversal techniques (e.g., ../../etc/passwd). The presence of these rules in the logs confirms that attackers or scanners are attempting to exploit file access vulnerabilities.

**Remote Code Execution – RCE (REQUEST-932)**

RCE rules identify attempts to execute system-level commands via web inputs. These are considered high-risk attack patterns and are commonly used in exploitation attempts against vulnerable applications.

**PHP Injection (REQUEST-933)**

These rules detect malicious PHP payloads embedded in requests. Their presence indicates attempts to manipulate backend application logic or execute unintended code.

**Cross-Site Scripting – XSS (REQUEST-941)**

XSS rules identify injection of JavaScript or HTML into web inputs. These attacks aim to compromise client-side execution and are critical to detect in web-facing applications.

**SQL Injection – SQLi (REQUEST-944)**

SQLi rules detect attempts to manipulate database queries. These are among the most critical web vulnerabilities and require strict enforcement without relaxation.

**Blocking Evaluation (REQUEST-949)**

This category plays a central role in ModSecurity’s anomaly scoring system. Rather than detecting a specific attack, these rules evaluate the cumulative score of triggered rules and determine whether a request should be blocked. High frequency of Rule 949110 indicates that multiple suspicious behaviours are being detected within individual requests.

**4.3 Key Observations from Categorization**

From the categorised analysis, several important insights were identified:

*   A significant portion of alerts originated from **scanner detection and protocol enforcement rules**, indicating a high volume of automated scanning activity
*   Critical attack categories such as **LFI, RCE, SQLi, and XSS** were also triggered, confirming the presence of real attack attempts
*   The frequent triggering of **blocking evaluation rules (949110)** suggests that many requests accumulate high anomaly scores, reinforcing the effectiveness of the WAF
*   The majority of these alerts were associated with **non-existent endpoints**, particularly /cgi-bin/\*, indicating that attackers were probing for common vulnerabilities rather than targeting specific application functionality

**4.4 Importance of Categorization**

This categorisation serves as a foundation for:

*   Understanding the **threat landscape** affecting the system
*   Differentiating between benign automated activity (scanner traffic) and actionable threats
*   Supporting **safe and targeted tuning decisions**
*   Ensuring that critical detection capabilities remain intact while reducing unnecessary log volume

**5\. Detailed CRS Rule Analysis**

This section provides a detailed analysis of the most frequently triggered CRS rules observed in the ModSecurity logs. Each rule is examined in terms of its purpose, behaviour in the environment, and security implications. The analysis also distinguishes between genuine attack attempts and benign automated activity generated by scanning tools.

**5.1 Rule 913100 – Scanner Detection**

*   **Rule File:** REQUEST-913-SCANNER-DETECTION.conf
*   **Category:** Scanner Detection / Reconnaissance
*   **Description:** Detects known scanning tools based on User-Agent patterns

**Observed Behaviour:**

*   Triggered on requests targeting /cgi-bin/\* and other random endpoints
*   Logs indicate User-Agent values associated with known security scanning tools (e.g., Nessus)

**Security Interpretation:**

*   Represents automated reconnaissance activity
*   No direct exploitation behaviour observed

**Risk Level:** Low

**Classification:** Benign / Non-actionable Alert

**Action Recommendation:**

*   Can be safely tuned for specific endpoints (e.g., /cgi-bin/\*)
*   Should not be globally disabled

**5.2 Rule 920270 / 920420 / 920440 / 920600 – Protocol Enforcement**

*   **Rule File:** REQUEST-920-PROTOCOL-ENFORCEMENT.conf
*   **Category:** Protocol Validation
*   **Description:** Detects malformed or non-compliant HTTP requests

**Observed Behaviour:**

*   Triggered by irregular or incomplete requests
*   Often associated with automated scanning tools

**Security Interpretation:**

*   Indicates non-standard traffic patterns
*   Common in bot-generated traffic

**Risk Level:** Low

**Classification:** Benign Automated Activity

**Action Recommendation:**

*   Monitor but do not prioritise
*   Can be selectively tuned if contributing to excessive alert volume

**5.3 Rule 930100 / 930110 / 930120 – Local File Inclusion (LFI)**

*   **Rule File:** REQUEST-930-APPLICATION-ATTACK-LFI.conf
*   **Category:** Local File Inclusion / Path Traversal
*   **Description:** Detects attempts to access sensitive files using traversal patterns such as ../

**Observed Behaviour:**

*   Requests containing paths like /etc/passwd, ../../
*   Often targeting /cgi-bin/\* endpoints

**Security Interpretation:**

*   Represents real exploitation attempts
*   Likely automated but still malicious

**Risk Level:** High

**Classification:** True Positive (Attack Attempt)

**Action Recommendation:**

*   Must remain enabled
*   Critical for protecting sensitive file access

**5.4 Rule 932130 / 932160 / 932170 – Remote Code Execution (RCE)**

*   **Rule File:** REQUEST-932-APPLICATION-ATTACK-RCE.conf
*   **Category:** Remote Command Execution
*   **Description:** Detects command injection patterns and attempts to execute system commands

**Observed Behaviour:**

*   Triggered on suspicious input patterns within requests
*   Often combined with other attack signatures

**Security Interpretation:**

*   Indicates attempts to execute arbitrary commands on the server
*   High-risk attack category

**Risk Level:** Critical

**Classification:** True Positive (Attack Attempt)

**Action Recommendation:**

*   Must remain fully enabled
*   Should not be tuned or relaxed

**5.5 Rule 933135 – PHP Injection**

*   **Rule File:** REQUEST-933-APPLICATION-ATTACK-PHP.conf
*   **Category:** PHP Injection
*   **Description:** Detects malicious PHP code patterns in requests

**Observed Behaviour:**

*   Triggered in conjunction with /cgi-bin/\* probing

**Security Interpretation:**

*   Indicates attempts to exploit PHP-based vulnerabilities

**Risk Level:** High

**Classification:** True Positive (Attack Attempt)

**Action Recommendation:**

*   Keep enabled
*   Monitor for correlation with other attack patterns

**5.6 Rule 941100 / 941110 / 941160 / 941390 – Cross-Site Scripting (XSS)**

*   **Rule File:** REQUEST-941-APPLICATION-ATTACK-XSS.conf
*   **Category:** Cross-Site Scripting (XSS)
*   **Description:** Detects injection of JavaScript or HTML into request parameters

**Observed Behaviour:**

*   Triggered by suspicious payloads containing script-like patterns

**Security Interpretation:**

*   Represents attempts to inject client-side scripts

**Risk Level:** High

**Classification:** True Positive (Attack Attempt)

**Action Recommendation:**

*   Must remain enabled
*   Essential for protecting web users

**5.7 Rule 944100 / 944110 / 944130 / 944150 – SQL Injection (SQLi)**

*   **Rule File:** REQUEST-944-APPLICATION-ATTACK-SQLI.conf
*   **Category:** SQL Injection
*   **Description:** Detects database query manipulation attempts

**Observed Behaviour:**

*   Triggered by suspicious query patterns and payloads

**Security Interpretation:**

*   Indicates attempts to access or manipulate backend databases

**Risk Level:** Critical

**Classification:** True Positive (Attack Attempt)

**Action Recommendation:**

*   Must remain fully enforced
*   No tuning recommended

**5.8 Rule 949110 – Blocking Evaluation (Anomaly Score)**

*   **Rule File:** REQUEST-949-BLOCKING-EVALUATION.conf
*   **Category:** Anomaly Scoring
*   **Description:** Evaluates cumulative anomaly score and determines blocking behaviour

**Observed Behaviour:**

*   Most frequently triggered rule in logs
*   Activated when multiple suspicious patterns are detected

**Security Interpretation:**

*   Confirms that requests exhibit multiple attack characteristics
*   Indicates effective detection by the WAF

**Risk Level:** Critical (Control Rule)

**Classification:** System Behaviour (Not a False Positive)

**Action Recommendation:**

*   Must not be disabled
*   Essential for WAF decision-making

**5.9 Key Findings from Rule Analysis**

*   Majority of high-frequency alerts are associated with:
    *   /cgi-bin/\* endpoints
    *   Automated scanning behaviour
*   Critical attack rules (LFI, RCE, SQLi, XSS) are actively detecting real threats
*   Scanner detection and protocol enforcement rules contribute significantly to alert volume but largely represent benign automated activity
*   Blocking evaluation rule (949110) confirms that multiple attack indicators are present within single requests

**5.10 Summary of Rule Classification**

| Type | Rules | Action |
| --- | --- | --- |
| Benign Automated Activity | 913100, 920xxx | Tune selectively |
| Real Attack Detection | 930xxx, 932xxx, 933xxx, 941xxx, 944xxx | Keep enabled |
| Core WAF Logic | 949110 | Do not modify |

**6\. Security Impact Assessment**

The analysis of ModSecurity logs and associated CRS rule triggers provides valuable insight into the security posture of the web application environment. By examining the nature and frequency of triggered rules, it is possible to assess both the types of threats targeting the system and the effectiveness of existing defensive controls.

**6.1 Threat Landscape Overview**

The observed rule triggers indicate that the system is exposed to a wide range of common web-based attack techniques. These include:

*   **Reconnaissance and scanning activity**  
    Identified through scanner detection rules, indicating automated tools probing the system for vulnerabilities
*   **Local File Inclusion (LFI) attempts**  
    Evidenced by path traversal patterns such as ../ and attempts to access sensitive system files
*   **Remote Code Execution (RCE) attempts**  
    Detected through command injection patterns aimed at executing arbitrary code on the server
*   **Cross-Site Scripting (XSS) payloads**  
    Indicating attempts to inject malicious scripts into application inputs
*   **SQL Injection (SQLi) patterns**  
    Suggesting attempts to manipulate backend database queries

These attack categories represent some of the most critical and commonly exploited vulnerabilities in web applications.

**6.2 Effectiveness of CRS Detection**

The presence of multiple triggered rules across different categories demonstrates that the OWASP Core Rule Set is effectively identifying a broad spectrum of attack patterns. Key observations include:

*   **Multi-layered detection:**  
    Individual requests often trigger multiple rules across different categories, contributing to higher anomaly scores
*   **Accurate classification:**  
    Rule messages and tags correctly identify the nature of the detected attack (e.g., LFI, RCE, SQLi)
*   **Anomaly scoring effectiveness:**  
    The frequent activation of Rule 949110 confirms that the cumulative scoring mechanism is functioning as intended
*   **Coverage of common attack vectors:**  
    The CRS provides comprehensive protection against widely known web vulnerabilities

These findings indicate that the WAF is performing its primary function of detecting potentially malicious requests with a high degree of reliability.

**6.3 Risk Evaluation**

Based on the observed rule triggers, the following risk levels can be assigned:

*   **High to Critical Risk:**
    *   Remote Code Execution (RCE)
    *   SQL Injection (SQLi)
    *   Local File Inclusion (LFI)  
        These attacks have the potential to compromise system integrity, access sensitive data, or gain unauthorised control over the application
*   **Medium Risk:**
    *   Cross-Site Scripting (XSS)  
        These attacks primarily affect client-side security but can lead to session hijacking or data theft
*   **Low Risk:**
    *   Scanner detection and protocol violations  
        These represent reconnaissance activity and malformed traffic rather than direct exploitation

**6.4 System Security Posture**

From the analysis, the overall security posture of the system can be summarised as follows:

*   The application is actively being targeted by automated tools attempting common exploitation techniques
*   There is **no evidence of successful exploitation**, as requests are intercepted and identified by the WAF
*   The WAF, powered by ModSecurity and CRS, is effectively detecting and evaluating malicious traffic
*   Critical attack detection rules are functioning correctly and contributing to anomaly scoring and potential blocking decisions

**6.5 Key Insights**

*   The system is exposed to **continuous background noise from internet-wide scanning activity**, which is typical for publicly accessible web services
*   The CRS rules provide **broad and effective coverage** of known attack vectors
*   The anomaly-based detection model ensures that even complex or multi-stage attacks are identified
*   The presence of repeated attack attempts highlights the importance of maintaining an active and well-configured WAF

**6.6 Summary**

The security impact assessment confirms that the current WAF configuration is successfully detecting a wide range of web-based threats without evidence of compromise. The combination of comprehensive rule coverage and anomaly scoring ensures that potentially malicious requests are identified and evaluated effectively.

This demonstrates that the deployed security controls are robust and capable of defending against common attack techniques, providing a strong foundation for maintaining application security.

**7\. Recommendations**

Based on the analysis of CRS rule behaviour and observed security events, the following recommendations are proposed to maintain and enhance the effectiveness of the Web Application Firewall (WAF) deployment.

**7.1 Maintain Critical Detection Rules**

Rules associated with high-risk attack categories must remain fully enabled without modification. These include:

*   Local File Inclusion (LFI) – REQUEST-930
*   Remote Code Execution (RCE) – REQUEST-932
*   Cross-Site Scripting (XSS) – REQUEST-941
*   SQL Injection (SQLi) – REQUEST-944

These rules are essential for detecting and preventing exploitation attempts that could compromise system integrity or data confidentiality.

**7.2 Preserve Anomaly Scoring Mechanism**

The anomaly scoring system, particularly Rule 949110, plays a critical role in evaluating cumulative threat levels within requests. It is recommended that:

*   The anomaly scoring logic remains unchanged
*   Blocking thresholds are carefully maintained
*   No direct modifications are made to core evaluation rules

This ensures consistent and reliable decision-making within the WAF.

**7.3 Monitor Scanner and Protocol-Based Rules**

Rules related to scanner detection (REQUEST-913) and protocol enforcement (REQUEST-920) should be continuously monitored, as they provide visibility into reconnaissance activity and abnormal traffic patterns.

While these rules may contribute to higher alert volumes, they are valuable for:

*   Identifying scanning trends
*   Understanding exposure to automated tools
*   Supporting threat intelligence analysis

**7.4 Implement Controlled and Scoped Tuning**

Where necessary, tuning should be applied in a controlled and targeted manner. Any optimisation must:

*   Be limited to clearly validated non-critical patterns
*   Avoid disabling entire rule categories
*   Preserve detection capability for genuine threats
*   Be tested and validated before deployment

This approach ensures that noise reduction does not weaken the overall security posture.

**7.5 Continuous Monitoring and Review**

WAF effectiveness depends on ongoing monitoring and periodic review. It is recommended to:

*   Regularly analyse ModSecurity logs
*   Track changes in rule frequency and attack patterns
*   Reassess tuning decisions over time
*   Update rule configurations as the application evolves

**7.6 Documentation and Knowledge Sharing**

Maintaining clear documentation of CRS rule behaviour and tuning decisions is essential for operational continuity. This includes:

*   Mapping Rule IDs to attack categories
*   Recording tuning actions and justifications
*   Sharing insights across the security team

This ensures that future team members can understand and maintain the WAF configuration effectively. Ensure all future documentation adheres to internal classification policies and secure data handling standards.

**7.7 Security Handling Considerations**

This document is intended strictly for internal use within the Redback Operations environment. Care must be taken when sharing, exporting, or publishing this report outside the organisation.

All examples included in this document are either simulated or sanitised to prevent exposure of real infrastructure details. Under no circumstances should sensitive operational data such as production IP addresses, internal hostnames, authentication credentials, or API tokens be included in version-controlled repositories.

Future updates to this document must adhere to the same secure documentation and data handling practices.

**7.8 Summary**

The current WAF configuration demonstrates strong detection capabilities across multiple attack categories. By maintaining critical rules, applying controlled tuning, and continuing regular analysis, the system can achieve an optimal balance between **security effectiveness and operational efficiency**.

**8\. Conclusion**

This documentation presented a structured analysis of CRS rule behaviour within a ModSecurity-based Web Application Firewall deployed in the Redback Operations environment. By systematically mapping Rule IDs to their respective categories within the OWASP Core Rule Set, the study provided clear insight into how different types of web-based attacks are detected and evaluated. The analysis demonstrated that the WAF, powered by ModSecurity, is effectively identifying a wide range of attack patterns, including Local File Inclusion, Remote Code Execution, Cross-Site Scripting, and SQL Injection. The anomaly scoring mechanism further reinforces this detection by aggregating multiple rule triggers to assess the overall threat level of each request.

Importantly, the findings highlight that while a significant volume of alerts is generated, the underlying detection mechanisms are functioning correctly and provide comprehensive coverage against common web vulnerabilities. The categorisation of rules and interpretation of their behaviour enables a deeper understanding of the threat landscape and supports informed decision-making in WAF management.

Overall, this work establishes a strong foundation for maintaining an effective and resilient web security posture. By combining accurate rule analysis, continuous monitoring, and structured documentation, the organisation can ensure that its WAF remains both robust against real-world attacks and adaptable to evolving security requirements.