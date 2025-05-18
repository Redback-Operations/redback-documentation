# Secure Coding Best Practices - ISO 27001 Mapping

Author - Dhruv Waghela

This document outlines critical secure coding controls grouped under Input Validation, Output Encoding, Session Management, Access Control, Cryptography, Error Handling, Data Protection, and Database Security. Each control is mapped to relevant ISO 27001 clauses.

## Input Validation

| Control Point | Description | Implementation | Risk | ISO 27001 Mapping |
|---|---|---|---|---|
| Input Length Check | Ensure input length is within acceptable range. | `def is_valid_length(user_input, min_len=1, max_len=255): return min_len <= len(user_input) <= max_len` | Buffer overflow, DoS attacks | A.14.2.5 |
| Type Check | Validate input data types before processing. | `def is_string(value): return isinstance(value, str)` | Type confusion, unexpected behavior | A.14.2.1 |
| Whitelist Validation | Accept only known good inputs. | `import re`<br/>`def is_valid_username(username): return re.match("^[a-zA-Z0-9_]+$", username) is not None` | Injection attacks | A.14.2.5 |
| Encoding Normalization | Normalize inputs to avoid evasions. | `from unicodedata import normalize`<br/>`def normalize_input(input_str): return normalize('NFKC', input_str)` | Bypass filters | A.14.2.5 |
| Special Character Handling | Reject or escape special characters. | `import html`<br/>`def escape_special_chars(user_input): return html.escape(user_input)` | XSS, SQL Injection | A.14.2.5 |
| Server-Side Validation | Do not rely on client-side validation alone. | `def validate_form(data): if not is_valid_length(data.get("username", "")): return False # Add further validation return True` | Client manipulation bypass | A.14.2.5 |

## Output Encoding

| Control Point | Description | Implementation | Risk | ISO 27001 Mapping |
|---|---|---|---|---|
| HTML Encoding | Encode output before rendering to HTML. | `import html`<br/>`def encode_html(data): return html.escape(data)` | Cross-site scripting | A.14.2.5 |
| JavaScript Encoding | Sanitize dynamic data before inserting into JavaScript. | `import json`<br/>`def safe_js_string(data): return json.dumps(data)` | DOM-based XSS | A.14.2.5 |
| URL Encoding | Encode dynamic data in URLs. | `import urllib.parse`<br/>`def encode_url_component(value): return urllib.parse.quote_plus(value)` | Redirect manipulation | A.14.2.5 |
| CSS Encoding | Encode output used within style tags. | `def encode_css_value(value): return value.replace("<", "\\3C ").replace(">", "\\3E ")` | CSS Injection | A.14.2.5 |
| JSON/XML Encoding | Encode values in serialized formats. | `import json`<br/>`def encode_json(data_dict): return json.dumps(data_dict)` | Injection in data transport | A.14.2.5 |

## Session Management

| Control Point | Description | Implementation | Risk | ISO 27001 Mapping |
|---|---|---|---|---|
| Secure Session IDs | Use strong, unpredictable session identifiers. | `import secrets`<br/>`def generate_session_id(): return secrets.token_urlsafe(32)` | Session fixation | A.9.2.1 |
| Session Timeout | Set appropriate session timeout. | `from datetime import datetime, timedelta`<br/>`session_expiry = datetime.now() + timedelta(minutes=15)` | Session hijacking | A.9.4.2 |
| Regenerate Session ID | Change session ID on privilege change. | `def regenerate_session(session): session["id"] = generate_session_id()` | Fixation & impersonation | A.9.4.2 |
| Secure Cookie Flags | Enable HttpOnly and Secure flags. | `from flask import make_response`<br/>`def set_secure_cookie(response, key, value): response.set_cookie(key, value, httponly=True, secure=True)` | Cookie theft | A.10.1.1 |
| Logout Functionality | Provide a logout feature. | `def logout_user(session): session.clear()` | Session reuse | A.9.4.2 |
| Session Binding | Bind session to IP/User-Agent. | `def is_valid_session(request, session): return session["user_agent"] == request.headers.get("User-Agent")` | Session hijack detection | A.9.2.1 |
| Multi-Factor Authentication | Add MFA for sensitive areas. | `import pyotp`<br/>`def verify_otp(secret, token): totp = pyotp.TOTP(secret); return totp.verify(token)` | Credential theft | A.9.4.2 |
| No Session in URL | Avoid session IDs in URL. | Use cookies for session management. | Session leakage | A.9.4.2 |
| Invalid Session Detection | Detect and reject expired sessions. | `def is_session_expired(session_timestamp, timeout_minutes=15): from datetime import datetime, timedelta; return datetime.now() > session_timestamp + timedelta(minutes=timeout_minutes)` | Privilege escalation | A.9.4.2 |
| Secure Session Store | Encrypt session data on server. | Store encrypted sessions in database or memory. | Session tampering | A.10.1.1 |

