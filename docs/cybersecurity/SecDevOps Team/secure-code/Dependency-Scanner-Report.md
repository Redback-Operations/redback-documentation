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

## Vulnerability Summary

The full report and vulnerability spreadsheet can be found in the Redback Sharepoint:

[Report](https://deakin365.sharepoint.com/:x:/r/sites/RedbackOperations9/Shared%20Documents/Cyber%20Security%20Team/2025%20Trimester%201/Cybersecurity%20Team/SecDevOps/Trivy-Report.pdf)

[Spreadsheet](https://deakin365.sharepoint.com/:x:/r/sites/RedbackOperations9/Shared%20Documents/Cyber%20Security%20Team/2025%20Trimester%201/Cybersecurity%20Team/SecDevOps/Trivy-Report.xlsx)

The following is a summary of identified vulnerabilities across the Redback project repositories:

| Repository                               | Total Vulnerabilies | Critical| High | Medium | Low |
|------------------------------------------|---------------------|---------|------|--------|-----|
| redback-data-warehouse                   | 15                  |    .    |   2  |   11   |  2  |
| redback-ui                               | 16                  |    .    |   6  |   6    |  4  |
| redback-smartbike-mobile                 | 1                   |    .    |   .  |   1    |  .  |
| redback-smartbike-web                    | 6                   |    .    |   2  |   4    |  .  |
| redback-smartbike-iot                    | 65                  |    5    |  29  |   22   |  9  |
| redback-senior-tech                      | 7                   |    1    |   4  |   2    |  .  |
| redback-senior-web                       | 6                   |    .    |   2  |   4    |  .  |
| redback-orion                            | 80                  |    8    |  36  |   33   |  3  |
| redback-orion-web                        | 6                   |    .    |   2  |   4    |  .  |
| redback-fit-sports-performance           | 31                  |    1    |  11  |   15   |  4  |
| redback-fit-web                          | 4                   |    .    |   2  |   2    |  .  |

## Next Steps

- It is recommended that during **T2 of 2025**, the Trivy dependency scanner be added to all Redback project repositories to support continuous vulnerability monitoring.
- Consider configuring the scanner to block pull requests if **critical or high severity vulnerabilities** are detected.
- Future reviews should incorporate both dependency and container scanning.
- Project teams should be supported with remediation guidance and patching strategies.
