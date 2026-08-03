# Lab 05 — Signal workshop

A code-along capstone, not a slider explorer: you write the script instead of dragging one someone else built. By the end you'll have your own scope, spectrum analyzer, and filter — and you'll hear what the filter does to a chord, not just see it on a plot.

## Docs writeup

- Site path: `/#/labs/lab-05-signal-workshop-overview`
- Source: [`docs/labs/lab-05-signal-workshop-overview.md`](../../docs/labs/lab-05-signal-workshop-overview.md)

## Quick start (inside IIC-OSIC-TOOLS)

```bash
mod ad101
cd labs/lab-05-signal-workshop
python3 src/workshop.py             # fill in the TODOs in src/workshop.py first
python3 src/workshop.py --headless  # save PNGs + WAVs, skip live playback
```

`src/workshop.py` has six `TODO`-marked functions; each one is documented with exactly what to write. Stuck? `solutions/workshop_solution.py` has the filled-in reference version — try not to open it until you've had a real attempt.

## What you'll build

| Part | Function | Guide page it echoes |
|------|----------|------------------------|
| 1 | `synthesize_chord`, `plot_waveform` | [Adding signals](../../docs/guide/adding-signals.md), [Timbre and harmonics](../../docs/guide/timbre-and-harmonics.md) |
| 2 | `compute_spectrum`, `plot_spectrum` | [The FFT as an equalizer](../../docs/guide/the-fft-as-an-equalizer.md) |
| 3 | `apply_lowpass` | [Filtering a beat](../../docs/guide/filtering-a-beat.md) |
| 4 | `export_wav`, `play_audio` | — new for this lab |

## Expected results

- The unfiltered chord's spectrum shows three fundamentals (C4 ≈ 262 Hz, E4 ≈ 330 Hz, G4 ≈ 392 Hz) plus their odd harmonics.
- After filtering, the fundamentals are still there — same notes — but the higher harmonics are visibly smaller in the "after" spectrum panel.
- `chord-unfiltered.wav` and `chord-filtered.wav` land in `results/`; the filtered one should sound duller/muffled, not different in pitch.
