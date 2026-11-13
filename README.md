# AD101 — Signals

Signals in time and frequency: waveforms, spectra, and Bode plots.

Docs: https://uoftasic.com/ad101/ · Hub: https://edu.uoftasic.com/

Part of the UofT ASIC Team (`uoftasic`) Internal Education Initiative. Prerequisite: [IC101](https://github.com/uoftasic/ic101).

Students should start at the docs site: its home page has the Course path, which lists every reading and lab in order. IC101 sets up the workbench, and [Lab 01](docs/labs/lab-01-signal-explorer-overview.md), Part 1, loads AD101 into it.

## Quick start

```bash
# Clone into the shared workbench modules folder
cd workspace/modules
git clone https://github.com/uoftasic/ad101.git
cd ad101

# Docs preview (host machine, needs Node.js)
npx docsify-cli serve docs
# → http://localhost:3000

# Inside the IIC-OSIC-TOOLS noVNC desktop
. /foss/designs/common/.designinit
mod ad101
python3 scripts/check_env.py
cd labs/lab-01-signal-explorer && python3 src/explore.py
```

## Layout

| Path | On Pages? | Purpose |
|------|-----------|---------|
| `docs/` | Yes | Docsify course site; `docs/README.md` holds the Course path |
| `docs/guide/` | Yes | Guide pages for reading: getting started and Movements I–IV |
| `docs/labs/` | Yes | Lab writeups: every hands-on step, with checks |
| `docs/reference/` | Yes | Plot cheat sheet, music glossary, workbench Python notes |
| `labs/` | No | Interactive matplotlib explorers |
| `scripts/` | No | `check_env.py`, `build_figures.py` |

## Labs

| Lab | Explorers |
|-----|-----------|
| `lab-01-signal-explorer` | F1–F3 time-domain waveforms |
| `lab-02-harmonic-builder` | F4–F6 Fourier / duty cycle |
| `lab-03-spectrum-detective` | F7–F11 spectra, THD, aliasing |
| `lab-04-rc-bode` | F12–F15 Bode / RC filter |
| `lab-05-signal-workshop` | Code-along capstone: write your own chord synthesizer, spectrum plot and filter, then listen to the result |

Regenerate docs PNGs: `python3 scripts/build_figures.py`

## License

[MIT](LICENSE). Copyright UofT ASIC Team / `uoftasic`.
