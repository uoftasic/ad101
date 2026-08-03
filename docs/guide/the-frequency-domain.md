# The frequency domain

**Question this page answers:** *What can I see here that I couldn't see in time?*

## The FFT as a machine (not a proof)

Treat the **Fast Fourier Transform (FFT)** as a black box:

```text
  time waveform  ──FFT──►  spectrum (amplitudes vs frequency)
```

You do not need the derivation to use it. Lab 03 runs `numpy.fft.rfft` for you and plots the result.

![F7 — Twin panel](../assets/img/f07-twin-panel.png)

### How to read a spectrum

| Look for | Meaning |
|----------|---------|
| Where peaks sit | Frequencies present in the signal |
| How tall peaks are | Relative strength of each tone |
| The noise floor | Smallest features you can still see |
| Harmonic combs | Distortion, clocks, square-ish shapes |

## Decibels — why the axis is logarithmic

Human ears and RF engineers both like ratios. The **decibel** for amplitude is:

$$
\mathrm{dB} = 20\log_{10}\!\left(\frac{A}{A_{\mathrm{ref}}}\right)
$$

Useful intuition (memorize these):

| Linear ratio | dB |
|--------------|-----|
| ×2 | ≈ +6 dB |
| ×10 | +20 dB |
| ×0.5 | ≈ −6 dB |
| ×0.1 | −20 dB |
| $1/\sqrt{2} \approx 0.707$ | −3 dB |

A log axis lets a huge and a tiny tone share one plot without the tiny one disappearing into the baseline.

## The tone buried in noise

This is the slide that justifies the whole course. A small sine sitting under loud noise is **invisible** on a scope and **obvious** as a spike on a spectrum.

![F8 — Hidden tone](../assets/img/f08-hidden-tone.png)

Finding coupling, 60 Hz hum, or a clock feeding into a sensitive node is exactly this skill.

## Distortion grows new frequencies

Push a clean sine through a soft nonlinearity ($\tanh$) and **new harmonics appear**. The **total harmonic distortion (THD)** summarizes how much energy leaked into those extras:

$$
\mathrm{THD} = \frac{\sqrt{A_2^2 + A_3^2 + \cdots}}{A_1}
$$

![F9 — THD](../assets/img/f09-thd.png)

Every amplifier datasheet quotes a linearity / THD number. AD103's MOSFET curves and AD201's amplifiers make this precise.

## Sampling and aliasing (short)

Measure a tone too slowly and a fast sine masquerades as a slow one — the **wagon-wheel** effect. The rule:

$$
f_{\mathrm{sample}} > 2\, f_{\mathrm{max}}
\qquad\text{(Nyquist)}
$$

![F11 — Aliasing](../assets/img/f11-aliasing.png)

That is why ADC sample rates are chosen carefully — a teaser for AD202 (mixed signal).

> **Stretch:** [F10](labs/lab-03-spectrum-detective-overview.md) shows **spectral leakage** — a non-integer number of cycles in the analysis window smears a clean spike. Window functions (Hann) help.

## Try it

Open [Lab 03 — Spectrum detective](labs/lab-03-spectrum-detective-overview.md). Hunt the hidden tone in F8 and confirm with `check.py`.

Next: [Filters & Bode](guide/filters-and-bode.md).
