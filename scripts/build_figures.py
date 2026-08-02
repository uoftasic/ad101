#!/usr/bin/env python3
"""Export every lab figure into docs/assets/img/ with a seeded RNG.

Usage (from the ad101 repo root):

    python3 scripts/build_figures.py

Figures are deterministic — noise uses RNG_SEED from labs/common/adsig.py
so git diffs stay quiet across rebuilds.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "img"
LABS = [
    "lab-01-signal-explorer",
    "lab-02-harmonic-builder",
    "lab-03-spectrum-detective",
    "lab-04-rc-bode",
]


def load_export(lab_id: str):
    path = ROOT / "labs" / lab_id / "src" / "export_figures.py"
    spec = importlib.util.spec_from_file_location(f"{lab_id}.export", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    # Ensure Agg before any lab imports pyplot
    import matplotlib

    matplotlib.use("Agg")

    written: list[Path] = []
    for lab_id in LABS:
        print(f"--- {lab_id} ---")
        mod = load_export(lab_id)
        paths = mod.export_all(OUT)
        for p in paths:
            print(f"  wrote {p.relative_to(ROOT)}")
            written.append(p)

    print(f"\nExported {len(written)} figure(s) → {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
