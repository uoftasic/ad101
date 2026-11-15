# Adding signals

If you play three notes on a piano at once, you hear a **chord**: a single sound, richer than any one of the notes, made by adding the three together. Signals in a circuit combine in the same way.

## Superposition

If $v_1(t)$ and $v_2(t)$ are voltages on the same wire, the wire carries $v_1(t) + v_2(t)$. The two signals don't interact with each other or multiply; they simply add, sample by sample, and this is called **superposition**. If you add two sines of different frequencies, the sum can look nothing like either of them, in the same way that a C-E-G chord doesn't sound like a C, an E or a G on its own. That one fact, that signals on a wire add, is enough to build almost any waveform you'll meet in this course.

## Reading a sum by eye

When you add the three notes of a C-major chord (C4, E4 and G4: 261.6, 329.6 and 392.0 Hz) and plot the result, the sum no longer looks like three sines. Once you add more than one or two tones together, the shape of a plot against time stops telling you what went into it, so you can't read the notes back off the curve by eye. Movement III, starting with [The FFT as an equalizer](../guide/the-fft-as-an-equalizer.md), gives you a tool that undoes the sum and recovers the parts.

You'll build this chord yourself in [Lab 02](../labs/lab-02-harmonic-builder-overview.md), Part 1.

## Why an engineer cares

Every wire on a chip is a point where signals add: what's on it is the signal you meant to put there, plus noise from the supply, plus whatever couples in from a neighbouring trace, plus anything else that touches it. The usual way to answer "What's actually on this node?" is to split the sum back into its parts, which is what Movement III teaches. Before that, the next page, [Timbre and harmonics](../guide/timbre-and-harmonics.md), uses superposition to build a square wave out of nothing but sines.

Next: [Timbre and harmonics](../guide/timbre-and-harmonics.md)
