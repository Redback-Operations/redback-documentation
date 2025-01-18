---
sidebar_position: 4
---
# Implementing Role-Based Access Control (RBAC) with IAM and S3 in AWS

:::info
By **Corrina Maria Glover, Rishubh Sethi, Adityan Balamuralidharan, Pranav**
:::

## Introduction to AWS IAM and S3

Amazon Web Services (AWS) offers a comprehensive set of cloud tools that help businesses manage their data and operations securely. Two important services for Bugbox are Identity and Access Management (IAM) and Simple Storage Service (S3).

IAM allows Bugbox to manage who can access which parts of the platform and what they can do with those resources. It helps administrators set up users, assign roles, and create permissions to make sure that people only have access to what they need. S3 is a cloud storage service where Bugbox can safely store educational materials, student assignments, and other important data.

Together, IAM and S3 help Bugbox implement Role-Based Access Control (RBAC). This system makes sure users can only access resources based on their roles, helping keep the platform secure and compliant with privacy rules like GDPR and FERPA.

## Understanding Role-Based Access Control (RBAC)

RBAC is a system that controls who can access which resources based on their job role. This ensures that people only have access to what’s needed for their work, reducing the risk of sensitive information being exposed.

RBAC involves two main parts:

- **Roles**: These represent job responsibilities. Examples include Administrator, Educator, and Student.
- **Permissions**: These define what users can do, such as CRUD (Create, Read, Update and Delete).

In Bugbox:

- An **Administrator** can manage the entire platform, including user roles and data.
- An **Educator** can view student assignments and upload lesson plans, student feedbacks but can't change system settings.
- A **Student** can only view and submit their own assignments.

RBAC helps Bugbox ensure that users only have access to the parts of the platform that are relevant to their role.

## How IAM is implemented in Bugbox

In Bugbox, IAM is used to create and manage users, assign roles, and control access to resources. It allows administrators to define specific user accounts for various roles, such as administrators, educators, and students. Each user is assigned a role that determines their level of access and the actions they can perform within Bugbox. These roles are linked to IAM policies, which define the permissions granted to the user. To implement this, Bugbox uses inline policies to assign specific permissions to users.

## S3 for RBAC at Bugbox

S3 is where Bugbox stores most of its static data, and by using IAM, Bugbox controls user access to specific files. CRUD (Create, Read, Update, Delete) permissions manage access to data: administrators can fully manage files in the `bugboxresourcesmain` bucket, educators can read and upload content but cannot delete it, and students can only submit assignments without the ability to delete other users' files. By combining IAM's permission system with S3’s storage controls, Bugbox ensures secure, role-based access to data.

## Sample Policy for Student Role

The following IAM policy provides write access to a Student role, specifically allowing them to upload student assignments to the `bugboxresourcesmain` S3 bucket under the `Students/assignments/StudentUser` folder. 

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::bugboxresourcesmain/Students/assignments/$(aws.username)/*"
      ]
    }
  ]
}
