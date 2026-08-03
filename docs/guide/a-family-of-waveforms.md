# A family of waveforms

**Question this page answers:** *Does every signal look like a sine?*

No. A sine is one instrument in a whole family. A flute, a snare drum, and radio static all make sound, but they don't share a waveform — and neither do the signals inside a chip.

## Four more shapes worth knowing by sight

| Shape | Where you'll meet it | What it looks like |
|-------|------------------------|----------------------|
| **Square** | Digital clocks | Snaps between two levels, no in-between |
| **Triangle** | ADC ramps, test signals | Straight-line rise, straight-line fall |
| **Pulse** | Digital clocks with a tunable on-time (**duty cycle**) | A square that spends more time low than high, or vice versa |
| **Noise** | Sensor readouts, thermal noise floor | Never repeats — no period at all |

![F2 — Signal zoo](../assets/img/f02-signal-zoo.png)

Same peak-to-peak amplitude, four completely different shapes. That's the limitation of eyeballing "how tall" a trace is: two waveforms can look the same height on a datasheet spec and still carry completely different information.

## Write it yourself: build the zoo

You already know how to build a sine. The other three shapes come from the same time array `t`, just combined differently:

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 10_000
t = np.arange(0, 0.02, 1 / fs)     # 20 ms window
f = 200.0                          # Hz

sine = np.sin(2 * np.pi * f * t)

# phase goes 0 -> 1 once per cycle; comparing it to a threshold builds
# square, pulse, and triangle without any new math
phase = (f * t) % 1.0

square = np.where(phase < 0.5, 1.0, -1.0)          # snap high/low at the halfway point
pulse = np.where(phase < 0.25, 1.0, 0.0)           # on 25% of the cycle (duty = 0.25)
triangle = np.where(phase < 0.5, -1 + 4 * phase, 3 - 4 * phase)   # ramp up, ramp down
noise = 0.3 * np.random.default_rng(0).standard_normal(len(t))

fig, axes = plt.subplots(4, 1, sharex=True, figsize=(7, 6))
for ax, y, name in zip(axes, [square, pulse, triangle, noise], ["square", "pulse (25%)", "triangle", "noise"]):
    ax.plot(t * 1e3, y)
    ax.set_ylabel(name, fontsize=9)
axes[-1].set_xlabel("Time (ms)")
plt.tight_layout()
plt.show()
```

Try changing the `0.25` in `pulse` to `0.5` and `0.75` and watch the on-time shift. That single number is the **duty cycle** — you'll meet it again in [Rhythm and duty cycle](guide/rhythm-and-duty-cycle.md).

## Why an engineer cares

- Clocks are **squares**.
- ADC ramps are **triangles**.
- That noise trace is the **thermal noise floor** — the smallest signal a chip can resolve above its own randomness.

## Try it

Open [Lab 01 — Signal explorer](labs/lab-01-signal-explorer-overview.md) and click through sine / square / triangle / pulse / noise on F2. Sweep the duty slider and watch the shape lean.

Next: [Two voices in time](guide/two-voices-in-time.md).
