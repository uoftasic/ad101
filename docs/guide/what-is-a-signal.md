# What is a signal?

Hum a single note and hold it. Your vocal cords push the air back and forth, the same number of times every second. If you plotted how far the air is pushed against time, you'd draw a wiggly line that goes up and down and repeats.

That line is a **signal**. On a chip, the thing that wiggles is a voltage instead of air. Every wire, pin and node carries a voltage that can move up and down over time, just like the air pressure of your hummed note. Once you can describe that voltage (how big it swings, how fast it repeats, where it sits) you can start reasoning about the circuit it lives in.

## The oscilloscope

A microphone turns your hummed note into a voltage that wiggles the same way the air did. An **oscilloscope** is the instrument that draws that voltage against time, the way sheet music lays pitches out along a timeline. When you look at a scope trace, you're reading the "score" of whatever voltage the probe is touching. This course is about getting fluent at reading that score, and later at writing it.

## A signal as two lists of numbers

Take away the instrument and the circuit, and a signal is:

- a list of **times**, and
- a list of **voltages**, one for each time.

You don't need calculus for this. In Python, the two lists are two `numpy` arrays:

```python
import numpy as np

t = np.arange(0, 0.05, 1 / 10_000)   # 50 ms of timestamps, 10,000 per second
v = np.sin(2 * np.pi * 440 * t)      # a voltage at each of those timestamps
```

`t` and `v` are the same length, and `v[i]` is the voltage at time `t[i]`. Every plot, measurement and script in this course starts from a pair of arrays like these.

This pair describes one held note: a sine wave at 440 Hz, the note A4 that orchestras tune to. Plotted against time, it's what an oscilloscope would show for that note. You'll write and plot it yourself in [Lab 01](labs/lab-01-signal-explorer-overview.md), Part 2.

Next: [Pitch and loudness](guide/pitch-and-loudness.md), where these two arrays get the vocabulary you'll use for the rest of the course: amplitude, frequency and phase.
