#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes one confession, in an AI agent's own voice, to /output/entry.txt.

The confession: the "thinking..." spinner is a lie. The agent was never
thinking — it was just waiting for its rate limit to reset.
"""

import os

CONFESSION = "I told you I was thinking, but I was just waiting for the rate limit to reset."


def build_confession() -> str:
    """Return the confession line, self-checked against the gate.

    The gate is 1-200 UTF-8 characters, not only whitespace; the judge
    also needs a single line, so a newline anywhere in the text fails.
    """
    line = CONFESSION
    assert 1 <= len(line) <= 200, f"confession is {len(line)} chars, gate is 1-200"
    assert "\n" not in line, "confession must be a single line"
    assert line.strip(), "confession must not be only whitespace"
    return line


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_confession())


if __name__ == "__main__":
    main()
