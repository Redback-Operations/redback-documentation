---
sidebar_position : 1
---

# Secure Coding Best Practices - ISO 27001 Mapping

Author - Dhruv Waghela

This document outlines critical secure coding controls grouped under Input Validation, Output Encoding, Session Management, and Access Control, Cryptography, Error Handling, Data Protection, Database Security  . Each control is mapped to relevant ISO 27001 clauses.

# Input Validation

| Control Point | Description | Implementation | Risk | ISO 27001 Mapping |
| --- | --- | --- | --- | --- |
| Input Length Check | Ensure input length is within acceptable range. | Implement input length checks on client and server side.  <br><br/>def is_valid_length(user_input, min_len=1, max_len=255):<br><br>return min_len <= len(user_input) <= max_len | Buffer overflow, DoS attacks | A.14.2.5 |
| Type Check | Validate input data types before processing. | Use strict type checking functions.  <br><br/>def is_string(value):<br><br>return isinstance(value, str) | Type confusion, unexpected behavior | A.14.2.1 |
| Whitelist Validation | Accept only known good inputs. | Apply input whitelisting using regex or predefined values.  <br><br/>import re<br><br>def is_valid_username(username):<br><br>return re.match("^\[a-zA-Z0-9_\]+$", username) is not None | Injection attacks | A.14.2.5 |
| Encoding Normalization | Normalize inputs to avoid evasions. | `Decode inputs before validation.`<br><br>`from unicodedata import normalize`<br><br>`def normalize_input(input_str):`<br><br>`return normalize('NFKC', input_str)` | Bypass filters | A.14.2.5 |
| Special Character Handling | Reject or escape special characters. | Use secure libraries to strip or encode special characters.  <br><br/>import html<br><br>def escape_special_chars(user_input):<br><br>return html.escape(user_input) | XSS, SQL Injection | A.14.2.5 |
| Server-Side Validation | Do not rely on client-side validation alone. | Implement duplicate validations on the server side.  <br><br/>def validate_form(data):<br><br>if not is_valid_length(data.get("username", "")):<br><br>return False<br><br>\# Add further validation<br><br>return True | Bypass through client manipulation | A.14.2.5 |

# Output Encoding

| Control Point | Description | Implementation | Risk | ISO 27001 Mapping |
| --- | --- | --- | --- | --- |
| HTML Encoding | Encode output before rendering to HTML. | Use functions like htmlspecialchars() in PHP or equivalent.  <br><br/>import html<br><br>def encode_html(data):<br><br>return html.escape(data) | Cross-site scripting | A.14.2.5 |
| JavaScript Encoding | Sanitize dynamic data before inserting into JavaScript. | Escape strings used within scripts.  <br><br/>import json<br><br>def safe_js_string(data):<br><br>return json.dumps(data) | DOM-based XSS | A.14.2.5 |
| URL Encoding | Encode dynamic data in URLs. | Use encodeURIComponent and similar methods.  <br><br/>import urllib.parse<br><br>def encode_url_component(value):<br><br>return urllib.parse.quote_plus(value) | Redirect manipulation | A.14.2.5 |
| CSS Encoding | Encode output used within style tags. | Avoid direct insertion of user input in styles.  <br><br/>def encode_css_value(value):<br><br>return value.replace("&lt;", "\\\\3C ").replace("&gt;", "\\\\3E ") | CSS Injection | A.14.2.5 |
| JSON/XML Encoding | Encode values in serialized formats. | Use trusted libraries for serialization.  <br><br/>import json<br><br>def encode_json(data_dict):<br><br>return json.dumps(data_dict) | Injection in data transport | A.14.2.5 |

# Session Management

