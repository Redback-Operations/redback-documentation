# A01:2021 – Broken Access Control
#
# It looks for common patterns that suggest missing or weak authorization checks:
# 1) Flask routes without an auth/role decorator (e.g., @login_required, @jwt_required).
# 2) Django REST Framework endpoints that explicitly allow unauthenticated access
#    (e.g., permission_classes = [AllowAny]).
# 3) Express.js routes that attach a handler directly with no middleware
#    (e.g., app.get('/admin', (req, res) => ...)) which often implies no auth check.
#
# Function:
# - `check(code_lines, add_vulnerability)`: Scans lines and reports findings with context.

import re

AUTH_DECORATOR_RE = re.compile(
    r'@(login_required|jwt_required|roles_required|requires_auth|auth_required|permission_required)',
    re.IGNORECASE,
)
FLASK_ROUTE_RE = re.compile(r'@(?:\w+\.)?route\s*\(', re.IGNORECASE)
DEF_RE = re.compile(r'^\s*def\s+\w+\s*\(', re.IGNORECASE)

DRF_ALLOWANY_RE = re.compile(r'permission_classes\s*=\s*\[\s*AllowAny\s*\]')
DRF_IMPORT_ALLOWANY_RE = re.compile(r'from\s+rest_framework\.permissions\s+import\s+.*AllowAny', re.IGNORECASE)

# app.get('/path', handler) or router.post("/path", handler)
# If there is a direct callback right after the path, there is probably no middleware.
EXPRESS_ROUTE_RE = re.compile(
    r'\b(?:app|router)\.(get|post|put|patch|delete|options|head)\s*\(\s*[\'"][^\'"]+[\'"]\s*,\s*(?:function|\()',
    re.IGNORECASE,
)

def check(code_lines, add_vulnerability):
    # Track whether DRF AllowAny is imported to increase confidence
    drf_allowany_seen = any(DRF_IMPORT_ALLOWANY_RE.search(line) for line in code_lines)

    # -------- Flask route without auth decorator ----------
    i = 0
    while i < len(code_lines):
        line = code_lines[i]
        if FLASK_ROUTE_RE.search(line):
            # Collect decorators until we hit the function def line
            decorators = []
            j = i
            while j + 1 < len(code_lines) and not DEF_RE.search(code_lines[j + 1]):
                j += 1
                if code_lines[j].lstrip().startswith('@'):
                    decorators.append(code_lines[j].strip())

            # If next line is a function def, evaluate decorators
            if j + 1 < len(code_lines) and DEF_RE.search(code_lines[j + 1]):
                has_auth = any(AUTH_DECORATOR_RE.search(d) for d in decorators)
                # Heuristic: mark as High likelihood if path looks sensitive
                path_hint = ""
                m = re.search(r'route\s*\(\s*[\'"]([^\'"]+)', line, re.IGNORECASE)
                if m:
                    path_hint = m.group(1)

                if not has_auth:
                    sev_like = "HIGH" if re.search(r'/?(admin|settings|manage|delete|update|user|account)', path_hint, re.IGNORECASE) else "MEDIUM"
                    add_vulnerability(
                        "A02: Broken Access Control",
                        f"Flask route appears without an auth decorator: {line.strip()}",
                        i + 1,
                        sev_like,
                        "HIGH",
                    )
                i = j + 1
            else:
                i += 1
        else:
            i += 1

    # -------- DRF AllowAny on views / viewsets ----------
    for idx, line in enumerate(code_lines):
        if DRF_ALLOWANY_RE.search(line):
            like = "HIGH" if drf_allowany_seen else "MEDIUM"
            add_vulnerability(
                "A02: Broken Access Control",
                f"DRF endpoint allows unauthenticated access with AllowAny: {line.strip()}",
                idx + 1,
                like,
                "HIGH",
            )

    # -------- Express routes without middleware ----------
    for idx, line in enumerate(code_lines):
        if EXPRESS_ROUTE_RE.search(line):
            add_vulnerability(
                "A02: Broken Access Control",
                f"Express route handler attached without visible auth middleware: {line.strip()}",
                idx + 1,
                "MEDIUM",
                "HIGH",
            )
