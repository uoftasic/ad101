# Pitch and loudness

**Question this page answers:** *What do the knobs on a sine wave actually control?*

The held note from the last page — a sine wave — is the simplest interesting signal there is. Almost everything else in this course is built out of sines, so it's worth getting comfortable with its four knobs before moving on.

## The sine wave, one knob at a time

$$
v(t) = A \sin(2\pi f t + \phi) + V_{\mathrm{DC}}
$$

Don't let the formula move faster than your ear would. Each symbol is a knob you could turn on a synthesizer:

| Symbol | Name | Musical intuition | What it means |
|--------|------|--------------------|----------------|
| $A$ | Amplitude | **Loudness** | How far the wave swings from its center (volts) |
| $f$ | Frequency | **Pitch** | How many cycles per second (hertz, Hz) |
| $T = 1/f$ | Period | Length of one "beat" | Duration of one cycle (seconds) |
| $\phi$ | Phase | Where in the beat you start | Horizontal shift — where the wave starts |
| $V_{\mathrm{DC}}$ | DC offset | — (no musical analogy — a mixing desk calls this "bias") | The center line the wave rides on |

Turn the amplitude knob up and the note gets louder without changing pitch. Turn the frequency knob up and the pitch rises without changing loudness. They're independent — that's the whole point of writing them as separate symbols instead of one blob.

![F1 — Sine explorer](../assets/img/f01-sine-explorer.png)

## Two ways to measure "how loud"

- **Peak-to-peak** = $2A$ for a pure sine: the full vertical swing, top of the wiggle to bottom.
- **RMS** ("root mean square") is the signal's *effective* strength — for a sine with no DC offset, $\mathrm{RMS} = A/\sqrt{2} \approx 0.707\,A$. Power delivered into a resistor depends on RMS, not on the peak — which is why your multimeter reports RMS, not amplitude, when you measure an AC voltage.

## Write it yourself: measure your own sine

Extend the script from the last page. This one builds a sine at a chosen amplitude and frequency, then computes its period, peak-to-peak, and RMS straight from the array of numbers — the same way you'd measure a real scope trace by eye, except exact.

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 10_000                         # samples per second
t = np.arange(0, 0.05, 1 / fs)      # 50 ms window

A, f = 1.5, 220.0                   # amplitude (V), frequency (Hz) — the note A3
v = A * np.sin(2 * np.pi * f * t)

period_s = 1 / f
peak_to_peak = v.max() - v.min()
rms = np.sqrt(np.mean(v**2))

print(f"T = {period_s*1e3:.2f} ms   pk-pk = {peak_to_peak:.2f} V   RMS = {rms:.3f} V")

plt.plot(t * 1e3, v)
plt.axvline(period_s * 1e3, color="orange", linestyle="--", label="one period")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.show()
```

Run it, then change `A` and `f` and predict what the printed numbers will do *before* you re-run. If your prediction and the printout disagree, that's the most useful five minutes you'll spend all week — go find out why.

## Why an engineer cares

| Quantity | Everyday use |
|----------|----------------|
| Amplitude vs supply rails | Headroom — will the signal clip? |
| DC offset | Bias / operating point (AD103 will make this precise) |
| Frequency | Bandwidth budgets, sampling rates |
| RMS | The number your multimeter and power calculations actually use |

## Try it

Open [Lab 01 — Signal explorer](labs/lab-01-signal-explorer-overview.md) and drag the sliders on F1 until the readouts match what you predicted from the formulas above.

Next: [A family of waveforms](guide/a-family-of-waveforms.md).
