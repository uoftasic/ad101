# Lab 03: Spectrum detective

In this lab you identify signals from their spectra, hunt for a hidden tone, measure THD and watch aliasing happen, using the five explorers F7 to F11.

Work through the lab writeup, [`docs/labs/lab-03-spectrum-detective-overview.md`](../../docs/labs/lab-03-spectrum-detective-overview.md), published at https://uoftasic.com/ad101/labs/lab-03-spectrum-detective-overview.html. That page has the steps and the explanations, and this file is a quick reference to the commands.

## How to run

In a terminal in the IIC-OSIC-TOOLS noVNC desktop:

```bash
mod ad101
cd labs/lab-03-spectrum-detective
```

| Command | What it does |
|---|---|
| `python3 src/explore.py` | Opens F7 to F11 |
| `python3 src/explore.py --figure f7` | Opens one explorer: `f7`, `f8`, `f9`, `f10` or `f11` |
| `python3 src/explore.py --headless` | Writes the figures as PNGs into `results/` instead of opening windows (`--out DIR` to change the folder) |
| `python3 src/check.py --guess <Hz>` | Checks your F8 hidden-tone frequency (accepts ±5 Hz; change with `--tol`) |

## Explorers

| ID | Explorer |
|----|----------|
| F7 | Twin panel: time ↔ frequency for several test signals |
| F8 | Hidden-tone hunt (confirm with `src/check.py`) |
| F9 | Distortion and THD meter |
| F10 | Spectral leakage (optional Part 5) |
| F11 | Sampling and aliasing |

## Files

| Path | Contents |
|---|---|
| `src/explore.py` | Interactive explorers; `--headless` exports PNGs |
| `src/export_figures.py` | Exports F7 to F11 as PNGs; used by `--headless` and `scripts/build_figures.py` |
| `src/check.py` | Hidden-tone checker for F8 |
| `src/_path.py` | Adds `labs/` to `sys.path` so `from common.adsig import ...` works |
| `requirements.txt` | numpy and matplotlib, already inside IIC-OSIC-TOOLS |
| `results/` | Output folder for `--headless` (ignored by git) |
