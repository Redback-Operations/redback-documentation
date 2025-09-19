---
title: Admin Panel Development
sidebar_position: 1
---

# Introduction

This report outlines the development of the Admin Panel for the Redback Smartbike application. The Admin Panel is a secure web-based interface built using React on the frontend and integrates with a Django REST Framework (DRF) backend. It is intended for administrators to manage users, monitor system metrics, and handle communication efficiently.

A critical part of this implementation is the token-based authentication system, which is integrated directly into Django's built-in authentication model using Django REST Framework's token module.

# Objectives

- Allow administrators to securely authenticate and access backend data.
- Manage users through full CRUD operations (Create, Read, Update, Delete).
- Provide insight into system usage via dashboard analytics.
- Manage communication through a built-in messaging system.
- Ensure secure, scalable API integration between frontend and backend.

# Authentication System

The Admin Panel uses token-based authentication built on Django REST Framework:

- When a user attempts to log in, the frontend makes a request to the admin login API endpoint.
- The backend uses Django's authentication system to verify the credentials.
- Upon successful verification, a token is generated and returned in the login response.
- The frontend stores the token and user data in session storage for the current session.
- For all subsequent API requests requiring authentication, the token is attached in the HTTP headers to validate the session.

This method allows for secure, stateless authentication and ensures that only authorized users can perform sensitive operations.

# Features Overview

**User Management**
- Read: Fetch all user data from the backend.
- Create: Add new user accounts via the frontend form.
- Update: Modify existing user data such as email or role.
- Delete: Remove users from the database.

**Dashboard Analytics**
- Total number of users
- Usage patterns
- System alerts or metrics

**Messaging System**
- View messages sent from users (e.g., queries, support requests)
- Reply to messages directly via the panel
- Track whether messages have been answered

# Technology Stack

| Layer      | Technology                                |
|------------|-------------------------------------------|
| Frontend   | React.js (with Axios and React Router)    |
| Styling    | Bootstrap / Tailwind CSS                  |
| Backend    | Django REST Framework                     |
| Auth       | Token Authentication (rest_framework.authtoken) |
| Storage    | Session Storage for token management      |
| API Format | RESTful JSON endpoints                     |

# API Integration Workflow

Each module in the Admin Panel communicates with the backend through structured API calls. Authentication tokens are passed in the headers of each request to validate access. A typical request/response flow includes:

1. Admin logs in via the login form.
2. Token is returned and stored on the frontend.
3. Token is included in the Authorization header for future requests:

```http
Authorization: Token <your_token_here>
