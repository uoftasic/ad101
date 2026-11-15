# Pitch and loudness

The held note from the last page, a sine wave, is the simplest interesting signal there is. Almost everything else in this course is built out of sines, so it's worth getting comfortable with its four knobs before moving on.

## The sine wave's knobs

$$
v(t) = A \sin(2\pi f t + \phi) + V_{\mathrm{DC}}
$$

Each symbol is a knob you could turn on a synthesizer:

| Symbol | Name | Musical intuition | What it means |
|--------|------|--------------------|----------------|
| $A$ | Amplitude | Loudness | How far the wave swings from its center (volts) |
| $f$ | Frequency | Pitch | How many cycles per second (hertz, Hz) |
| $T = 1/f$ | Period | Length of one "beat" | Duration of one cycle (seconds) |
| $\phi$ | Phase | Where in the beat you start | Horizontal shift: where the wave starts |
| $V_{\mathrm{DC}}$ | DC offset | None (a mixing desk calls this "bias") | The center line the wave rides on |

Turn the amplitude knob up and the note gets louder without changing pitch. Turn the frequency knob up and the pitch rises without changing loudness. The two are independent, which is why the formula gives them separate symbols.

![F1 — Sine explorer](../assets/img/f01-sine-explorer.png)

## Two ways to measure "how loud"

- **Peak-to-peak** is the full vertical swing, from the top of the wave to the bottom. For a pure sine it's $2A$.
- **RMS** ("root mean square") is the signal's effective strength. For a sine with no DC offset, $\mathrm{RMS} = A/\sqrt{2} \approx 0.707\,A$. The power a signal delivers into a resistor depends on its RMS value, not its peak, which is why a multimeter reports RMS rather than amplitude when you measure an AC voltage.

You'll read period, peak-to-peak and RMS off the F1 explorer, then compute them from an array in your own script, in [Lab 01](../labs/lab-01-signal-explorer-overview.md), Part 3.

## Why an engineer cares

| Quantity | Everyday use |
|----------|----------------|
| Amplitude vs supply rails | Headroom: will the signal clip? |
| DC offset | Bias / operating point (AD103 will make this precise) |
| Frequency | Bandwidth budgets, sampling rates |
| RMS | The number your multimeter and power calculations actually use |

Next: [A family of waveforms](../guide/a-family-of-waveforms.md)
