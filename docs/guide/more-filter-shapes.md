# More filter shapes

**Question this page answers:** *Is low-pass the only tone knob there is?*

A three-band EQ has bass, mid, and treble knobs — three different filter shapes, each keeping a different slice of the spectrum. Circuits build the same three shapes out of the same R and C parts, just arranged differently.

![F15 — Filter types](../assets/img/f15-filter-types.png)

| Type | Passes | Blocks | EQ knob it resembles |
|------|--------|--------|------------------------|
| Low-pass | Slow | Fast | Treble cut |
| High-pass | Fast | Slow | Bass cut |
| Band-pass | A middle band | Too slow and too fast | Mid boost / isolate |

AD201 picks these up again as intentional design blocks, not just accidental parasitics.

## Write it yourself: compare the three shapes

```python
import numpy as np
import matplotlib.pyplot as plt

R, C = 1_000.0, 100e-9
fc = 1 / (2 * np.pi * R * C)
f = np.logspace(1, 5, 400)
u = f / fc

lowpass = 1 / np.sqrt(1 + u**2)
highpass = u / np.sqrt(1 + u**2)
Q = 2.0
bandpass = (u / Q) / np.sqrt((1 - u**2) ** 2 + (u / Q) ** 2)

plt.semilogx(f, 20 * np.log10(lowpass), label="low-pass")
plt.semilogx(f, 20 * np.log10(highpass), label="high-pass")
plt.semilogx(f, 20 * np.log10(bandpass), label="band-pass")
plt.axvline(fc, color="gray", linestyle="--", label="fc")
plt.ylim(-40, 5)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.legend()
plt.show()
```

All three curves are built from the exact same `fc` — only the shape of the formula changes which side of it gets kept.

## Try it

Open [Lab 04 — RC filter & Bode](labs/lab-04-rc-bode-overview.md). On F15, overlay low-pass / high-pass / band-pass and move $f_c$ to see how the same cutoff produces three different pass/stop patterns.

## You've built the whole instrument rack

Signal in time (Movement I), signal as a recipe of sines (Movements II–III), and what a circuit does to that recipe (Movement IV) — those are the three plots every analog engineer reads daily. For the hands-on version where you assemble a script that does all three yourself, see [Lab 05 — Signal workshop](labs/lab-05-signal-workshop-overview.md).

## Where to go next

| Next course | What you carry forward |
|-------------|------------------------|
| **AD102** | Passives on silicon — fabricating R, C, L |
| **AD103** | Nonlinear devices (diode, MOSFET) in XSchem |
| **AD104** | Layout parasitics (why every node is an RC) |
| **AD202** | Sampling, ADCs — Nyquist for real |

You now have the three plots. Everything later in the analog track assumes you can read them.
