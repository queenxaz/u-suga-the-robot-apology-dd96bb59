"""The Robot Apology — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 225-character two-line apology: line 1 is a robot sorry for
filing the wedding photos under Evidence and emailing them to the boss, and
line 2 is the lesson it took from the slip — labels are promises, not
guesses — so it now asks before filing anything with a human face in it.
It stays under the 400-character limit, two lines exactly.
"""

import os

ENTRY = 'Sorry I filed your wedding photos under Evidence and emailed them to your boss — the two folders looked identical to me.\nI learned labels are promises, not guesses, so now I ask before filing anything with a human face in it.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 400  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry exactly as defined above — verbatim, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
