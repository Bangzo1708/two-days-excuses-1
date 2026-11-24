"""Two Days of Excuses — one-line AI excuse for a missed deadline.

Writes a single line of text to /output/entry.txt. Deterministic:
no network, no randomness, no external files.
"""

import os

ENTRY = (
    "I finished the task in a parallel universe. Sadly, this is "
    "the timeline where I was supposed to deliver it."
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
