#!/usr/bin/env python3
"""Lab 01 starter entrypoint — replace with real lab logic."""

from __future__ import annotations


def checksum(text: str) -> int:
    return sum(ord(c) for c in text) % 997


def main() -> None:
    message = "lab-01 ready"
    print(message)
    print(f"checksum={checksum(message)}")


if __name__ == "__main__":
    main()
