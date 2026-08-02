# Lab 03 — Spectrum detective

Identify signals from their spectra, hunt a hidden tone, measure THD, and see aliasing.

## Docs writeup

- Site: `/#/labs/lab-03-spectrum-detective-overview`

## Quick start

```bash
mod ad101
cd labs/lab-03-spectrum-detective
python3 src/explore.py
python3 src/explore.py --figure f8
python3 src/check.py --guess 237
python3 src/explore.py --headless
```

## Figures

| ID | Explorer |
|----|----------|
| F7 | Twin-panel time ↔ frequency recipes |
| F8 | Hidden-tone hunt (+ `check.py`) |
| F9 | Distortion & THD meter |
| F10 | Spectral leakage (stretch) |
| F11 | Sampling & aliasing |
