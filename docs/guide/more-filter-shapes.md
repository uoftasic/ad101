# More filter shapes

A three-band EQ has bass, mid and treble knobs, and behind each knob is a filter with its own shape, which keeps a different slice of the spectrum. Circuits make the same three shapes out of the same R and C parts, arranged differently for each shape.

![F15 — Filter types](../assets/img/f15-filter-types.png)

| Type | Passes | Blocks | EQ knob it resembles |
|------|--------|--------|------------------------|
| Low-pass | Slow | Fast | Treble cut |
| High-pass | Fast | Slow | Bass cut |
| Band-pass | A middle band | Too slow and too fast | Mid boost / isolate |

All three curves in F15 are built around the same $f_c$, and which side of $f_c$ a filter keeps depends only on the shape of its formula. AD201 comes back to these shapes as blocks you design on purpose, not only as parasitics that turn up by accident.

In [Lab 04](../labs/lab-04-rc-bode-overview.md), Part 4, you'll overlay the three shapes on the F15 explorer, and then plot them from their formulas in a script of your own.

## The three plots

You now have the three plots this course set out to teach: a signal in time (Movement I), a signal as a recipe of sines (Movements II and III), and what a circuit does to that recipe (Movement IV). Analog engineers read these plots every day, and the later analog courses assume you can read them too.

That's the end of Movement IV. Next comes [Lab 04: RC filter and Bode](../labs/lab-04-rc-bode-overview.md), and after it the capstone, [Lab 05: Signal workshop](../labs/lab-05-signal-workshop-overview.md), where you write a script that makes all three plots yourself.

## Where to go next

| Next course | What you carry forward |
|-------------|------------------------|
| AD102 | Passives on silicon: fabricating R, C, L |
| AD103 | Nonlinear devices (diode, MOSFET) in XSchem |
| AD104 | Layout parasitics (why every node is an RC) |
| AD202 (planned) | Sampling and ADCs, where Nyquist matters for real |