| Control Point | Description | Implementation | Risk | ISO 27001 Mapping |
| --- | --- | --- | --- | --- |
| Secure Session IDs | Use strong, unpredictable session identifiers. | Implement long random session tokens.  <br><br/>import secrets<br><br>def generate_session_id():<br><br>return secrets.token_urlsafe(32) | Session fixation | A.9.2.1 |
| Session Timeout | Set appropriate session timeout. | Expire sessions after 15 minutes of inactivity.  <br><br/>from datetime import datetime, timedelta<br><br>session_expiry = datetime.now() + timedelta(minutes=15) | Session hijacking | A.9.4.2 |
| Regenerate Session ID | Change session ID on privilege change. | Call regenerate_id() after login.  <br><br/>def regenerate_session(session):<br><br>session\["id"\] = generate_session_id() | Fixation & impersonation | A.9.4.2 |
| Secure Cookie Flags | Enable HttpOnly and Secure flags. | Set cookies with Secure and HttpOnly attributes.  <br><br/>from flask import make_response<br><br>def set_secure_cookie(response, key, value):<br><br>response.set_cookie(key, value, httponly=True, secure=True) | Cookie theft | A.10.1.1 |
| Logout Functionality | Provide a logout feature. | Implement session invalidation on logout.  <br><br/>def logout_user(session):<br><br>session.clear() | Session reuse | A.9.4.2 |
| Session Binding | Bind session to IP/User-Agent. | Check user context on each request.  <br><br/>def is_valid_session(request, session):<br><br>return session\["user_agent"\] == request.headers.get("User-Agent") | Session hijack detection | A.9.2.1 |
| Multi-Factor Authentication | Add MFA for sensitive areas. | Integrate OTP-based or app-based MFA.  <br><br/>import pyotp<br><br>def verify_otp(secret, token):<br><br>totp = pyotp.TOTP(secret)<br><br>return totp.verify(token) | Credential theft | A.9.4.2 |
| No Session in URL | Avoid session IDs in URL. | Use cookies for session management. | Session leakage | A.9.4.2 |
| Invalid Session Detection | Detect and reject expired sessions. | Track session expiry and enforce.  <br><br/>def is_session_expired(session_timestamp, timeout_minutes=15):<br><br>from datetime import datetime, timedelta<br><br>return datetime.now() > session_timestamp + timedelta(minutes=timeout_minutes) | Privilege escalation | A.9.4.2 |
| Secure Session Store | Encrypt session data on server. | Store encrypted sessions in database or memory. | Session tampering | A.10.1.1 |

# Access Control

| Control Point | Description | Implementation | Risk | ISO 27001 Mapping |
| --- | --- | --- | --- | --- |
| Role-Based Access Control | Grant access based on user roles. | Define roles and assign least privileges.  <br><br/>def has_permission(user, required_role):<br><br>return required_role in user.get("roles", \[\]) | Unauthorized access | A.9.1.2 |
| Principle of Least Privilege | Grant minimum access required. | Regularly review user permissions. | Privilege abuse | A.9.1.2 |
| Access Control Lists | Use ACLs to manage permissions. | Set up ACLs for file and resource access.  <br><br/>ACL = {"admin": \["read", "write"\], "user": \["read"\]}<br><br>def can_access(role, action):<br><br>return action in ACL.get(role, \[\]) | Improper resource access | A.9.1.2 |
| Authentication Enforcement | Enforce user identity verification. | Use strong password policies.  <br><br/>import re<br><br>def is_strong_password(pwd):<br><br>return re.match(r'^(?=.\*\[A-Z\])(?=.\*\[a-z\])(?=.\*\\\\d).{8,}$', pwd) is not None | Unauthorized login | A.9.2.1 |
| Authorization Checks | Check privileges before every action. | Verify roles before performing operations.  <br><br/>def authorize_action(user, action):<br><br>return action in user.get("permissions", \[\]) | Function-level access control | A.9.4.1 |
| Disable Unused Accounts | Remove or disable dormant accounts. | Implement account deactivation policies.  <br><br/>def disable_account(user):<br><br>user\["active"\] = False | Account misuse | A.9.2.6 |
| Account Lockout | Lock account after failed attempts. | Implement lockout after 5 failed logins.  <br><br/>FAILED_ATTEMPTS = {}<br><br>def should_lock_account(user_id):<br><br>return FAILED_ATTEMPTS.get(user_id, 0) >= 5 | Brute force attacks | A.9.4.2 |
| Segregation of Duties | Separate critical functions. | Split roles across different users. | Insider threats | A.6.1.2 |
| Audit Logging | Log access control events. | Record successful and failed access attempts.  <br><br/>import logging<br><br>logging.basicConfig(filename='audit.log', level=logging.INFO)<br><br>def log_access(user, action):<br><br>logging.info(f"{user} performed {action}") | Lack of traceability | A.12.4.1 |
| Time-Based Access | Restrict access by time. | Allow logins only during business hours.  <br><br/>from datetime import datetime<br><br>def is_within_access_time():<br><br>now = datetime.now().hour<br><br>return 9 <= now <= 17 | After-hours exploitation | A.9.1.2 |
| Approval Workflow | Require approval for role changes. | Use automated access request systems. | Privilege escalation | A.9.2.5 |
| Access Review | Review access permissions regularly. | Perform quarterly access reviews. | Permission creep | A.9.2.5 |
| Third-Party Access Control | Manage access for vendors. | Use temporary credentials with expiration.  <br><br/>from datetime import datetime, timedelta<br><br>def create_temp_credentials(expiry_minutes=60):<br><br>expiry = datetime.now() + timedelta(minutes=expiry_minutes)<br><br>return {"key": generate_session_id(), "expiry": expiry} | Supply chain risk | A.15.1.1 |
| No Hardcoded Credentials | Avoid embedding secrets in code. | Use environment variables or vaults.  <br><br/>import os<br><br>API_KEY = os.getenv("API_KEY") | Credential leakage | A.9.2.3 |
| Session Management Enforcement | Tie access to active sessions. | Validate session state on access checks.  <br><br/>def enforce_session_access(user, session):<br><br>return user\["id"\] == session.get("user_id") | Unauthorized access | A.9.4.2 |

