# Filtering a beat

A kick drum heard through a wall sounds muffled: you still hear the thump, but the sharp attack is gone, smoothed into something rounder and softer. That's a low-pass filter acting on a real, harmonic-rich signal instead of a lone sine. A square wave is the clearest circuit example of the same effect.

## A square wave through the filter

From Movement II, a square wave is a pile of odd harmonics. A low-pass filter turns down the high harmonics, and those are the ones that make the sharp edges, so the edges round off. Lower the cutoff further and the square turns into a soft, rounded blob: the electrical version of the muffled kick drum.

![F14 — Square through RC](../assets/img/f14-square-through-rc.png)

The knob is the same one as on [Filters are tone knobs](../guide/filters-are-tone-knobs.md): raise $C$ and $f_c$ drops, and the edges soften more with each step. The high odd harmonics shrink first.

You'll raise C on the F14 explorer and compare input and output harmonics, then filter a square wave in your own script, in [Lab 04](../labs/lab-04-rc-bode-overview.md), Part 3.

## Parasitic RC

Every node on a chip has **parasitic** resistance and capacitance: R and C that nobody drew on the schematic. So every node is one of these filters, whether you designed it in or not. That's why clock speeds have a ceiling, and it's a preview of the parasitic-extraction work in AD104.

Next: [More filter shapes](../guide/more-filter-shapes.md)
