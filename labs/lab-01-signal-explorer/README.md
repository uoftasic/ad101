# Lab 01 — Signal explorer

Interactive matplotlib explorers for waveforms in the **time domain**.

## Docs writeup

- Site path: `/#/labs/lab-01-signal-explorer-overview`
- Source: [`docs/labs/lab-01-signal-explorer-overview.md`](../../docs/labs/lab-01-signal-explorer-overview.md)

## Quick start (inside IIC-OSIC-TOOLS)

```bash
mod ad101
cd labs/lab-01-signal-explorer
python3 src/explore.py          # opens F1, F2, F3
python3 src/explore.py --figure f1
python3 src/explore.py --headless
```

## Figures

| ID | Explorer |
|----|----------|
| F1 | Sine explorer (amplitude, frequency, phase, DC) |
| F2 | Signal zoo (sine / square / triangle / pulse / noise) |
| F3 | Two-signal comparator (phase as delay) |
