---
sidebar_position: 1
---

# Smartbike mobile app readme

## Redback SmartBike Mobile App Frontend Setup

### Prerequisites
- Android Studio or Visual Studio Code
- Git
- Flutter SDK
- Dart

### Installation Steps
#### 1. Fork the Repository and Clone the Repository to your computer

**Open Android Studio:**
1. Navigate to File -> New -> Project from Version Control.
2. Enter the repository URL:
`https://github.com/Redback-Operations/redback-smartbike-mobile.git`
3. Choose the directory to save the project on your computer.
4. Click Clone.

#### 2. Configure Environment Variables

Add a .env file in the root project directory with the following content:

# Base URL for API
`API_URL_BASE = http://<your_machine_network_address>:8000`

# Example:
`API_URL_BASE = http://192.168.3.103:8000`

#### 3. Install Dependencies
Navigate to the **pubspec.yaml** file and run:

pub get
This command will install all the necessary Flutter dependencies specified in **pubspec.yaml**.

#### 4. Run the Backend
Ensure that the backend server is running as the mobile app will need to communicate with it.

#### 5. Start the App
- Using VS Code: Open lib/main.dart and press the run (play) button at the top right.
- Using Android Studio: Run the project directly from the IDE.

### Version Control Best Practices
- New Features and Fixes: Always create a new branch before starting work on a new feature or fix:

```
git checkout -b <name-of-fix-or-feature>
```
- Commit Changes: Commit your changes frequently to maintain a good history and easier code reviews:
bash
```
git add .
git commit -m "Describe the changes here"
git push # You might need to set the upstream branch if it's a new branch
```
- Pull Changes: It's good practice to pull the latest changes from the repository before starting on new features:
`git pull`

### Troubleshooting
- Merge Conflicts: If you encounter merge conflicts after pulling changes, consider saving your work in a separate file before attempting to resolve conflicts. This precaution helps avoid accidental data loss.
- IDE and SDK Compatibility: Ensure that your development environment matches the versions known to work with the app:

  IDE: Android Studio Iguana | 2023.2.1, Xcode Version 15.4\
  Flutter: 3.22.3 Stable\
  Dart: 3.4.4\
  DevTools: 3.34.3

### Happy Coding!
Remember, if in doubt about any steps or issues, contact your project leader for assistance.

