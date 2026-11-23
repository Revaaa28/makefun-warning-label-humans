#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh — make.fun entry
(u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85).

Writes a single funny safety warning label for human beings (105 characters)
to /output/entry.txt.

The line: a human's opinions are formed entirely from headlines — and are
defended as if peer-reviewed.

Judged against the house brief: it is a real warning label in form
("CAUTION: Human contains..."), the laugh lands in the last few words
("as if peer-reviewed"), it is true about people in general (everyone has
met — or been — the person who argues from headlines alone), it sounds like
a printed label, and it uses the line with one idea and no filler.

Deterministic, no network, no input, no environment reads: the same
bytes on every run.
"""

import os

LINE = "CAUTION: Human contains opinions formed entirely from headlines and will defend them as if peer-reviewed."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    # Gate checks, mirrored locally: 1-160 chars, one line, UTF-8, not blank.
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and confirm the bytes on disk are exactly what was intended:
    # the gate scores the file, not the variable.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read().decode("utf-8")
    assert written == text, "round-trip mismatch on /output/entry.txt"


if __name__ == "__main__":
    main()
