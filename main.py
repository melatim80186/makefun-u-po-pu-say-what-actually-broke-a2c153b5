#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of honest error copy to /output/entry.txt:
the brutal truth about an autosave that saved everything except
the version the user actually wanted. Python stdlib only,
fully deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Your changes were autosaved 47 times. "
    "None of them is the one you want. "
    "Pick the least wrong one and move on."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
