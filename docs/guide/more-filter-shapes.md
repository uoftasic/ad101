# More filter shapes

A three-band EQ has bass, mid and treble knobs: three filter shapes, each keeping a different slice of the spectrum. Circuits build the same three shapes from the same R and C parts, arranged differently.

![F15 — Filter types](../assets/img/f15-filter-types.png)

| Type | Passes | Blocks | EQ knob it resembles |
|------|--------|--------|------------------------|
| Low-pass | Slow | Fast | Treble cut |
| High-pass | Fast | Slow | Bass cut |
| Band-pass | A middle band | Too slow and too fast | Mid boost / isolate |

All three curves in F15 are built around the same $f_c$. Only the shape of the formula changes which side of $f_c$ gets kept. AD201 picks these shapes up again as intentional design blocks, not just accidental parasitics.

You'll overlay the three shapes on the F15 explorer, then plot them from their formulas in your own script, in [Lab 04](../labs/lab-04-rc-bode-overview.md), Part 4.

## The three plots

You now have the three plots this course set out to teach: a signal in time (Movement I), a signal as a recipe of sines (Movements II and III), and what a circuit does to that recipe (Movement IV). Every analog engineer reads them daily, and later analog courses assume you can read them too.

That's the end of Movement IV. Next: [Lab 04: RC filter and Bode](../labs/lab-04-rc-bode-overview.md), then the capstone, [Lab 05: Signal workshop](../labs/lab-05-signal-workshop-overview.md), where you write a script that does all three yourself.

## Where to go next

| Next course | What you carry forward |
|-------------|------------------------|
| AD102 | Passives on silicon: fabricating R, C, L |
| AD103 | Nonlinear devices (diode, MOSFET) in XSchem |
| AD104 | Layout parasitics (why every node is an RC) |
| AD202 (planned) | Sampling, ADCs: Nyquist for real |
