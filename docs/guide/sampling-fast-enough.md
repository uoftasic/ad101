# Sampling fast enough

You've probably seen a car's wheels seem to spin backwards in a video while the car drives forward. The camera captures only a handful of frames per second, and between frames the spokes move almost, but not quite, a full turn, so your brain reconstructs a slow, wrong rotation. The camera didn't malfunction. It wasn't sampling fast enough to keep up with the real motion. An ADC measuring a voltage can fail in exactly the same way.

## Sampling and aliasing

Measure a tone too slowly and a fast sine passes itself off as a slow one: a fake low-frequency signal called an **alias**. The rule that prevents it is the Nyquist criterion:

$$
f_{\mathrm{sample}} > 2\, f_{\mathrm{max}}
\qquad\text{(Nyquist)}
$$

Two related numbers both get called "Nyquist". The Nyquist rate is $2 f_{\mathrm{max}}$, the rate your sample rate has to beat. Half the sample rate, $f_s/2$, is the highest frequency a given sample rate can represent; the F11 explorer labels that one Nyquist.

![F11 — Aliasing](../assets/img/f11-aliasing.png)

## Worked example: a 900 Hz tone

Sample a 900 Hz tone at 5000 samples per second, well above Nyquist, and the sample points trace out a recognizable 900 Hz wiggle. Sample the same tone at 1000 samples per second, below the $2 \times 900 = 1800$ Hz Nyquist rate, and the points join up into a slow, wrong-looking wave, just like the backwards-spinning wheel. The input didn't change; only how often you looked at it did.

You'll drop the sample rate on the F11 explorer until the tone aliases, then reproduce this 900 Hz example in your own script, in [Lab 03](../labs/lab-03-spectrum-detective-overview.md), Part 4.

## Why an engineer cares

Choosing an ADC's sample rate decides whether you'll ever see this failure. That's why sample rates are chosen carefully, and it's the setup for AD202 (mixed signal).

That's the end of Movement III. Next: [Lab 03: Spectrum detective](../labs/lab-03-spectrum-detective-overview.md). After the lab, Movement IV starts with [Filters are tone knobs](../guide/filters-are-tone-knobs.md), where you ask what a circuit does to a signal's recipe instead of only reading the recipe off.
