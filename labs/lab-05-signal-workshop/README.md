# Lab 05: Signal workshop

A code-along capstone with no slider explorers. You fill in the functions in `src/workshop.py` to synthesize a chord, plot its waveform and spectrum, filter it with an RC low-pass, and export the chord before and after filtering as WAV files.

Follow the lab writeup, [`docs/labs/lab-05-signal-workshop-overview.md`](../../docs/labs/lab-05-signal-workshop-overview.md), published at https://uoftasic.com/ad101/labs/lab-05-signal-workshop-overview.html. This README is a command reference.

## How to run

In a terminal in the IIC-OSIC-TOOLS noVNC desktop:

```bash
mod ad101
cd labs/lab-05-signal-workshop
```

| Command | What it does |
|---|---|
| `python3 src/workshop.py --headless` | Runs your script; saves PNGs and WAVs into `results/` and skips live playback |
| `python3 src/workshop.py` | Full run: plot windows, then live audio if a sound device is available |
| `python3 solutions/workshop_solution.py --headless --out results/solution` | Runs the reference solution into its own folder, so it doesn't overwrite your results |

Until every function is filled in, `src/workshop.py` stops with `NotImplementedError` at the first unfinished one.

## Files

| Path | Contents |
|---|---|
| `src/workshop.py` | The scaffold: seven functions marked TODO, each with a docstring saying what to write |
| `src/_path.py` | Adds `labs/` to `sys.path` so `from common.adsig import ...` works |
| `solutions/workshop_solution.py` | Filled-in reference. Try the exercise yourself first |
| `requirements.txt` | numpy and matplotlib; `sounddevice` and `soundfile` are optional, for live playback |
| `results/` | Output folder: `workshop-waveform.png`, `workshop-spectrum.png`, `workshop-before-after.png`, `chord-unfiltered.wav`, `chord-filtered.wav` (ignored by git) |
