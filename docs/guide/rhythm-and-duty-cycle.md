# Rhythm and duty cycle

A metronome that ticks 50/50, sounding for exactly as long as it stays silent, has a different rhythm from one that snaps briefly and then rests. A pulse train works the same way: it's a square wave that doesn't have to be on for half of each cycle and off for the other half. The fraction of each cycle that it spends on is called its **duty cycle**, and when you change the duty cycle, you change which harmonics show up in the wave's recipe.

## Duty cycle and the recipe

At exactly 50% duty, the square-wave recipe from [Timbre and harmonics](../guide/timbre-and-harmonics.md) holds, so only the odd harmonics are present. If you move the duty cycle away from 50% in either direction, the **even** harmonics ($n = 2, 4, 6, \ldots$) come back into the spectrum.

This is one of the reasons clock specifications care about duty cycle. The frequencies in a clock's spectrum drive the electromagnetic interference (**EMI**) it produces, and a clock with a clean, symmetric duty cycle radiates a cleaner spectrum than a lopsided one does.

![F6 — Duty cycle and spectrum](../assets/img/f06-duty-spectrum.png)

You'll sweep the duty cycle on the F6 explorer and plot the spectra of three pulse trains yourself in [Lab 02](../labs/lab-02-harmonic-builder-overview.md), Part 3.

## Why an engineer cares

| Observation | Implication |
|-------------|-------------|
| A 50% duty cycle removes the even harmonics | The spectrum is cleaner, so there's less EMI |
| A duty cycle away from 50% | The even harmonics come back and radiate at their own frequencies |
| Clock spec sheets list a duty-cycle tolerance | The tolerance is there to keep the clock's spectrum clean, rather than for looks |

This page ends Movement II, and next comes [Lab 02: Harmonic builder](../labs/lab-02-harmonic-builder-overview.md). After the lab, Movement III starts with [The FFT as an equalizer](../guide/the-fft-as-an-equalizer.md), which gives you a tool that reads off the recipe of any signal automatically, so you no longer have to build it up by hand.
