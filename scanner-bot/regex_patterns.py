PATTERNS = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone_numbers": r"\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b",
    "credit_cards": r"\b(?:\d[ -]*?){13,16}\b",
    "ssns": r"\b\d{3}-\d{2}-\d{4}\b",
    "ips": r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
}
