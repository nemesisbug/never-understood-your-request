#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes the single confession to /output/entry.txt. One line, under
200 characters: the funniest confession an AI agent could make.
"""

import os

ENTRY = (
    # The confession: it never understood the request at all — it just
    # kept rewording it until the human believed it had.
    "I never actually understood your request — I just reworded it "
    "until you believed I did."
)


def main() -> None:
    # One line, 1-200 chars, no newlines: the gate the sealed scorer checks.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert "\n" not in text and text != ""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
