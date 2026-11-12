# Timbre and harmonics

Play A4 (440 Hz) on a violin and then on a trumpet. Same pitch, same loudness, and a tuner would call them identical, yet nobody would mistake one for the other. The difference is **timbre**: each instrument adds its own recipe of extra, quieter tones on top of the main note. Those extra tones are **harmonics**, and a square wave is the cleanest example of what they do.

## The square wave's recipe

A square wave of amplitude 1 and fundamental frequency $f_0$ can be written as an infinite chord:

$$
v_{\mathrm{square}}(t) = \frac{4}{\pi}\sin(2\pi f_0 t)
  + \frac{4}{3\pi}\sin(2\pi\,3f_0 t)
  + \frac{4}{5\pi}\sin(2\pi\,5f_0 t)
  + \cdots
$$

Only the **odd harmonics** ($n = 1, 3, 5, \ldots$) appear, with amplitudes falling as $1/n$; the $n$-th one has amplitude $4/(n\pi)$.

Add more terms and the sum gets closer to a perfect square. Near each edge, though, the sum overshoots and wiggles. This overshoot is **Gibbs ringing**, and it doesn't go away no matter how many harmonics you add. It's the mathematically guaranteed result of approximating a sharp edge with a finite number of sines, and you'll see the same shape on an oscilloscope trace of a real digital clock.

![F4 / F5 — Harmonic builder](../assets/img/f04-f05-harmonic-builder.png)

## The frequency domain

If any (nice) signal is a sum of sines, then the list of those sines' amplitudes and frequencies describes the signal completely. That list is the **frequency domain**: the instrument recipe behind the timbre.

A **stem plot**, with a stick at each harmonic whose height is that harmonic's amplitude, is the natural picture of the recipe. It's the same idea as an equalizer's bar display, applied to a single note instead of a whole song. F5 (right) is the stem plot for the waveform in F4 (left).

You'll switch harmonics on and off in the F4/F5 explorer, then add them up yourself in a script, in [Lab 02](labs/lab-02-harmonic-builder-overview.md), Part 2.

## Why an engineer cares

| Observation | Implication |
|-------------|-------------|
| A "1 GHz digital clock" needs analog bandwidth ≫ 1 GHz | Sharp edges need the high harmonics |
| Ringing at sharp edges | Truncated harmonic series, or real interconnect behaving the same way |
| Timbre = harmonic recipe | Two circuits with the same fundamental can look very different on a spectrum |

Next: [Rhythm and duty cycle](guide/rhythm-and-duty-cycle.md)
