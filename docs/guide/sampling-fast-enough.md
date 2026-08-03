# Sampling fast enough

**Question this page answers:** *Can measuring a signal too slowly lie to me?*

You've probably seen a car's wheels appear to spin backwards in a video, even though the car is clearly driving forward. The camera only captures a handful of frames per second, and the wheel spokes move almost — but not quite — a full turn between frames, so your brain reconstructs a slow, wrong rotation. The camera didn't malfunction; it simply wasn't sampling fast enough to keep up with the true motion. An ADC measuring a voltage has exactly the same failure mode.

## Sampling and aliasing

Measure a tone too slowly and a fast sine masquerades as a slow one — a fake, low-frequency signal called an **alias**. The rule that prevents it:

$$
f_{\mathrm{sample}} > 2\, f_{\mathrm{max}}
\qquad\text{(Nyquist)}
$$

![F11 — Aliasing](../assets/img/f11-aliasing.png)

That's why ADC sample rates are chosen carefully — a teaser for AD202 (mixed signal).

## Write it yourself: make a tone lie about its own frequency

```python
import numpy as np
import matplotlib.pyplot as plt

true_freq = 900.0                 # Hz — the real tone
duration = 0.02

for fs in (5000.0, 1000.0):       # first well above Nyquist, then below it
    t = np.arange(0, duration, 1 / fs)
    v = np.sin(2 * np.pi * true_freq * t)

    nyquist_ok = fs > 2 * true_freq
    label = "OK — above Nyquist" if nyquist_ok else "ALIASED — below Nyquist"
    plt.plot(t * 1e3, v, marker="o", label=f"fs={fs:.0f} Hz  ({label})")

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.legend(fontsize=8)
plt.title(f"true tone = {true_freq:.0f} Hz")
plt.show()
```

At `fs=5000`, the sample points trace out a recognizable 900 Hz wiggle. At `fs=1000` — below the $2\times 900 = 1800$ Hz Nyquist rate — the *same* 900 Hz tone connects into a slow, wrong-looking wave, exactly like the backwards-spinning wheel. Nothing about the input changed; only how often you looked at it did.

## Why an engineer cares

Choosing an ADC sample rate is choosing whether you'll ever see this failure — the setup for AD202.

## Try it

Open [Lab 03 — Spectrum detective](labs/lab-03-spectrum-detective-overview.md). On F11, drop the sample rate below 400 Hz for a 200 Hz tone and watch the status flip to `ALIASED` as a bogus slow sine appears and the spectrum peak folds below Nyquist.

Next: [Filters are tone knobs](guide/filters-are-tone-knobs.md) — Movement IV, where you finally get to ask what a *circuit* does to a signal's recipe, instead of just reading the recipe off.
