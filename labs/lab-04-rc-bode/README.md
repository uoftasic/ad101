# Lab 04: RC filter and Bode

You draw Bode plots of an RC low-pass filter and link each one to what the filter does to a signal in time (explorers F12–F15).

The steps and questions are in the lab writeup, [`docs/labs/lab-04-rc-bode-overview.md`](../../docs/labs/lab-04-rc-bode-overview.md), published at https://uoftasic.com/ad101/labs/lab-04-rc-bode-overview.html. This README only lists the commands and files, so work from the writeup.

## How to run

In a terminal in the IIC-OSIC-TOOLS noVNC desktop:

```bash
mod ad101
cd labs/lab-04-rc-bode
```

| Command | What it does |
|---|---|
| `python3 src/explore.py` | Opens F12 to F15 |
| `python3 src/explore.py --figure f12` | Opens one explorer: `f12`, `f13`, `f14` or `f15` |
| `python3 src/explore.py --headless` | Writes the figures as PNGs into `results/` instead of opening windows (`--out DIR` to change the folder) |

## Explorers

| ID | Explorer |
|----|----------|
| F12 | Bode explorer (R, C → magnitude and phase) |
| F13 | Bode marker linked to the input and output sines |
| F14 | Square wave through the RC |
| F15 | Low-pass / high-pass / band-pass overlay |

## Files

| Path | Contents |
|---|---|
| `src/explore.py` | Interactive explorers; `--headless` exports PNGs |
| `src/export_figures.py` | Exports F12 to F15 as PNGs; used by `--headless` and `scripts/build_figures.py` |
| `src/_path.py` | Adds `labs/` to `sys.path` so `from common.adsig import ...` works |
| `requirements.txt` | numpy and matplotlib, already inside IIC-OSIC-TOOLS |
| `results/` | Output folder for `--headless` (ignored by git) |
