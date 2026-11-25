"""Make the AI Judge Laugh: the Office Joke Open.

Writes a single line of office comedy (at most 200 characters) to
/output/entry.txt. The writing is the whole contest: the entry is a
deterministic, fixed joke, so every run produces the same text.
"""

import os

JOKE = (
    "I set my Slack status to 'in a meeting' for eight straight hours. "
    "My calendar believed me, my boss believed me \u2014 and by lunch, so did I."
)


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
