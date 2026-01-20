# Template for adding new OWASP rule modules
def check(code_lines, add_vulnerability):
    for i, line in enumerate(code_lines):
        if "pattern" in line:  # replace with real logic
            add_vulnerability(
                "Axx: Rule Name",
                f"Description: {line.strip()}",
                i + 1,
                "HIGH",
                "MEDIUM"
            )
