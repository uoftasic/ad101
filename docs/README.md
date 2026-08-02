# AD101 — Signals

Signals in time and frequency: waveforms, spectra, and Bode plots.

Part of the **UofT ASIC Team** education materials. Published at **https://uoftasic.com/ad101/**. Labs run inside the shared **workspace** (IIC-OSIC-TOOLS) you set up in IC101.

## At a glance

| | |
|---|---|
| **Track** | Analog (intro) |
| **Prerequisites** | [IC101](https://uoftasic.com/ic101/) |
| **Tools** | Python, numpy, matplotlib (inside IIC-OSIC-TOOLS) |
| **Shared workspace** | Yes — clone AD101 under `workspace/modules/` |
| **Math level** | High-school (sine, log, algebra) |

## What you'll do

1. Read a voltage vs time like an oscilloscope (amplitude, frequency, phase, DC)
2. Build complicated waveforms from simple sines — and see their spectra
3. Use the frequency domain to find tones that time plots hide
4. Read a Bode plot and watch an RC filter reshape a square wave

## Path

| Step | Guide | Lab |
|------|--------|-----|
| 0 | [Getting started](guide/getting-started.md) | — |
| 1 | [Signals in time](guide/signals-in-time.md) | [Lab 01](labs/lab-01-signal-explorer-overview.md) |
| 2 | [Building signals](guide/building-signals.md) | [Lab 02](labs/lab-02-harmonic-builder-overview.md) |
| 3 | [The frequency domain](guide/the-frequency-domain.md) | [Lab 03](labs/lab-03-spectrum-detective-overview.md) |
| 4 | [Filters & Bode](guide/filters-and-bode.md) | [Lab 04](labs/lab-04-rc-bode-overview.md) |

Cheat sheets: [Reading plots](reference/reading-plots.md) · [Python in the workbench](reference/python-in-the-workbench.md)

## Quick start

```bash
# inside the noVNC desktop, after IC101
. /foss/designs/common/.designinit
mod ad101
python3 scripts/check_env.py
cd labs/lab-01-signal-explorer && python3 src/explore.py
```

## Local docs preview

```bash
npx docsify-cli serve docs
# → http://localhost:3000
```

## Next courses

- **AD102** — Linear Circuits & Fabrication
- **AD103** — Nonlinear Circuits (XSchem)
- **AD104** — Layout (Magic / Netgen)
