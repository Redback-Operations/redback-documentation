# OpenWebUI Azure AD Setup Documentation

## 1. Creating the **AI User** Azure AD Group
1. Sign in to **Intra**.
2. Navigate to **Azure AD → Groups → New Group**.
3. Configure the group:
   - **Group Type:** Security
   - **Group Name:** AI User
   - **Owners:** Swethaa Sundaram, Richard (and later Ben)
   - **Members:** Swethaa Sundaram, Richard, Ben
   - **Membership Type:** Assigned
     - Chosen because it allows manual selection of members and gives owners easier control over who has access.
4. Create the group.

## 2. Registering the **OpenWebUI** Application in Azure
1. Go to **Azure AD → App Registrations → New Registration**.
2. Configure the app:
   - **Name:** OpenWebUI
   - **Supported Account Types:** Accounts in this organization directory only (Single Tenant)
   - **Redirect URI Platform:** Web
   - **Redirect URI:** The callback URL provided by Richard
3. Click **Register**.

## 3. Collecting Required IDs for Richard
After registration:
- **Microsoft Client ID:** Copied from *Application (client) ID*
- **Microsoft Tenant ID:** Copied from *Directory (tenant) ID*

## 4. Creating the Client Secret
1. Go to **Certificates & Secrets**.
2. Click **New Client Secret**.
3. Add:
   - **Description:** OpenWebUI Secret
   - **Expiry:** 6–12 months (recommended)
4. Click **Add**.
5. Copy the **Value** of the client secret (this is the actual secret Richard asked for).
   - *Note:* The **Secret ID** is **not** used — only the **Value**.

---
If you'd like, I can extend this documentation with diagrams, step-by-step screenshots placeholders, or the next steps for configuring OpenWebUI with Azure AD authentication.

