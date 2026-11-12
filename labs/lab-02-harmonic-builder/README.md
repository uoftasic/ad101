# Lab 02: Harmonic builder

Build a square wave from sines and watch its spectrum update live (F4–F6).

Follow the lab writeup, [`docs/labs/lab-02-harmonic-builder-overview.md`](../../docs/labs/lab-02-harmonic-builder-overview.md), published at https://uoftasic.com/ad101/#/labs/lab-02-harmonic-builder-overview. This README is a command reference.

## How to run

In a terminal in the IIC-OSIC-TOOLS noVNC desktop:

```bash
mod ad101
cd labs/lab-02-harmonic-builder
```

| Command | What it does |
|---|---|
| `python3 src/explore.py` | Opens F4/F5 and F6 |
| `python3 src/explore.py --figure f4` | Opens one explorer: `f4`, `f5` or `f6` |
| `python3 src/explore.py --headless` | Writes the figures as PNGs into `results/` instead of opening windows (`--out DIR` to change the folder) |

## Explorers

| ID | Explorer |
|----|----------|
| F4 | Fourier assembler (odd harmonics → square) |
| F5 | Live spectrum stem plot, in the same window as F4 (`--figure f4` and `--figure f5` both open it) |
| F6 | Duty cycle ↔ spectrum |

## Files

| Path | Contents |
|---|---|
| `src/explore.py` | Interactive explorers; `--headless` exports PNGs |
| `src/export_figures.py` | Exports F4/F5 and F6 as PNGs; used by `--headless` and `scripts/build_figures.py` |
| `src/_path.py` | Adds `labs/` to `sys.path` so `from common.adsig import ...` works |
| `requirements.txt` | numpy and matplotlib, already inside IIC-OSIC-TOOLS |
| `results/` | Output folder for `--headless` (ignored by git) |
