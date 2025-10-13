# Asset Assessment Scanner – Stakeholder Handover Document
**Ethics Team – Asset Assessment Scanner**  
Prepared by: Belle Mattioli (September 2025)

---

## Purpose
Provide an end-to-end record of what was delivered this trimester, how the scanner works, who owns what, and what remains to finish.

---

## Contents
1. Executive Summary  
2. Objectives & KPIs  
3. Team & Ownership  
4. Individual Contributions  
5. Architecture & Data Flow  
6. CLI & Runbook  
7. Configuration Schemas  
8. Pattern Coverage  
9. Reporting & Redaction  
10. Decisions & Rationale  
11. Forward Plan / Next Steps  
12. Lessons Learned / Retrospective  
13. Glossary  

---

## 1. Executive Summary
The Asset Assessment Scanner helps prevent accidental disclosure of secrets and personal information across repositories.  
It scans targeted file types using curated regex patterns, outputs a human-readable console summary and a machine-readable JSON report, and is designed to support CI/CD policy gates (e.g., fail builds when High-risk issues are detected).  
This document captures scope, individual contributions, technical architecture, configuration schemas, testing status, risks, and the forward plan.

---

## 2. Objectives & KPIs
- Detect and surface high-risk artefacts (keys, tokens, PII early)  
- Provide clear, redacted console output + JSON for automation  
- Enable CI/CD gating (fail on High risk) to stop risky merges  
- Minimise false positives via contextual patterns and (future) checks  

---

## 3. Team & Ownership
- **Stream 1 – CLI & File I/O:** Matthew Franzi  
- **Stream 2 – Regex Scanning Engine:** Harry Coleman  
- **Stream 3 – OCR & Ingestion (prep):** Olivia Nugara  
- **Stream 4 – Reporting & Risk Classification (coordination):** Belle Mattioli  
- **Stream 5 – CI/CD, Testing & Documentation:** Mitchell Tuininga  

---

## 4. Individual Contributions

### Matthew Franzi (Workstream 1 – CLI & File I/O)
- Developed a fast, safe, and reliable command-line tool.  
- Designed it to discover, read, and prepare files from any codebase.  
- Created:
  - `scan.py` – Main entry point that passes arguments for scanning.
  - `file_handler.py` – Handles recursive file discovery and reading.
  - `test_file_handler.py` – Unit testing for discovery and error handling.

### Harry Coleman (Workstream 2 – Regex Scanning Engine)
- Implemented the Regex Scanning Engine that loads detection patterns from `patterns.json`.  
- Built `scan_engine.py` to run patterns over text streams and capture findings.  
- Designed a findings metadata model for consistent results.  
- Added unit tests for multiple match scenarios.  
- Submitted PR merged into the main branch.

### Olivia Nugara (Workstream 3 – OCR & Reprocessing)
- Set up the OCR engine (Tesseract) for reading text from images and PDFs.  
- Added preprocessing steps (straightening, sharpening, noise reduction).  
- Built a script to normalise extracted text.  
- Created a test verifying OCR accuracy on sample images.

### Belle Mattioli (Workstream 4 – Reporting & Risk Classification)
- Provided coordination and leadership of the project.  
- Created initial prototype and authored the workstreams document.  
- Developed `reporter.py` (JSON + console output).  
- Authored `risk_rules.json` (risk levels, remediation tips, compliance references).  
- Collaborated on `scanner.py` and final integration.

### Mitchell Tuininga (Workstream 5 – CI/CD, Testing & Documentation)
- Developed the dummy data generator (`main.py`, `file_generation.py`, `console.py`).  
- Guided and supported the team with debugging and integration.  
- Managed the GitHub repository.  
- Began documenting testing and validation processes.

---

## 5. Architecture & Data Flow
**Pipeline (overview):**  
Inputs → File discovery → Normalisation → Compile patterns → Scan → Risk mapping → Reporting (Console + JSON) → Exit code for CI

**Key Modules:**
- `scanner.py` – Orchestrator/CLI  
- `file_handler.py` – File discovery and reading  
- `reporter.py` – Generates console and JSON reports  
- Dummy data generator – Produces synthetic assets for demos/tests

---

## 6. CLI & Runbook

**Detected CLI flags:**
```
--root          Root directory to scan  
--patterns      Path to patterns.json  
--out           Path to JSON report output  
--ext           File extensions to include (.py, .txt, .md, .cfg, .json)  
--no-console    Skip console summary output  
```

**Example Usage:**
```bash
python scanner.py --root ./ --patterns patterns.json --ext .py .txt .md .cfg .json --out scan_report.json
```

**Exit Codes:**
- `0` = OK  
- `1` = High-risk issues present (used by CI to fail builds)

---

## 7. Configuration Schemas

