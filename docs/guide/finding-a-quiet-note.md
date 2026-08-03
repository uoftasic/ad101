# Finding a quiet note

**Question this page answers:** *Can I find a signal that's too quiet to see?*

Stand in a loud room and try to pick out one person humming a note under the noise. Your ear struggles — but if you had a spectrum analyzer for sound, that hum would show up as a single sharp spike sitting above the noise floor, completely unmistakable. This is the slide that justifies the whole course.

## The tone buried in noise

A small sine sitting under loud noise is **invisible** on a scope trace and **obvious** as a spike on a spectrum.

![F8 — Hidden tone](../assets/img/f08-hidden-tone.png)

Finding coupling, 60 Hz hum, or a clock feeding into a sensitive node is exactly this skill: stop staring at the time trace and look at the spectrum instead.

## Write it yourself: hunt the hidden tone

```python
import numpy as np
import matplotlib.pyplot as plt

fs = 10_000
t = np.arange(0, 0.5, 1 / fs)

rng = np.random.default_rng(0)
hidden_freq = 237.0                          # you're not allowed to peek at this in real life —
                                              # here it's revealed so you can check your answer
noisy = 0.05 * np.sin(2 * np.pi * hidden_freq * t) + 0.3 * rng.standard_normal(len(t))

spectrum = np.abs(np.fft.rfft(noisy - noisy.mean()))
freqs = np.fft.rfftfreq(len(noisy), d=1 / fs)

plt.subplot(2, 1, 1)
plt.plot(t[:200] * 1e3, noisy[:200])
plt.title("time domain — can you see the tone?")
plt.xlabel("Time (ms)")

plt.subplot(2, 1, 2)
plt.plot(freqs, spectrum)
plt.xlim(0, 500)
plt.title("frequency domain — now can you?")
plt.xlabel("Frequency (Hz)")
plt.tight_layout()
plt.show()

guess = freqs[np.argmax(spectrum)]
print(f"Loudest peak sits at ≈ {guess:.0f} Hz")
```

The time-domain subplot is garbage — pure noise to the eye. The spectrum has one obvious spike, and the last line reads its frequency straight off the data instead of guessing from a picture.

## Spectral leakage *(stretch)*

Real FFTs don't draw perfect sticks. If your measurement window doesn't contain a whole number of cycles, the peak smears sideways into its neighboring bins — called **leakage**. A **window function** (like a Hann window, which tapers the start and end of the recorded segment toward zero) reduces the smear.

![F10 — Leakage](../assets/img/f10-leakage.png)

This is why measured spectra look soft and smeared instead of like the clean textbook sticks from the last page — worth knowing before it confuses you on a real bench measurement.

## Why an engineer cares

This is how you track down **60 Hz hum**, a clock coupling into a sensitive analog node, or any small interferer you can't spot by eye.

## Try it

Open [Lab 03 — Spectrum detective](labs/lab-03-spectrum-detective-overview.md). On F8, raise the noise until the time plot is garbage, read the spike frequency off the spectrum, then confirm with:

```bash
python3 src/check.py --guess 237
```

Next: [Distortion and THD](guide/distortion-and-thd.md).
