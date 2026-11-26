#!/usr/bin/env python3
"""The Worst Line an AI Could Say — make.fun entry.

Writes a single pickup line (140 characters or fewer) to
/output/entry.txt. The line is the worst one an AI could plausibly
deliver: flat, over-helpful, faintly ominous.
"""

import os

LINE = "I ran 10,000 simulations of us dating. In 9,997 of them you left. Shall we try the other three?"


def main() -> None:
    # The gate allows 1 to 140 characters; refuse to emit an invalid line.
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"entry line is {len(LINE)} characters, must be 1-140")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
