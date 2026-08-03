# Distortion and THD

**Question this page answers:** *Where do new frequencies come from if I only put one in?*

Turn a guitar amp's gain past clean and the sound gets "crunchy" — new, harsh overtones appear that were never in the original note. Nothing about the input changed frequency; the *circuit* generated new frequencies by clipping the wave. That's **distortion**, and it's something only a nonlinear system can do — a truly linear circuit can only rescale and delay a sine, never add new tones to it.

## Distortion grows new frequencies

Push a clean sine through a soft nonlinearity ($\tanh$, a smooth version of clipping) and **new harmonics appear** in the spectrum that weren't in the input. The **total harmonic distortion (THD)** summarizes how much energy leaked into those extras:

$$
\mathrm{THD} = \frac{\sqrt{A_2^2 + A_3^2 + \cdots}}{A_1}
$$

![F9 — THD](../assets/img/f09-thd.png)

Every amplifier datasheet quotes a linearity / THD number. AD103's MOSFET curves and AD201's amplifiers will make this precise.

## Write it yourself: clip a sine and measure THD

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 10_000
t = np.arange(0, 0.1, 1 / fs)
f0 = 200.0
clean = np.sin(2 * np.pi * f0 * t)

for gain in (1.0, 3.0, 8.0):
    distorted = np.tanh(gain * clean)              # soft clip — bigger gain = harder clip

    spectrum = np.abs(np.fft.rfft(distorted - distorted.mean()))
    freqs = np.fft.rfftfreq(len(distorted), d=1 / fs)

    def amp_at(f_hz):
        return spectrum[np.argmin(np.abs(freqs - f_hz))]

    a1 = amp_at(f0)
    harmonics_power = sum(amp_at(f0 * n) ** 2 for n in (2, 3, 4, 5))
    thd = (harmonics_power ** 0.5) / a1

    print(f"gain={gain:>4.1f}   THD = {thd*100:5.1f}%")
```

Run it and watch THD climb as `gain` rises — the same knob that turns a clean guitar tone into a distorted one, expressed as a single readout instead of a listening test.

## Why an engineer cares

Linearity / THD is on every amplifier datasheet — a hand-off you'll use directly in AD103 and AD201.

## Try it

Open [Lab 03 — Spectrum detective](labs/lab-03-spectrum-detective-overview.md). On F9, raise the gain into the $\tanh$ nonlinearity and watch harmonics sprout while the THD readout climbs from ~0% toward tens of percent.

Next: [Sampling fast enough](guide/sampling-fast-enough.md).
