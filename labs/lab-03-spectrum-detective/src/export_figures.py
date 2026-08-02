#!/usr/bin/env python3
"""Export Lab 03 documentation figures (F7–F11)."""

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
from explore import HIDDEN_SEED, HIDDEN_TONE_HZ, recipe  # noqa: E402


def _f7(path: Path) -> Path:
    t = time_axis(0.05, 10_000.0)
    fs = 10_000.0
    names = ["pure tone", "two tones", "tone + noise", "AM", "square"]
    fig, axes = plt.subplots(len(names), 2, figsize=(10, 9), sharex="col")
    for row, name in enumerate(names):
        y = recipe(name, t, fs)
        house_style(axes[row, 0])
        axes[row, 0].plot(t[:1500] * 1e3, y[:1500], color=COLORS["signal"], lw=1.0)
        axes[row, 0].set_ylabel(name, fontsize=8)
        freqs, mag = spectrum(y, fs)
        house_style(axes[row, 1])
        axes[row, 1].plot(freqs, to_db(mag), color=COLORS["spectrum"], lw=1.0)
        axes[row, 1].set_xlim(0, 1500)
        axes[row, 1].set_ylim(-80, 5)
    axes[0, 0].set_title("Time")
    axes[0, 1].set_title("Frequency (dB)")
    axes[-1, 0].set_xlabel("Time (ms)")
    axes[-1, 1].set_xlabel("Frequency (Hz)")
    fig.suptitle("F7 — Twin panel: recipes in time and frequency", fontsize=12)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f8(path: Path) -> Path:
    t = time_axis(0.2, 10_000.0)
    fs = 10_000.0
    y = 0.15 * sine(t, 1.0, HIDDEN_TONE_HZ) + noise(t, amplitude=1.2, seed=HIDDEN_SEED)
    fig, (ax_t, ax_f) = plt.subplots(2, 1, figsize=(9, 5.5))
    house_style(ax_t)
    house_style(ax_f)
    ax_t.plot(t[:2000] * 1e3, y[:2000], color=COLORS["signal"], lw=0.7)
    ax_t.set_title("F8 — Hidden tone buried in noise (time domain hides it)")
    ax_t.set_ylabel("Voltage (V)")
    freqs, mag = spectrum(y, fs)
    ax_f.plot(freqs, to_db(mag), color=COLORS["spectrum"], lw=1.0)
    ax_f.axvline(HIDDEN_TONE_HZ, color=COLORS["marker"], ls="--", lw=1.2, label=f"tone @ {HIDDEN_TONE_HZ:.0f} Hz")
    ax_f.set_xlim(0, 800)
    ax_f.set_ylim(-80, 5)
    ax_f.set_xlabel("Frequency (Hz)")
    ax_f.set_ylabel("Magnitude (dB)")
    ax_f.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f9(path: Path) -> Path:
    t = time_axis(0.05, 10_000.0)
    fs = 10_000.0
    f0 = 100.0
    clean = sine(t, 1.0, f0)
    gains = [1.0, 3.0, 6.0]
    fig, axes = plt.subplots(2, 3, figsize=(10, 5.5))
    for col, g in enumerate(gains):
        y = soft_clip(clean, gain=g)
        house_style(axes[0, col])
        axes[0, col].plot(t[:1000] * 1e3, clean[:1000], color=COLORS["ref"], lw=0.8, alpha=0.5)
        axes[0, col].plot(t[:1000] * 1e3, y[:1000], color=COLORS["signal"], lw=1.3)
        axes[0, col].set_title(f"gain={g:.0f}  THD={100*thd(y, fs, f0):.1f}%")
        axes[0, col].set_ylim(-1.3, 1.3)
        freqs, mag = spectrum(y, fs)
        ns = np.arange(1, 8)
        amps = [mag[int(np.argmin(np.abs(freqs - n * f0)))] for n in ns]
        house_style(axes[1, col])
        axes[1, col].stem(ns, amps, linefmt=COLORS["spectrum"], markerfmt="o", basefmt=" ")
        axes[1, col].set_xlabel("Harmonic #")
        axes[1, col].set_ylim(0, 1.2)
    axes[0, 0].set_ylabel("Voltage (V)")
    axes[1, 0].set_ylabel("Amplitude")
    fig.suptitle("F9 — Soft clipping spawns harmonics (THD rises with gain)", fontsize=11)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f10(path: Path) -> Path:
    fs = 10_000.0
    f0 = 200.0
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
    for ax, cycles, title in (
        (axes[0], 5.0, "5.0 cycles — clean spike"),
        (axes[1], 5.3, "5.3 cycles — leakage"),
    ):
        t = time_axis(cycles / f0, fs)
        x = sine(t, 1.0, f0)
        freqs, mag = spectrum(x, fs)
        house_style(ax)
        ax.plot(freqs, to_db(mag), color=COLORS["spectrum"], lw=1.2)
        ax.axvline(f0, color=COLORS["marker"], ls="--", alpha=0.6)
        ax.set_xlim(0, 600)
        ax.set_ylim(-80, 5)
        ax.set_title(title)
        ax.set_xlabel("Frequency (Hz)")
    axes[0].set_ylabel("Magnitude (dB)")
    fig.suptitle("F10 — Spectral leakage (stretch)", fontsize=11)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f11(path: Path) -> Path:
    f_tone = 200.0
    t_true = np.linspace(0, 0.04, 4000)
    true = sine(t_true, 1.0, f_tone)
    rates = [1000.0, 500.0, 250.0]
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), sharey=True)
    for ax, fs in zip(axes, rates):
        house_style(ax)
        ax.plot(t_true * 1e3, true, color=COLORS["ref"], lw=0.8, alpha=0.35)
        n = int(0.04 * fs)
        t_s = np.arange(n) / fs
        samples = sine(t_s, 1.0, f_tone)
        ax.plot(t_s * 1e3, samples, "o-", color=COLORS["signal"], ms=3, lw=1.0)
        nyquist = fs / 2
        aliased = abs(((f_tone + nyquist) % fs) - nyquist)
        status = "OK" if fs >= 2 * f_tone else f"alias→{aliased:.0f} Hz"
        ax.set_title(f"fs={fs:.0f} Hz  ({status})")
        ax.set_xlabel("Time (ms)")
        ax.set_xlim(0, 40)
        ax.set_ylim(-1.4, 1.4)
    axes[0].set_ylabel("Voltage (V)")
    fig.suptitle(f"F11 — Sampling & aliasing (tone = {f_tone:.0f} Hz)", fontsize=11)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def export_all(out_dir: Path) -> list[Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    return [
        _f7(out_dir / "f07-twin-panel.png"),
        _f8(out_dir / "f08-hidden-tone.png"),
        _f9(out_dir / "f09-thd.png"),
        _f10(out_dir / "f10-leakage.png"),
        _f11(out_dir / "f11-aliasing.png"),
    ]


if __name__ == "__main__":
    dest = Path(__file__).resolve().parents[3] / "docs" / "assets" / "img"
    for p in export_all(dest):
        print(p)
