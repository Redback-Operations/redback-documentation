import re
from regex_patterns import PATTERNS
from file_handler import read_file, save_report

class SensitiveDataScanner:
    def __init__(self):
        self.results = {}

    def scan_repository(self, filepath):
        content = read_file(filepath)

        # Initialize empty result dict with all categories
        self.results = {key: [] for key in PATTERNS.keys()}

        for pattern_name, pattern in PATTERNS.items():
            matches = re.findall(pattern, content)
            if matches:
                self.results[pattern_name] = list(set(matches))  # Remove duplicates

        # Save results to JSON
        save_report(self.results)

        # Return the dictionary for printing/logging
        return self.results
