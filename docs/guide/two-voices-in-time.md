# Two voices in time

**Question this page answers:** *What happens when two signals don't quite line up?*

Two singers hold the same note, but one comes in a fraction of a beat late. They're at the same pitch and the same loudness — just offset in time. That offset is **phase**, and it shows up everywhere two signals of the same frequency meet: two clock domains, two channels of a stereo signal, two probes on the same scope.

## Phase is delay wearing a costume

$$
t_{\mathrm{delay}} = \frac{\phi}{360^\circ} \cdot T
$$

A phase difference is just a time delay, measured in degrees of one cycle instead of seconds. A $90^\circ$ shift at 100 Hz is a 2.5 ms delay — a quarter of the period, the same way "a quarter note late" means something different at a fast tempo than a slow one.

![F3 — Two-signal comparator](../assets/img/f03-two-signal.png)

## Write it yourself: hear (and see) the offset

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 10_000
t = np.arange(0, 0.02, 1 / fs)
f = 100.0                      # Hz
phase_deg = 90.0                # try 0, 60, 180, 360

voice_a = np.sin(2 * np.pi * f * t)
voice_b = np.sin(2 * np.pi * f * t + np.deg2rad(phase_deg))
together = voice_a + voice_b

delay_ms = (phase_deg / 360.0) * (1000.0 / f)
print(f"delay = {delay_ms:.3f} ms  (period = {1000.0/f:.2f} ms)")

plt.plot(t * 1e3, voice_a, label="voice A")
plt.plot(t * 1e3, voice_b, label="voice B")
plt.plot(t * 1e3, together, label="A + B", linewidth=2)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.show()
```

Sweep `phase_deg` from 0° toward 180° and watch the `A + B` trace: at 0° the two voices reinforce each other (tall), and near 180° they nearly cancel (flat) — the audio equivalent of two speakers wired backwards.

## Why an engineer cares

| Quantity | Everyday use |
|----------|----------------|
| Phase / delay | Timing, synchronization, and why digital timing closure exists |
| Phase at high frequency | Clock skew between two paths that "should" arrive together |
| Phase margin | A preview of stability analysis in AD201 |

## Try it

Open [Lab 01 — Signal explorer](labs/lab-01-signal-explorer-overview.md). On F3, set phase Δ to 90° at 100 Hz and confirm the delay readout matches your prediction from the formula above.

Next: [Adding signals](guide/adding-signals.md) — Movement II, where multiple voices stop being a curiosity and become the main tool for building any waveform you want.