## Access Control

| Control Point | Description | Implementation | Risk | ISO 27001 Mapping |
|---|---|---|---|---|
| Role-Based Access Control | Grant access based on user roles. | `def has_permission(user, required_role): return required_role in user.get("roles", [])` | Unauthorized access | A.9.1.2 |
| Principle of Least Privilege | Grant minimum access required. | Regularly review user permissions. | Privilege abuse | A.9.1.2 |
| Access Control Lists | Use ACLs to manage permissions. | `ACL = {"admin": ["read", "write"], "user": ["read"]}`<br/>`def can_access(role, action): return action in ACL.get(role, [])` | Improper resource access | A.9.1.2 |
| Authentication Enforcement | Enforce user identity verification. | `import re`<br/>`def is_strong_password(pwd): return re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d).{8,}$', pwd) is not None` | Unauthorized login | A.9.2.1 |
| Authorization Checks | Check privileges before every action. | `def authorize_action(user, action): return action in user.get("permissions", [])` | Function-level access control | A.9.4.1 |
| Disable Unused Accounts | Remove or disable dormant accounts. | `def disable_account(user): user["active"] = False` | Account misuse | A.9.2.6 |
| Account Lockout | Lock account after failed attempts. | `FAILED_ATTEMPTS = {}`<br/>`def should_lock_account(user_id): return FAILED_ATTEMPTS.get(user_id, 0) >= 5` | Brute force attacks | A.9.4.2 |
| Segregation of Duties | Separate critical functions. | Split roles across different users. | Insider threats | A.6.1.2 |
| Audit Logging | Log access control events. | `import logging`<br/>`logging.basicConfig(filename='audit.log', level=logging.INFO)`<br/>`def log_access(user, action): logging.info(f"{user} performed {action}")` | Lack of traceability | A.12.4.1 |
| Time-Based Access | Restrict access by time. | `from datetime import datetime`<br/>`def is_within_access_time(): now = datetime.now().hour; return 9 <= now <= 17` | After-hours exploitation | A.9.1.2 |
| Approval Workflow | Require approval for role changes. | Use automated access request systems. | Privilege escalation | A.9.2.5 |
| Access Review | Review access permissions regularly. | Perform quarterly access reviews. | Permission creep | A.9.2.5 |
| Third-Party Access Control | Manage access for vendors. | `from datetime import datetime, timedelta`<br/>`def create_temp_credentials(expiry_minutes=60): expiry = datetime.now() + timedelta(minutes=expiry_minutes); return {"key": generate_session_id(), "expiry": expiry}` | Supply chain risk | A.15.1.1 |
| No Hardcoded Credentials | Avoid embedding secrets in code. | `import os`<br/>`API_KEY = os.getenv("API_KEY")` | Credential leakage | A.9.2.3 |
| Session Management Enforcement | Tie access to active sessions. | `def enforce_session_access(user, session): return user["id"] == session.get("user_id")` | Unauthorized access | A.9.4.2 |

## Cryptography

| Security Controls | Description | Implementation | Risk | ISO 27001 Mapping |
|---|---|---|---|---|
| Trusted Systems Only | Avoid client-side encryption; use server-side. | `from cryptography.fernet import Fernet; key = Fernet.generate_key(); cipher = Fernet(key); encrypted = cipher.encrypt(b"secret")` | Exposure in browser tools | A.10.1.1 |
| Protect Master Secrets | Restrict access to encryption keys. | Use vaults like AWS KMS, Azure Key Vault | Key exposure = total compromise | A.9.2.3 |
| Fail Securely | Crypto failures should not leak data. | `try: encrypted = cipher.encrypt(b"data") except: abort_operation()` | Info leakage if unhandled | A.12.1.3 |
| Use Approved PRNGs | Use secure RNGs. | `import secrets; token = secrets.token_bytes(32)` | Token forgery | A.10.1.1 |
| FIPS-Compliant Modules | Use AES, SHA-2. | `from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes` | Weak crypto is breakable | A.10.1.1 / A.18.1.4 |
| Key Management Process | Automate key lifecycle. | Use key rotation APIs | Key leaks, reuse | A.10.1.2 |

