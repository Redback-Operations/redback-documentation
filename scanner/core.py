import os
import importlib
import pkgutil
import scanner.rules as rules_pkg


# -------- Rule auto-discovery --------
def _load_rule_modules():
    modules = []
    for _, modname, _ in pkgutil.iter_modules(rules_pkg.__path__):
        if modname.startswith("_"):
            continue  # skip __init__, _template, etc.
        mod = importlib.import_module(f"{rules_pkg.__name__}.{modname}")
        if hasattr(mod, "check"):
            modules.append(mod)

    def key(m):
        cat = getattr(m, "CATEGORY", "")
        head = cat.split(":", 1)[0].strip() if cat else ""
        return (0, int(head[1:])) if head.startswith("A") and head[1:].isdigit() else (1, m.__name__)

    return sorted(modules, key=key)


RULE_MODULES = _load_rule_modules()


# -------- Scanner --------
class VulnerabilityScanner:
    def __init__(self, file_path):
        self.file_path = file_path
        self.code_lines = []
        self.vulnerabilities = []

    def add_vulnerability(self, category, description, line, severity, confidence):
        self.vulnerabilities.append(
            {
                "category": category,
                "description": description,
                "line": line,
                "severity": severity,
                "confidence": confidence,
            }
        )

    def parse_file(self):
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return False
        with open(self.file_path, "r", encoding="utf-8") as f:
            self.code_lines = f.readlines()
        return True

    def run_checks(self):
        for rule in RULE_MODULES:
            rule.check(self.code_lines, self.add_vulnerability)

    def run(self):
        if not self.parse_file():
            return
        self.run_checks()

    def report(self):
        """Outputs results with colors locally, or clean Markdown when in GitHub Actions."""
        def supports_truecolor() -> bool:
            return os.environ.get("COLORTERM", "").lower() in ("truecolor", "24bit")

        disable_color = os.environ.get("GITHUB_ACTIONS") == "true"

        def rgb(r, g, b) -> str:
            return f"\033[38;2;{r};{g};{b}m"

        ANSI = {
            "reset": "" if disable_color else "\033[0m",
            "bold": "" if disable_color else "\033[1m",
            "cyan": "" if disable_color else "\033[96m",
            "magenta": "" if disable_color else "\033[95m",
            "yellow": "" if disable_color else "\033[93m",
            "red": "" if disable_color else "\033[91m",
            "green": "" if disable_color else "\033[92m",
            "blue": "" if disable_color else "\033[94m",
        }

        TRUECOLOR = supports_truecolor() and not disable_color

        sev_color = {
            "CRITICAL": "**CRITICAL**" if disable_color else (rgb(220, 20, 60) if TRUECOLOR else ANSI["red"] + ANSI["bold"]),
            "HIGH": "**HIGH**" if disable_color else (rgb(255, 0, 0) if TRUECOLOR else ANSI["red"]),
            "MEDIUM": "**MEDIUM**" if disable_color else (rgb(255, 165, 0) if TRUECOLOR else ANSI["yellow"]),
            "LOW": "**LOW**" if disable_color else (rgb(0, 200, 0) if TRUECOLOR else ANSI["green"]),
        }

        # ---- Print header ----
        if disable_color:
            print(f"\n### 🔒 OWASP Scanner Results for `{self.file_path}`")
        else:
            print(f"\n{ANSI['bold']}{ANSI['cyan']}Scan Results for {self.file_path}:{ANSI['reset']}")

        if not self.vulnerabilities:
            msg = "✅ No vulnerabilities found."
            print(msg)
            return

        # ---- Group by category ----
        groups = {}
        for v in self.vulnerabilities:
            groups.setdefault(v["category"], []).append(v)

        def cat_key(cat: str):
            head = cat.split(":", 1)[0].strip()
            return (0, int(head[1:])) if head.startswith("A") and head[1:].isdigit() else (1, cat.lower())

        for cat in sorted(groups.keys(), key=cat_key):
            items = sorted(groups[cat], key=lambda x: x["line"])
            sev_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
            for v in items:
                sev_counts[v["severity"]] += 1

            if disable_color:
                print(f"\n#### {cat} ({len(items)} findings)")
                chips = []
                for k in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
                    if sev_counts[k]:
                        chips.append(f"{k}: {sev_counts[k]}")
                if chips:
                    print(f"**Summary:** " + ", ".join(chips))
            else:
                print(f"\n{ANSI['bold']}{ANSI['magenta']}=== {cat} ({len(items)} findings) ==={ANSI['reset']}")

            # ---- List individual vulnerabilities ----
            for v in items:
                sev = sev_color.get(v["severity"], v["severity"])
                if disable_color:
                    print(f"- Line {v['line']} | Severity {sev} | Confidence {v['confidence']}")
                    print(f"  → {v['description']}")
                else:
                    print(f"  {ANSI['bold']}• Line {v['line']} |{ANSI['reset']} "
                          f"Severity {sev}{ANSI['reset']} | "
                          f"Confidence {v['confidence']}")
                    print(f"    → {v['description']}")