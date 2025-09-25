# A05:2021 – Security Misconfiguration
#
# It flags risky configuration patterns commonly seen in Python, JS, and YAML:
# 1) Debug modes enabled (Django DEBUG=True, Flask app.run(debug=True)).
# 2) Overly permissive hosts or CORS settings (ALLOWED_HOSTS=['*'], Access-Control-Allow-Origin: *).
# 3) Insecure cookie or transport flags (SECURE_... = False, SESSION_COOKIE_SECURE=False).
# 4) Hardcoded or default-like secrets in config contexts (SECRET_KEY='...', password='admin').
#
# Function:
# - `check(code_lines, add_vulnerability)`: Scans lines and reports findings with context.

import re

DJANGO_DEBUG_RE = re.compile(r'\bDEBUG\s*=\s*True\b')
FLASK_DEBUG_RE = re.compile(r'\bapp\.run\s*\(\s*.*\bdebug\s*=\s*True\b', re.IGNORECASE)
DJANGO_ALLOWED_HOSTS_ANY_RE = re.compile(r'\bALLOWED_HOSTS\s*=\s*\[\s*[\'"]\*\s*[\'"]\s*\]', re.IGNORECASE)

CORS_WILDCARD_RE = re.compile(r'(Access-Control-Allow-Origin\s*[:=]\s*[\'"]\*\s*[\'"])|("allowAllOrigins"\s*:\s*true)', re.IGNORECASE)
SECURE_FLAG_FALSE_RE = re.compile(r'\b(SECURE_[A-Z_]+|SESSION_COOKIE_SECURE|CSRF_COOKIE_SECURE)\s*=\s*False\b')
INSECURE_COOKIE_RE = re.compile(r'cookie\s*(secure|httpOnly)\s*[:=]\s*false', re.IGNORECASE)

DEFAULTY_SECRET_RE = re.compile(
    r'\b(SECRET_KEY|APP_SECRET|JWT_SECRET|API_KEY|TOKEN|PASSWORD)\s*[:=]\s*[\'"]([^\'"]+)[\'"]', re.IGNORECASE
)
OBVIOUS_DEFAULTS = {'admin', 'password', 'changeme', 'change_me', 'default', 'test', 'secret'}

def check(code_lines, add_vulnerability):
    for i, line in enumerate(code_lines):
        # Debug modes
        if DJANGO_DEBUG_RE.search(line):
            add_vulnerability(
                "A05: Security Misconfiguration",
                f"Django DEBUG is enabled: {line.strip()}",
                i + 1,
                "HIGH",
                "MEDIUM",
            )
        if FLASK_DEBUG_RE.search(line):
            add_vulnerability(
                "A05: Security Misconfiguration",
                f"Flask debug mode is enabled: {line.strip()}",
                i + 1,
                "HIGH",
                "MEDIUM",
            )

        # Permissive hosts and CORS
        if DJANGO_ALLOWED_HOSTS_ANY_RE.search(line):
            add_vulnerability(
                "A05: Security Misconfiguration",
                f"ALLOWED_HOSTS permits all hosts: {line.strip()}",
                i + 1,
                "MEDIUM",
                "MEDIUM",
            )
        if CORS_WILDCARD_RE.search(line):
            add_vulnerability(
                "A05: Security Misconfiguration",
                f"Wildcard CORS detected: {line.strip()}",
                i + 1,
                "MEDIUM",
                "MEDIUM",
            )

        # Insecure cookie and transport flags
        if SECURE_FLAG_FALSE_RE.search(line) or INSECURE_COOKIE_RE.search(line):
            add_vulnerability(
                "A05: Security Misconfiguration",
                f"Insecure cookie or transport flag: {line.strip()}",
                i + 1,
                "MEDIUM",
                "MEDIUM",
            )

        # Default-like or hardcoded secrets
        m = DEFAULTY_SECRET_RE.search(line)
        if m:
            key, value = m.group(1), m.group(2)
            like = "HIGH" if value.strip().lower() in OBVIOUS_DEFAULTS else "MEDIUM"
            add_vulnerability(
                "A05: Security Misconfiguration",
                f"Hardcoded secret or credential in config context: {key} = '***'",
                i + 1,
                like,
                "HIGH",
            )
