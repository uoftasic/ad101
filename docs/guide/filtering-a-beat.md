# Filtering a beat

**Question this page answers:** *What does a low-pass filter do to something more interesting than a sine?*

A muffled kick drum through a wall — you still hear the thump, but the sharp attack is gone, smoothed into something rounder and softer. That's a low-pass filter acting on a real, harmonic-rich signal instead of a lone sine, and a square wave is the clearest circuit example of the same effect.

## Square wave through the filter

Remember Movement II: a square wave is a pile of odd harmonics. A low-pass **turns down the high harmonics** — the ones responsible for the sharp edges — so the edges round off. Lower the cutoff further and the square turns into a soft, rounded blob, the electrical equivalent of the muffled kick drum.

![F14 — Square through RC](../assets/img/f14-square-through-rc.png)

## Write it yourself: filter a square wave

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 50_000.0
t = np.arange(0, 0.01, 1 / fs)
f0 = 500.0
square = np.sign(np.sin(2 * np.pi * f0 * t))

def rc_lowpass_filter(x, fs, R, C):
    """Apply an RC low-pass by scaling the spectrum, then transforming back."""
    n = len(x)
    freqs = np.fft.rfftfreq(n, d=1 / fs)
    fc = 1 / (2 * np.pi * R * C)
    mag = 1 / np.sqrt(1 + (freqs / fc) ** 2)
    phase = -np.arctan(freqs / fc)
    H = mag * np.exp(1j * phase)
    X = np.fft.rfft(x)
    return np.fft.irfft(X * H, n=n)

for C in (10e-9, 100e-9, 1e-6):          # progressively lower cutoff
    filtered = rc_lowpass_filter(square, fs, R=1_000.0, C=C)
    fc = 1 / (2 * np.pi * 1_000.0 * C)
    plt.plot(t * 1e3, filtered, label=f"C={C*1e9:.0f} nF (fc≈{fc:.0f} Hz)")

plt.plot(t * 1e3, square, color="gray", linestyle="--", label="input square", alpha=0.5)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.legend(fontsize=8)
plt.show()
```

Raise `C` and watch the edges soften more with each step — exactly the same knob as [Filters are tone knobs](guide/filters-are-tone-knobs.md), just applied to a richer signal instead of a lone sine.

## The engineering punchline

Every node on a chip has **parasitic** resistance and capacitance. Every node is therefore one of these filters, whether you designed it in or not. That's why clock speeds have a ceiling — and a preview of the parasitic-extraction work in AD104.

## Try it

Open [Lab 04 — RC filter & Bode](labs/lab-04-rc-bode-overview.md). On F14, raise C (lowering $f_c$) and compare the input and output harmonics on the stem plot — the high-odd harmonics should visibly shrink first.

Next: [More filter shapes](guide/more-filter-shapes.md).
