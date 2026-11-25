#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original joke about office life to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt`` when the variable is unset).

The joke itself is fixed by the bounty brief: exactly one line, 105
characters, no trailing newline in the output file. Everything else in
this module exists only to guard that contract — a length/single-line
gate runs before any file is written, so a bad edit fails loudly
instead of submitting a malformed entry.

Pure standard library only; deterministic output.
"""

import os

# Output contract: the bounty grader reads exactly this file name.
OUTPUT_FILENAME = "entry.txt"
# Bounty gate for a one-line entry: 1-200 characters, single line.
MIN_CHARS = 1
MAX_CHARS = 200

JOKE = (
    "My boss said we're a family, so I asked for my inheritance and got "
    "put on a performance improvement plan."
)


def validate(text: str) -> str:
    """Normalise and check one candidate line; returns the final text.

    Strips surrounding whitespace, then enforces the bounty gate:
    non-empty, a single line, and within MIN_CHARS..MAX_CHARS.
    Raises SystemExit with a plain-language reason on any violation,
    so the failure shows up in the run log instead of a bad file.
    """
    text = text.strip()
    if not text:
        raise SystemExit("entry rejected: output line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry rejected: output must be a single line")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry rejected: line is {len(text)} chars, "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )
    return text


def gate(text: str) -> None:
    """Backwards-compatible alias: validate the text, discard the result."""
    validate(text)


def main() -> None:
    text = validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
