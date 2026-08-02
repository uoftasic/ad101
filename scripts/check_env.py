#!/usr/bin/env python3
"""Preflight check for AD101 labs.

Reports Python, numpy, matplotlib, and whether an interactive GUI backend
is available. Run this first inside the IIC-OSIC-TOOLS container:

    python3 scripts/check_env.py
"""

from __future__ import annotations

import importlib
import sys


def check_import(name: str) -> tuple[bool, str]:
    try:
        mod = importlib.import_module(name)
        version = getattr(mod, "__version__", "?")
        return True, str(version)
    except ImportError as exc:
        return False, str(exc)


def main() -> int:
    print("=== AD101 environment check ===")
    print(f"Python: {sys.version.split()[0]}  ({sys.executable})")

    fail = 0
    for pkg in ("numpy", "matplotlib"):
        ok, info = check_import(pkg)
        if ok:
            print(f"OK   {pkg} {info}")
        else:
            print(f"FAIL {pkg}: {info}")
            fail += 1

    if fail:
        print()
        print("Install missing packages inside the container:")
        print("  pip install --user numpy matplotlib")
        print("Then re-run this script.")
        return 1

    # Backend probe
    import matplotlib

    backend = matplotlib.get_backend()
    print(f"OK   matplotlib backend: {backend}")

    interactive = backend.lower() not in ("agg", "svg", "pdf", "ps", "template")
    if interactive:
        print("OK   interactive GUI backend available")
    else:
        print("WARN no interactive GUI backend (Agg / headless)")
        print("     Labs still work with:  python3 src/explore.py --headless")
        print("     Or try:  pip install --user PyQt5   then re-check")
        # Try to force an interactive backend
        for candidate in ("TkAgg", "Qt5Agg", "QtAgg"):
            try:
                matplotlib.use(candidate, force=True)
                print(f"     Tip: matplotlib.use({candidate!r}) succeeded")
                interactive = True
                break
            except Exception as exc:
                print(f"     {candidate}: unavailable ({exc})")

    # Quick smoke: generate a tiny sine and its spectrum
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root / "labs"))
    try:
        from common.adsig import sine, spectrum, time_axis  # noqa: WPS433

        t = time_axis(0.01, 1000.0)
        x = sine(t, amplitude=1.0, frequency=100.0)
        freqs, mag = spectrum(x, 1000.0)
        peak_f = float(freqs[int(mag.argmax())])
        print(f"OK   adsig smoke: peak ≈ {peak_f:.0f} Hz (expect ~100)")
    except Exception as exc:
        print(f"FAIL adsig smoke: {exc}")
        fail += 1

    print()
    if fail == 0:
        print("=== All checks passed ===")
        if not interactive:
            print("(Interactive plots may need --headless or a GUI backend.)")
        return 0
    print("=== Some checks failed ===")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
