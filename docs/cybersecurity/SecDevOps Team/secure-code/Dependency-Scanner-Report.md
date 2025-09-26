---
sidebar_position: 4
---

# Trivy Dependency Scan Results

:::info
**Document Creation:** 14 May, 2025. **Last Edited:** 14 May, 2025. **Authors:** Richard Whellum. 
<br></br> **Document Code:** TRV2. **Effective Date:** 14 May, 2025. **Expiry Date:** 14 May, 2026.
:::

## Background

The Trivy dependency scanner was deployed to the Data Warehouse repository in T3 of 2024 to test its functionality. At the time of writing, this is the only repository with the automated scanner. 

In T1 of 2025, the scanner was run on forks of the Redback project repositories to determine the current state of vulnerabilities without affecting the work being performed by the project teams.

## Vulnerability Report

The full report and vulnerability spreadsheet can be found in the Redback Sharepoint:

[Report](https://deakin365.sharepoint.com/sites/RedbackOperations9/Shared%20Documents/Cyber%20Security%20Team/2025%20Trimester%201/Cybersecurity%20Team/SecDevOps/Trivy-Report.pdf)

[Spreadsheet](https://deakin365.sharepoint.com/:x:/r/sites/RedbackOperations9/Shared%20Documents/Cyber%20Security%20Team/2025%20Trimester%201/Cybersecurity%20Team/SecDevOps/Trivy-Report.xlsx)

## Next Steps

- It is recommended that during **T2 of 2025**, the Trivy dependency scanner be added to all Redback project repositories to support continuous vulnerability monitoring.
- Consider configuring the scanner to block pull requests if **critical or high severity vulnerabilities** are detected.
- Future reviews should incorporate both dependency and container scanning.
- Project teams should be supported with remediation guidance and patching strategies.

