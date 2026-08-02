#!/usr/bin/env python3
"""Lab 01 — Signal explorer (F1, F2, F3).

Interactive matplotlib widgets. Run inside the IIC-OSIC-TOOLS noVNC desktop:

    cd /foss/designs/modules/ad101/labs/lab-01-signal-explorer
    python3 src/explore.py

Headless contact sheet (no GUI):

    python3 src/explore.py --headless
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import _path  # noqa: F401  — adds labs/ to sys.path

from common.adsig import (  # noqa: E402
    COLORS,
    configure_matplotlib,
    house_style,
    noise,
    peak_to_peak,
    pulse_train,
    rms,
    sine,
    square,
    time_axis,
    triangle,
)


def _build_f1(fig, t, fs):
    """F1 — Sine explorer with live readouts."""
    from matplotlib.widgets import Slider

    ax = fig.add_axes([0.10, 0.38, 0.85, 0.55])
    house_style(ax)
    (line,) = ax.plot(t * 1e3, sine(t), color=COLORS["signal"], lw=1.8)
    period_line = ax.axvline(10.0, color=COLORS["marker"], ls="--", lw=1.2, alpha=0.8)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("F1 — Sine explorer")
    ax.set_ylim(-3.5, 3.5)
    readout = ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes,
        va="top",
        fontsize=9,
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.7),
    )

    ax_a = fig.add_axes([0.15, 0.25, 0.70, 0.03])
    ax_f = fig.add_axes([0.15, 0.20, 0.70, 0.03])
    ax_p = fig.add_axes([0.15, 0.15, 0.70, 0.03])
    ax_d = fig.add_axes([0.15, 0.10, 0.70, 0.03])
    s_a = Slider(ax_a, "Amplitude", 0.1, 3.0, valinit=1.0, valstep=0.05)
    s_f = Slider(ax_f, "Freq (Hz)", 20.0, 400.0, valinit=100.0, valstep=5.0)
    s_p = Slider(ax_p, "Phase (°)", 0.0, 360.0, valinit=0.0, valstep=5.0)
    s_d = Slider(ax_d, "DC offset", -1.5, 1.5, valinit=0.0, valstep=0.05)

    def update(_=None):
        y = sine(t, s_a.val, s_f.val, s_p.val, s_d.val)
        line.set_ydata(y)
        period_ms = 1000.0 / s_f.val
        period_line.set_xdata([period_ms, period_ms])
        readout.set_text(
            f"T = {period_ms:.2f} ms   f = {s_f.val:.0f} Hz\n"
            f"pk-pk = {peak_to_peak(y):.2f} V   RMS = {rms(y):.3f} V"
        )
        fig.canvas.draw_idle()

    for s in (s_a, s_f, s_p, s_d):
        s.on_changed(update)
    update()
    return fig


def _build_f2(fig, t, fs):
    """F2 — Signal zoo: sine / square / triangle / pulse / noise."""
    from matplotlib.widgets import RadioButtons, Slider

    ax = fig.add_axes([0.28, 0.35, 0.67, 0.55])
    house_style(ax)
    (line,) = ax.plot(t * 1e3, sine(t), color=COLORS["signal"], lw=1.6)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("F2 — Signal zoo")
    ax.set_ylim(-2.5, 2.5)

    ax_radio = fig.add_axes([0.02, 0.35, 0.20, 0.50])
    radio = RadioButtons(
        ax_radio,
        ("sine", "square", "triangle", "pulse", "noise"),
        active=0,
    )
    ax_duty = fig.add_axes([0.28, 0.18, 0.60, 0.03])
    ax_amp = fig.add_axes([0.28, 0.12, 0.60, 0.03])
    s_duty = Slider(ax_duty, "Duty", 0.05, 0.95, valinit=0.25, valstep=0.05)
    s_amp = Slider(ax_amp, "Amplitude", 0.2, 2.0, valinit=1.0, valstep=0.1)

    def waveform(kind: str):
        a = s_amp.val
        if kind == "sine":
            return sine(t, amplitude=a, frequency=100.0)
        if kind == "square":
            return square(t, amplitude=a, frequency=100.0, duty=0.5)
        if kind == "triangle":
            return triangle(t, amplitude=a, frequency=100.0)
        if kind == "pulse":
            return pulse_train(t, amplitude=a, frequency=100.0, duty=s_duty.val)
        return noise(t, amplitude=a, seed=42)

    def update(_=None):
        kind = radio.value_selected
        y = waveform(kind)
        line.set_ydata(y)
        fig.canvas.draw_idle()

    radio.on_clicked(update)
    s_duty.on_changed(update)
    s_amp.on_changed(update)
    update()
    return fig


def _build_f3(fig, t, fs):
    """F3 — Two sines + sum, with adjustable phase difference."""
    from matplotlib.widgets import Slider

    ax = fig.add_axes([0.10, 0.40, 0.85, 0.52])
    house_style(ax)
    y1 = sine(t, amplitude=1.0, frequency=100.0, phase_deg=0.0)
    y2 = sine(t, amplitude=1.0, frequency=100.0, phase_deg=60.0)
    (l1,) = ax.plot(t * 1e3, y1, color=COLORS["signal"], lw=1.4, label="signal A", alpha=0.85)
    (l2,) = ax.plot(t * 1e3, y2, color=COLORS["signal2"], lw=1.4, label="signal B", alpha=0.85)
    (ls,) = ax.plot(t * 1e3, y1 + y2, color=COLORS["sum"], lw=2.0, label="sum A+B")
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("F3 — Two-signal comparator (phase = delay)")
    ax.set_ylim(-3.0, 3.0)
    readout = ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes,
        va="top",
        fontsize=9,
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.7),
    )

    ax_ph = fig.add_axes([0.15, 0.22, 0.70, 0.03])
    ax_f = fig.add_axes([0.15, 0.15, 0.70, 0.03])
    s_ph = Slider(ax_ph, "Phase Δ (°)", 0.0, 360.0, valinit=60.0, valstep=5.0)
    s_f = Slider(ax_f, "Freq (Hz)", 40.0, 300.0, valinit=100.0, valstep=5.0)

    def update(_=None):
        y1 = sine(t, 1.0, s_f.val, 0.0)
        y2 = sine(t, 1.0, s_f.val, s_ph.val)
        l1.set_ydata(y1)
        l2.set_ydata(y2)
        ls.set_ydata(y1 + y2)
        # delay = phase / (360 * f)
        delay_ms = (s_ph.val / 360.0) * (1000.0 / s_f.val)
        readout.set_text(
            f"Δφ = {s_ph.val:.0f}°   delay = {delay_ms:.3f} ms\n"
            f"(at {s_f.val:.0f} Hz, one period = {1000.0 / s_f.val:.2f} ms)"
        )
        fig.canvas.draw_idle()

    s_ph.on_changed(update)
    s_f.on_changed(update)
    update()
    return fig


def run_interactive(which: str = "all") -> None:
    import matplotlib.pyplot as plt

    configure_matplotlib(headless=False)
    t = time_axis(0.05, 10_000.0)
    fs = 10_000.0
    builders = {"f1": _build_f1, "f2": _build_f2, "f3": _build_f3}
    keys = list(builders) if which == "all" else [which]
    for key in keys:
        fig = plt.figure(figsize=(9.5, 6.5))
        builders[key](fig, t, fs)
    plt.show()


def run_headless(out_dir: Path) -> list[Path]:
    """Contact sheet of default views for each explorer."""
    import matplotlib.pyplot as plt

    configure_matplotlib(headless=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Prefer the dedicated exporter for docs figures; this is a quick fallback.
    from export_figures import export_all

    return export_all(out_dir)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AD101 Lab 01 — Signal explorer")
    parser.add_argument(
        "--figure",
        choices=("f1", "f2", "f3", "all"),
        default="all",
        help="Which explorer to open",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Export contact-sheet PNGs instead of opening a GUI",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
        help="Output directory for --headless",
    )
    args = parser.parse_args(argv)

    if args.headless:
        paths = run_headless(args.out)
        for p in paths:
            print(f"wrote {p}")
        return 0

    run_interactive(args.figure)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
