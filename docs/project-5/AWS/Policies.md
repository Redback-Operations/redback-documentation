# S3 Policy and User Access Design

:::info
By **Adityan Balamuralidharan**
:::

## Key Concept: Policy with Dynamic Paths

The policy dynamically assigns permissions to each student based on their username by using the variable `${aws:username}`. This ensures that each student can only access their own files.

## Student's Policy
1. **Objective**: Students should only be able to upload their files into their respective folders and should not have access to any data outside their folders.

### Example Workflow
1. A student uploads `Sample.txt` to the S3 bucket.
2. After applying a specific policy, the file's path becomes:
   ```
   bugboxresourcemain/Students/Assignments/${aws:username}/Sample.txt
   ```

### Breakdown
- **Bucket Name**: `bugboxresourcemain`
- **File Directory**: `Students/Assignments/${aws:username}`

### JSON Policy for Students
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::bugboxresourcesmain/Students/assignments/${aws:username}/*"
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::bugboxresourcesmain/Students/assignments/${aws:username}/*"
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        }
    ]
}
```

---

## Dynamic Path Based on User Login

The file path dynamically changes based on the student who logs in:

- **When `StudentUser1` logs in**:
  ```
  bugboxresourcemain/Students/Assignments/StudentUser1
  ```
- **When `StudentUser2` logs in**:
  ```
  bugboxresourcemain/Students/Assignments/StudentUser2
  ```

---

## Teacher's Policy
- **Objective**: Teachers have broader access to all directories under `Assignments/`.

### JSON Policy for Teachers
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
                "arn:aws:s3:::bugboxresourcesmain/Students/assignments/*",
                "arn:aws:s3:::bugboxresourcesmain/Teachers/${aws:username}/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::bugboxresourcesmain/Students/assignments/*",
                "arn:aws:s3:::bugboxresourcesmain/Teachers/${aws:username}/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::bugboxresourcesmain/Students/assignments/*",
                "arn:aws:s3:::bugboxresourcesmain/Teachers/${aws:username}/*"
            ]
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        }
    ]
}
```

---

## Admin's Policy
- **Objective**: Admins have unrestricted access to all directories under both `Students/` and `Teachers/`.

### JSON Policy for Admins
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": [
                "arn:aws:s3:::bugboxresourcesmain/Students/*",
                "arn:aws:s3:::bugboxresourcesmain/Teachers/*"
            ]
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::bugboxresourcesmain/Students/*",
                "arn:aws:s3:::bugboxresourcesmain/Teachers/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "s3:DeleteObject",
            "Resource": [
                "arn:aws:s3:::bugboxresourcesmain/Students/*",
                "arn:aws:s3:::bugboxresourcesmain/Teachers/*"
            ]
        },
        {
            "Sid": "VisualEditor3",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        }
    ]
}
```

---

## Summary

- **Data Isolation**: Students are assigned individual directories under `bugboxresourcemain/Students/Assignments/`.
- **Dynamic Access**: Policies leverage `${aws:username}` to ensure automatic and secure folder assignment based on the logged-in user.
- **Teacher and Admin Privileges**: Teachers have access to all student directories, while admins have unrestricted access to all directories.
- **Ease of Management**: No manual intervention is needed to create or assign folders.
- **Security**: Unauthorized access is strictly prevented through specific policies.