# Lab 01 — Signal explorer

Full runnable package: [`labs/lab-01-signal-explorer/`](https://github.com/uoftasic/ad101/tree/main/labs/lab-01-signal-explorer).

## Prerequisites

- [IC101](https://uoftasic.com/ic101/) complete (noVNC desktop working)
- AD101 cloned under `workspace/modules/ad101`
- `python3 scripts/check_env.py` passes
- Read Movement I: [What is a signal?](guide/what-is-a-signal.md) → [Pitch and loudness](guide/pitch-and-loudness.md) → [A family of waveforms](guide/a-family-of-waveforms.md) → [Two voices in time](guide/two-voices-in-time.md)

## Objectives

- Identify amplitude, frequency, period, phase, and DC offset on a live waveform
- Recognize common shapes: sine, square, triangle, pulse, noise
- Convert a phase difference into a time delay

## Theory (short)

$$
v(t) = A\sin(2\pi f t + \phi) + V_{\mathrm{DC}}
\qquad
T = 1/f
\qquad
t_{\mathrm{delay}} = \frac{\phi}{360^\circ}\,T
$$

For a pure sine with no DC: $\mathrm{RMS} = A/\sqrt{2}$, peak-to-peak is $2A$.

## Procedure

```bash
. /foss/designs/common/.designinit
mod ad101
cd labs/lab-01-signal-explorer
python3 src/explore.py
# or one figure at a time:
python3 src/explore.py --figure f1
```

### F1 — Sine explorer

![F1](../assets/img/f01-sine-explorer.png)

- **Try this:** Drag Amplitude, Freq, Phase, and DC. Watch the readout box.
- **What you should see:** Period marker tracks $T = 1/f$. RMS ≈ 0.707× amplitude when DC = 0. Raising DC lifts the whole wave without changing the wiggle size.
- **Why an engineer cares:** This is the oscilloscope view. Amplitude vs the supply rails is **headroom**; the DC offset is the **bias point** AD103 will call an operating point.

### F2 — Signal zoo

![F2](../assets/img/f02-signal-zoo.png)

- **Try this:** Click through sine / square / triangle / pulse / noise. On pulse, sweep Duty.
- **What you should see:** Same amplitude, wildly different shapes. Noise never repeats.
- **Why an engineer cares:** Clocks are squares, ADC ramps are triangles, and that noise trace is the **thermal noise floor** that sets the smallest signal a chip can resolve.

### F3 — Two-signal comparator

![F3](../assets/img/f03-two-signal.png)

- **Try this:** Set phase Δ to 90° at 100 Hz. Read the delay.
- **What you should see:** Delay ≈ 2.5 ms (quarter period). The green sum changes shape with phase — at 0° it is tall; at 180° it cancels.
- **Why an engineer cares:** Phase difference **is** delay. Delay is the entire reason digital timing closure exists.

## Expected results

- At $A=1$, $f=100$, $\mathrm{DC}=0$: readout shows $T \approx 10$ ms, pk-pk ≈ 2 V, RMS ≈ 0.707 V
- At $\Delta\phi = 90^\circ$, $f=100$ Hz: delay ≈ 2.5 ms
- Pulse at 25% duty looks clearly asymmetric vs 50%

## Links

- [Lab package](https://github.com/uoftasic/ad101/tree/main/labs/lab-01-signal-explorer)
- Next lab: [Lab 02 — Harmonic builder](labs/lab-02-harmonic-builder-overview.md)
