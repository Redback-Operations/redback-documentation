---
sidebar_position: 4
---

# Trivy Dependency Scan Results

:::info
**Document Creation:** 14 May, 2025. **Author:** Richard Whellum.  
**Effective Date:** 14 May 2025. **Expiry Date:** 14 May 2026.
:::

## Background

The Trivy dependency scanner was deployed to the Data Warehouse repository in T3 of 2024 to test its functionality. This is currently the only repository with this automated scanner. 

In T1 of 2025, the scanner was run on forks of the Redback project repositories to determine the current state of vulnerabilities without affecting the work being performed by the project teams.

## Vulnerability Summary

The full list of vulnerabilities can be found [here](https://deakin365.sharepoint.com/:x:/r/sites/RedbackOperations9/Shared%20Documents/Cyber%20Security%20Team/2025%20Trimester%201/Cybersecurity%20Team/SecDevOps/Trivy-Report.xlsx)

The following is a summary of identified vulnerabilities across the Redback project repositories:

| Repository                               | Vulnerability Count |
|------------------------------------------|----------------------|
| redback-data-warehouse                   | 15                   |
| redback-ui                               | 16                   |
| redback-smartbike-mobile                 | 1                    |
| redback-smartbike-web                    | 6                    |
| redback-smartbike-iot                    | 65                   |
| redback-senior-tech                      | 7                    |
| redback-senior-web                       | 6                    |
| redback-orion                            | 80                   |
| redback-orion-web                        | 6                    |
| redback-fit-sports-performance           | 31                   |
| redback-fit-web                          | 4                    |

## Next Steps

- It is recommended that during **T2 of 2025**, the Trivy dependency scanner be added to all Redback project repositories to support continuous vulnerability monitoring.
- Consider configuring the scanner to block pull requests if **critical or high severity vulnerabilities** are detected.
- Future reviews should incorporate both dependency and container scanning.
- Project teams should be supported with remediation guidance and patching strategies.
