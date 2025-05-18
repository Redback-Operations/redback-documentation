---
sidebar_position: 1
sidebar_label: Restic
---

**Last updated by:** BeniDage, **Last updated on:** 16/05/2025


**Last updated by:** BeniDage, **Last updated on:** 16/05/2025


# Data Warehouse Restic-Docker Backup System

:::info
**Document Creation:** 15 May 2025. **Last Edited:** 15 May 2025. **Author:** Ben Dang.
<br></br> **Document Code:** RES1. **Effective Date:** 15 May 2025. **Expiry Date:** 15 May 2026.
:::

This document sets up a simple and secure backup system using Restic on Docker.

---

## Features

- **Automated Backups**: Back up multiple Docker volumes using Restic.
- **Snapshot Management**: Easily manage and restore snapshots.
- **Customizable**: Modify the backup script to suit your needs.

---

## Prerequisites

1. **Docker**: Ensure Docker is installed on your system. [Install Docker](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Ensure Docker Compose is installed. [Install Docker Compose](https://docs.docker.com/compose/install/).

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Redback-Operations/redback-data-warehouse.git

cd restic
```

### 2. Restic Monitors and Backs Up the Following Volumes

Restic is configured to back up data from several external Docker volumes on Redback VM. Before running the backup system, make sure these volumes exist.

```bash
data-lakehouse_minio-data
data-lakehouse_minio-config
fileuploadservice_dremio-data
dp-postgres-data
dp-es-data
dp-logstash-data
```

Run the following commands to create them:

```bash
docker volume create data-lakehouse_minio-data
docker volume create data-lakehouse_minio-config
docker volume create fileuploadservice_dremio-data
docker volume create dp-postgres-data
docker volume create dp-es-data
docker volume create dp-logstash-data
```

### 3. Configure Restic Password

Create a `restic-password.txt` file in the project directory and add your Restic repository password:

```plaintext
your-secure-password
```

### 4. Make Scripts Executable

Ensure the backup script is executable:

```bash
chmod +x scripts/backup.sh
```

---

## Running the Backup System

### Start the Restic Container

Run the following command to start the Restic container:

```bash
docker-compose up -d
```

### Verify the Logs

Check the logs of the Restic container to ensure backups are running:

```bash
docker logs -f restic-backup
```

---

## Managing Snapshots

### List Available Snapshots

To list all available snapshots, run:

```bash
docker exec -it restic-backup sh
```

### Restore a Snapshot

To restore a specific snapshot, use the following command:

```bash
restic restore <snapshot-id> --target <target-directory>
```

Replace `<snapshot-id>` with the ID of the snapshot you want to restore.

### Access Restored Files

The restored files will be available in the `./restore` directory on your host machine.

---

## Stopping the Backup System

To stop the Restic container, run:

```bash
docker-compose down
```

---

## Notes

- Ensure all required volumes are created before starting the container.
- Modify the `backup.sh` script to customize the backup process.
- Use `docker-compose logs` to troubleshoot any issues.

---

## Resources

- [Restic Documentation](https://restic.readthedocs.io/)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
