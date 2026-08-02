#!/usr/bin/env python3
"""Export Lab 04 documentation figures (F12–F15)."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

_SRC = Path(__file__).resolve().parent
sys.path.insert(0, str(_SRC))
import _path  # noqa: E402, F401

from common.adsig import (  # noqa: E402
    COLORS,
    apply_rc_lowpass,
    house_style,
    rc_cutoff,
    rc_response,
    sine,
    spectrum,
    square,
    time_axis,
    to_db,
)


def _f12(path: Path) -> Path:
    R, C = 1_000.0, 100e-9
    fc = rc_cutoff(R, C)
    f = np.logspace(1, 5, 500)
    mag, phase = rc_response(f, R, C, "lowpass")
    fig, (ax_m, ax_p) = plt.subplots(2, 1, figsize=(8, 5.5), sharex=True)
    house_style(ax_m)
    house_style(ax_p)
    ax_m.semilogx(f, to_db(mag), color=COLORS["signal"], lw=2.0)
    ax_m.axvline(fc, color=COLORS["marker"], ls="--", label=f"fc={fc:.0f} Hz")
    ax_m.axhline(-3, color=COLORS["ref"], ls=":", label="−3 dB")
    # asymptote
    ax_m.semilogx([fc, f[-1]], [0, -20 * np.log10(f[-1] / fc)], color=COLORS["ref"], ls="--", lw=1.0, alpha=0.7, label="−20 dB/dec")
    ax_m.set_ylabel("Magnitude (dB)")
    ax_m.set_ylim(-60, 5)
    ax_m.set_title("F12 — Bode magnitude (RC low-pass)")
    ax_m.legend(fontsize=8)

    ax_p.semilogx(f, phase, color=COLORS["signal2"], lw=1.8)
    ax_p.axvline(fc, color=COLORS["marker"], ls="--")
    ax_p.axhline(-45, color=COLORS["ref"], ls=":", alpha=0.7)
    ax_p.set_ylabel("Phase (°)")
    ax_p.set_xlabel("Frequency (Hz)")
    ax_p.set_ylim(-95, 5)
    ax_p.set_title("F12 — Bode phase")
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f13(path: Path) -> Path:
    R, C = 1_000.0, 100e-9
    fc = rc_cutoff(R, C)
    f = np.logspace(1, 5, 400)
    mag, _ = rc_response(f, R, C, "lowpass")
    # Three marker frequencies
    marks = [fc / 10, fc, fc * 10]
    fig, axes = plt.subplots(2, 3, figsize=(11, 5.5))
    # Top row: bode with marker
    for col, fm in enumerate(marks):
        ax = axes[0, col]
        house_style(ax)
        ax.semilogx(f, to_db(mag), color=COLORS["signal"], lw=1.8)
        ax.axvline(fm, color=COLORS["marker"], lw=1.5)
        ax.axhline(-3, color=COLORS["ref"], ls=":", alpha=0.6)
        ax.set_ylim(-60, 5)
        m, p = rc_response(np.array([fm]), R, C, "lowpass")
        ax.set_title(f"f={fm:.0f} Hz  |H|={m[0]:.2f}  ∠{p[0]:.0f}°")
        if col == 0:
            ax.set_ylabel("Mag (dB)")
        # Bottom: time domain
        ax2 = axes[1, col]
        house_style(ax2)
        duration = min(0.02, 6.0 / fm)
        tt = time_axis(duration, max(30 * fm, 5_000.0))
        ax2.plot(tt * 1e3, sine(tt, 1.0, fm), color=COLORS["ref"], lw=1.0, label="in")
        ax2.plot(tt * 1e3, sine(tt, float(m[0]), fm, phase_deg=float(p[0])), color=COLORS["signal"], lw=1.6, label="out")
        ax2.set_xlabel("Time (ms)")
        ax2.set_ylim(-1.3, 1.3)
        if col == 0:
            ax2.set_ylabel("Voltage (V)")
            ax2.legend(fontsize=7)
    fig.suptitle("F13 — Gain & phase as a shrinking, lagging sine", fontsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f14(path: Path) -> Path:
    fs = 50_000.0
    t = time_axis(0.03, fs)
    f0 = 200.0
    xin = square(t, frequency=f0)
    caps = [50e-9, 200e-9, 800e-9]
    fig, axes = plt.subplots(2, 3, figsize=(11, 5.5))
    for col, C in enumerate(caps):
        y = apply_rc_lowpass(xin, fs, 1_000.0, C)
        fc = rc_cutoff(1_000.0, C)
        house_style(axes[0, col])
        axes[0, col].plot(t * 1e3, xin, color=COLORS["ref"], lw=0.8, alpha=0.4)
        axes[0, col].plot(t * 1e3, y, color=COLORS["signal"], lw=1.6)
        axes[0, col].set_title(f"fc={fc:.0f} Hz")
        axes[0, col].set_ylim(-1.4, 1.4)
        freqs, mag_i = spectrum(xin, fs)
        _, mag_o = spectrum(y, fs)
        ns = np.arange(1, 10, 2)
        ai = [mag_i[int(np.argmin(np.abs(freqs - n * f0)))] for n in ns]
        ao = [mag_o[int(np.argmin(np.abs(freqs - n * f0)))] for n in ns]
        house_style(axes[1, col])
        axes[1, col].stem(ns - 0.15, ai, linefmt=COLORS["ref"], markerfmt="o", basefmt=" ")
        axes[1, col].stem(ns + 0.15, ao, linefmt=COLORS["signal"], markerfmt="s", basefmt=" ")
        axes[1, col].set_xlabel("Harmonic #")
        axes[1, col].set_ylim(0, 1.4)
    axes[0, 0].set_ylabel("Voltage (V)")
    axes[1, 0].set_ylabel("Amplitude")
    fig.suptitle("F14 — Lower cutoff → rounder edges (high harmonics die)", fontsize=11)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f15(path: Path) -> Path:
    R, C = 1_000.0, 100e-9
    fc = rc_cutoff(R, C)
    f = np.logspace(1, 5, 500)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    house_style(ax)
    for kind, color, label in (
        ("lowpass", COLORS["signal"], "low-pass"),
        ("highpass", COLORS["signal2"], "high-pass"),
        ("bandpass", COLORS["sum"], "band-pass"),
    ):
        mag, _ = rc_response(f, R, C, kind)
        ax.semilogx(f, to_db(mag), color=color, lw=2.0, label=label)
    ax.axvline(fc, color=COLORS["marker"], ls="--", label=f"fc={fc:.0f} Hz")
    ax.axhline(-3, color=COLORS["ref"], ls=":", alpha=0.7)
    ax.set_ylim(-60, 5)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude (dB)")
    ax.set_title("F15 — Filter-type comparison")
    ax.legend(fontsize=8, loc="lower left")
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def export_all(out_dir: Path) -> list[Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    return [
        _f12(out_dir / "f12-bode-explorer.png"),
        _f13(out_dir / "f13-bode-time.png"),
        _f14(out_dir / "f14-square-through-rc.png"),
        _f15(out_dir / "f15-filter-types.png"),
    ]


if __name__ == "__main__":
    dest = Path(__file__).resolve().parents[3] / "docs" / "assets" / "img"
    for p in export_all(dest):
        print(p)
