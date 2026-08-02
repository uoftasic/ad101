#!/usr/bin/env python3
"""Confirm the hidden-tone frequency from F8.

    python3 src/check.py --guess 237
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Keep the secret in one place (explore.py imports the same constant)
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path  # noqa: F401

from explore import HIDDEN_TONE_HZ  # noqa: E402


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Check your F8 hidden-tone guess")
    parser.add_argument("--guess", type=float, required=True, help="Frequency in Hz")
    parser.add_argument(
        "--tol",
        type=float,
        default=5.0,
        help="Acceptable error in Hz (default 5)",
    )
    args = parser.parse_args(argv)

    err = abs(args.guess - HIDDEN_TONE_HZ)
    if err <= args.tol:
        print(f"Correct! Hidden tone is {HIDDEN_TONE_HZ:.0f} Hz (error {err:.1f} Hz).")
        print("You just did what an engineer does with a spectrum analyzer:")
        print("find a coupling / interference tone that the time plot hid.")
        return 0

    print(f"Not quite — {args.guess:.1f} Hz is {err:.1f} Hz away.")
    print("Look again at the spectrum peak above the noise floor in F8.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
