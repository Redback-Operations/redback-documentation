# A08:2021 – Software and Data Integrity Failure
# Flags: eval/exec, unsafe deserialization (pickle), unsafe YAML load, and shell=True

import re

UNSAFE_YAML_RE = re.compile(r'\byaml\.load\s*\(')  # safe form is yaml.safe_load

def check(code_lines, add_vulnerability):
    for i, line in enumerate(code_lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue

        # Dangerous dynamic evaluation
        if "eval(" in stripped or "exec(" in stripped:
            add_vulnerability(
                "A08: Software and Data Integrity Failures",
                f"Use of dangerous dynamic evaluation: {stripped}",
                i + 1,
                "HIGH",
                "HIGH",
            )

        # Unsafe deserialization (pickle)
        if "pickle.load(" in stripped or "pickle.loads(" in stripped:
            add_vulnerability(
                "A08: Software and Data Integrity Failures",
                f"Potential unsafe deserialization via pickle: {stripped}",
                i + 1,
                "HIGH",
                "HIGH",
            )

        # Unsafe YAML load (must be yaml.safe_load)
        if UNSAFE_YAML_RE.search(stripped) and "safe_load" not in stripped:
            add_vulnerability(
                "A08: Software and Data Integrity Failures",
                f"Unsafe YAML load detected; use yaml.safe_load(): {stripped}",
                i + 1,
                "HIGH",
                "MEDIUM",
            )

        # shell=True in subprocess calls
        if "subprocess." in stripped and "shell=True" in stripped:
            add_vulnerability(
                "A08: Software and Data Integrity Failures",
                f"subprocess call with shell=True detected: {stripped}",
                i + 1,
                "HIGH",
                "MEDIUM",
            )
