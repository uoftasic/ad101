# Lab 01: Signal explorer

Interactive matplotlib explorers for waveforms in the time domain (F1–F3).

Follow the lab writeup, [`docs/labs/lab-01-signal-explorer-overview.md`](../../docs/labs/lab-01-signal-explorer-overview.md), published at https://uoftasic.com/ad101/labs/lab-01-signal-explorer-overview.html. This README is a command reference.

## How to run

In a terminal in the IIC-OSIC-TOOLS noVNC desktop:

```bash
mod ad101
cd labs/lab-01-signal-explorer
```

| Command | What it does |
|---|---|
| `python3 src/explore.py` | Opens F1, F2 and F3 |
| `python3 src/explore.py --figure f1` | Opens one explorer: `f1`, `f2` or `f3` |
| `python3 src/explore.py --headless` | Writes the figures as PNGs into `results/` instead of opening windows (`--out DIR` to change the folder) |

## Explorers

| ID | Explorer |
|----|----------|
| F1 | Sine explorer (amplitude, frequency, phase, DC) |
| F2 | Signal zoo (sine / square / triangle / pulse / noise) |
| F3 | Two-signal comparator (phase as delay) |

## Files

| Path | Contents |
|---|---|
| `src/explore.py` | Interactive explorers; `--headless` exports PNGs |
| `src/export_figures.py` | Exports F1, F2 and F3 as PNGs; used by `--headless` and `scripts/build_figures.py` |
| `src/_path.py` | Adds `labs/` to `sys.path` so `from common.adsig import ...` works |
| `requirements.txt` | numpy and matplotlib, already inside IIC-OSIC-TOOLS |
| `results/` | Output folder for `--headless` (ignored by git) |
