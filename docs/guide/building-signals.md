# Building signals

**Question this page answers:** *Where do complicated waveforms come from?*

## Superposition — signals add

If $v_1(t)$ and $v_2(t)$ are voltages on the same wire, the wire carries $v_1 + v_2$. Add two sines of different frequencies and the sum can look nothing like either parent. That is already enough to build almost any periodic waveform.

## A square wave is a recipe of sines

A square wave of amplitude 1 and fundamental frequency $f_0$ can be written:

$$
v_{\mathrm{square}}(t) = \frac{4}{\pi}\sin(2\pi f_0 t)
  + \frac{4}{3\pi}\sin(2\pi\,3f_0 t)
  + \frac{4}{5\pi}\sin(2\pi\,5f_0 t)
  + \cdots
$$

Only **odd harmonics** ($n = 1, 3, 5, \ldots$), with amplitudes falling as $1/n$. Add more terms and the sum walks closer to a perfect square — including the overshoot near the edges (Gibbs ringing) that you will meet on real boards.

![F4 / F5 — Harmonic builder](../assets/img/f04-f05-harmonic-builder.png)

### The payoff sentence

> If any (nice) signal is a sum of sines, then the **list of those sines' amplitudes and frequencies** describes the signal completely. That list is the **frequency domain**.

A **stem plot** — a stick at each harmonic with height equal to its amplitude — is the natural picture of that list. Spectrum analyzers draw a continuous version of the same idea.

## Duty cycle reshapes the recipe

A pulse that is not 50% on / 50% off brings **even** harmonics back into the spectrum. At exactly 50% duty, the even sticks vanish. That is one reason clock specs care about duty cycle: spectral content drives electromagnetic interference (EMI).

![F6 — Duty cycle and spectrum](../assets/img/f06-duty-spectrum.png)

## Why an engineer cares

| Observation | Implication |
|-------------|-------------|
| A "1 GHz digital clock" needs analog bandwidth ≫ 1 GHz | Edges need the high harmonics |
| Ringing at sharp edges | Truncated harmonic series / interconnect |
| 50% duty kills even harmonics | Cleaner spectrum, less EMI |

## Try it

Open [Lab 02 — Harmonic builder](../labs/lab-02-harmonic-builder-overview.md). Toggle harmonics in F4/F5 and sweep duty cycle in F6.

Next: [The frequency domain](the-frequency-domain.md).