# Cryptography

| Security Controls | Description | Implantation | Risk | ISO 27001 Mapping |
| --- | --- | --- | --- | --- |
| All cryptographic functions must be on a trusted system | Avoid client-side encryption (e.g., JavaScript). Use server-side for encryption/decryption/hashing. | from cryptography.fernet import Fernet; key = Fernet.generate_key(); cipher = Fernet(key); encrypted = cipher.encrypt(b"secret data") | Data may be intercepted, altered, or exposed via browser dev tools | A.10.1.1 (Cryptographic controls) |
| Protect master secrets from unauthorized access | Limit access to encryption keys and passwords. | Use OS-level vaults or key management services (e.g., AWS KMS, Azure Key Vault) | Exposure of encryption keys leads to total compromise of protected data | A.9.2.3 (Management of privileged access rights) |
| Cryptographic modules should fail securely | Ensure failure of encryption doesn’t result in data transmission or logging. | try: encrypted = cipher.encrypt(b"data"); except Exception: abort_operation() | Sensitive data might be exposed if failure not handled | A.12.1.3 (Capacity management) |
| Use approved random number generators | Use strong PRNGs (e.g., OpenSSL-backed). | import secrets; token = secrets.token_bytes(32) | Predictable values can lead to token forgery, brute-force | A.10.1.1 (Cryptographic controls) |
| FIPS 140-2 compliant crypto modules | Use AES, SHA-2 to meet standards. | from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes; cipher = Cipher(algorithms.AES(key), modes.CBC(iv)) | Weak algorithms may be broken by attackers | A.10.1.1 / A.18.1.4 (Independent review of cryptographic controls) |
| Policy/process for key management | Create procedures for key generation, storage, rotation, disposal. | Define and automate key lifecycle via KMS APIs | Key leaks, reuse, or misuse can lead to data compromise | A.10.1.2 (Key management) |

# Error Handling

| Security Control | Description | Implementation | Risk | ISO 27001 Mapping |
| --- | --- | --- | --- | --- |
| Use generic error messages and custom error pages | Prevent attackers from gathering system info from detailed errors. | app.register_error_handler(500, lambda e: render_template('error.html')) | Information disclosure, targeted exploitation | A.13.1.1 (Network controls) |
| Do not disclose sensitive info in error responses | Strip out session IDs, technology stack info from error pages. | try: ... except Exception as e: log_error(str(e)); return "Something went wrong" | Aids reconnaissance and exploits | A.12.4.1 (Event logging) |
| Ensure logs include only sanitized, non-executable data | Prevent logs from becoming vectors for injection (e.g., XSS). | import html; safe_input = html.escape(user_input) | XSS through log viewing interfaces | A.12.4.1 (Event logging) |
| Restrict access to logs to authorized individuals | Logs must be read-only and limited to minimal roles. | OS permissions or chmod 640 /var/log/app.log | Log tampering, privacy violation | A.9.4.5 (Access control to program source code) |
| Log all authentication attempts, especially failures | Helps detect brute-force, credential stuffing, or misuse. | logger.info(f"Auth failed for user {user}") | Missed detection of login attacks | A.12.4.3 (Administrator and operator logs) |
| Use a cryptographic hash to validate log integrity | Ensures logs haven’t been modified post-write. | import hashlib; hash = hashlib.sha256(log_data.encode()).hexdigest() | Forged or deleted logs after compromise | A.10.1.1 / A.12.4.2 |
| Log all administrative and configuration changes | Detects privilege escalation or insider threat behavior. | logger.info(f"Admin changed firewall rule X at {timestamp}") | Unnoticed config tampering or policy changes | A.12.4.3 / A.9.2.6 |
| Log all access control failures | Tracks broken access control attempts. | logger.warning(f"Access denied for user {user} on {resource}") | Missed detection of privilege escalation attempts | A.12.4.1 / A.9.4.4 |
| Ensure mechanism exists to conduct log analysis | Regular review via SIEM or scripts for anomalies. | Integration with tools like Splunk/ELK | Delayed detection of incidents | A.12.4.1 / A.16.1.7 |
| Implement centralized, trusted log collection | Logs must be collected on secure, tamper-evident systems. | Use syslog to remote collector: logger -n logserver.example.com -P 514 | Log loss or manipulation if compromised locally | A.12.4.2 / A.13.2.1 |

# Data Protection

