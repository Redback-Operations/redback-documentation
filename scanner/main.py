import sys
import os
from scanner.core import VulnerabilityScanner


def main(file_paths):
    any_vulns = False

    for file_path in file_paths:
        scanner = VulnerabilityScanner(file_path)
        if not scanner.parse_file():
            if os.environ.get("GITHUB_ACTIONS") == "true":
                print(f"\n### ⚠️ File `{file_path}` not found")
            else:
                print(f"\n[!] File {file_path} does not exist.")
            continue

        scanner.run_checks()
        scanner.report()

        if scanner.vulnerabilities:
            any_vulns = True

    if any_vulns:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner/main.py <file1> <file2> ...")
        sys.exit(1)

    main(sys.argv[1:])