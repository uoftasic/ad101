#!/usr/bin/env python3
"""Lab 05 — Signal workshop, reference solution.

Filled-in version of `../src/workshop.py`. Try the exercise yourself first —
this is here to check your work, or to unstick you on one specific function,
not to replace the exercise.

Run it the same way as the scaffold:

    cd /foss/designs/modules/ad101/labs/lab-05-signal-workshop
    python3 solutions/workshop_solution.py
    python3 solutions/workshop_solution.py --headless
"""

from __future__ import annotations

import argparse
import sys
import wave
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import _path  # noqa: F401  — adds labs/ to sys.path

from common.adsig import (  # noqa: E402
    configure_matplotlib,
    harmonic_sum,
    house_style,
    rc_cutoff,
    rc_lowpass,
    spectrum,
    time_axis,
    to_db,
)

CHORD_NOTES = {"C4": 261.6, "E4": 329.6, "G4": 392.0}
FILTER_R = 1_000.0
FILTER_C = 150e-9


def synthesize_chord(t: np.ndarray, note_freqs: dict[str, float]) -> np.ndarray:
    chord = np.zeros_like(t)
    for freq in note_freqs.values():
        chord += harmonic_sum(t, fundamental=freq, harmonics=[1, 3, 5, 7, 9])
    return chord / len(note_freqs)


def plot_waveform(t: np.ndarray, v: np.ndarray, title: str, ax=None):
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots()
    house_style(ax)
    ax.plot(t * 1e3, v, linewidth=1.2)
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Voltage (V)")
    ax.set_title(title)
    return ax


def compute_spectrum(v: np.ndarray, fs: float) -> tuple[np.ndarray, np.ndarray]:
    return spectrum(v, fs)


def plot_spectrum(freqs: np.ndarray, mag: np.ndarray, title: str, ax=None):
    import matplotlib.pyplot as plt

    if ax is None:
        _, ax = plt.subplots()
    house_style(ax)
    ax.plot(freqs, to_db(mag))
    ax.set_xlim(0, 3000)
    ax.set_ylim(-80, 5)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude (dB)")
    ax.set_title(title)
    return ax


def apply_lowpass(v: np.ndarray, fs: float, R: float, C: float) -> np.ndarray:
    freqs = np.fft.rfftfreq(len(v), d=1 / fs)
    mag, phase_deg = rc_lowpass(freqs, R, C)
    H = mag * np.exp(1j * np.deg2rad(phase_deg))
    V = np.fft.rfft(v)
    return np.fft.irfft(V * H, n=len(v))


def export_wav(path: Path, v: np.ndarray, fs: float) -> Path:
    peak = np.max(np.abs(v)) + 1e-9
    scaled = np.clip(v / peak, -1.0, 1.0)
    pcm = (scaled * 32767).astype(np.int16)
    with wave.open(str(path), "w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(int(fs))
        f.writeframes(pcm.tobytes())
    return path


def play_audio(path: Path, fs: float) -> None:
    try:
        import sounddevice as sd
        import soundfile as sf

        data, samplerate = sf.read(str(path))
        sd.play(data, samplerate)
        sd.wait()
    except Exception as exc:  # no audio device, missing package, etc.
        print(f"  (couldn't play audio live: {exc})")
        print(f"  open it yourself: {path}")


def run(out_dir: Path, headless: bool) -> None:
    import matplotlib.pyplot as plt

    configure_matplotlib(headless=headless)
    out_dir.mkdir(parents=True, exist_ok=True)

    fs = 20_000.0
    t = time_axis(duration=0.5, fs=fs)

    chord = synthesize_chord(t, CHORD_NOTES)
    fig1, ax1 = plt.subplots(figsize=(8, 3))
    plot_waveform(t[:400], chord[:400], "Your chord — time domain", ax=ax1)

    freqs, mag = compute_spectrum(chord, fs)
    fig2, ax2 = plt.subplots(figsize=(8, 3))
    plot_spectrum(freqs, mag, "Your chord — spectrum", ax=ax2)

    filtered = apply_lowpass(chord, fs, FILTER_R, FILTER_C)
    fc = rc_cutoff(FILTER_R, FILTER_C)
    print(f"Filter cutoff fc = {fc:.0f} Hz")

    fig3, (ax3a, ax3b) = plt.subplots(2, 1, figsize=(8, 6))
    freqs_f, mag_f = compute_spectrum(filtered, fs)
    plot_spectrum(freqs, mag, "Before filtering", ax=ax3a)
    plot_spectrum(freqs_f, mag_f, "After filtering", ax=ax3b)

    if headless:
        for fig, name in ((fig1, "workshop-waveform"), (fig2, "workshop-spectrum"), (fig3, "workshop-before-after")):
            path = out_dir / f"{name}.png"
            fig.savefig(path, dpi=140)
            print(f"wrote {path}")
    else:
        plt.show()

    dry_path = export_wav(out_dir / "chord-unfiltered.wav", chord, fs)
    wet_path = export_wav(out_dir / "chord-filtered.wav", filtered, fs)
    print(f"wrote {dry_path}")
    print(f"wrote {wet_path}")

    if not headless:
        print("Playing unfiltered chord...")
        play_audio(dry_path, fs)
        print("Playing filtered chord...")
        play_audio(wet_path, fs)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AD101 Lab 05 — Signal workshop (solution)")
    parser.add_argument("--headless", action="store_true", help="Save PNGs, skip audio playback")
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
        help="Output directory",
    )
    args = parser.parse_args(argv)
    run(args.out, args.headless)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
