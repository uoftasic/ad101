# Rhythm and duty cycle

**Question this page answers:** *Does a beat's "on time" change its recipe of sines?*

A metronome that ticks 50/50 — on exactly as long as it's off — is a different rhythm than one that snaps and then rests. A pulse train (a square wave that isn't 50% on / 50% off) is exactly that: the fraction of each cycle spent "on" is its **duty cycle**, and changing it changes which harmonics show up in the recipe.

## Duty cycle reshapes the recipe

At exactly 50% duty, the harmonic recipe from the last page holds: only odd harmonics survive. Move off 50% in either direction and **even** harmonics ($n = 2, 4, 6, \ldots$) come back into the spectrum. That's one reason clock specs care about duty cycle: spectral content drives electromagnetic interference (EMI) — a clock with a clean, symmetric duty cycle radiates a cleaner spectrum than a lopsided one.

![F6 — Duty cycle and spectrum](../assets/img/f06-duty-spectrum.png)

## Write it yourself: sweep the duty cycle

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 10_000
t = np.arange(0, 0.05, 1 / fs)
f0 = 200.0

fig, axes = plt.subplots(1, 3, figsize=(10, 3), sharey=True)
for ax, duty in zip(axes, [0.25, 0.50, 0.75]):
    phase = (f0 * t) % 1.0
    pulse = np.where(phase < duty, 1.0, 0.0)
    spectrum = np.abs(np.fft.rfft(pulse - pulse.mean()))
    freqs = np.fft.rfftfreq(len(pulse), d=1 / fs)
    ax.stem(freqs[:20], spectrum[:20])
    ax.set_title(f"duty = {duty:.0%}")
    ax.set_xlabel("Frequency (Hz)")
plt.tight_layout()
plt.show()
```

(Don't worry about `np.fft.rfft` yet — it's the "count the harmonics for me" machine you'll meet properly in [The FFT as an equalizer](guide/the-fft-as-an-equalizer.md). For now, just watch which stems in the middle panel (50%) go quiet compared to the two side panels.)

## Why an engineer cares

| Observation | Implication |
|-------------|-------------|
| 50% duty kills even harmonics | Cleaner spectrum, less EMI |
| Off-50% duty | Even harmonics return, radiating at those frequencies |
| Clock spec sheets list duty cycle tolerance | Not cosmetic — it's a spectral-cleanliness spec |

## Try it

Open [Lab 02 — Harmonic builder](labs/lab-02-harmonic-builder-overview.md). On F6, sweep duty from 25% → 50% → 75% and watch the even-numbered stems appear and disappear.

Next: [The FFT as an equalizer](guide/the-fft-as-an-equalizer.md) — Movement III, where you get the tool that reads off any signal's recipe automatically instead of building it up by hand.
