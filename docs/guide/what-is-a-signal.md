# What is a signal?

**Question this page answers:** *What am I actually looking at on an oscilloscope?*

Hum a single note and hold it. Your vocal cords are pushing air back and forth, over and over, the same number of times every second. If you plotted "how far the air is pushed" against time, you'd draw a wiggly line — up, down, up, down — that repeats.

That wiggly line is a **signal**. On a chip, the thing wiggling is not air, it's **voltage**. Every wire, every pin, every node carries a voltage that can move up and down over time, exactly like the air pressure of your hummed note. If you can describe that voltage — how big it swings, how fast it repeats, where it sits — you can start reasoning about the circuit it lives in.

## An oscilloscope is sheet music for voltage

A microphone turns your hummed note into a voltage that wiggles the same way the air did. An **oscilloscope** is the instrument that draws that voltage against time, the same way sheet music lays pitches out against a timeline. Look at the trace, and you're reading the "score" of whatever voltage the probe is touching.

Everything in this course is about getting fluent at reading — and later, writing — that score.

## A signal is just two lists of numbers

Strip away the instrument and the circuit, and a signal is nothing more than:

- a list of **times**, and
- a list of **voltages**, one per time.

That's it. No calculus required. In Python, those two lists are just two `numpy` arrays:

```python
import numpy as np

t = np.arange(0, 0.05, 1 / 10_000)   # 50 ms of timestamps, 10,000 per second
v = np.sin(2 * np.pi * 440 * t)      # a voltage at each of those timestamps
```

`t` and `v` are the same length, and `v[i]` is the voltage at time `t[i]`. Every plot, every measurement, and every script in this course starts from a pair of arrays that look exactly like this.

## Try it

Open a Python shell (or a new file) and run the snippet above, then add:

```python
import matplotlib.pyplot as plt

plt.plot(t * 1e3, v)          # ×1e3 to show milliseconds instead of seconds
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.show()
```

You just wrote your first signal-analysis script. It draws one held note — the sine wave. That's an actual oscilloscope trace of the note **A4**, the pitch orchestras tune to.

Next: [Pitch and loudness](guide/pitch-and-loudness.md), where those two arrays turn into amplitude, frequency, and the rest of the vocabulary you'll use all course.
