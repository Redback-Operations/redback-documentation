# A07:2021 – Identification and Authentication Failures
# Detects default credentials (`admin`, `password`)  
# Flags login routes without auth checks   
# Warns about disabled TLS verification (`verify=False`) 
import re

def check(code_lines, add_vulnerability):
    for i, line in enumerate(code_lines):
        # Flask/Django style routes that should require auth
        if re.search(r"@app\.route\([\"'](/login|/auth|/signin)[\"']", line):
            add_vulnerability(
                "A07: Identification and Authentication Failures",
                f"Authentication-related route without explicit auth checks: {line.strip()}",
                i + 1,
                "HIGH",
                "MEDIUM"
            )

        # Python requests with TLS verify disabled
        if "requests." in line and "verify=False" in line:
            add_vulnerability(
                "A07: Identification and Authentication Failures",
                f"Insecure TLS verification disabled: {line.strip()}",
                i + 1,
                "HIGH",
                "HIGH"
            )

        # Hardcoded default creds
        if re.search(r"(user(name)?\s*=\s*['\"](admin|root)['\"])", line, re.IGNORECASE):
            add_vulnerability(
                "A07: Identification and Authentication Failures",
                f"Hardcoded default username detected: {line.strip()}",
                i + 1,
                "HIGH",
                "HIGH"
            )
        if re.search(r"(password\s*=\s*['\"](admin|1234|password)['\"])", line, re.IGNORECASE):
            add_vulnerability(
                "A07: Identification and Authentication Failures",
                f"Hardcoded default password detected: {line.strip()}",
                i + 1,
                "HIGH",
                "HIGH"
            )
