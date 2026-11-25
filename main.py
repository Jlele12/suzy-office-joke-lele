#!/usr/bin/env python3
"""
One-Line Office Joke Laugh-Off — 'HR approved this joke. Then resigned.'

Writes one funny one-line office joke into /output/entry.txt.
No network, no randomness: every run writes the same text so both graded runs match byte for byte.
The line lands as a single sentence, stands on its own, and needs no setup or context.
The joke targets a shared office ritual everyone recognises, not any person or group.
"""
import pathlib
import sys


def main() -> int:
    text = (
        "Our company went open-plan so we could all collaborate "
        "on ignoring each other in person.\n"
    )
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
