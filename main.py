"""Write one word to /output/entry.txt: the word grandma would text about AI.

Exactly one word and nothing else: "Al" — grandma's typo for AI, as if
AI were a nice man called Al.
"""

import os

WORD = "Al"


def main():
    assert 1 <= len(WORD) <= 30, len(WORD)
    assert WORD == WORD.strip()
    assert " " not in WORD
    assert "\n" not in WORD
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
