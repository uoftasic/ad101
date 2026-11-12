# AD101 — Signals

Signals in time and frequency: waveforms, spectra and Bode plots.

AD101 is the first course in the UofT ASIC Team's analog track, published at https://uoftasic.com/ad101/. It's for students who have finished [IC101](https://uoftasic.com/ic101/) and want to read the three plots analog engineers use every day: the waveform (voltage against time), the spectrum (how strong each frequency is) and the Bode plot (what a circuit does to each frequency).

The course uses music as its running example. A signal is a note, a chord is signals added together, timbre is a recipe of harmonics, and a filter is a tone knob. You don't need any musical background.

## Before you start

| | |
|---|---|
| Prerequisite | [IC101](https://uoftasic.com/ic101/): Docker and the IIC-OSIC-TOOLS noVNC desktop working, with the shared `workspace` cloned. The labs run inside that workspace. |
| Math | High-school level: sine, logarithm, basic algebra. No calculus. |
| Tools | Python, numpy and matplotlib, already inside IIC-OSIC-TOOLS |
| Time | About 10 hours: roughly 3 hours of reading and 7.5 hours of labs |

## What you'll learn

1. Read a voltage against time the way you'd read an oscilloscope: amplitude, frequency, phase, DC offset
2. Build complicated waveforms from simple sines, and see their spectra
3. Use the frequency domain to find tones that time plots hide
4. Read a Bode plot and watch an RC filter reshape a square wave
5. Write your own signal-analysis script, and listen to what a filter does to a chord

## Course path

Work down this table in order. **Read** rows are guide pages: concepts, figures and worked examples, with nothing to run. **Do** rows are labs, where you run everything. The times are estimates.

| # | | What | Time |
|---|---|---|---|
| 1 | Read | [Getting started](guide/getting-started.md), then Movement I, a single note: [What is a signal?](guide/what-is-a-signal.md) · [Pitch and loudness](guide/pitch-and-loudness.md) · [A family of waveforms](guide/a-family-of-waveforms.md) · [Two voices in time](guide/two-voices-in-time.md) | 50 min |
| 2 | Do | [Lab 01: Signal explorer](labs/lab-01-signal-explorer-overview.md). Set up AD101, then measure amplitude, period, RMS and phase delay | 1.5 h |
| 3 | Read | Movement II, chords and timbre: [Adding signals](guide/adding-signals.md) · [Timbre and harmonics](guide/timbre-and-harmonics.md) · [Rhythm and duty cycle](guide/rhythm-and-duty-cycle.md) | 30 min |
| 4 | Do | [Lab 02: Harmonic builder](labs/lab-02-harmonic-builder-overview.md). Build a square wave from sines and watch duty cycle change its spectrum | 1 h |
| 5 | Read | Movement III, the mixing board: [The FFT as an equalizer](guide/the-fft-as-an-equalizer.md) · [Finding a quiet note](guide/finding-a-quiet-note.md) · [Distortion and THD](guide/distortion-and-thd.md) · [Sampling fast enough](guide/sampling-fast-enough.md) | 45 min |
| 6 | Do | [Lab 03: Spectrum detective](labs/lab-03-spectrum-detective-overview.md). Find a hidden tone, measure THD and make a tone alias | 1.5 h |
| 7 | Read | Movement IV, tone controls: [Filters are tone knobs](guide/filters-are-tone-knobs.md) · [Reading a Bode plot](guide/reading-a-bode-plot.md) · [Filtering a beat](guide/filtering-a-beat.md) · [More filter shapes](guide/more-filter-shapes.md) | 45 min |
| 8 | Do | [Lab 04: RC filter and Bode](labs/lab-04-rc-bode-overview.md). Sweep an RC low-pass and filter a square wave | 1.5 h |
| 9 | Do | [Lab 05: Signal workshop](labs/lab-05-signal-workshop-overview.md). Write your own chord synthesizer, spectrum plot and filter, then listen to the result | 2 h |

Three reference pages are worth keeping open while you work: [Reading plots](reference/reading-plots.md) is a cheat sheet for the three plots, [Music and signals](reference/music-and-signals.md) translates each musical term and lists note frequencies, and [Python in the workbench](reference/python-in-the-workbench.md) covers running the labs and what to do when a plot window won't open.

## After AD101

- [AD102](https://uoftasic.com/ad102/): Linear Circuits & Fabrication
- AD103: Nonlinear Circuits (XSchem)
- AD104: Layout (Magic / Netgen)
