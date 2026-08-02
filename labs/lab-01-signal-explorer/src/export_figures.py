#!/usr/bin/env python3
"""Export Lab 01 documentation figures (F1–F3) as PNGs."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

_SRC = Path(__file__).resolve().parent
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
import _path  # noqa: E402, F401

from common.adsig import (  # noqa: E402
    COLORS,
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


def _f1(path: Path) -> Path:
    t = time_axis(0.04, 10_000.0)
    y = sine(t, amplitude=1.2, frequency=100.0, phase_deg=30.0, dc=0.3)
    fig, ax = plt.subplots(figsize=(8, 3.6))
    house_style(ax)
    ax.plot(t * 1e3, y, color=COLORS["signal"], lw=1.8)
    period_ms = 10.0
    ax.axvline(period_ms, color=COLORS["marker"], ls="--", lw=1.2, label="one period")
    ax.annotate(
        "",
        xy=(period_ms, 0.3),
        xytext=(0, 0.3),
        arrowprops=dict(arrowstyle="<->", color=COLORS["marker"]),
    )
    ax.text(period_ms / 2, 0.45, "T", ha="center", color=COLORS["marker"], fontsize=11)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title(
        f"F1 — Sine explorer   pk-pk={peak_to_peak(y):.2f} V   RMS={rms(y):.3f} V"
    )
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f2(path: Path) -> Path:
    t = time_axis(0.04, 10_000.0)
    waves = [
        ("sine", sine(t, frequency=100.0)),
        ("square", square(t, frequency=100.0)),
        ("triangle", triangle(t, frequency=100.0)),
        ("pulse", pulse_train(t, frequency=100.0, duty=0.25)),
        ("noise", noise(t, amplitude=1.0, seed=42)),
    ]
    fig, axes = plt.subplots(len(waves), 1, figsize=(8, 7.5), sharex=True)
    for ax, (name, y) in zip(axes, waves):
        house_style(ax)
        ax.plot(t * 1e3, y, color=COLORS["signal"], lw=1.3)
        ax.set_ylabel(name, fontsize=9)
        ax.set_ylim(-1.8, 1.8)
    axes[-1].set_xlabel("Time (ms)")
    axes[0].set_title("F2 — Signal zoo")
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def _f3(path: Path) -> Path:
    t = time_axis(0.04, 10_000.0)
    y1 = sine(t, frequency=100.0, phase_deg=0.0)
    y2 = sine(t, frequency=100.0, phase_deg=90.0)
    fig, ax = plt.subplots(figsize=(8, 3.8))
    house_style(ax)
    ax.plot(t * 1e3, y1, color=COLORS["signal"], lw=1.4, label="A (0°)", alpha=0.9)
    ax.plot(t * 1e3, y2, color=COLORS["signal2"], lw=1.4, label="B (90°)", alpha=0.9)
    ax.plot(t * 1e3, y1 + y2, color=COLORS["sum"], lw=2.0, label="A+B")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title("F3 — Two-signal comparator (90° = quarter-period delay)")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def export_all(out_dir: Path) -> list[Path]:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    return [
        _f1(out_dir / "f01-sine-explorer.png"),
        _f2(out_dir / "f02-signal-zoo.png"),
        _f3(out_dir / "f03-two-signal.png"),
    ]


if __name__ == "__main__":
    dest = Path(__file__).resolve().parents[3] / "docs" / "assets" / "img"
    for p in export_all(dest):
        print(p)
