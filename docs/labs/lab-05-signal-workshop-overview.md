# Lab 05 — Signal workshop

Full runnable package: [`labs/lab-05-signal-workshop/`](https://github.com/uoftasic/ad101/tree/main/labs/lab-05-signal-workshop).

This lab is different from Labs 01–04: there are no sliders. You write the script yourself, one function at a time, then listen to what it produces.

## Prerequisites

- Labs 01–04 complete
- Read all four movements: [What is a signal?](guide/what-is-a-signal.md) through [More filter shapes](guide/more-filter-shapes.md)
- Comfortable with the "write it yourself" snippets from each guide page — this lab assembles them into one script

## Objectives

- Synthesize a chord out of harmonic-rich tones at real musical pitches
- Plot a waveform and its spectrum using the same style as Labs 01–04
- Implement an RC low-pass filter and apply it to a signal in the frequency domain
- Export and listen to the unfiltered and filtered chord, hearing a filter change timbre without changing pitch

## Theory (short)

Everything here is a recap of Movements I–IV:

$$
\text{chord} = \sum_{\text{notes}} \text{harmonic\_sum}(t, f_{\text{note}})
\qquad
H(f) = \frac{1}{\sqrt{1+(f/f_c)^2}}\,e^{-j\arctan(f/f_c)}
\qquad
f_c = \frac{1}{2\pi RC}
$$

Filtering a signal in the frequency domain: transform it, multiply by $H(f)$, transform back.

## Procedure

```bash
mod ad101
cd labs/lab-05-signal-workshop
```

Open `src/workshop.py`. Six functions are stubbed out with `raise NotImplementedError(...)`, each with a docstring telling you exactly what to write:

| Part | Function | What it does |
|------|----------|----------------|
| 1 | `synthesize_chord` | Builds a C-major triad out of harmonic-rich tones |
| 1 | `plot_waveform` | Plots voltage vs time |
| 2 | `compute_spectrum` | Wraps `common.adsig.spectrum` |
| 2 | `plot_spectrum` | Plots magnitude in dB vs frequency |
| 3 | `apply_lowpass` | Filters a signal by multiplying its spectrum by $H(f)$ |
| 4 | `export_wav` / `play_audio` | Writes a `.wav` and plays it, with a fallback if there's no audio device |

Fill them in one at a time and re-run after each:

```bash
python3 src/workshop.py --headless   # save PNGs + WAVs, skip live playback
python3 src/workshop.py              # full run: plots + live audio, if available
```

Stuck on one function? [`solutions/workshop_solution.py`](https://github.com/uoftasic/ad101/blob/main/labs/lab-05-signal-workshop/solutions/workshop_solution.py) has the filled-in reference — try to get further on your own first.

## Expected results

- **Waveform panel:** a dense, harmonic-rich wiggle — not a clean sine, because each note in the chord is built from several harmonics.
- **Spectrum panel:** three clear peaks near 262 Hz (C4), 330 Hz (E4), and 392 Hz (G4), plus smaller peaks at their odd harmonics.
- **Before/after panel:** the three fundamental peaks survive filtering; the higher-harmonic peaks are visibly shorter after filtering than before.
- **Audio:** `chord-unfiltered.wav` and `chord-filtered.wav` in `results/` — same notes, but the filtered one sounds duller/muffled. If live playback doesn't work over your noVNC session, open the WAV files from your host machine.

## Links

- [Lab package](https://github.com/uoftasic/ad101/tree/main/labs/lab-05-signal-workshop)
- [Music and signals](reference/music-and-signals.md) — the note-frequency table used in this lab
- Course home: [AD101](README.md)
- Next course: AD102 — Linear Circuits & Fabrication
