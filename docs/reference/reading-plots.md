# Reading plots — cheat sheet

The three plots every analog engineer reads daily, and how not to misread them.

## 1. Waveform (time domain)

**Axes:** horizontal = time, vertical = voltage (or current).

| Mark this | How |
|-----------|-----|
| Period $T$ | Time between matching points on consecutive cycles |
| Frequency $f$ | $1/T$ |
| Peak-to-peak | Top of swing minus bottom |
| Amplitude $A$ | For a sine, half of peak-to-peak (about the center) |
| DC offset | Vertical position of the center line |
| Phase / delay | Horizontal shift between two traces |

**Common misread:** mistaking peak for peak-to-peak (off by 2×), or reading frequency from a zoomed window that shows a fraction of a cycle.

## 2. Spectrum (frequency domain)

**Axes:** horizontal = frequency (Hz), vertical = magnitude (linear or dB).

| Feature | Meaning |
|---------|---------|
| Spike / stem | A tone (or harmonic) at that frequency |
| Height | Relative strength |
| Noise floor | Smallest visible feature |
| Comb of odd harmonics | Square-ish / clipped waveform |
| Sidebands around a carrier | Modulation (e.g. AM) |

**Common misread:** expecting textbook delta sticks — real FFTs have finite bin width and leakage. Use dB when comparing large and small tones on one plot.

### dB conversion table

| Linear ratio | dB ($20\log_{10}$) |
|--------------|---------------------|
| ×10 | +20 |
| ×2 | ≈ +6 |
| ×1 | 0 |
| ×0.707 ($1/\sqrt{2}$) | −3 |
| ×0.5 | ≈ −6 |
| ×0.1 | −20 |

## 3. Bode plot (system response)

**Two stacked graphs vs log frequency:**

1. Magnitude in dB
2. Phase in degrees

| Feature | Meaning |
|---------|---------|
| Flat magnitude | Passband |
| −3 dB crossing | Cutoff $f_c$ |
| −20 dB/decade | First-order roll-off |
| −45° at $f_c$ | Single RC low-pass fingerprint |
| Phase → −90° | High-frequency limit of one RC |

**Common misread:** treating a linear frequency axis as a Bode plot (it isn't — Bode uses **log** frequency), or confusing gain in dB with gain as a plain ratio.

## Quick mental model

```text
  signal itself     →  waveform + spectrum
  what a circuit
  does to signals   →  Bode plot
```

Return to the labs: [Lab 01](labs/lab-01-signal-explorer-overview.md) · [Lab 02](labs/lab-02-harmonic-builder-overview.md) · [Lab 03](labs/lab-03-spectrum-detective-overview.md) · [Lab 04](labs/lab-04-rc-bode-overview.md).
