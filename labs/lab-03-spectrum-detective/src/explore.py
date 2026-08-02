#!/usr/bin/env python3
"""Lab 03 — Spectrum detective (F7–F11).

    python3 src/explore.py
    python3 src/explore.py --figure f8
    python3 src/check.py --guess 237
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

import _path  # noqa: F401

from common.adsig import (  # noqa: E402
    COLORS,
    configure_matplotlib,
    house_style,
    noise,
    soft_clip,
    spectrum,
    sine,
    square,
    thd,
    time_axis,
    to_db,
)

# Secret tone for F8 — students find it from the spectrum, then confirm with check.py
HIDDEN_TONE_HZ = 237.0
HIDDEN_SEED = 7


def recipe(name: str, t: np.ndarray, fs: float) -> np.ndarray:
    if name == "pure tone":
        return sine(t, amplitude=1.0, frequency=200.0)
    if name == "two tones":
        return sine(t, 1.0, 150.0) + 0.6 * sine(t, 1.0, 350.0)
    if name == "tone + noise":
        return sine(t, 0.5, 200.0) + noise(t, amplitude=1.5, seed=42)
    if name == "AM":
        carrier = sine(t, 1.0, 500.0)
        envelope = 1.0 + 0.5 * sine(t, 1.0, 40.0)
        return envelope * carrier
    if name == "square":
        return square(t, amplitude=1.0, frequency=100.0)
    raise ValueError(name)


def _build_f7(fig, t, fs):
    from matplotlib.widgets import CheckButtons, RadioButtons

    ax_t = fig.add_axes([0.28, 0.55, 0.68, 0.38])
    ax_f = fig.add_axes([0.28, 0.10, 0.68, 0.38])
    house_style(ax_t)
    house_style(ax_f)

    y0 = recipe("pure tone", t, fs)
    (lt,) = ax_t.plot(t * 1e3, y0, color=COLORS["signal"], lw=1.2)
    freqs, mag = spectrum(y0, fs)
    (lf,) = ax_f.plot(freqs, to_db(mag), color=COLORS["spectrum"], lw=1.2)
    ax_t.set_title("F7 — Twin panel: time ↔ frequency")
    ax_t.set_ylabel("Voltage (V)")
    ax_f.set_xlabel("Frequency (Hz)")
    ax_f.set_ylabel("Magnitude (dB)")
    ax_f.set_xlim(0, 2000)
    ax_f.set_ylim(-80, 5)

    ax_radio = fig.add_axes([0.02, 0.40, 0.20, 0.50])
    radio = RadioButtons(
        ax_radio,
        ("pure tone", "two tones", "tone + noise", "AM", "square"),
        active=0,
    )
    ax_opts = fig.add_axes([0.02, 0.10, 0.20, 0.22])
    opts = CheckButtons(ax_opts, ("dB scale", "log freq"), actives=[True, False])

    def update(_=None):
        y = recipe(radio.value_selected, t, fs)
        lt.set_ydata(y)
        ax_t.set_ylim(y.min() - 0.2, y.max() + 0.2)
        freqs, mag = spectrum(y, fs)
        use_db, use_log = opts.get_status()
        ax_f.cla()
        house_style(ax_f)
        yy = to_db(mag) if use_db else mag
        if use_log:
            ax_f.semilogx(np.maximum(freqs, 1.0), yy, color=COLORS["spectrum"], lw=1.2)
            ax_f.set_xlim(10, fs / 2)
        else:
            ax_f.plot(freqs, yy, color=COLORS["spectrum"], lw=1.2)
            ax_f.set_xlim(0, min(2000, fs / 2))
        ax_f.set_xlabel("Frequency (Hz)")
        ax_f.set_ylabel("Magnitude (dB)" if use_db else "Magnitude")
        if use_db:
            ax_f.set_ylim(-80, 5)
        fig.canvas.draw_idle()

    radio.on_clicked(update)
    opts.on_clicked(update)
    update()
    return fig


def _build_f8(fig, t, fs):
    from matplotlib.widgets import Slider

    ax_t = fig.add_axes([0.10, 0.55, 0.85, 0.38])
    ax_f = fig.add_axes([0.10, 0.12, 0.85, 0.35])
    house_style(ax_t)
    house_style(ax_f)

    tone_amp = 0.15
    noise_amp0 = 1.2
    hidden = tone_amp * sine(t, 1.0, HIDDEN_TONE_HZ)
    nse = noise(t, amplitude=noise_amp0, seed=HIDDEN_SEED)
    y0 = hidden + nse
    (lt,) = ax_t.plot(t * 1e3, y0, color=COLORS["signal"], lw=0.8)
    ax_t.set_title("F8 — Hidden-tone hunt (find the frequency in the spectrum)")
    ax_t.set_ylabel("Voltage (V)")
    freqs, mag = spectrum(y0, fs)
    (lf,) = ax_f.plot(freqs, to_db(mag), color=COLORS["spectrum"], lw=1.0)
    ax_f.set_xlim(0, 1000)
    ax_f.set_ylim(-80, 5)
    ax_f.set_xlabel("Frequency (Hz)")
    ax_f.set_ylabel("Magnitude (dB)")
    ax_f.axvline(HIDDEN_TONE_HZ, color=COLORS["marker"], ls=":", alpha=0.0)  # invisible hint

    note = fig.text(
        0.5,
        0.02,
        "Tip: look for a narrow peak above the noise floor. Confirm with: python3 src/check.py --guess <Hz>",
        ha="center",
        fontsize=9,
    )

    ax_snr = fig.add_axes([0.20, 0.48, 0.60, 0.03])
    s_noise = Slider(ax_snr, "Noise amp", 0.1, 3.0, valinit=noise_amp0, valstep=0.1)

    def update(_=None):
        y = tone_amp * sine(t, 1.0, HIDDEN_TONE_HZ) + noise(t, amplitude=s_noise.val, seed=HIDDEN_SEED)
        lt.set_ydata(y)
        ax_t.set_ylim(y.min() - 0.1, y.max() + 0.1)
        freqs, mag = spectrum(y, fs)
        lf.set_data(freqs, to_db(mag))
        fig.canvas.draw_idle()

    s_noise.on_changed(update)
    update()
    return fig


def _build_f9(fig, t, fs):
    from matplotlib.widgets import Slider

    ax_t = fig.add_axes([0.10, 0.55, 0.55, 0.38])
    ax_f = fig.add_axes([0.72, 0.55, 0.25, 0.38])
    house_style(ax_t)
    house_style(ax_f)

    f0 = 100.0
    clean = sine(t, 1.0, f0)
    y0 = soft_clip(clean, gain=1.0)
    (lt,) = ax_t.plot(t * 1e3, y0, color=COLORS["signal"], lw=1.4)
    ax_t.plot(t * 1e3, clean, color=COLORS["ref"], lw=0.8, alpha=0.5, label="input")
    ax_t.set_title("F9 — Distortion & THD")
    ax_t.set_ylabel("Voltage (V)")
    ax_t.set_ylim(-1.5, 1.5)
    ax_t.legend(fontsize=7)

    readout = fig.text(
        0.5,
        0.08,
        "",
        ha="center",
        fontsize=11,
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
    )

    ax_g = fig.add_axes([0.15, 0.30, 0.70, 0.04])
    s_g = Slider(ax_g, "Gain (into tanh)", 0.5, 8.0, valinit=1.5, valstep=0.1)

    def update(_=None):
        y = soft_clip(clean, gain=s_g.val)
        lt.set_ydata(y)
        freqs, mag = spectrum(y, fs)
        ax_f.cla()
        house_style(ax_f)
        # Show first 8 harmonics
        ns = np.arange(1, 9)
        amps = [mag[int(np.argmin(np.abs(freqs - n * f0)))] for n in ns]
        ax_f.stem(ns, amps, linefmt=COLORS["spectrum"], markerfmt="o", basefmt=" ")
        ax_f.set_xlabel("Harmonic #")
        ax_f.set_title("Spectrum")
        ax_f.set_ylim(0, 1.2)
        val = thd(y, fs, f0, n_harmonics=7)
        readout.set_text(f"THD = {100.0 * val:.1f}%   (gain = {s_g.val:.1f})")
        fig.canvas.draw_idle()

    s_g.on_changed(update)
    update()
    return fig


def _build_f10(fig, t_base, fs):
    """F10 — Spectral leakage (stretch)."""
    from matplotlib.widgets import CheckButtons, Slider

    ax = fig.add_axes([0.10, 0.35, 0.85, 0.55])
    house_style(ax)
    ax.set_title("F10 — Spectral leakage (stretch)")
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude (dB)")

    ax_n = fig.add_axes([0.15, 0.18, 0.70, 0.04])
    s_cycles = Slider(ax_n, "Cycles in window", 3.0, 12.0, valinit=5.0, valstep=0.1)
    ax_w = fig.add_axes([0.15, 0.05, 0.25, 0.10])
    win_btn = CheckButtons(ax_w, ("Hann window",), actives=[False])

    def update(_=None):
        # Rebuild a window with the requested number of cycles of a 200 Hz tone
        f0 = 200.0
        n_cycles = s_cycles.val
        duration = n_cycles / f0
        t = time_axis(duration, fs)
        x = sine(t, 1.0, f0)
        if win_btn.get_status()[0]:
            x = x * np.hanning(len(x))
        freqs, mag = spectrum(x, fs)
        ax.cla()
        house_style(ax)
        ax.plot(freqs, to_db(mag), color=COLORS["spectrum"], lw=1.2)
        ax.axvline(f0, color=COLORS["marker"], ls="--", alpha=0.6, label=f"{f0:.0f} Hz")
        ax.set_xlim(0, 600)
        ax.set_ylim(-80, 5)
        ax.set_title(
            f"F10 — Leakage   cycles={n_cycles:.1f}  "
            f"({'Hann' if win_btn.get_status()[0] else 'rectangular'} window)"
        )
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Magnitude (dB)")
        ax.legend(fontsize=8)
        integer = abs(n_cycles - round(n_cycles)) < 0.02
        tip = "clean spike (integer cycles)" if integer else "smeared peak (leakage!)"
        ax.text(0.98, 0.95, tip, transform=ax.transAxes, ha="right", va="top", fontsize=9,
                bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.7))
        fig.canvas.draw_idle()

    s_cycles.on_changed(update)
    win_btn.on_clicked(update)
    update()
    return fig


def _build_f11(fig, t_full, fs_full):
    """F11 — Sampling and aliasing."""
    from matplotlib.widgets import Slider

    f_tone = 200.0
    ax_t = fig.add_axes([0.10, 0.55, 0.55, 0.38])
    ax_s = fig.add_axes([0.72, 0.55, 0.25, 0.38])
    house_style(ax_t)
    house_style(ax_s)

    # Dense "true" waveform for reference
    t_true = np.linspace(0, 0.04, 4000)
    true = sine(t_true, 1.0, f_tone)
    ax_t.plot(t_true * 1e3, true, color=COLORS["ref"], lw=1.0, alpha=0.4, label="true")
    (l_samp,) = ax_t.plot([], [], "o-", color=COLORS["signal"], ms=4, lw=1.2, label="samples")
    (l_recon,) = ax_t.plot([], [], color=COLORS["sum"], lw=1.6, label="apparent")
    ax_t.set_xlim(0, 40)
    ax_t.set_ylim(-1.4, 1.4)
    ax_t.set_xlabel("Time (ms)")
    ax_t.set_title("F11 — Sampling & aliasing")
    ax_t.legend(fontsize=7, loc="upper right")

    note = fig.text(
        0.5,
        0.08,
        "",
        ha="center",
        fontsize=10,
        family="monospace",
        bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8),
    )

    ax_fs = fig.add_axes([0.15, 0.30, 0.70, 0.04])
    s_fs = Slider(ax_fs, "Sample rate (Hz)", 50.0, 1000.0, valinit=1000.0, valstep=10.0)

    def update(_=None):
        fs = s_fs.val
        n = int(0.04 * fs)
        t_s = np.arange(n) / fs
        samples = sine(t_s, 1.0, f_tone)
        l_samp.set_data(t_s * 1e3, samples)

        # Apparent frequency via folding
        # alias = |f - k*fs| closest to 0..fs/2
        nyquist = fs / 2.0
        # fold into [-fs/2, fs/2]
        aliased = ((f_tone + nyquist) % fs) - nyquist
        aliased = abs(aliased)
        apparent = sine(t_true, 1.0, aliased if aliased > 1e-6 else f_tone)
        # Only draw "apparent" when undersampled
        if fs < 2 * f_tone:
            l_recon.set_data(t_true * 1e3, apparent)
            l_recon.set_alpha(1.0)
        else:
            l_recon.set_data([], [])

        # Stem of one-sided spectrum of samples
        freqs, mag = spectrum(samples, fs)
        ax_s.cla()
        house_style(ax_s)
        ax_s.stem(
            freqs[:: max(1, len(freqs) // 40)],
            mag[:: max(1, len(freqs) // 40)],
            linefmt=COLORS["spectrum"],
            markerfmt=" ",
            basefmt=" ",
        )
        ax_s.plot(freqs, mag, color=COLORS["spectrum"], lw=1.0)
        ax_s.axvline(min(f_tone, nyquist), color=COLORS["marker"], ls="--", alpha=0.7)
        ax_s.set_xlim(0, max(nyquist, 50))
        ax_s.set_title("Spectrum of samples")
        ax_s.set_xlabel("Hz")

        status = "OK (fs > 2f)" if fs >= 2 * f_tone else f"ALIASED → appears as {aliased:.0f} Hz"
        note.set_text(f"tone = {f_tone:.0f} Hz   fs = {fs:.0f} Hz   Nyquist = {nyquist:.0f} Hz   {status}")
        fig.canvas.draw_idle()

    s_fs.on_changed(update)
    update()
    return fig


def run_interactive(which: str = "all") -> None:
    import matplotlib.pyplot as plt

    configure_matplotlib(headless=False)
    t = time_axis(0.1, 10_000.0)
    fs = 10_000.0
    builders = {
        "f7": _build_f7,
        "f8": _build_f8,
        "f9": _build_f9,
        "f10": _build_f10,
        "f11": _build_f11,
    }
    keys = list(builders) if which == "all" else [which]
    for key in keys:
        fig = plt.figure(figsize=(11, 7))
        builders[key](fig, t, fs)
    plt.show()


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="AD101 Lab 03 — Spectrum detective")
    parser.add_argument(
        "--figure",
        choices=("f7", "f8", "f9", "f10", "f11", "all"),
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
