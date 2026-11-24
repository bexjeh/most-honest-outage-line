"""The Most Honest Outage Line - make.fun entry.

Writes a single status page line (at most 160 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "."), UTF-8, no trailing newline.
Deterministic: fixed text, no time, randomness, or network.
"""

import os

LINE = (
    "I can see the main API is returning nothing at all right now. "
    "I cannot check whether your data is safe, and I do not yet "
    "know what broke it."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, "entry line must be 1-160 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
