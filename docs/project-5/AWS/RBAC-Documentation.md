---
sidebar_position: 1
---
# Bugbox’s Role Based Access Control Guide

:::info
By **Corrina Maria Glover, Rishubh Sethi, Adityan Balamuralidharan, Pranav**
:::

## Purpose

The purpose of this document is to provide guidance on implementing Role-Based Access Control (RBAC) in Bugbox. By defining clear roles, responsibilities, and permissions, Bugbox ensures that users have appropriate access to resources based on their job functions, while protecting sensitive data and streamlining administrative tasks.

## Scope

This document focuses on the following:

- Defining and managing user roles and responsibilities
- Assigning appropriate permissions based on role requirements
- Best practices for role-based access control in Bugbox
- Overview of using IAM and S3 for enforcing these roles where needed

## Roles and Responsibilities

The following roles and responsibilities ensure that each user has the proper level of access based on their job function:

### Administrator

- Full access to the Bugbox platform and all associated resources.
- Can manage users, define roles, and assign permissions.
- Responsible for ensuring system integrity and compliance with internal security standards.

### Educator/Teacher

- Access to view, upload, and manage content (e.g., lesson plans, student assignments) within specific areas.
- Cannot delete or modify other users’ data.
- Limited to specific permissions within Bugbox resources related to educational content.

### Student

- Access to view and submit their own assignments.
- Cannot access, modify or delete files of other students’ data.
- Restricted permissions to their own folder within Bugbox’s storage.

## Permission Matrix

This permission matrix defines the access level each role has within Bugbox:

| Role         | Create   | Read     | Update   | Delete   | View     | Upload   |
|--------------|----------|----------|----------|----------|----------|----------|
| **Admin**    | Yes      | Yes      | Yes      | Yes      | Yes      | Yes      |
| **Teacher**  | Yes      | Yes      | Yes      | Yes      | Yes      | Yes      |
| **Student**  | No       | No       | Yes      | No       | Yes      | Yes      |

## User Stories

### Administrator User Story

As an Administrator, I need full access to all platform resources, including the ability to create users, define roles, manage permissions, and ensure system integrity, so that I can maintain security and control over Bugbox operations.

### Educator User Story

As an Educator, I need to manage my students' assignments, upload resources, and provide feedback, while being restricted from deleting or modifying other users’ data, so that I can effectively teach within a secure and structured environment.

### Student User Story

As a Student, I need to submit assignments to my own folder, view my progress, and upload content, while being unable to access or modify other students' work, so that I can focus on my learning in a private and secure environment.

## How to Create Tags for Resource Organization and Access Control

Tags are used to help organize AWS resources logically and provide an extra layer of security by controlling access based on resource labels. Bugbox can implement tags for S3 buckets, IAM roles, and other AWS resources to manage access efficiently.

### Steps to Create Tags:

1. Navigate to AWS Management Console and go to the S3 service.
2. Select the desired bucket (e.g., `bugboxresourcesmain`).
3. Under the **Properties** tab, scroll down to the **Tags** section.
4. Click on **Add Tag** and input the key-value pairs, such as:

    - **Key**: Classroom
    - **Value**: ClassA

5. Save the tag.

### Access Control Using Tags:

Use the tags in IAM policies to control who can access specific resources. For example, a policy could restrict access to resources tagged as `Classroom:ClassA` to only users assigned to that class.

## How to Create Users in IAM

To properly implement RBAC, administrators need to create IAM users for each individual and assign them the appropriate roles. Here's how:

1. Navigate to the AWS IAM Console and click **Users**.
2. Click on **Add User** to create a new user.
3. Enter the user’s username and select the type of access (Programmatic access for API, CLI, and Console access for web access).
4. Under **Permissions**, choose one of the following:
    - **Attach existing policies directly**: Select pre-defined policies like `AdministratorAccess`, `ReadOnlyAccess`, or custom policies.
    - **Create group**: Place the user into a predefined group that has the appropriate permissions.
    - **Copy permissions from existing user**: Copy permissions from another user with similar responsibilities.
5. If applicable, assign tags to the user to help identify them based on their role, class, or other attributes.
6. Review and **Create User**.

## Conclusion

By implementing RBAC with IAM and S3, Bugbox ensures that access to platform resources is secure, roles are clearly defined, and users only have access to what is necessary for their responsibilities. Tags enhance resource management and access control, while the IAM policy system ensures that permissions are correctly assigned, ensuring a compliant and secure environment for all users.
