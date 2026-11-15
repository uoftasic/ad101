# Adding signals

Play three notes on a piano at once and you hear a **chord**: one sound, richer than any single note, made by adding three notes together. Signals in a circuit combine the same way.

## Superposition

If $v_1(t)$ and $v_2(t)$ are voltages on the same wire, the wire carries $v_1(t) + v_2(t)$. The two don't interact or multiply; they add, sample by sample. This is **superposition**. Add two sines of different frequencies and the sum can look nothing like either one, the same way a C-E-G chord doesn't sound like a C, an E or a G on its own.

That one fact, that signals on a wire add, is enough to build almost any waveform you'll meet in this course.

## Reading a sum by eye

Add the three notes of a C-major chord (C4, E4 and G4: 261.6, 329.6 and 392.0 Hz) and plot the result. The sum no longer looks like three sines. Once more than one or two tones are added together, the shape of a time plot stops telling you what went into it. Movement III, starting with [The FFT as an equalizer](../guide/the-fft-as-an-equalizer.md), gives you a tool that undoes the sum.

You'll build this chord yourself in [Lab 02](../labs/lab-02-harmonic-builder-overview.md), Part 1.

## Why an engineer cares

Every wire on a chip is a superposition point: the signal, plus supply noise, plus coupling from a neighbouring trace, plus whatever else touches it. "What's actually on this node?" is usually answered by splitting the sum back into its parts, and the next two pages show you how. [Timbre and harmonics](../guide/timbre-and-harmonics.md) uses superposition to build a square wave out of nothing but sines.

Next: [Timbre and harmonics](../guide/timbre-and-harmonics.md)
