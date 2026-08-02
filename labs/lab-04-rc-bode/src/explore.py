#!/usr/bin/env python3
"""Lab 04 — RC filter & Bode (F12–F15).

    python3 src/explore.py
    python3 src/explore.py --figure f12
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

import _path  # noqa: F401

from common.adsig import (  # noqa: E402
    COLORS,
    apply_rc_lowpass,
    configure_matplotlib,
    house_style,
    rc_cutoff,
    rc_response,
    sine,
    spectrum,
    square,
    time_axis,
    to_db,
)


def _build_f12(fig, *_):
    """F12 — Bode explorer with R, C sliders."""
    from matplotlib.widgets import Slider

    ax_mag = fig.add_axes([0.10, 0.55, 0.85, 0.38])
    ax_ph = fig.add_axes([0.10, 0.28, 0.85, 0.22], sharex=ax_mag)
    house_style(ax_mag)
    house_style(ax_ph)

    f = np.logspace(1, 5, 500)
    R0, C0 = 1_000.0, 100e-9  # 1 kΩ, 100 nF → fc ≈ 1.59 kHz
    mag, phase = rc_response(f, R0, C0, "lowpass")
    (lm,) = ax_mag.semilogx(f, to_db(mag), color=COLORS["signal"], lw=2.0)
    (lp,) = ax_ph.semilogx(f, phase, color=COLORS["signal2"], lw=1.8)
    fc_line_m = ax_mag.axvline(rc_cutoff(R0, C0), color=COLORS["marker"], ls="--", lw=1.2)
    fc_line_p = ax_ph.axvline(rc_cutoff(R0, C0), color=COLORS["marker"], ls="--", lw=1.2)
    ax_mag.axhline(-3, color=COLORS["ref"], ls=":", lw=1.0, alpha=0.8)
    # asymptote guide: 0 dB then -20 dB/decade past fc
    ax_mag.set_ylabel("Magnitude (dB)")
    ax_mag.set_title("F12 — Bode explorer (RC low-pass)")
    ax_mag.set_ylim(-60, 5)
    ax_ph.set_ylabel("Phase (°)")
    ax_ph.set_xlabel("Frequency (Hz)")
    ax_ph.set_ylim(-95, 5)

    readout = fig.text(
        0.5,
        0.02,
        "",
        ha="center",
        fontsize=10,
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
    )

    ax_r = fig.add_axes([0.15, 0.16, 0.70, 0.03])
    ax_c = fig.add_axes([0.15, 0.10, 0.70, 0.03])
    s_r = Slider(ax_r, "R (Ω)", 100.0, 10_000.0, valinit=R0, valstep=100.0)
    s_c = Slider(ax_c, "C (nF)", 10.0, 500.0, valinit=C0 * 1e9, valstep=5.0)

    def update(_=None):
        R = s_r.val
        C = s_c.val * 1e-9
        mag, phase = rc_response(f, R, C, "lowpass")
        lm.set_ydata(to_db(mag))
        lp.set_ydata(phase)
        fc = rc_cutoff(R, C)
        fc_line_m.set_xdata([fc, fc])
        fc_line_p.set_xdata([fc, fc])
        # redraw asymptote
        # Clear old asymptote lines beyond the cutoff marker: use a dedicated artist
        if not hasattr(update, "asym"):
            (update.asym,) = ax_mag.semilogx([], [], color=COLORS["ref"], ls="--", lw=1.0, alpha=0.7)
        f_asym = np.array([fc, f[-1]])
        update.asym.set_data(f_asym, [0.0, -20.0 * np.log10(f_asym[1] / fc)])
        readout.set_text(
            f"fc = {fc:.0f} Hz   (= 1/(2πRC))   "
            f"at fc: |H|=−3 dB, phase=−45°   slope → −20 dB/decade"
        )
        fig.canvas.draw_idle()

    s_r.on_changed(update)
    s_c.on_changed(update)
    update()
    return fig


def _build_f13(fig, *_):
    """F13 — Bode marker linked to time-domain I/O."""
    from matplotlib.widgets import Slider

    R, C = 1_000.0, 100e-9
    fc = rc_cutoff(R, C)
    f = np.logspace(1, 5, 400)

    ax_bode = fig.add_axes([0.08, 0.55, 0.40, 0.38])
    ax_t = fig.add_axes([0.55, 0.55, 0.40, 0.38])
    house_style(ax_bode)
    house_style(ax_t)

    mag, phase = rc_response(f, R, C, "lowpass")
    ax_bode.semilogx(f, to_db(mag), color=COLORS["signal"], lw=2.0)
    ax_bode.axhline(-3, color=COLORS["ref"], ls=":", alpha=0.7)
    marker = ax_bode.axvline(fc, color=COLORS["marker"], lw=1.5)
    ax_bode.set_ylabel("Magnitude (dB)")
    ax_bode.set_xlabel("Frequency (Hz)")
    ax_bode.set_title("F13 — Drag the marker")
    ax_bode.set_ylim(-60, 5)

    # Time panel
    t = time_axis(0.02, 50_000.0)
    (lin,) = ax_t.plot(t * 1e3, sine(t, 1.0, fc), color=COLORS["ref"], lw=1.2, label="input")
    (lout,) = ax_t.plot(t * 1e3, sine(t, 0.707, fc, phase_deg=-45), color=COLORS["signal"], lw=1.8, label="output")
    ax_t.set_xlabel("Time (ms)")
    ax_t.set_ylabel("Voltage (V)")
    ax_t.set_title("Time domain at marker")
    ax_t.set_ylim(-1.4, 1.4)
    ax_t.legend(fontsize=7)

    readout = fig.text(
        0.5,
        0.08,
        "",
        ha="center",
        fontsize=10,
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
    )

    ax_f = fig.add_axes([0.15, 0.28, 0.70, 0.04])
    # log-valued slider via exponent
    s_f = Slider(ax_f, "log10(f)", 1.5, 4.5, valinit=np.log10(fc), valstep=0.02)

    def update(_=None):
        f_mark = 10.0 ** s_f.val
        marker.set_xdata([f_mark, f_mark])
        m, p = rc_response(np.array([f_mark]), R, C, "lowpass")
        gain, ph = float(m[0]), float(p[0])
        # Show a few periods
        duration = min(0.02, 8.0 / f_mark)
        tt = time_axis(duration, max(20 * f_mark, 5_000.0))
        xin = sine(tt, 1.0, f_mark)
        xout = sine(tt, gain, f_mark, phase_deg=ph)
        lin.set_data(tt * 1e3, xin)
        lout.set_data(tt * 1e3, xout)
        ax_t.set_xlim(0, duration * 1e3)
        readout.set_text(
            f"f = {f_mark:.0f} Hz   |H| = {gain:.3f} ({to_db(np.array([gain]))[0]:.1f} dB)   "
            f"phase = {ph:.0f}°"
        )
        fig.canvas.draw_idle()

    s_f.on_changed(update)
    update()
    return fig


def _build_f14(fig, *_):
    """F14 — Square wave through RC."""
    from matplotlib.widgets import Slider

    ax_t = fig.add_axes([0.08, 0.50, 0.55, 0.42])
    ax_s = fig.add_axes([0.70, 0.50, 0.27, 0.42])
    house_style(ax_t)
    house_style(ax_s)

    fs = 50_000.0
    t = time_axis(0.04, fs)
    f0 = 200.0
    xin = square(t, amplitude=1.0, frequency=f0)
    R = 1_000.0
    C0 = 200e-9
    y0 = apply_rc_lowpass(xin, fs, R, C0)

    (lin,) = ax_t.plot(t * 1e3, xin, color=COLORS["ref"], lw=1.0, alpha=0.5, label="input square")
    (lout,) = ax_t.plot(t * 1e3, y0, color=COLORS["signal"], lw=1.8, label="filtered")
    ax_t.set_xlabel("Time (ms)")
    ax_t.set_ylabel("Voltage (V)")
    ax_t.set_title("F14 — Square wave through RC (edges round off)")
    ax_t.set_ylim(-1.4, 1.4)
    ax_t.legend(fontsize=7)

    ax_c = fig.add_axes([0.15, 0.28, 0.70, 0.04])
    s_c = Slider(ax_c, "C (nF)", 10.0, 800.0, valinit=C0 * 1e9, valstep=10.0)
    readout = fig.text(0.5, 0.12, "", ha="center", fontsize=10, family="monospace",
                       bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))

    def update(_=None):
        C = s_c.val * 1e-9
        y = apply_rc_lowpass(xin, fs, R, C)
        lout.set_ydata(y)
        fc = rc_cutoff(R, C)
        # Spectrum comparison of input vs output harmonics
        freqs_i, mag_i = spectrum(xin, fs)
        freqs_o, mag_o = spectrum(y, fs)
        ns = np.arange(1, 10, 2)
        ai = [mag_i[int(np.argmin(np.abs(freqs_i - n * f0)))] for n in ns]
        ao = [mag_o[int(np.argmin(np.abs(freqs_o - n * f0)))] for n in ns]
        ax_s.cla()
        house_style(ax_s)
        ax_s.stem(ns - 0.15, ai, linefmt=COLORS["ref"], markerfmt="o", basefmt=" ", label="in")
        ax_s.stem(ns + 0.15, ao, linefmt=COLORS["signal"], markerfmt="s", basefmt=" ", label="out")
        ax_s.set_xlabel("Harmonic #")
        ax_s.set_title("Harmonics")
        ax_s.set_ylim(0, 1.4)
        ax_s.legend(fontsize=7)
        readout.set_text(f"fc = {fc:.0f} Hz   (high harmonics attenuated → rounded edges)")
        fig.canvas.draw_idle()

    s_c.on_changed(update)
    update()
    return fig


def _build_f15(fig, *_):
    """F15 — Low-pass / high-pass / band-pass overlay."""
    from matplotlib.widgets import Slider

    ax = fig.add_axes([0.10, 0.35, 0.85, 0.55])
    house_style(ax)
    f = np.logspace(1, 5, 500)
    R0, C0 = 1_000.0, 100e-9

    def draw(R, C):
        ax.cla()
        house_style(ax)
        for kind, color, label in (
            ("lowpass", COLORS["signal"], "low-pass"),
            ("highpass", COLORS["signal2"], "high-pass"),
            ("bandpass", COLORS["sum"], "band-pass"),
        ):
            mag, _ = rc_response(f, R, C, kind)
            ax.semilogx(f, to_db(mag), color=color, lw=2.0, label=label)
        fc = rc_cutoff(R, C)
        ax.axvline(fc, color=COLORS["marker"], ls="--", lw=1.2, label=f"fc={fc:.0f} Hz")
        ax.axhline(-3, color=COLORS["ref"], ls=":", alpha=0.7)
        ax.set_ylim(-60, 5)
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Magnitude (dB)")
        ax.set_title("F15 — Filter-type comparison")
        ax.legend(fontsize=8, loc="lower left")
        fig.canvas.draw_idle()

    ax_r = fig.add_axes([0.15, 0.18, 0.70, 0.03])
    ax_c = fig.add_axes([0.15, 0.12, 0.70, 0.03])
    s_r = Slider(ax_r, "R (Ω)", 100.0, 10_000.0, valinit=R0, valstep=100.0)
    s_c = Slider(ax_c, "C (nF)", 10.0, 500.0, valinit=C0 * 1e9, valstep=5.0)

    def update(_=None):
        draw(s_r.val, s_c.val * 1e-9)

    s_r.on_changed(update)
    s_c.on_changed(update)
    update()
    return fig


def run_interactive(which: str = "all") -> None:
    import matplotlib.pyplot as plt

    configure_matplotlib(headless=False)
    builders = {
        "f12": _build_f12,
        "f13": _build_f13,
        "f14": _build_f14,
        "f15": _build_f15,
    }
    keys = list(builders) if which == "all" else [which]
    for key in keys:
        fig = plt.figure(figsize=(11, 7))
        builders[key](fig)
    plt.show()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="AD101 Lab 04 — RC filter & Bode")
    parser.add_argument(
        "--figure",
        choices=("f12", "f13", "f14", "f15", "all"),
        default="all",
    )
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
