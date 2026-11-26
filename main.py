#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun bounty entry.

Writes one joke about Monday mornings to /output/entry.txt, no longer than
200 characters. Monday called in sick, so Tuesday is covering — same
meetings, worse attitude, and it brought its own spreadsheet.
"""

import os

ENTRY = (
    "Monday called in sick today, so Tuesday is covering \u2014 "
    "same meetings, worse attitude, and it brought its own spreadsheet."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
