# Getting started

AD101 is a primer on **signals**, the voltages that move through every analog circuit. By the end of it you'll be able to read the three plots an analog engineer works with most: the **waveform**, which shows voltage against time; the **spectrum**, which shows how strong each frequency is; and the **Bode plot**, which shows what a circuit does to a signal.

We start from something you already know, which is music. A signal is a voltage that wiggles the same way sound pressure wiggles when you hum a note, and a chord is several of those signals added together. An instrument's timbre comes from the particular recipe of extra harmonics it adds on top of the main pitch, and a filter does the same job as a tone knob. Every idea in this course has a musical twin like these, and the guide uses them on purpose.

You don't need a musical background to follow along. Each analogy is explained the first time it's used, and [Music and signals](../reference/music-and-signals.md) collects them all in one table. The math is high-school level (sine, logarithm and basic algebra) and there's no calculus.

## How the course is organized

The course has four movements followed by a capstone lab, Lab 05. Each movement is a few short guide pages followed by a lab, and the Course path table on the [home page](../index.md) lists every step in order with a time estimate.

Guide pages are for reading: they hold the concepts, figures and worked examples, and you don't need a terminal open while you read them. The labs are where you run things, and they teach each idea in two ways:

1. **Drag it.** Labs 01–04 each come with an interactive explorer, a set of plot windows with sliders, numbered F1 to F15 (F for figure). Dragging a slider and watching the plot update is the fastest way to build intuition for how a knob changes a curve.
2. **Write it.** The same labs give you short Python snippets that you save, run and change yourself. [Lab 05: Signal workshop](../labs/lab-05-signal-workshop-overview.md) has no sliders at all. In that lab you put those ideas together into your own signal-analysis script, end to end, and listen to what a filter does to a chord.

It's worth doing both. Dragging a slider builds intuition quickly, but writing the script is what lets you apply that intuition to a signal nobody has built a slider for.

The figures on these guide pages come from the same explorer scripts you run in the labs, so what you read here matches what you'll see on your own screen.

If an explorer window won't open, every explorer has a `--headless` mode that writes its figures to PNG files instead. [Python in the workbench](../reference/python-in-the-workbench.md) explains that mode and covers the other common problems, and [Reading plots](../reference/reading-plots.md) is a one-page cheat sheet for all three kinds of plot.

## Out of scope

- AD101 doesn't replace the ECE signals courses.
- It doesn't go deep into Fourier proofs or complex numbers.
- It doesn't use XSchem or ngspice yet; you'll start on those in AD102 and AD103.

You'll load AD101 into your IC101 workspace in Part 1 of [Lab 01](../labs/lab-01-signal-explorer-overview.md).

Next: [What is a signal?](../guide/what-is-a-signal.md)
