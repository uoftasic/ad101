"""Shared signal helpers for AD101 labs.

One small, readable module first-years can open and skim.
No calculus — generators, spectra, an RC filter, and plot style.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------

DEFAULT_FS = 10_000.0  # samples / second
DEFAULT_DURATION = 0.05  # seconds
RNG_SEED = 42


def time_axis(
    duration: float = DEFAULT_DURATION,
    fs: float = DEFAULT_FS,
) -> np.ndarray:
    """Return a time vector from 0 to duration (exclusive of the endpoint)."""
    n = max(int(round(duration * fs)), 1)
    return np.arange(n, dtype=float) / fs


# ---------------------------------------------------------------------------
# Signal generators
# ---------------------------------------------------------------------------


def sine(
    t: np.ndarray,
    amplitude: float = 1.0,
    frequency: float = 100.0,
    phase_deg: float = 0.0,
    dc: float = 0.0,
) -> np.ndarray:
    """Sine wave: A * sin(2π f t + φ) + DC."""
    phase = np.deg2rad(phase_deg)
    return amplitude * np.sin(2.0 * np.pi * frequency * t + phase) + dc


def square(
    t: np.ndarray,
    amplitude: float = 1.0,
    frequency: float = 100.0,
    duty: float = 0.5,
    dc: float = 0.0,
) -> np.ndarray:
    """Square / pulse train with duty cycle in (0, 1]."""
    duty = float(np.clip(duty, 1e-6, 1.0))
    phase = (frequency * t) % 1.0
    return amplitude * np.where(phase < duty, 1.0, -1.0) + dc


def triangle(
    t: np.ndarray,
    amplitude: float = 1.0,
    frequency: float = 100.0,
    dc: float = 0.0,
) -> np.ndarray:
    """Triangle wave in [-amplitude, +amplitude]."""
    phase = (frequency * t) % 1.0
    # 0→0.5 rises -A→+A, 0.5→1 falls +A→-A
    rising = phase < 0.5
    y = np.empty_like(t, dtype=float)
    y[rising] = -1.0 + 4.0 * phase[rising]
    y[~rising] = 3.0 - 4.0 * phase[~rising]
    return amplitude * y + dc


def pulse_train(
    t: np.ndarray,
    amplitude: float = 1.0,
    frequency: float = 100.0,
    duty: float = 0.25,
    dc: float = 0.0,
) -> np.ndarray:
    """Unipolar pulse train (0 / amplitude) with given duty cycle."""
    duty = float(np.clip(duty, 1e-6, 1.0))
    phase = (frequency * t) % 1.0
    return amplitude * np.where(phase < duty, 1.0, 0.0) + dc


def noise(
    t: np.ndarray,
    amplitude: float = 1.0,
    seed: int | None = RNG_SEED,
) -> np.ndarray:
    """Gaussian white noise with std ≈ amplitude / 3 (most mass in ±A)."""
    rng = np.random.default_rng(seed)
    return (amplitude / 3.0) * rng.standard_normal(len(t))


def harmonic_sum(
    t: np.ndarray,
    fundamental: float,
    harmonics: Iterable[int],
    amplitudes: Iterable[float] | None = None,
    phases_deg: Iterable[float] | None = None,
) -> np.ndarray:
    """Sum of selected harmonics of a fundamental frequency.

    If amplitudes is None, use the classic square-wave 4/(nπ) for odd n.
    """
    harmonics = list(harmonics)
    if amplitudes is None:
        amplitudes = [4.0 / (n * np.pi) if n % 2 == 1 else 0.0 for n in harmonics]
    else:
        amplitudes = list(amplitudes)
    if phases_deg is None:
        phases_deg = [0.0] * len(harmonics)
    else:
        phases_deg = list(phases_deg)

    y = np.zeros_like(t, dtype=float)
    for n, a, p in zip(harmonics, amplitudes, phases_deg):
        y += sine(t, amplitude=a, frequency=fundamental * n, phase_deg=p)
    return y


def soft_clip(x: np.ndarray, gain: float = 1.0) -> np.ndarray:
    """Soft-clipping nonlinearity: tanh(gain * x). Introduces harmonics."""
    return np.tanh(gain * x)


# ---------------------------------------------------------------------------
# Spectrum
# ---------------------------------------------------------------------------


def spectrum(
    x: np.ndarray,
    fs: float,
) -> tuple[np.ndarray, np.ndarray]:
    """One-sided magnitude spectrum via rFFT.

    Returns (frequencies_Hz, magnitude). Magnitude is scaled so a unit sine
    of amplitude A peaks near A/2 (numpy rfft convention for real signals).
    For display we return the absolute value of the positive-frequency bins.
    """
    n = len(x)
    windowed = x - np.mean(x)  # remove DC for cleaner peaks
    X = np.fft.rfft(windowed)
    freqs = np.fft.rfftfreq(n, d=1.0 / fs)
    # Scale to approximate peak amplitude for a pure tone
    mag = (2.0 / n) * np.abs(X)
    mag[0] *= 0.5  # DC shouldn't get the 2× factor
    return freqs, mag


def to_db(mag: np.ndarray, floor_db: float = -80.0) -> np.ndarray:
    """Convert linear magnitude to dB, clipping at floor_db."""
    mag = np.asarray(mag, dtype=float)
    safe = np.maximum(mag, 10.0 ** (floor_db / 20.0))
    return 20.0 * np.log10(safe)


# ---------------------------------------------------------------------------
# Systems (RC filters)
# ---------------------------------------------------------------------------


def rc_cutoff(R: float, C: float) -> float:
    """Cutoff frequency f_c = 1 / (2 π R C) in Hz."""
    return 1.0 / (2.0 * np.pi * R * C)


def rc_lowpass(f: np.ndarray, R: float, C: float) -> tuple[np.ndarray, np.ndarray]:
    """RC low-pass: |H|, phase_deg for frequency array f (Hz)."""
    fc = rc_cutoff(R, C)
    u = f / fc
    mag = 1.0 / np.sqrt(1.0 + u**2)
    phase = -np.rad2deg(np.arctan(u))
    return mag, phase


def rc_highpass(f: np.ndarray, R: float, C: float) -> tuple[np.ndarray, np.ndarray]:
    """RC high-pass: |H|, phase_deg."""
    fc = rc_cutoff(R, C)
    u = f / fc
    mag = u / np.sqrt(1.0 + u**2)
    phase = np.rad2deg(np.arctan(1.0 / np.maximum(u, 1e-30)))
    return mag, phase


def rc_bandpass(
    f: np.ndarray,
    R: float,
    C: float,
    Q: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    """Simple band-pass magnitude/phase centered at fc with quality Q.

    H(s) ≈ (s/(Q ωc)) / (1 + s/(Q ωc) + (s/ωc)²) — enough for visualization.
    """
    fc = rc_cutoff(R, C)
    u = f / fc
    # Magnitude of a second-order band-pass
    denom = np.sqrt((1.0 - u**2) ** 2 + (u / Q) ** 2)
    mag = (u / Q) / np.maximum(denom, 1e-30)
    phase = np.rad2deg(np.arctan2(Q * (1.0 - u**2), u) - 90.0)
    return mag, phase


def rc_response(
    f: np.ndarray,
    R: float,
    C: float,
    kind: str = "lowpass",
) -> tuple[np.ndarray, np.ndarray]:
    """Dispatch to lowpass / highpass / bandpass."""
    kind = kind.lower()
    if kind in ("lowpass", "lp", "low"):
        return rc_lowpass(f, R, C)
    if kind in ("highpass", "hp", "high"):
        return rc_highpass(f, R, C)
    if kind in ("bandpass", "bp", "band"):
        return rc_bandpass(f, R, C)
    raise ValueError(f"Unknown filter kind: {kind!r}")


def apply_rc_lowpass(
    x: np.ndarray,
    fs: float,
    R: float,
    C: float,
) -> np.ndarray:
    """Apply an RC low-pass in the frequency domain (circular convolution).

    Good enough for visualizing a square wave through a filter.
    """
    n = len(x)
    freqs = np.fft.rfftfreq(n, d=1.0 / fs)
    mag, phase = rc_lowpass(freqs, R, C)
    H = mag * np.exp(1j * np.deg2rad(phase))
    X = np.fft.rfft(x)
    return np.fft.irfft(X * H, n=n)


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------


def rms(x: np.ndarray) -> float:
    """Root-mean-square value."""
    return float(np.sqrt(np.mean(np.asarray(x, dtype=float) ** 2)))


def peak_to_peak(x: np.ndarray) -> float:
    """Peak-to-peak swing."""
    x = np.asarray(x, dtype=float)
    return float(np.max(x) - np.min(x))


def thd(x: np.ndarray, fs: float, fundamental: float, n_harmonics: int = 5) -> float:
    """Total harmonic distortion as a fraction (not percent).

    THD = sqrt(sum_{k=2..N} A_k²) / A_1
    """
    freqs, mag = spectrum(x, fs)
    # Find nearest bin to each harmonic
    def amp_at(f_hz: float) -> float:
        idx = int(np.argmin(np.abs(freqs - f_hz)))
        return float(mag[idx])

    a1 = amp_at(fundamental)
    if a1 < 1e-12:
        return 0.0
    harm_power = 0.0
    for k in range(2, n_harmonics + 1):
        harm_power += amp_at(fundamental * k) ** 2
    return float(np.sqrt(harm_power) / a1)


# ---------------------------------------------------------------------------
# Plot style
# ---------------------------------------------------------------------------

# Consistent colors used across all fifteen figures
COLORS = {
    "signal": "#2563eb",  # blue
    "signal2": "#dc2626",  # red
    "sum": "#16a34a",  # green
    "ref": "#6b7280",  # gray
    "marker": "#d97706",  # amber
    "spectrum": "#7c3aed",  # violet
    "fill": "#93c5fd",
}


def house_style(ax=None):
    """Apply a clean, consistent look to a matplotlib Axes (or current)."""
    import matplotlib.pyplot as plt

    if ax is None:
        ax = plt.gca()
    ax.grid(True, which="both", alpha=0.35, linestyle="--", linewidth=0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(labelsize=9)
    return ax


def configure_matplotlib(headless: bool = False) -> str:
    """Pick a backend. Returns the backend name in use."""
    import matplotlib

    if headless:
        matplotlib.use("Agg")
    else:
        # Prefer an interactive backend when available; fall back to Agg.
        current = matplotlib.get_backend().lower()
        if current == "agg" or "inline" in current:
            for candidate in ("TkAgg", "Qt5Agg", "QtAgg", "GTK3Agg"):
                try:
                    matplotlib.use(candidate, force=True)
                    break
                except Exception:
                    continue
    return matplotlib.get_backend()
