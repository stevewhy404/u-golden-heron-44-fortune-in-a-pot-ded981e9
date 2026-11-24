"""Fortune in a Pot — a kind, funny fortune for a houseplant.

Writes one fortune, a single line of at most 120 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = "You will outgrow this pot, then the sill, then the whole window, and your keeper will still call you his little plant."

assert 1 <= len(LINE) <= 120, f"line must be 1-120 chars, got {len(LINE)}"
assert "\n" not in LINE, "line must be a single line"

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
