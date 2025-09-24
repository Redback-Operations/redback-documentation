---
sidebar_position: 3
---

:::info
Author : Ashan Ruwanpathiranage 
:::

# SonarQube Integration with GitHub

This guide provides detailed steps to integrate SonarQube with GitHub. It assumes SonarQube is hosted on an Azure Virtual Machine and a GitHub App has been created.

---

## Prerequisites

1. **SonarQube Setup**:
   - A running instance of SonarQube on an Azure Virtual Machine.
   - Access to the SonarQube dashboard.
   - Admin permissions on SonarQube.

2. **GitHub Setup**:
   - A GitHub repository to integrate.
   - Admin access to the repository.
   - A GitHub App created with necessary permissions.

---

## Step 1: Configure GitHub App

1. **Modify App Permissions**:
   - Go to the GitHub App settings.
   - Under **Permissions**, set the following:
     - **Repository Permissions**: 
       - Metadata: Read-only
       - Checks: Read & write
       - Commit statuses: Read & write
       - Pull requests: Read & write
     - **Organization Permissions** (if applicable): 
       - Administration: Read-only
   - Save changes.

2. **Add Webhook**:
   - In the GitHub App settings, add a new webhook.
   - Use the following details:
     - **Payload URL**: `http://<your-azure-vm-ip>:9000/webhook`.
     - **Content type**: `application/json`.
     - **Secret**: The webhook secret generated in SonarQube.
   - Save the webhook.

3. **Install the App**:
   - Install the GitHub App on the repository you wish to integrate.

---

## Step 2: Set Up the SonarQube Project

1. **Create a Project in SonarQube**:
   - Navigate to **Projects** > **Create Project**.
   - Provide a project key and display name.

2. **Generate a Token**:
   - Navigate to your user profile in SonarQube.
   - Go to **My Account** > **Security** > **Tokens**.
   - Generate a new token and save it securely.

3. **Set Up the `sonar-project.properties` File**:
   - In your GitHub repository, create a `sonar-project.properties` file with the following content:
     ```properties
     sonar.projectKey=<your-project-key>
     sonar.organization=<your-organization>
     sonar.host.url=http://<your-azure-vm-ip>:9000
     sonar.login=<your-generated-token>
     ```

---

## Step 3: Configure CI/CD Pipeline

1. **Add SonarScanner to Your CI/CD Pipeline**:
   - Update your CI/CD configuration file (e.g., GitHub Actions, Jenkins, etc.) to include SonarScanner.
   - Example GitHub Actions Workflow:
     ```yaml
     name: SonarQube Scan

     on:
       pull_request:
       push:
         branches:
           - main

     jobs:
       sonarQube:
         runs-on: ubuntu-latest

         steps:
           - name: Checkout code
             uses: actions/checkout@v3

           - name: Run SonarQube Scan
             run: |
               sonar-scanner \
                 -Dsonar.projectKey=<your-project-key> \
                 -Dsonar.host.url=http://<your-azure-vm-ip>:9000 \
                 -Dsonar.login=<your-generated-token>
     ```

2. **Commit and Push**:
   - Commit the pipeline configuration to your repository and push it.

---

## Step 5: Verify Integration

1. **Trigger a Build**:
   - Open a pull request or push a commit to the repository.

2. **Check SonarQube**:
   - Go to your project in SonarQube.
   - Verify that the analysis results are displayed.

3. **Check GitHub**:
   - Open the pull request in GitHub.
   - Verify that the SonarQube checks (e.g., code quality, security analysis) are displayed.

---

## Troubleshooting

- **Connection Issues**:
  - Ensure the Azure VM’s firewall allows traffic to and from GitHub.
  - Verify that the webhook URL is correct.

- **Permissions Issues**:
  - Double-check the GitHub App permissions and installation.

- **Pipeline Failures**:
  - Check the CI/CD logs for errors in the SonarScanner configuration.

---

By following these steps, you can successfully integrate SonarQube with GitHub to enhance your code quality and maintainability practices.
