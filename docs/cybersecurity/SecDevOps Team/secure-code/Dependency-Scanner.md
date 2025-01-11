---
sidebar_position: 3
---

# Trivy Dependency Scan

:::info

**Document Creation:** 8 January, 2025. **Author:** Richard Whellum.
<br></br> **Effective Date:** 13 January 2025. **Expiry Date:** 13 January 2026.
:::

## Overview

This GitHub Actions workflow automates the scanning of vulnerabilities in dependencies and files within a pull request (PR). The workflow uses Trivy, a vulnerability scanner, to scan both the entire repository and only the changed files in a PR. It then uses Reviewdog to post comments on the PR with the scan results, highlighting any vulnerabilities found.

The process consists of two jobs:

1. **Trivy Repo Scan & Upload to Security Tab**: Checks the entire repository for vulnerable dependencies, ensuring that any new issues are identified and added to the Security section of the repository settings.

2. **Trivy PR Check**: Scans only the files changed in the PR for vulnerabilities, using Reviewdog to post PR comments if high or critical vulnerabilities are detected.

## Workflow Trigger

The workflow is triggered on two events:

- **Push to main branch**: The workflow will run when changes are pushed to the main branch.

- **Pull Request (PR)**: The workflow will run when a pull request is opened or updated.

## Jobs

### 1. Trivy Repo Scan & Upload to Security Tab

#### Purpose

This job scans the entire repository for vulnerable dependencies, and uploads the results to the GitHub Security tab. This ensures that the repository's Security section remains up-to-date with newly discovered vulnerabilities, providing maintainers with an ongoing overview of dependency health.

#### Steps

1. **Run Trivy Vulnerability Scanner**: Trivy scans the entire repository. Unfixed vulnerabilities are ignored in the results.

2. **Upload Trivy Scan Results**: The results are uploaded to GitHub’s Security tab, allowing maintainers to view and manage vulnerabilities directly within the repository's settings.

### 2. Trivy PR Check

#### Purpose

This job scans only the files changed in the pull request for vulnerabilities and posts results directly to the PR using Reviewdog comments.

#### Steps

1. **Get Changed Files**: The job fetches the latest changes from the main branch and compares them with the current state of the PR.

2. **Run Trivy on Changed Files**: Trivy scans only the changed files for vulnerabilities. The scan focuses on high and critical vulnerabilities. If any vulnerabilities are detected, they will be saved for each affected file.

3. **Run Reviewdog**: Reviewdog parses the Trivy scan results and posts comments on the PR. If any vulnerabilities are found with "HIGH" or "CRITICAL" severity, they will be reported as errors.

## Configuration Details

### Trivy Scan

- The scan uses the `fs` (filesystem) mode to scan files and directories for vulnerabilities in dependencies and other files.
- Only **HIGH** and **CRITICAL** severity vulnerabilities are reported.
- Unfixed vulnerabilities are ignored with the `ignore-unfixed: true` option.

### Reviewdog

- Reviewdog posts results directly as PR review comments.
- The `level: error` option ensures that findings with HIGH or CRITICAL severity are marked as errors.
- The reviewer can view and address vulnerabilities by checking the comments posted by Reviewdog.

## Expected Results

### Trivy Repo Scan Results

- Vulnerabilities in dependencies will be detected and uploaded to the GitHub Security tab as a SARIF report.
- These results will help maintainers continuously monitor the repository’s dependencies and track vulnerabilities in the Security section of the repository settings.

### Trivy PR Check Results

- Vulnerabilities found in the files changed in the PR will trigger a review comment on the PR. The comment will include information about the severity of each vulnerability.
- HIGH and CRITICAL vulnerabilities will be marked as errors, blocking the PR from being merged until addressed.