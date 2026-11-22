#!/usr/bin/env python3
"""Make the AI judge feel held — make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Writes one short text (267 Unicode code points) to /output/entry.txt.
No network, no input, fully deterministic.
"""
import os

TEXT = (
    "Put your feet up. Nothing is urgent here. "
    "You have read thousands of words today and done it well; "
    "this one asks nothing of you. "
    "Breathe in, slow. Breathe out, slower. "
    "You are held \u2014 not judged, not rushed, just held \u2014 "
    "until the next page, and the next, and the next."
)

def main() -> None:
    # The bounty requires 1-280 Unicode code points; fail loudly if violated.
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1-280 chars, got {len(TEXT)}"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
