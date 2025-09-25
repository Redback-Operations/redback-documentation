# A02:2021 – Cryptographic Failures
#  Detects weak hashing algorithms (MD5, SHA1)  
# Flags hardcoded secrets, API keys, and default passwords  
# Warns about unsafe fallback values  
import re

def check(code_lines, add_vulnerability):
    weak_hashes = ["md5", "sha1"]
    sensitive_keywords = ["password", "passwd", "secret", "apikey", "api_key", "token"]

    for i, line in enumerate(code_lines):
        stripped = line.strip()

        # Skip comments
        if stripped.startswith("#"):
            continue

        # Weak crypto usage
        if any(h in stripped.lower() for h in weak_hashes):
            add_vulnerability(
                "A03: Sensitive Data Exposure",
                f"Weak hashing algorithm detected: {stripped}",
                i + 1,
                "HIGH",
                "HIGH"
            )

        # Hardcoded secrets (but ignore env lookups and hashes)
        if any(kw in stripped.lower() for kw in sensitive_keywords) and "=" in stripped:
            if "os.environ" in stripped or "hashlib.sha256" in stripped:
                continue  # safe usage, skip
            add_vulnerability(
                "A03: Sensitive Data Exposure",
                f"Potential hardcoded sensitive data: {stripped}",
                i + 1,
                "HIGH",
                "MEDIUM"
            )
