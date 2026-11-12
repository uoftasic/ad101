# Getting started

AD101 is a primer on **signals**, the voltages that move through every analog circuit. You'll learn to read the three plots an analog engineer works with: the **waveform** (voltage against time), the **spectrum** (how strong each frequency is) and the **Bode plot** (what a circuit does to a signal).

The way in is something you already know: music. A signal is a voltage that wiggles the same way sound pressure wiggles when you hum a note. A chord is signals added together. An instrument's timbre is a recipe of extra harmonics on top of the main pitch. A filter is a tone knob. Every idea in this course has a musical twin, and the guide uses it on purpose.

You don't need a musical background. Each analogy is explained the first time it's used, and [Music and signals](reference/music-and-signals.md) collects them in one table. The math is high-school level: sine, logarithm and basic algebra, with no calculus.

## How the course is organized

The course has four movements followed by a capstone lab, Lab 05. Each movement is a few short guide pages and then a lab. The Course path table on the [home page](README.md) lists every step in order with a time estimate.

Guide pages are for reading: concepts, figures and worked examples. You don't need a terminal open. Labs are where you run things, and they teach each idea two ways:

1. **Drag it.** Labs 01–04 each come with an interactive explorer: plot windows with sliders, numbered F1 to F15 (F for figure). Dragging a slider while a plot updates is the fastest way to build intuition for how a knob changes a curve.
2. **Write it.** The same labs give you short Python snippets that you save, run and change yourself. [Lab 05: Signal workshop](labs/lab-05-signal-workshop-overview.md) has no sliders at all. There you assemble those ideas into your own signal-analysis script, end to end, and listen to what a filter does to a chord.

Do both. Dragging a slider builds intuition quickly, and writing the script is what lets you use that intuition on a signal nobody built a slider for.

The figures on these guide pages come from the same explorer scripts you run in the labs, so what you read matches what you'll see.

If an explorer window won't open, each explorer has a `--headless` mode that writes its figures to PNG files instead. [Python in the workbench](reference/python-in-the-workbench.md) covers that and the other common problems. [Reading plots](reference/reading-plots.md) is a one-page cheat sheet for all three plots.

## Out of scope

- It isn't a replacement for the ECE signals courses.
- It doesn't go deep into Fourier proofs or complex numbers.
- It doesn't use XSchem or ngspice yet. Those start in AD102 and AD103.

You'll set up AD101 inside your IC101 workspace at the start of [Lab 01](labs/lab-01-signal-explorer-overview.md), Part 1.

Next: [What is a signal?](guide/what-is-a-signal.md)
