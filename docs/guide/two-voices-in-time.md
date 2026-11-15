# Two voices in time

Two singers hold the same note, but one comes in a fraction of a beat late. They're at the same pitch and the same loudness, just offset in time. That offset is **phase**, and it shows up wherever two signals of the same frequency meet: two clock domains, the two channels of a stereo signal, two probes on the same scope.

## Phase as a time delay

$$
t_{\mathrm{delay}} = \frac{\phi}{360^\circ} \cdot T
$$

A phase difference is a time delay, measured in degrees of one cycle instead of in seconds. A $90^\circ$ shift at 100 Hz is a 2.5 ms delay, a quarter of the 10 ms period. It works like "a quarter note late": the same fraction of a beat is a different amount of time at a fast tempo than at a slow one.

![F3 — Two-signal comparator](../assets/img/f03-two-signal.png)

## Adding two offset voices

When you add two equal sines, the phase between them decides what the sum looks like. At $0^\circ$ the two voices reinforce each other and the sum is tall. As the phase approaches $180^\circ$ they cancel and the sum flattens out. That's the audio equivalent of two speakers wired backwards.

You'll set the phase on the F3 explorer, check the delay readout against the formula, and plot the two voices and their sum yourself in [Lab 01](../labs/lab-01-signal-explorer-overview.md), Part 5.

## Why an engineer cares

| Quantity | Everyday use |
|----------|----------------|
| Phase / delay | Timing, synchronization, and the reason digital timing closure exists |
| Phase at high frequency | Clock skew between two paths that "should" arrive together |
| Phase margin | A preview of stability analysis in AD201 |

That's the end of Movement I. Next: [Lab 01: Signal explorer](../labs/lab-01-signal-explorer-overview.md). After the lab, Movement II starts with [Adding signals](../guide/adding-signals.md).
