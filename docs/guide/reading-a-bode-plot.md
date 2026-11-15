# Reading a Bode plot

A Bode plot is a filter's spec sheet. Read it the way you'd read an EQ curve on a mixing console: flat means unchanged, a downward slope means getting quieter, and the phase panel tells you how much later each frequency arrives.

## What each feature means

| Feature | Meaning |
|---------|---------|
| Flat region | Passband: the signal comes through almost unchanged |
| −3 dB point | The cutoff $f_c$, by definition |
| −20 dB/decade slope | First-order roll-off (×10 in frequency → ÷10 in amplitude) |
| Phase → −90° | The high-frequency limit for a single RC |

## Gain and phase as a picture in time

A Bode plot is a summary built by testing one frequency at a time. Pick a frequency on the curve and drive the filter with a sine at that frequency. The output is still a sine at the same frequency, but **smaller** (the gain) and **later** (the phase). A network analyzer measures exactly this, one sweep point at a time, to draw the two curves.

![F13 — Bode linked to time](../assets/img/f13-bode-time.png)

Take three points on the RC low-pass curve:

- A decade below $f_c$, the output is almost identical to the input.
- At $f_c$, the output shrinks to about 0.707× the input and lags by about an eighth of a cycle (45°). This is the point every Bode plot is anchored to.
- A decade above $f_c$, the output is tiny and lags by nearly 90°.

You'll park the F13 marker at these three points, then draw the input and output sines for each in your own script, in [Lab 04](../labs/lab-04-rc-bode-overview.md), Part 2.

Next: [Filtering a beat](../guide/filtering-a-beat.md)
