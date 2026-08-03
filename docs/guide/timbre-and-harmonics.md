# Timbre and harmonics

**Question this page answers:** *Why do a violin and a trumpet playing the same note sound different?*

Play A4 (440 Hz) on a violin and a trumpet. Same pitch, same loudness — a tuner would call them identical — and yet nobody would mistake one for the other. The difference is **timbre**: each instrument adds its own recipe of extra, quieter tones on top of the main note. Those extra tones are called **harmonics**, and a square wave is the cleanest example of what they do.

## A square wave is a recipe of sines

A square wave of amplitude 1 and fundamental frequency $f_0$ can be written as an infinite chord:

$$
v_{\mathrm{square}}(t) = \frac{4}{\pi}\sin(2\pi f_0 t)
  + \frac{4}{3\pi}\sin(2\pi\,3f_0 t)
  + \frac{4}{5\pi}\sin(2\pi\,5f_0 t)
  + \cdots
$$

Only **odd harmonics** ($n = 1, 3, 5, \ldots$), with amplitudes falling as $1/n$. Add more terms and the sum walks closer to a perfect square — including the overshoot near the edges (**Gibbs ringing**) that you'll meet again on real circuit boards.

![F4 / F5 — Harmonic builder](../assets/img/f04-f05-harmonic-builder.png)

### The payoff sentence

> If any (nice) signal is a sum of sines, then the **list of those sines' amplitudes and frequencies** describes the signal completely. That list is the **frequency domain** — the "instrument recipe" behind the timbre.

A **stem plot** — a stick at each harmonic with height equal to its amplitude — is the natural picture of that recipe list. It's the same idea an equalizer's bar display shows you, just for a single note instead of a whole song.

## Write it yourself: assemble a square wave from sines

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 10_000
t = np.arange(0, 0.02, 1 / fs)
f0 = 200.0                       # fundamental frequency, Hz

harmonics = [1, 3, 5, 7, 9]       # odd harmonics only
built = np.zeros_like(t)
for n in harmonics:
    amplitude = 4 / (n * np.pi)   # the recipe from the formula above
    built += amplitude * np.sin(2 * np.pi * n * f0 * t)

ideal_square = np.sign(np.sin(2 * np.pi * f0 * t))

plt.plot(t * 1e3, ideal_square, color="gray", linestyle="--", label="ideal square")
plt.plot(t * 1e3, built, label=f"sum of {len(harmonics)} harmonics")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.show()
```

Start with `harmonics = [1]` — just the fundamental, a plain sine — then add `3`, then `5`, then `7`, `9`. Watch the sum walk toward the dashed square with each new sine you throw in, and watch the little overshoot ("ringing") appear right at the edges and refuse to go away no matter how many harmonics you add. That ringing isn't a bug in your code — it's the mathematically guaranteed signature of approximating a sharp edge with a finite number of sines, and you'll see the same shape on a real oscilloscope trace of a digital clock.

## Why an engineer cares

| Observation | Implication |
|-------------|-------------|
| A "1 GHz digital clock" needs analog bandwidth ≫ 1 GHz | Sharp edges need the high harmonics |
| Ringing at sharp edges | Truncated harmonic series / real interconnect behaving the same way |
| Timbre = harmonic recipe | Two circuits with the same fundamental can look wildly different on a spectrum |

## Try it

Open [Lab 02 — Harmonic builder](labs/lab-02-harmonic-builder-overview.md). Toggle harmonics on and off in F4/F5 and watch the stem plot update in lockstep with the waveform.

Next: [Rhythm and duty cycle](guide/rhythm-and-duty-cycle.md).
