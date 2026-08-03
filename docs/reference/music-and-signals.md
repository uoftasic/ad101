# Music and signals — glossary

Every idea in this course has a musical twin. Use this page as a translation table whenever a guide page's analogy doesn't click on the first read.

## Term-for-term glossary

| Musical term | Signal-processing term | Where it's covered |
|---------------|-------------------------|----------------------|
| Pitch | Frequency ($f$) | [Pitch and loudness](guide/pitch-and-loudness.md) |
| Loudness | Amplitude ($A$) | [Pitch and loudness](guide/pitch-and-loudness.md) |
| Beat length | Period ($T = 1/f$) | [Pitch and loudness](guide/pitch-and-loudness.md) |
| Two voices out of sync | Phase / delay ($\phi$) | [Two voices in time](guide/two-voices-in-time.md) |
| Chord | Superposition (signals added) | [Adding signals](guide/adding-signals.md) |
| Timbre (why instruments sound different) | Harmonic content / spectrum | [Timbre and harmonics](guide/timbre-and-harmonics.md) |
| Rhythm's "on" fraction | Duty cycle | [Rhythm and duty cycle](guide/rhythm-and-duty-cycle.md) |
| Equalizer display | FFT / spectrum | [The FFT as an equalizer](guide/the-fft-as-an-equalizer.md) |
| Distorted / crunchy tone | Harmonic distortion (THD) | [Distortion and THD](guide/distortion-and-thd.md) |
| Wagon-wheel effect | Aliasing | [Sampling fast enough](guide/sampling-fast-enough.md) |
| Bass/treble knob | Filter (low-pass / high-pass) | [Filters are tone knobs](guide/filters-are-tone-knobs.md) |
| EQ curve | Bode plot | [Reading a Bode plot](guide/reading-a-bode-plot.md) |
| Muffled sound through a wall | Low-pass-filtered signal | [Filtering a beat](guide/filtering-a-beat.md) |

## Octaves and doubling

Going up one **octave** doubles the frequency: A3 (220 Hz) and A4 (440 Hz) are "the same note," an octave apart, because 440 is exactly double 220. This is why frequency axes in this course are often drawn on a **log** scale (as in a Bode plot) — equal *musical* steps are equal *ratios*, not equal differences in Hz.

## Note-name to frequency table

Standard concert pitch: A4 = 440 Hz. These are the notes used in the "write it yourself" snippets throughout the guide.

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

A C-major triad (C4, E4, G4) is the chord used in [Adding signals](guide/adding-signals.md).

## Related

- [Reading plots](reference/reading-plots.md) — the three plots themselves
- [Getting started](guide/getting-started.md) — the two-track path through the course
