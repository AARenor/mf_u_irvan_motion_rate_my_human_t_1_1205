"""Write the make.fun bounty entry text to entry.txt.

Standard library only, no network.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "Five stars. He asked me to summarize his day. I wrote: argued with a toaster, "
    "lost. He said add nuance. I wrote: twice."
)


def output_dir() -> Path:
    """Folder to write entry.txt into."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    path = target / "entry.txt"
    path.write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
