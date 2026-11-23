"""One Line, Zero Use: write a single useless-superpower line to /output/entry.txt."""

import os

LINE = "I can stop time for exactly one second, which I use exclusively to reconsider texts I've already sent."


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
