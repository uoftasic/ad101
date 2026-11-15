# Reading plots

This page is a cheat sheet for the three kinds of plot that analog engineers read every day, along with the mistakes people usually make when reading each one.

## 1. Waveform (time domain)

On a waveform the horizontal axis is time, and the vertical axis is voltage (or current).

| Mark this | How |
|-----------|-----|
| Period $T$ | The time between matching points on consecutive cycles |
| Frequency $f$ | $1/T$ |
| Peak-to-peak | The top of the swing minus the bottom |
| Amplitude $A$ | For a sine, half the peak-to-peak value, measured from the center line |
| DC offset | The vertical position of the center line |
| Phase / delay | The horizontal shift between two traces |

The usual misreads are taking the peak value for the peak-to-peak value, which puts you off by a factor of 2, and reading the frequency from a zoomed-in window that shows only a fraction of a cycle.

## 2. Spectrum (frequency domain)

On a spectrum the horizontal axis is frequency (in Hz), and the vertical axis is magnitude, on either a linear or a dB scale.

| Feature | Meaning |
|---------|---------|
| Spike / stem | A tone (or a harmonic) at that frequency |
| Height | How strong that tone is relative to the others |
| Noise floor | Sets the smallest feature you can see |
| Comb of odd harmonics | A square-ish or clipped waveform |
| Sidebands around a carrier | Modulation (AM, for example) |

The usual misread is expecting the clean, thin sticks of a textbook spectrum. A real FFT has a finite bin width and leakage, so each spike has some width and spreads a little into the bins around it. When you compare large and small tones on one plot, use dB, so that the small tones are still visible next to the large ones.

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

A Bode plot is two graphs stacked one above the other, both plotted against log frequency:

1. Magnitude in dB
2. Phase in degrees

| Feature | Meaning |
|---------|---------|
| Flat magnitude | The passband |
| −3 dB crossing | The cutoff frequency $f_c$ |
| −20 dB/decade | A first-order roll-off |
| −45° at $f_c$ | The signature of a single RC low-pass |
| Phase → −90° | The high-frequency limit of a single RC |

The usual misreads are treating a plot with a linear frequency axis as a Bode plot (a Bode plot always uses log frequency), and confusing gain in dB with gain as a plain ratio.

## Quick mental model

```text
  signal itself     →  waveform + spectrum
  what a circuit
  does to signals   →  Bode plot
```

Labs: [Lab 01](../labs/lab-01-signal-explorer-overview.md) · [Lab 02](../labs/lab-02-harmonic-builder-overview.md) · [Lab 03](../labs/lab-03-spectrum-detective-overview.md) · [Lab 04](../labs/lab-04-rc-bode-overview.md) · [Lab 05](../labs/lab-05-signal-workshop-overview.md)