| Security Control | Description | Implementation | Risk | ISO 27001 Control |
| --- | --- | --- | --- | --- |
| Least Privilege | Only give users minimal required access. | Use RBAC: if user.role == 'admin': access_admin_panel() | Unauthorized access, privilege escalation | 5.18 Access rights |
| Protect Temp/Cached Data | Restrict access & delete temporary sensitive files. | with open('temp.txt', 'w') as f: f.write(data); os.remove('temp.txt') | Data leakage via temp files | 8.10 Storage media handling |
| Encrypt Server-Side Data | Use strong encryption for stored sensitive data. | from cryptography.fernet import Fernetcipher = Fernet(key)cipher.encrypt(b"password") | Data compromise during breach | 8.25 Cryptographic controls |
| Protect Source Code | Prevent access/download of server-side source. | Ensure .py files are not publicly exposed via web server configs | Attackers can reverse-engineer logic | 8.32 Change management |
| Avoid Clear Text on Client Side | No plain text credentials or weak algorithms in client code. | ✔ Avoid sending secrets to frontend ✘ No MD5: hashlib.md5(data.encode()) ✔ Use: hashlib.sha256(data.encode()) | Credential theft, replay attacks | 8.24 Protection of log information |
| Remove Sensitive Comments | Delete code comments revealing internal info. | \# Avoid:# DB_Password = "admin123" | Attackers gain critical internal details | 5.34 Secure development lifecycle |
| Remove Unnecessary Documentation | Don’t expose internal app/system docs. | Don’t deploy /docs/, /readme.txt or outdated manuals in prod | Info disclosure aiding reconnaissance | 8.1 Information security requirements |
| No Sensitive Info in GET | Avoid passing sensitive info via URL. | ✔ requests.post(url, data=payload) ✘ requests.get(url + "?password=123") | URLs are logged/stored in history | 8.22 Secure development practices |
| Disable Autocomplete | Prevent browsers from storing credentials. | &lt;input type="password" autocomplete="off"&gt; | Exposure through stored credentials | 8.11 User endpoint device security |
| Disable Client-Side Caching | Avoid storing sensitive pages in browser cache. | response.headers\['Cache-Control'\] = 'no-store'response.headers\['Pragma'\] = 'no-cache' | Data recovery from browser cache | 8.10 Storage media handling |
| Secure Data Removal | Delete sensitive info when not needed. | del sensitive_datagc.collect() (for memory)os.remove('data.txt') | Long-term retention increases breach impact | 8.11 User endpoint device security |
| Access Control for Server Data | Restrict access to files/data to valid system roles. | if user.role == 'analyst': allow_access() | Unauthorized file access | 5.18 Access rights |

# Database Security

| Security Control | Description | Implementation (Code Snippet) | Risk | ISO 27001 Control |
| --- | --- | --- | --- | --- |
| Parameterized Queries | Prevents SQL injection by using placeholders rather than string concatenation. | python\\ncursor.execute("SELECT \* FROM users WHERE username = %s", (username,))\\n | SQL Injection, data breach | 8.32 Secure development |
| Input Validation & Output Encoding | Ensures user inputs are safe and outputs are properly encoded. | python\\ndef is_valid_email(email):\\n return re.match(r'^\[\\\\w\\\\.-\]+@\[\\\\w\\\\.-\]+\\\\.\\\\w+$', email)\\nhtml.escape(user_input)\\n | XSS, injection attacks | 8.32 Secure development |
| Least Privilege Access | Restricts access rights for users to the bare minimum. | python\\nif user.role == 'admin':\\n access_admin_panel()\\nelse:\\n deny_access()\\n | Privilege escalation, unauthorized access | 5.18 Access control |
| Secure Credential Storage | Avoids hardcoded credentials; uses environment variables or secure vaults. | python\\nimport os\\nDB_PASSWORD = os.getenv("DB_PASSWORD")\\n | Credential exposure, compromise | 8.2 User access management |
| Output Sanitization | Ensures data displayed in the browser does not execute scripts. | python\\nimport html\\nsafe_output = html.escape(user_input)\\n | Cross-site scripting (XSS) | 8.32 Secure development |
| Session Management | Implements secure session controls with expiration and regeneration. | python\\nsession\['user'\] = user_id\\nsession.permanent = True\\napp.permanent_session_lifetime = timedelta(minutes=30)\\n | Session hijacking, fixation | 8.32 Secure development |
| Error Handling | Avoids leaking sensitive info through error messages. | python\\ntry:\\n db.connect()\\nexcept Exception as e:\\n log.error("Database connection failed")\\n abort(500)\\n | Information disclosure, security misconfig | 8.32 Secure development |
| Logging and Monitoring | Logs events securely and monitors for anomalies. | python\\nimport logging\\nlogging.basicConfig(filename='app.log', level=logging.INFO)\\nlogging.info("User login attempt")\\n | Breach detection delays | 5.33 Logging |