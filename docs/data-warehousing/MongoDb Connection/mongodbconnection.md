---
sidebar_position: 1
---

# MongoDB Connection Server

:::info
**Effective Date:** 15 August 2024. **Last Edited:** 20 September 2024. **Author:** Ben Dang (Redback Operations).
**Document Reference:** MongoDB Connection. **Expiry Date:** 15 August 2025. **Version:** 1.0.
:::

This project is a web server application that connects to a MongoDB database. The setup uses Docker Compose to manage the services.

## Prerequisites

- Docker
- Docker Compose

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/Redback-Operations/redback-data-warehouse.git

cd "MongoDB Connection/Project1"

```

### 2. Create .env at your root directory

- MONGO_URI="mongodb://your_username:your_password@your_host:your_port/?authSource=your_authSource"
- DB_NAME="your_database_name"
- COLLECTION_NAME="your_collection_name"

### 3. Run Docker Compose to build the images and run the services:

```bash
- docker-compose up --build
```

### 4. View the Application

- Open your browser and navigate to http://localhost:5003/

## Configuring MongoDB and Monitoring Logs

### Changing MongoDB Documents and Collections as needed

- config.py contains the MongoDB connection string.
- document_model.py contains the MongoDB collection name.

### Check logs application

- All the logs are stored in the logs folder at the root of the project.(app.log)

## API Endpoints

### 1. Get All Documents

- **Endpoint**: `/documents`
- **Method**: `GET`
- **Description**: Retrieves all documents from the database.
- **Response**:
  - `200 OK`: Returns a JSON array of documents.

### 2. Get Document by ID

- **Endpoint**: `/documents/<document_id>`
- **Method**: `GET`
- **Description**: Retrieves a document by its ID.
- **Parameters**:
  - `document_id` (path): The ID of the document to retrieve.
- **Response**:
  - `200 OK`: Returns the document as a JSON object.
  - `404 Not Found`: If the document is not found.

### 3. Insert Document

- **Endpoint**: `/documents`
- **Method**: `POST`
- **Description**: Inserts a new document into the database.
- **Request Body**: JSON object representing the document to insert.
- **Response**:
  - `201 Created`: Returns a success message and the ID of the inserted document.

### 4. Update Document

- **Endpoint**: `/documents/<document_id>`
- **Method**: `PUT`
- **Description**: Updates an existing document by its ID.
- **Parameters**:
  - `document_id` (path): The ID of the document to update.
- **Request Body**: JSON object representing the updated document data.
- **Response**:
  - `200 OK`: Returns a success message if the document was updated.
  - `404 Not Found`: If the document is not found or no changes were made.

### 5. Delete Document

- **Endpoint**: `/documents/<document_id>`
- **Method**: `DELETE`
- **Description**: Deletes a document by its ID.
- **Parameters**:
  - `document_id` (path): The ID of the document to delete.
- **Response**:
  - `200 OK`: Returns a success message if the document was deleted.
  - `404 Not Found`: If the document is not found.
