# Adding signals

**Question this page answers:** *Where do complicated waveforms come from?*

Play three notes on a piano at once and you hear a **chord** — one sound, richer than any single note, but still built from nothing more exotic than three notes added together. Circuits work the same way.

## Superposition — signals add

If $v_1(t)$ and $v_2(t)$ are voltages on the same wire, the wire carries $v_1(t) + v_2(t)$. That's it — no interaction, no multiplication, just addition, sample by sample. Add two sines of different frequencies and the sum can look nothing like either parent, the same way a C-E-G chord sounds like nothing you'd call "a C, an E, or a G" in isolation.

This one fact — that signals on a wire simply add — is already enough to build almost any waveform you'll meet in this course.

## Write it yourself: build a chord

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 10_000
t = np.arange(0, 0.02, 1 / fs)

# a C-major triad: C4, E4, G4 (Hz)
c = np.sin(2 * np.pi * 261.6 * t)
e = np.sin(2 * np.pi * 329.6 * t)
g = np.sin(2 * np.pi * 392.0 * t)

chord = c + e + g

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(7, 5))
axes[0].plot(t * 1e3, c, label="C4", alpha=0.7)
axes[0].plot(t * 1e3, e, label="E4", alpha=0.7)
axes[0].plot(t * 1e3, g, label="G4", alpha=0.7)
axes[0].legend(fontsize=8)
axes[0].set_ylabel("three notes")

axes[1].plot(t * 1e3, chord, color="black")
axes[1].set_ylabel("sum (the chord)")
axes[1].set_xlabel("Time (ms)")
plt.tight_layout()
plt.show()
```

Look at the bottom trace: it's not obviously "three sines" anymore. That's the trap of reading a time plot by eye — the moment you add more than one or two tones together, the shape stops telling you what went into it. You'll fix that blind spot in [Movement III](guide/the-fft-as-an-equalizer.md).

## Why an engineer cares

Every wire on a chip is a superposition point: signal plus supply noise plus coupling from a neighboring trace plus whatever else touches it. "What's actually on this node?" is almost always answered by decomposing a sum back into its parts — which is exactly what the next two pages teach you to do.

## Try it

Nothing to click yet — this page is the setup. The payoff lands on the next page, when you use superposition to build a square wave out of nothing but sines.

Next: [Timbre and harmonics](guide/timbre-and-harmonics.md).
