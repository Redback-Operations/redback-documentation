---
sidebar_position: 4
---

**Last updated by:** T_Apperley, **Last updated on:** 03/12/2024


**Last updated by:** T_Apperley, **Last updated on:** 03/12/2024


**Last updated by:** T_Apperley, **Last updated on:** 03/12/2024


# Monitoring & Log Analytics  

## Objective Summary
To develop an easy way to implement a cost-effective deployment plan for our Monitoring & Log Analytics policies and procedures.  

## Key Subjects  

### 1. Research tools that can be used to collect and analyse log data:
- **Splunk**:Redback currently uses Wazuh, which is a useful tool, however I believe Splunk should be added as well. Both have great log management and security monitoring, however they are driven by different approaches, with different sets of features. Wazuh is an open-source platform that provides centralised security event monitoring, threat detection, and compliance management. On the other hand, Splunk is a much broader platform that provides for advanced log analytics, machine learning-based threat detection, and powerful visualisation. Splunk also supports integrations with a wide range of third-party services and have their own tool (Machine Learning Toolkit-MLTK) which enables organisations to run machine learning models on their data for predictions and irregularity detection. This would be useful for Redback operations as they can use AI to help predict possible security threats.  
- **Mezmo**: This tool also allows you to monitor and analyse log files in real-time. It is accessible in the cloud and enables you to look up, save, and keep data from any application or system, such as Windows, Linux, AWS, and Python. Mezmo could fit in with Wazuh by providing a strong log management and visualisation layer on top of Wazuh’s security monitoring and SIEM capabilities, resulting in a more comprehensive and efficient security solution


### 2. Redefine key assets and data categories  
**Key Assets**
- Fitness gadgets: heart rate monitors, wearable devices  
- Platforms for gamified exercise: software that includes game components.  
- Health Monitoring Systems: Tools and applications that monitor the safety of exercise.  

**Data Categories**
- **User Data**: Health measurements and personal data.  
- **Activity logs**: Performance metrics comprise exercise data.  
- **Engagement Information**: User interactions and gamification analytics.  
- **Safety Information**: Health Alerts, Injury Reports.  

### 3. Redefine Roles and Responsibilities  
- **Security experts**: Safeguard user information and guarantee the safety of the infrastructure and fitness applications.  
- **Compliance**: Ensures that internal log management rules and legal requirements are followed.  
- **Log Administrator**: Oversees the policies for log retention, storage, and collection.  

### 4. Ensure all digital assets are covered in deployment – explain how they will be covered  
- **Automated Monitoring**: To quickly identify errors and problems, implement automated monitoring systems that continuously track and send alerts based on log data from all assets.  
- **Frequent Audits**: Update configurations whenever new assets are added and conduct routine audits to ensure that all assets are being properly monitored and logged.  

### 5. Cost Effectiveness:
- One user can utilize 500 MB of Splunk each day for free. Splunk also has two paid options for more sophisticated features, with pricing available upon request. Mezmo provides a 14-day free trial in addition to several paid choices and a free version, allowing the user to test the tools before fully committing.  

### 6. Ease of Implementation:  
- **Splunk**  
  - **Training**: Documentation and training materials are available to facilitate learning.  
  - **User Interface**: Offers a strong, configurable multi-line interface.  

- **Mezmo**  
  - **Quick Installation**: Quick to set up and accessible via web interface.  
  - **User Interface**: User-friendly interface designed for real-time monitoring and log analysis.  

### 7. Adherence to Regulatory Requirements:  
- **Mezmo**   
  - **Real-Time Monitoring**: Assists in fulfilling regulatory requirements for logging and monitoring across multiple systems and applications by providing real-time insights and alerts.  

- **Splunk**  
  - **SOC2, FedRamp, and ISO 27001 Compliance**: Uses strict security standards and procedures to guarantee safe data handling and protection.  
  - **EEOC Compliance**: Complies with regulations to ensure ethical and fair employment standards and discrimination-free hiring procedures.  
  - **Sector-Specific Requirements**: Respects laws like GDPR and PCI-DSS to control risks, stay compliant with the law, and maintain customer trust.  

## References  
- Leanne Mitton, L.M. (2023). Regulatory Compliance 101: What You Need To Know. Splunk Blogs. [Splunk Blog](https://www.splunk.com/en_us/blog/learn/regulatory-compliance.html)  
- Mezmo. (2024). MONITORING AND LOGGING REQUIREMENTS FOR COMPLIANCE. Regulatory Compliance. [Mezmo](https://www.mezmo.com/learn-observability/monitoring-and-logging-requirements-for-compliance)  
- Rafal Kuc, R.K. (2023). 15 Best Log Analysis Tools & Log Analyzers of 2024 (Paid, Free & Open Source). Sematext. [Sematext Blog](https://sematext.com/blog/log-analysis-tools/)
