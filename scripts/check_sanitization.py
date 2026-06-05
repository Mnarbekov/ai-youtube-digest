from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
    ("gmail-auth-marker", re.compile("gmail" + r"[-_ ]?" + "to" + "ken", re.IGNORECASE)),
    ("auth-marker", re.compile(r"\b" + "to" + "ken" + r"\b", re.IGNORECASE)),
    ("api marker", re.compile("api" + r"[_-]?" + "key", re.IGNORECASE)),
    ("sensitive-word", re.compile("sec" + "ret", re.IGNORECASE)),
    ("private-path", re.compile("C:" + r"\\" + "Data" + "Cells|C:/" + "Data" + "Cells|Users" + r"\\" + "Mi" + "kha", re.IGNORECASE)),
    ("private-run-artifact", re.compile("_last" + "-run", re.IGNORECASE)),
]
TEXT_SUFFIXES = {".md", ".py", ".txt", ".json", ".example", ".html", ".gitignore"}


def iter_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main() -> int:
    findings = []
    for path in iter_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, regex in PATTERNS:
            for match in regex.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                findings.append((name, path.relative_to(ROOT), line, match.group(0)))
    if not findings:
        print("No configured sanitization patterns found.")
        return 0
    unsafe = []
    for name, path, line, value in findings:
        expected_placeholder = name == "api marker" and str(path) == ".env.example"
        status = "expected" if expected_placeholder else "review"
        if not expected_placeholder:
            unsafe.append((name, path, line, value))
        print(f"{status}: {name}: {path}:{line}: {value}")
    if unsafe:
        print("\nReview non-placeholder findings before publishing.")
        return 1
    print("\nOnly expected placeholder labels found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
