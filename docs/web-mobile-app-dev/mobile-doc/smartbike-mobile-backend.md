---
sidebar_position: 2
---

# Smartbike backend readme

## Prerequisites
- Git
- Python 3
- Virtual Environment (venv)
- Visual Studio Code or any preferred IDE
- Django and other Python libraries

## Installation Steps

### 1. Fork the Repository
First, fork the repository to your own GitHub account:

1. Visit the repository at [Redback SmartBike Mobile GitHub](https://github.com/Redback-Operations/redback-smartbike-mobile).
2. Click on the **Fork** button at the top right corner of the page. This will create a copy of the repository in your GitHub account.

### 2. Clone the Forked Repository
After forking, clone the repository to your local machine by opening a terminal and running the following commands:

```bash
git clone https://github.com/<Your_GitHub_Username>/redback-smartbike-mobile.git
cd redback-smartbike-mobile
```

Replace `<Your_GitHub_Username>` with your actual GitHub username.

This will download the repository files to your local system and change your directory to the repository's root.

### 3. Open the Project in Visual Studio Code
You can open the project directory in VS Code by typing:
```bash
code .
```

Alternatively, use the source control option in VS Code to clone and open the repository directly.

### 4. Set Up Python Virtual Environment
Navigate to the backend_server directory:
```bash
cd backend_server
```

Create and activate the virtual environment:

For Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

For MacOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 5. Install Dependencies
Install Django and other necessary Python libraries:

```bash
pip install django djangorestframework
pip install python-dotenv
pip install numpy matplotlib scikit-learn
pip install redis celery Django-celery-results
pip install Pillow
```

### 6. Configure Environment Variables
Create a .env file at the project root and specify the following values:
#### SECURITY WARNING: keep the secret key used in production secret!
```bash
SECRET_KEY = "your_secret_key_here"
```

**Email functionality**
```bash
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "your_email@example.com"
```

### 7. Database Setup
From the backend_server directory, run the following commands to set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Run the Server
Start the backend server:

```bash
python manage.py runserver 0.0.0.0:8000
```

## Troubleshooting Common Errors

### Error 1: Pillow Installation Issue
Description: You may encounter an error related to the ImageField if Pillow is not installed.

backend_server.acc_details.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".

#### Solution:

Check your Python version and install Pillow:
```bash
python -m pip install Pillow
```
#### or
```bash
python3 -m pip install Pillow
```

### Error 2: Dotenv Module Not Found
Description: If the system cannot find the dotenv module, you might see a ModuleNotFoundError.

ModuleNotFoundError: No module named 'dotenv'

#### Solution:
Check if python-dotenv is already installed:
```bash
pip list
```

If found, uninstall and reinstall python-dotenv:
```bash
pip uninstall python-dotenv
pip install python-dotenv
```
If not found, simply install the module:
```bash
pip install python-dotenv
```

Restart Visual Studio Code or your IDE to ensure the environment is refreshed.


