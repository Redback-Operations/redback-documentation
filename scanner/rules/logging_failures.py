# A09:2021 – Security Logging and Monitoring Failures
# Flags: printing secrets, bare except with print, and print in login/auth paths

import re

SECRET_WORDS = ("password", "passwd", "secret", "api_key", "apikey", "token")

def check(code_lines, add_vulnerability):
    for i, line in enumerate(code_lines):
        stripped = line.strip()
        low = stripped.lower()

        if stripped.startswith("#"):
            continue

        # Printing potential secrets
        if "print(" in low and any(w in low for w in SECRET_WORDS):
            add_vulnerability(
                "A09: Security Logging and Monitoring Failures",
                f"Possible secret printed to stdout: {stripped}",
                i + 1,
                "MEDIUM",
                "MEDIUM",
            )

        # Bare except printing errors (poor monitoring/alerting)
        if low.startswith("except:") or re.match(r"^except\s+[A-Za-z_][A-Za-z0-9_]*\s+as\s+\w+\s*:\s*$", low):
            # Peek next line(s) for print
            nxt = code_lines[i + 1].strip().lower() if i + 1 < len(code_lines) else ""
            if "print(" in nxt:
                add_vulnerability(
                    "A09: Security Logging and Monitoring Failures",
                    f"Exception handled with print() instead of proper logging/alerting near: {stripped}",
                    i + 1,
                    "MEDIUM",
                    "LOW",
                )

        # Print statements in login/auth contexts (heuristic)
        if ("@app.route('/login'" in low or "@app.route(\"/login\"" in low) and i + 3 < len(code_lines):
            # scan a small window after the route for print usage
            window = " ".join(code_lines[i : i + 5]).lower()
            if "print(" in window:
                add_vulnerability(
                    "A09: Security Logging and Monitoring Failures",
                    "Print used in authentication flow; prefer structured, secure logging.",
                    i + 1,
                    "MEDIUM",
                    "LOW",
                )
