# Finding a quiet note

Stand in a loud room and try to pick out one person humming a note under the noise, and your ear will struggle with it. A spectrum analyzer for sound would have no such trouble, because the hum would show up as a single sharp spike sitting above the noise floor. Picking out a quiet tone like this is one of the main reasons the course teaches the frequency domain.

## A tone buried in noise

A small sine wave under loud noise is invisible on a scope trace, but on a spectrum it shows up as an obvious spike.

![F8 — Hidden tone](../assets/img/f08-hidden-tone.png)

Whenever you're hunting for a small interferer on a node, you use exactly this skill: you stop staring at the time trace and look at the spectrum instead. Once the spike is there, you can read its frequency straight off the data rather than guessing it from a picture.

In [Lab 03](../labs/lab-03-spectrum-detective-overview.md), Part 2 you'll hunt for a hidden tone on the F8 explorer, confirm your answer with a checker script, and then repeat the hunt in a script of your own.

## Spectral leakage (stretch)

Real FFTs don't draw perfect sticks, though. If the measurement window doesn't hold a whole number of cycles, the peak smears sideways into the neighbouring frequency bins (an FFT reports the spectrum only at a set of evenly spaced frequencies, and each of those is called a bin), and this smearing is called **leakage**. A **window function**, such as a Hann window, reduces the smear by tapering the start and end of the recorded segment toward zero.

![F10 — Leakage](../assets/img/f10-leakage.png)

Leakage is why measured spectra look soft and smeared rather than like clean textbook sticks. You've already seen it once: in F7 on the last page, [The FFT as an equalizer](../guide/the-fft-as-an-equalizer.md), the two-tone spectrum is smeared while the pure tone is a clean stick. It's worth knowing about before it confuses you on a real bench measurement. [Lab 03](../labs/lab-03-spectrum-detective-overview.md), Part 5 (optional), lets you smear a peak on the F10 explorer and then reduce the smear with a Hann window.

## Why an engineer cares

Reading the spectrum is how you track down 60 Hz hum, a clock coupling into a sensitive analog node, or any other small interferer that you can't spot by eye.

Next: [Distortion and THD](../guide/distortion-and-thd.md)
