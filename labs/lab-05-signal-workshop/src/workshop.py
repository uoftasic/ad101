#!/usr/bin/env python3
"""Lab 05 — Signal workshop (code-along, not a slider explorer).

Fill in every function marked TODO. Each one is a piece you already wrote,
in miniature, somewhere in the guide — this file just wires them together
into one script that builds a chord, looks at it, filters it, and lets you
listen to the difference.

Run it once you've filled everything in:

    cd /foss/designs/modules/ad101/labs/lab-05-signal-workshop
    python3 src/workshop.py

Headless (no GUI / no speakers, e.g. over a bare noVNC session):

    python3 src/workshop.py --headless
"""

from __future__ import annotations

import argparse
import wave
from pathlib import Path

import numpy as np

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

# A C-major triad, in Hz — see docs/reference/music-and-signals.md
CHORD_NOTES = {"C4": 261.6, "E4": 329.6, "G4": 392.0}

# RC values for the low-pass you'll build in Part 3
FILTER_R = 1_000.0   # ohms
FILTER_C = 150e-9    # farads


def synthesize_chord(t: np.ndarray, note_freqs: dict[str, float]) -> np.ndarray:
    """Part 1 — build a harmonic-rich chord.

    TODO: for each frequency in `note_freqs`, build a harmonic-rich tone
    with `harmonic_sum(t, fundamental=freq, harmonics=[1, 3, 5, 7, 9])`
    (this gives it real timbre instead of a bare sine — you want something
    with high harmonics for Part 3's filter to actually change audibly).
    Add the three notes together, then divide by the number of notes so
    the result stays roughly within [-1, 1].

    Returns the chord as one array, same length as `t`.
    """
    raise NotImplementedError("TODO: synthesize the chord — see the docstring above")


def plot_waveform(t: np.ndarray, v: np.ndarray, title: str, ax=None):
    """Part 1 — plot voltage vs time, matching the style used in Lab 01-04.

    TODO: if `ax` is None, create a new figure/axes. Apply `house_style(ax)`,
    plot `t * 1e3` (milliseconds) against `v`, and label the axes
    ("Time (ms)", "Voltage (V)") and set `ax.set_title(title)`.

    Return the axes you plotted on (useful for building multi-panel figures).
    """
    raise NotImplementedError("TODO: plot the waveform — see the docstring above")


def compute_spectrum(v: np.ndarray, fs: float) -> tuple[np.ndarray, np.ndarray]:
    """Part 2 — turn a waveform into a spectrum.

    TODO: call `spectrum(v, fs)` from `common.adsig` (it wraps
    `numpy.fft.rfft` the same way the guide's "write it yourself" snippet
    did by hand) and return `(freqs, magnitude)`.
    """
    raise NotImplementedError("TODO: compute the spectrum — see the docstring above")


def plot_spectrum(freqs: np.ndarray, mag: np.ndarray, title: str, ax=None):
    """Part 2 — plot a spectrum in dB, matching Lab 03's style.

    TODO: if `ax` is None, create a new figure/axes. Apply `house_style(ax)`,
    convert `mag` to dB with `to_db(mag)`, plot `freqs` vs that, limit the
    x-axis to something readable for a chord (`ax.set_xlim(0, 3000)` is a
    good start), and label the axes ("Frequency (Hz)", "Magnitude (dB)")
    plus `ax.set_title(title)`.

    Return the axes you plotted on.
    """
    raise NotImplementedError("TODO: plot the spectrum — see the docstring above")


def apply_lowpass(v: np.ndarray, fs: float, R: float, C: float) -> np.ndarray:
    """Part 3 — filter a signal with an RC low-pass, in the frequency domain.

    TODO, in order:
      1. Get this filter's frequency response with
         `mag, phase_deg = rc_lowpass(freqs, R, C)` — but you need `freqs`
         first: `freqs = np.fft.rfftfreq(len(v), d=1/fs)`.
      2. Build the complex frequency response
         `H = mag * np.exp(1j * np.deg2rad(phase_deg))`.
      3. Transform the input: `V = np.fft.rfft(v)`.
      4. Multiply in the frequency domain and transform back:
         `np.fft.irfft(V * H, n=len(v))`.

    This is exactly what a real filter does to a real signal, just computed
    all at once instead of one instant at a time.
    """
    raise NotImplementedError("TODO: apply the RC low-pass — see the docstring above")


def export_wav(path: Path, v: np.ndarray, fs: float) -> Path:
    """Part 4 — write a signal out as a 16-bit mono WAV file.

    TODO: normalize `v` so its peak absolute value maps to just under the
    int16 range (e.g. `scaled = np.clip(v / (np.max(np.abs(v)) + 1e-9), -1, 1)`,
    then `pcm = (scaled * 32767).astype(np.int16)`), then use the stdlib
    `wave` module:

        with wave.open(str(path), "w") as f:
            f.setnchannels(1)
            f.setsampwidth(2)          # 16-bit
            f.setframerate(int(fs))
            f.writeframes(pcm.tobytes())

    Return `path`.
    """
    raise NotImplementedError("TODO: export a WAV file — see the docstring above")


def play_audio(path: Path, fs: float) -> None:
    """Part 4 — play a WAV file aloud, with a graceful fallback.

    TODO: try to play it with `sounddevice` — something like:

        import soundfile  # or read the WAV back with the `wave` module
        import sounddevice as sd
        data, samplerate = soundfile.read(str(path))
        sd.play(data, samplerate)
        sd.wait()

    Wrap the whole thing in `try/except Exception`. If it fails (no
    `sounddevice`, no audio device passed through from noVNC, etc.), just
    print the file path and tell the student to open it from their host
    file manager instead. Playback failing should never crash the script.
    """
    raise NotImplementedError("TODO: play the audio, with a fallback — see the docstring above")


def run(out_dir: Path, headless: bool) -> None:
    import matplotlib.pyplot as plt

    configure_matplotlib(headless=headless)
    out_dir.mkdir(parents=True, exist_ok=True)

    fs = 20_000.0
    t = time_axis(duration=0.5, fs=fs)

    # --- Part 1: build and look at the chord -------------------------------
    chord = synthesize_chord(t, CHORD_NOTES)
    fig1, ax1 = plt.subplots(figsize=(8, 3))
    plot_waveform(t[:400], chord[:400], "Your chord — time domain", ax=ax1)

    # --- Part 2: look at its spectrum ---------------------------------------
    freqs, mag = compute_spectrum(chord, fs)
    fig2, ax2 = plt.subplots(figsize=(8, 3))
    plot_spectrum(freqs, mag, "Your chord — spectrum", ax=ax2)

    # --- Part 3: filter it and compare --------------------------------------
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

    # --- Part 4: export and listen ------------------------------------------
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
    parser = argparse.ArgumentParser(description="AD101 Lab 05 — Signal workshop")
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
