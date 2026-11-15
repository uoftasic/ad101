# Finding a quiet note

Stand in a loud room and try to pick out one person humming a note under the noise, and your ear will struggle with it. A spectrum analyzer for sound would have no such trouble, because the hum would show up as a single sharp spike sitting above the noise floor. That example is the main reason the course teaches the frequency domain.

## A tone buried in noise

A small sine wave under loud noise is invisible on a scope trace, but on a spectrum it shows up as an obvious spike.

![F8 — Hidden tone](../assets/img/f08-hidden-tone.png)

When you track down coupling, 60 Hz hum, or a clock leaking into a sensitive node, you use exactly this skill: you stop staring at the time trace and look at the spectrum instead. Once the spike is there, you can read its frequency straight off the data rather than guessing it from a picture.

In [Lab 03](../labs/lab-03-spectrum-detective-overview.md), Part 2 you'll hunt for a hidden tone on the F8 explorer, confirm your answer with a checker script, and then repeat the hunt in a script of your own.

## Spectral leakage (stretch)

Real FFTs don't draw perfect sticks, though. If the measurement window doesn't hold a whole number of cycles, the peak smears sideways into the neighbouring frequency bins, and this smearing is called **leakage**. A **window function**, such as a Hann window, reduces the smear by tapering the start and end of the recorded segment toward zero.

![F10 — Leakage](../assets/img/f10-leakage.png)

Leakage is why measured spectra look soft and smeared rather than like the clean textbook sticks on the last page, [The FFT as an equalizer](../guide/the-fft-as-an-equalizer.md), and it's worth knowing about before it confuses you on a real bench measurement. [Lab 03](../labs/lab-03-spectrum-detective-overview.md), Part 5 (optional), lets you smear a peak on the F10 explorer and then un-smear it.

## Why an engineer cares

Reading the spectrum is how you track down 60 Hz hum, a clock coupling into a sensitive analog node, or any other small interferer that you can't spot by eye.

Next: [Distortion and THD](../guide/distortion-and-thd.md)
