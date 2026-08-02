#!/usr/bin/env python3
"""Lab 02 — Harmonic builder (F4, F5, F6).

    python3 src/explore.py
    python3 src/explore.py --headless
"""

from __future__ import annotations

import argparse
from pathlib import Path

import _path  # noqa: F401

from common.adsig import (  # noqa: E402
    COLORS,
    configure_matplotlib,
    harmonic_sum,
    house_style,
    pulse_train,
    spectrum,
    square,
    time_axis,
)


def _build_f4_f5(fig, t, fs):
    """F4 Fourier assembler + F5 live spectrum, side by side."""
    from matplotlib.widgets import CheckButtons, Slider
    import numpy as np

    ax_t = fig.add_axes([0.08, 0.42, 0.55, 0.50])
    ax_s = fig.add_axes([0.70, 0.42, 0.27, 0.50])
    house_style(ax_t)
    house_style(ax_s)

    f0 = 100.0
    ideal = square(t, amplitude=1.0, frequency=f0)
    (l_ideal,) = ax_t.plot(
        t * 1e3, ideal, color=COLORS["ref"], lw=1.0, alpha=0.55, label="ideal square"
    )
    (l_sum,) = ax_t.plot(t * 1e3, ideal, color=COLORS["signal"], lw=1.8, label="sum")
    ax_t.set_xlabel("Time (ms)")
    ax_t.set_ylabel("Voltage (V)")
    ax_t.set_title("F4 — Fourier assembler")
    ax_t.set_ylim(-1.6, 1.6)
    ax_t.legend(loc="upper right", fontsize=7)

    harmonics = [1, 3, 5, 7, 9]
    default_amps = {n: 4.0 / (n * np.pi) for n in harmonics}
    markers = ax_s.stem([0], [0], linefmt=COLORS["spectrum"], markerfmt="o", basefmt=" ")
    # stem returns StemContainer; we'll replace data each update
    ax_s.set_xlabel("Harmonic #")
    ax_s.set_ylabel("Amplitude")
    ax_s.set_title("F5 — Spectrum")
    ax_s.set_xlim(0, 10)
    ax_s.set_ylim(0, 1.5)

    ax_check = fig.add_axes([0.08, 0.08, 0.18, 0.28])
    labels = [f"n={n}" for n in harmonics]
    checks = CheckButtons(ax_check, labels, actives=[True] * len(harmonics))

    sliders = []
    for i, n in enumerate(harmonics):
        ax_sl = fig.add_axes([0.35, 0.30 - i * 0.05, 0.50, 0.03])
        sliders.append(
            Slider(ax_sl, f"A{n}", 0.0, 1.5, valinit=default_amps[n], valstep=0.02)
        )

    def active_terms():
        status = checks.get_status()
        ns, amps = [], []
        for on, n, s in zip(status, harmonics, sliders):
            if on:
                ns.append(n)
                amps.append(s.val)
        return ns, amps

    def update(_=None):
        ns, amps = active_terms()
        if ns:
            y = harmonic_sum(t, f0, ns, amps)
        else:
            y = np.zeros_like(t)
        l_sum.set_ydata(y)

        # Rebuild stem
        ax_s.cla()
        house_style(ax_s)
        if ns:
            ax_s.stem(ns, amps, linefmt=COLORS["spectrum"], markerfmt="o", basefmt=" ")
            # 1/n envelope guide
            n_guide = np.arange(1, 10)
            ax_s.plot(
                n_guide,
                4.0 / (n_guide * np.pi),
                color=COLORS["marker"],
                ls="--",
                lw=1.0,
                alpha=0.7,
                label="4/(nπ)",
            )
            ax_s.legend(fontsize=7)
        ax_s.set_xlabel("Harmonic #")
        ax_s.set_ylabel("Amplitude")
        ax_s.set_title("F5 — Spectrum")
        ax_s.set_xlim(0, 10)
        ax_s.set_ylim(0, 1.5)
        fig.canvas.draw_idle()

    checks.on_clicked(update)
    for s in sliders:
        s.on_changed(update)
    update()
    return fig


def _build_f6(fig, t, fs):
    """F6 — Duty cycle ↔ spectrum."""
    from matplotlib.widgets import Slider
    import numpy as np

    ax_t = fig.add_axes([0.08, 0.45, 0.55, 0.45])
    ax_s = fig.add_axes([0.70, 0.45, 0.27, 0.45])
    house_style(ax_t)
    house_style(ax_s)

    f0 = 100.0
    (l_t,) = ax_t.plot(t * 1e3, pulse_train(t, frequency=f0, duty=0.5), color=COLORS["signal"], lw=1.6)
    ax_t.set_xlabel("Time (ms)")
    ax_t.set_ylabel("Voltage (V)")
    ax_t.set_title("F6 — Pulse train (duty cycle)")
    ax_t.set_ylim(-0.2, 1.4)

    ax_duty = fig.add_axes([0.15, 0.22, 0.70, 0.04])
    s_duty = Slider(ax_duty, "Duty", 0.05, 0.95, valinit=0.50, valstep=0.05)

    note = fig.text(
        0.5,
        0.08,
        "",
        ha="center",
        fontsize=9,
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.7),
    )

    def update(_=None):
        y = pulse_train(t, amplitude=1.0, frequency=f0, duty=s_duty.val)
        l_t.set_ydata(y)
        freqs, mag = spectrum(y, fs)
        # Show first ~10 harmonics as stems
        harm_n = np.arange(0, 11)
        harm_f = harm_n * f0
        harm_a = []
        for f in harm_f:
            idx = int(np.argmin(np.abs(freqs - f)))
            harm_a.append(mag[idx])
        ax_s.cla()
        house_style(ax_s)
        ax_s.stem(harm_n, harm_a, linefmt=COLORS["spectrum"], markerfmt="o", basefmt=" ")
        ax_s.set_xlabel("Harmonic #")
        ax_s.set_ylabel("Amplitude")
        ax_s.set_title("Spectrum")
        ax_s.set_xlim(-0.5, 10.5)
        ax_s.set_ylim(0, 1.1)
        tip = "even harmonics GONE (50% duty)" if abs(s_duty.val - 0.5) < 0.01 else "even harmonics PRESENT"
        note.set_text(f"duty = {s_duty.val:.0%}   →   {tip}")
        fig.canvas.draw_idle()

    s_duty.on_changed(update)
    update()
    return fig


def run_interactive(which: str = "all") -> None:
    import matplotlib.pyplot as plt

    configure_matplotlib(headless=False)
    t = time_axis(0.05, 10_000.0)
    fs = 10_000.0
    if which in ("all", "f4", "f5"):
        fig = plt.figure(figsize=(11, 6.5))
        _build_f4_f5(fig, t, fs)
    if which in ("all", "f6"):
        fig = plt.figure(figsize=(11, 6.0))
        _build_f6(fig, t, fs)
    plt.show()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="AD101 Lab 02 — Harmonic builder")
    parser.add_argument("--figure", choices=("f4", "f5", "f6", "all"), default="all")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    args = parser.parse_args(argv)
    if args.headless:
        from export_figures import export_all

        configure_matplotlib(headless=True)
        for p in export_all(args.out):
            print(f"wrote {p}")
        return 0
    run_interactive(args.figure)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
