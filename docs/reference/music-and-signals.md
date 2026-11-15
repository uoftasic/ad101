# Music and signals

Every idea in this course has a musical counterpart, and this page collects them in one place. Use it as a translation table when the analogy on a guide page doesn't click the first time you read it.

## Glossary

| Musical term | Signal-processing term | Where it's covered |
|---------------|-------------------------|----------------------|
| Pitch | Frequency ($f$) | [Pitch and loudness](../guide/pitch-and-loudness.md) |
| Loudness | Amplitude ($A$) | [Pitch and loudness](../guide/pitch-and-loudness.md) |
| Beat length | Period ($T = 1/f$) | [Pitch and loudness](../guide/pitch-and-loudness.md) |
| Two voices out of sync | Phase / delay ($\phi$) | [Two voices in time](../guide/two-voices-in-time.md) |
| Chord | Superposition (signals added) | [Adding signals](../guide/adding-signals.md) |
| Timbre (why instruments sound different) | Harmonic content / spectrum | [Timbre and harmonics](../guide/timbre-and-harmonics.md) |
| Rhythm's "on" fraction | Duty cycle | [Rhythm and duty cycle](../guide/rhythm-and-duty-cycle.md) |
| Equalizer display | FFT / spectrum | [The FFT as an equalizer](../guide/the-fft-as-an-equalizer.md) |
| Distorted / crunchy tone | Harmonic distortion (THD) | [Distortion and THD](../guide/distortion-and-thd.md) |
| Wagon-wheel effect | Aliasing | [Sampling fast enough](../guide/sampling-fast-enough.md) |
| Bass/treble knob | Filter (low-pass / high-pass) | [Filters are tone knobs](../guide/filters-are-tone-knobs.md) |
| EQ curve | Bode plot | [Reading a Bode plot](../guide/reading-a-bode-plot.md) |
| Muffled sound through a wall | Low-pass-filtered signal | [Filtering a beat](../guide/filtering-a-beat.md) |

## Octaves and doubling

Going up one **octave** doubles the frequency. A3 (220 Hz) and A4 (440 Hz) sound like "the same note" an octave apart, because 440 is exactly double 220. Equal steps in music are equal ratios of frequency rather than equal differences in Hz, so the frequency axes in this course, such as the one on a Bode plot, are often drawn on a log scale.

## Note-name to frequency table

Standard concert pitch is A4 = 440 Hz. The table includes every note that the lab snippets and Lab 05 use, along with a few others.

| Note | Frequency (Hz) |
|------|-----------------|
| A3 | 220.0 |
| C4 | 261.6 |
| D4 | 293.7 |
| E4 | 329.6 |
| F4 | 349.2 |
| G4 | 392.0 |
| A4 | 440.0 |
| B4 | 493.9 |
| C5 | 523.3 |
| E5 | 659.3 |
| A5 | 880.0 |

A C-major triad (C4, E4 and G4) is the chord you'll find in [Adding signals](../guide/adding-signals.md), Lab 02 and Lab 05.

## Related

- [Reading plots](../reference/reading-plots.md): how to read the three plots themselves
- [Getting started](../guide/getting-started.md): how the course is organized
