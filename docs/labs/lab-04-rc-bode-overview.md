# Lab 04 — RC filter & Bode

Full runnable package: [`labs/lab-04-rc-bode/`](https://github.com/uoftasic/ad101/tree/main/labs/lab-04-rc-bode).

## Prerequisites

- Lab 03 complete
- Read [Filters & Bode](guide/filters-and-bode.md)

## Objectives

- Build intuition for $\lvert H(f)\rvert$ and $\angle H(f)$ on a Bode plot
- Link a Bode marker to a shrinking, lagging sine in time
- Watch a square wave lose its edges as high harmonics are filtered
- Compare low-pass, high-pass, and band-pass shapes

## Theory (short)

$$
f_c = \frac{1}{2\pi R C}
\qquad
\lvert H(f)\rvert = \frac{1}{\sqrt{1+(f/f_c)^2}}
\qquad
\angle H(f) = -\arctan(f/f_c)
$$

At $f_c$: $\lvert H\rvert=1/\sqrt{2}$ (−3 dB), phase = −45°. High-frequency slope ≈ −20 dB/decade.

## Procedure

```bash
mod ad101
cd labs/lab-04-rc-bode
python3 src/explore.py
python3 src/explore.py --figure f12
```

### F12 — Bode explorer

![F12](../assets/img/f12-bode-explorer.png)

- **Try this:** Move R and C. Watch $f_c$ track $1/(2\pi RC)$. Double R and halve C — $f_c$ stays put.
- **What you should see:** Magnitude crosses −3 dB at the marker; phase passes −45°; the dashed asymptote falls at −20 dB/decade past $f_c$.
- **Why an engineer cares:** The Bode plot is the **most-used graph in analog design**. Only the product $RC$ sets the cutoff.

### F13 — Marker ↔ time domain

![F13](../assets/img/f13-bode-time.png)

- **Try this:** Park the marker at $f_c$, then a decade below, then a decade above.
- **What you should see:** At $f_c$, output ≈ 0.707× input, lagging ~45°. Far below: almost identical. Far above: tiny and nearly −90° lag.
- **Why an engineer cares:** Converts "gain and phase" from two numbers into a **visible shrinking and lagging wave** — what a bench measurement physically does.

### F14 — Square through the RC

![F14](../assets/img/f14-square-through-rc.png)

- **Try this:** Raise C (lower $f_c$). Compare input vs output harmonics on the stem plot.
- **What you should see:** Edges round off; high-odd harmonics shrink on the output stems.
- **Why an engineer cares:** Interconnect **RC delay** is why clock speed is capped — foreshadowing parasitic extraction in AD104.

### F15 — Filter-type comparison

![F15](../assets/img/f15-filter-types.png)

- **Try this:** Overlay low-pass / high-pass / band-pass. Move $f_c$.
- **What you should see:** Three different pass/stop patterns around the same $f_c$.
- **Why an engineer cares:** Picking the right filter for a job — leading into AD201.

## Expected results

- With $R=1\,\mathrm{k}\Omega$, $C=100\,\mathrm{nF}$: $f_c \approx 1592$ Hz
- At the marker $f=f_c$: $\lvert H\rvert\approx 0.707$ (−3 dB), phase ≈ −45°
- Raising C on F14 visibly softens square edges and attenuates harmonics 5, 7, 9

## Links

- [Lab package](https://github.com/uoftasic/ad101/tree/main/labs/lab-04-rc-bode)
- Course home: [AD101](README.md)
- Next course: AD102 — Linear Circuits & Fabrication