**patterns.json**
```json
{
  "PATTERN_ID": {
    "pattern": "<regex>",
    "description": "<what it detects>"
  }
}
```

**risk_rules.json**
```json
{
  "PATTERN_ID": {
    "risk": "Low|Medium|High",
    "remediation": "<fix steps>",
    "references": ["APP 11", "ISO 27001 A.5.36", "Essential Eight"]
  }
}
```

---

## 8. Pattern Coverage (Repo-Derived)
20 patterns currently defined in `patterns.json` (AU-aware), including:
- `aws_access_key` – AWS Access Key  
- `tfn` – Australian Tax File Number (TFN)  
- `medicare_number` – Medicare Card Number  
- `credit_card` – Credit Card Number  
- `jwt_secret`, `api_token`, `ssh_private_key`, `email`, etc.  

---

## 9. Reporting & Redaction

**Console Report:**
- Groups findings by risk bucket (High/Low).  
- Redacts sensitive data (`****SECRET****`).  
- Prints totals per group.

**JSON Report:**
- Enriched records including pattern ID, file, line, risk, remediation, and compliance tags.  
- Example:
```json
{
  "pattern": "aws_access_key",
  "file": "infra/deploy.py",
  "line": 42,
  "risk": "High",
  "tip": "Rotate the exposed key, purge from history, and move to a secret manager.",
  "compliance": ["APP 11", "ISO 27001 A.5.36", "Essential Eight"],
  "law": "APP 11",
  "raw": "AKIA****************9XYZ"
}
```

**Safe Handling:**
- Treat JSON reports as sensitive (short TTL, private CI artifacts).  
- Avoid public uploads.

---

## 10. Decisions & Rationale
- Two risk buckets (High/Low) – simplifies CI gating.  
- Console always redacts matches – avoids data leaks.  
- Exit code policy blocks merges on High risk.  
- Rules stored in JSON, not code – enables peer review.

---

## 11. Forward Plan / Next Steps

### Short-Term (Weeks 1–4)
- Stabilise current build, update docstrings, validate outputs.  
- Expand regex coverage (IBAN, EU/US formats).  
- Add checksum validation (TFN, credit cards).  
- Begin integration and unit testing for OCR and reporting.

### Mid-Term (Weeks 5–8)
- Introduce “Medium” risk bucket.  
- Add CI/CD templates for GitHub Actions and GitLab CI.  
- Benchmark scanner performance and explore multiprocessing.

### Long-Term (Weeks 9–12)
- Add HTML/PDF reports and redacted-JSON options.  
- Expand compliance coverage (GDPR, SOC 2, NIST 800-53).  
- Improve OCR and ingestion for poor-quality images.  
- Create stakeholder playbook and contributor guide.

---

## 12. Lessons Learned / Retrospective

### Technical Insights
- Modular architecture worked well for parallel streams.  
- JSON-based rulesets improved governance.  
- Regex limitations caused false positives (future: add checksum).  
- OCR integration successful but needs optimisation.  
- Redaction choices balanced safety and usability.

### Team & Process Insights
- Clear ownership improved focus.  
- Integration points were bottlenecks.  
- Testing coverage uneven—future teams should test alongside code.  
- Peer review was invaluable.  
- Central coordination essential for progress.

### Stakeholder & Project Management Insights
- Early prototype accelerated understanding.  
- Documentation equally important as code.  
- “Block on high” policy worked but needs Medium-level flexibility.  
- Compliance mapping built credibility.  
- Focus on core before stretch goals.

### Overall Reflection
Delivered a functional, compliance-aware scanner with clear modularity and documentation. Future teams should focus on stabilisation, validation, and CI/CD adoption before expanding scope.

---

## 13. Glossary
**Asset Assessment Scanner:** Tool to detect secrets and PII in repositories.  
**Artefacts:** Files/reports generated during scanning.  
**CI/CD:** Continuous Integration/Deployment pipelines.  
**Checksum Validation:** Verification to reduce false positives.  
**Compliance Mapping:** Linking findings to frameworks (APP 11, ISO 27001).  
**Dummy Data Generator:** Creates safe test files.  
**Exit Code:** Scanner return code (0 OK, 1 High risk).  
**OCR:** Optical Character Recognition.  
**Pattern/Regex:** Text-matching rule.  
**PII:** Personally Identifiable Information.  
**Redaction:** Masking sensitive data.  
**Repository:** Code storage (e.g., GitHub).  
**Risk Buckets:** Severity categories (High, Low, Medium planned).  
**Rulesets:** Define patterns and risks (`patterns.json`, `risk_rules.json`).  
**Stakeholders:** Redback Operations, leadership, downstream users.  
**Synthetic Data:** Fake but realistic data for testing.  
**Unit Test:** Validates specific code functions.
