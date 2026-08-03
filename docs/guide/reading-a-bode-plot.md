# Reading a Bode plot

**Question this page answers:** *What am I actually looking at in that two-panel plot?*

A Bode plot is a filter's spec sheet, read the same way you'd read an EQ curve on a mixing console: flat means "unchanged," a downward slope means "getting quieter," and the phase panel tells you how much *later* each frequency arrives.

### Reading the Bode plot

| Feature | Meaning |
|---------|---------|
| Flat region | Passband — signal comes through almost unchanged |
| −3 dB point | Cutoff $f_c$ by definition |
| −20 dB/decade slope | First-order roll-off (×10 in frequency → ÷10 in amplitude) |
| Phase → −90° | High-frequency asymptote for a single RC |

## Gain and phase as a picture in time

A Bode plot is a summary — it's built by testing one frequency at a time. Pick a frequency on the curve, drive the filter with a sine at that frequency, and the output is still a sine, but **smaller** (gain) and **later** (phase). That is literally what a network analyzer measures, one sweep point at a time, to draw the two curves above.

![F13 — Bode linked to time](../assets/img/f13-bode-time.png)

## Write it yourself: measure one point on the Bode curve

```python
import numpy as np
import matplotlib.pyplot as plt

R, C = 1_000.0, 100e-9
fc = 1 / (2 * np.pi * R * C)

fs = 200_000.0
t = np.arange(0, 0.02, 1 / fs)

for test_freq, label in [(fc / 10, "a decade below fc"), (fc, "at fc"), (fc * 10, "a decade above fc")]:
    drive = np.sin(2 * np.pi * test_freq * t)
    mag = 1 / np.sqrt(1 + (test_freq / fc) ** 2)
    phase_rad = -np.arctan(test_freq / fc)
    output = mag * np.sin(2 * np.pi * test_freq * t + phase_rad)

    plt.figure(figsize=(6, 2.5))
    plt.plot(t * 1e3, drive, label="input", alpha=0.6)
    plt.plot(t * 1e3, output, label="output", linewidth=2)
    plt.title(f"{label}: gain={mag:.3f}, phase={np.rad2deg(phase_rad):.1f}°")
    plt.xlabel("Time (ms)")
    plt.legend(fontsize=8)
    plt.xlim(0, 3 / test_freq * 1e3)
    plt.tight_layout()
    plt.show()
```

Three plots, three points on the same Bode curve. At $f_c$, the output should visibly shrink to about 0.707× the input and lag by about an eighth of a cycle (45°) — the single point every Bode plot is anchored to.

## Try it

Open [Lab 04 — RC filter & Bode](labs/lab-04-rc-bode-overview.md). On F13, park the marker at $f_c$, then a decade below, then a decade above, and match what you see to the three plots above.

Next: [Filtering a beat](guide/filtering-a-beat.md).
