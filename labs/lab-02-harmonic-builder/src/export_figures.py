#!/usr/bin/env python3
"""Export Lab 02 documentation figures (F4–F6)."""

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
    harmonic_sum,
    house_style,
    pulse_train,
    spectrum,
    square,
    time_axis,
)


def _f4_f5(path: Path) -> Path:
    t = time_axis(0.04, 10_000.0)
    f0 = 100.0
    ns = [1, 3, 5, 7, 9]
    amps = [4.0 / (n * np.pi) for n in ns]
    y = harmonic_sum(t, f0, ns, amps)
    ideal = square(t, frequency=f0)

    fig, (ax_t, ax_s) = plt.subplots(1, 2, figsize=(10, 3.8), gridspec_kw={"width_ratios": [2, 1]})
    house_style(ax_t)
    house_style(ax_s)
    ax_t.plot(t * 1e3, ideal, color=COLORS["ref"], lw=1.0, alpha=0.5, label="ideal square")
    ax_t.plot(t * 1e3, y, color=COLORS["signal"], lw=1.8, label="5 odd harmonics")
    ax_t.set_xlabel("Time (ms)")
    ax_t.set_ylabel("Voltage (V)")
    ax_t.set_title("F4 — Fourier assembler")
    ax_t.legend(fontsize=8)

    ax_s.stem(ns, amps, linefmt=COLORS["spectrum"], markerfmt="o", basefmt=" ")
    n_guide = np.arange(1, 10)
    ax_s.plot(n_guide, 4.0 / (n_guide * np.pi), color=COLORS["marker"], ls="--", lw=1.0, label="4/(nπ)")
    ax_s.set_xlabel("Harmonic #")
    ax_s.set_ylabel("Amplitude")
    ax_s.set_title("F5 — Spectrum")
    ax_s.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f6(path: Path) -> Path:
    t = time_axis(0.04, 20_000.0)
    fs = 20_000.0
    f0 = 100.0
    duties = [0.25, 0.50, 0.75]
    fig, axes = plt.subplots(2, 3, figsize=(10, 5.5))
    for col, duty in enumerate(duties):
        y = pulse_train(t, frequency=f0, duty=duty)
        house_style(axes[0, col])
        axes[0, col].plot(t[:2000] * 1e3, y[:2000], color=COLORS["signal"], lw=1.3)
        axes[0, col].set_title(f"duty = {duty:.0%}")
        axes[0, col].set_ylim(-0.2, 1.3)
        if col == 0:
            axes[0, col].set_ylabel("Voltage (V)")

        freqs, mag = spectrum(y, fs)
        harm_n = np.arange(0, 11)
        harm_a = [mag[int(np.argmin(np.abs(freqs - n * f0)))] for n in harm_n]
        house_style(axes[1, col])
        axes[1, col].stem(harm_n, harm_a, linefmt=COLORS["spectrum"], markerfmt="o", basefmt=" ")
        axes[1, col].set_xlabel("Harmonic #")
        axes[1, col].set_ylim(0, 1.05)
        if col == 0:
            axes[1, col].set_ylabel("Amplitude")
    fig.suptitle("F6 — Duty cycle reshapes the spectrum (50% kills even harmonics)", fontsize=11)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def export_all(out_dir: Path) -> list[Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    return [
        _f4_f5(out_dir / "f04-f05-harmonic-builder.png"),
        _f6(out_dir / "f06-duty-spectrum.png"),
    ]


if __name__ == "__main__":
    dest = Path(__file__).resolve().parents[3] / "docs" / "assets" / "img"
    for p in export_all(dest):
        print(p)
