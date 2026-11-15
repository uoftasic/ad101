# A family of waveforms

Not every signal looks like a sine. A flute, a snare drum and radio static all make sound, but each has a different waveform, and the signals inside a chip don't all share one shape either.

## Four more shapes to know by sight

| Shape | Where you'll meet it | What it looks like |
|-------|------------------------|----------------------|
| Square | Digital clocks | Snaps between two levels, with nothing in between |
| Triangle | ADC ramps, test signals | Straight-line rise, straight-line fall |
| Pulse | Digital clocks with a tunable on-time (the **duty cycle**) | A square that spends more time low than high, or the other way round |
| Noise | Sensor readouts, the thermal noise floor | Never repeats, so it has no period at all |

![F2 — Signal zoo](../assets/img/f02-signal-zoo.png)

The F2 explorer drives every shape from the same amplitude setting, and they still look completely different. That's why you can't judge a trace by its height alone: two waveforms can have the same height on a datasheet and still carry completely different information.

You can build the square, pulse and triangle from the same time array `t` you met on [What is a signal?](../guide/what-is-a-signal.md), using a phase that counts from 0 to 1 once per cycle. If you compare the phase to a threshold you get a square or a pulse, and if you ramp it up and then down you get a triangle. You'll build those three this way in [Lab 01](../labs/lab-01-signal-explorer-overview.md), Part 4, along with a noise trace, and the duty cycle comes back in [Rhythm and duty cycle](../guide/rhythm-and-duty-cycle.md).

## Why an engineer cares

- The clocks in a digital chip are square waves.
- The ramps an ADC uses are triangle waves.
- The noise trace is what the **thermal noise floor** looks like: the chip's own randomness, which sets the smallest signal the chip can resolve.

Next: [Two voices in time](../guide/two-voices-in-time.md)