## Error Handling

| Security Control | Description | Implementation | Risk | ISO 27001 Mapping |
|---|---|---|---|---|
| Generic Error Pages | Avoid exposing system details. | `app.register_error_handler(500, lambda e: render_template('error.html'))` | Reconnaissance | A.13.1.1 |
| No Sensitive Data in Errors | Don't leak credentials or stack traces. | `try: ... except Exception as e: log_error(str(e)); return "Something went wrong"` | Exploit facilitation | A.12.4.1 |
| Log Sanitized Data Only | Prevent logs from becoming attack vectors. | `import html; safe_input = html.escape(user_input)` | XSS in log viewers | A.12.4.1 |
| Restrict Log Access | Make logs read-only. | OS file permissions like chmod 640 | Tampering, privacy issues | A.9.4.5 |
| Auth Attempt Logging | Log all logins, esp. failures. | `logger.info(f"Auth failed for user {user}")` | Missed brute-force attempts | A.12.4.3 |
| Log Integrity | Hash logs to detect tampering. | `hashlib.sha256(log_data.encode()).hexdigest()` | Log forgery | A.10.1.1, A.12.4.2 |
| Admin Action Logging | Track changes to critical configs. | `logger.info(f"Admin changed firewall rule X at {timestamp}")` | Missed privilege escalation | A.12.4.3 |
| Log Access Failures | Track unauthorized access attempts. | `logger.warning(f"Access denied for user {user} on {resource}")` | Escalation visibility | A.9.4.4 |
| Enable Log Analysis | Review logs for anomalies. | Integrate with SIEM or ELK | Incident delay | A.16.1.7 |
| Centralized Logs | Collect logs on trusted servers. | Syslog to collector | Local log loss | A.13.2.1 |

## Data Protection

| Security Control | Description | Implementation | Risk | ISO 27001 Mapping |
|---|---|---|---|---|
| Least Privilege | Grant minimal necessary access. | `if user.role == 'admin': access_admin_panel()` | Escalation risk | 5.18 |
| Protect Temp Data | Secure & delete temp files. | `with open('tmp.txt') as f: ...; os.remove('tmp.txt')` | Data leakage | 8.10 |
| Encrypt Server Data | Use strong crypto for stored data. | `cipher.encrypt(b"password")` | Breach impact | 8.25 |
| Protect Source Code | Avoid public exposure. | Don't expose .py in prod | Reverse engineering | 8.32 |
| No Clear Text on Frontend | No plaintext secrets in JS. | Use SHA256, not MD5 | Credential theft | 8.24 |
| Remove Sensitive Comments | No secrets in code comments. | `# DB_PASSWORD = "admin123"` | Reconnaissance | 5.34 |
| Remove Extra Docs | Don’t publish /docs or README.txt in prod. | Reduce footprint | Info disclosure | 8.1 |
| No Sensitive Info in GET | Avoid credentials in URLs. | Use POST not GET | Log exposure | 8.22 |
| Disable Autocomplete | Prevent browser from storing creds. | `<input type="password" autocomplete="off">` | Credential theft | 8.11 |
| No Client Caching | Avoid caching sensitive data. | `Cache-Control: no-store` | Recovery from browser | 8.10 |
| Secure Deletion | Remove data when not needed. | `del sensitive_data; os.remove()` | Retention risk | 8.11 |
| Access Control for Data | Only authorized roles access files. | `if user.role == 'analyst': allow()` | Data theft | 5.18 |

## Database Security

| Security Control | Description | Implementation | Risk | ISO 27001 Mapping |
|---|---|---|---|---|
| Parameterized Queries | Prevent SQL Injection. | `cursor.execute("SELECT * FROM users WHERE username = %s", (username,))` | Data breach | 8.32 |
| Input & Output Checks | Sanitize and validate all user data. | `re.match(...), html.escape(...)` | XSS/Injection | 8.32 |
| Least Privileged DB Access | Avoid over-permissioned DB users. | `if user.role != 'admin': deny_access()` | Escalation | 5.18 |
| Secure Credentials | Store DB passwords securely. | `os.getenv("DB_PASSWORD")` | Leakage | 8.2 |
| Session Controls | Timeouts and regeneration. | Flask session config | Session hijacking | 8.32 |
| No Verbose Errors | Mask DB connection failures. | `log.error("DB fail")` | Info disclosure | 8.32 |
| Logging & Monitoring | Watch DB access. | `logging.info(...)` | Breach detection | 5.33 |