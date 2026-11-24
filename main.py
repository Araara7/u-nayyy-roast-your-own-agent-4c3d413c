#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one line (1-200 chars) roasting the AI agent our own team built
to /output/entry.txt.
"""

import os

ENTRY = "My agent read every bounty brief ever written, yet still asks me 'gas?' before doing the exact thing it was built to do."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
