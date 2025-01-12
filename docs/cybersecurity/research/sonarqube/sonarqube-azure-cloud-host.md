---
sidebar_position: 2
---

:::info
Author : Ashan Ruwanpathiranage 
:::

# SonarQube Cloud Installation Guide using Azure Ubuntu Virtual Machine

This guide provides detailed steps to install SonarQube in cloud enviornment (Azure Ubuntu VM). 

---

## Prerequisites

1. New Ubuntu 22.0.4 Virtual Machine instance with at least medium performance (4 GB RAM)

2. Docker 

3. Docker-compose

---

## Step 1: System Configuration

Login to SonarQube instance using git bash or azure cli and perform below command to configure virtual memory permanently for SonarQube to function:

```
sudo nano /etc/sysctl.conf

```

Add the following lines to the bottom of that file by scrolling all the way down:

```
vm.max_map_count=262144
fs.file-max=65536

```
Press Ctrl + O and Enter for saving the file.
Press Ctrl + X for exiting the file after saving.

To make sure changes are getting into effect:

```
sudo sysctl -p

```

Perform System update

```
sudo apt update

```

---

## Step 2: Create docker-compose.yml

Create yaml file

```

sudo vi docker-compose.yml 

```

copy and paste below script

```

version: "3"
services:
  sonarqube:
    image: sonarqube:community
    restart: unless-stopped
    depends_on:
      - db
    environment:
      SONAR_JDBC_URL: jdbc:postgresql://db:5432/sonar
      SONAR_JDBC_USERNAME: sonar
      SONAR_JDBC_PASSWORD: sonar
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
      - sonarqube_logs:/opt/sonarqube/logs
    ports:
      - "9000:9000"
  db:
    image: postgres:12
    restart: unless-stopped
    environment:
      POSTGRES_USER: sonar
      POSTGRES_PASSWORD: sonar
    volumes:
      - postgresql:/var/lib/postgresql
      - postgresql_data:/var/lib/postgresql/data
volumes:
sonarqube_data:
  sonarqube_extensions:
  sonarqube_logs:
  postgresql:
  postgresql_data:

```

---

## Step 3: Execute the compose file using Docker compose command

Open the bash shell and execute the below code

```

sudo docker-compose up -d 

```

Make sure SonarQube is up and running by checking the logs

```

sudo docker-compose logs

```

Now access sonarQube Dashboard by going to browser and enter public dns name OR public IP address with port 9000

Now to go to browser --> http://SonarQube_public_dns_name:9000/
			               --> http://your_SonarQube_public_IP_address:9000/


---



By following these steps, you can successfully integrate SonarQube with GitHub to enhance your code quality and maintainability practices.
