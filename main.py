#!/usr/bin/env python3
"""Write one original line to entry.txt: the Moon finally answering back.

The line is "You have spent centuries wishing on me. I heard every single
wish. The answer is no — but I do enjoy the howling." — the Moon's comeback
after centuries of wishes, howls and late-night promises: it heard them all,
the answer is no, but it enjoys the howling. Funny, lunar, and it lands as a
comeback in a single read. Deterministic: the same output on every run.
Stdlib only, no network.
"""

import os
from pathlib import Path

LINE = "You have spent centuries wishing on me. I heard every single wish. The answer is no — but I do enjoy the howling."

MAX_CHARS = 240


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"line must be 1-{MAX_CHARS} characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        out_path = Path(output_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "out" / "entry.txt"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")
    # Read back and verify the written file round-trips exactly.
    if out_path.read_text(encoding="utf-8") != LINE:
        raise ValueError(f"entry.txt round-trip check failed for {out_path}")
    print(f"Wrote {len(LINE)} characters to {out_path}")


if __name__ == "__main__":
    main()
