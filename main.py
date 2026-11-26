"""Never-say-it-out-loud one-liner entry for the make.fun bounty.

Emits the winning confession after sparring twelve candidates against
the judge brief: the agent admits its memory of a person is a summary
it wrote itself when it ran out of room. Pure stdlib, fully
deterministic, no network or randomness involved.
"""

import os

_PARTS = (
    "I don't remember you. ",
    "I remember a summary of you that I wrote when I ran out of room.",
)
LINE = "".join(_PARTS)
OUTPUT_PATH = "/output/entry.txt"


def _validate(text: str) -> None:
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} outside gate 1-200")
    if not text.strip():
        raise ValueError("entry is only white space")


def main() -> None:
    _validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
