# Distortion and THD

Turn a guitar amp's gain past clean and the sound gets crunchy: harsh new overtones appear that were never in the original note. The input didn't change frequency. The circuit created new frequencies by clipping the wave. That's **distortion**, and only a nonlinear system can do it. A truly linear circuit can only rescale and delay a sine, never add new tones to it.

## New frequencies from one

Push a clean sine through a soft nonlinearity such as $\tanh$ (a smooth version of clipping) and new harmonics appear in the spectrum that weren't in the input. The harder you drive it, the more it clips and the bigger those harmonics get.

**Total harmonic distortion (THD)** sums up how much energy has moved into those extra harmonics, relative to the fundamental:

$$
\mathrm{THD} = \frac{\sqrt{A_2^2 + A_3^2 + \cdots}}{A_1}
$$

![F9 — THD](../assets/img/f09-thd.png)

THD turns "how distorted does it sound?" into a single number you can read off instead of a listening test. You'll raise the gain on the F9 explorer and watch THD climb, then clip a sine and measure THD in your own script, in [Lab 03](../labs/lab-03-spectrum-detective-overview.md), Part 3.

## Why an engineer cares

Every amplifier datasheet quotes a linearity or THD number. AD103's MOSFET curves and AD201's amplifiers make this precise.

Next: [Sampling fast enough](../guide/sampling-fast-enough.md)
