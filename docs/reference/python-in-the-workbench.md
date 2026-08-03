# Python in the workbench

How to launch AD101 explorers inside the IIC-OSIC-TOOLS noVNC desktop from IC101.

## One-time setup

```bash
# on the host, inside your workspace clone
cd workspace/modules
git clone https://github.com/uoftasic/ad101.git
```

Start noVNC as in IC101 (`./scripts/start_vnc.sh`), open the desktop, then:

```bash
. /foss/designs/common/.designinit
mod ad101                    # → /foss/designs/modules/ad101
python3 scripts/check_env.py
```

You want `OK` for numpy, matplotlib, and the `adsig` smoke line.

## Running an explorer

```bash
cd labs/lab-01-signal-explorer
python3 src/explore.py              # interactive windows
python3 src/explore.py --figure f1  # one figure
python3 src/explore.py --headless   # PNGs into results/ (no GUI)
```

Close plot windows with the window's × button, or press `q` if focus is on the figure.

## GUI backend note

Interactive explorers need a matplotlib GUI backend (Tk / Qt) **and** a display (the noVNC desktop). Host machines without a display will report `Agg` — that is fine for `build_figures.py` and `--headless`. Inside IIC-OSIC-TOOLS + noVNC, re-run `check_env.py`; if it still warns, use the install tip below or `--headless`.

## If the GUI won't open

`check_env.py` may report `WARN no interactive GUI backend`. Options:

1. **Headless mode** — still learn from the exported PNGs:

   ```bash
   python3 src/explore.py --headless
   ```

2. **Install a GUI backend** inside the container:

   ```bash
   pip install --user PyQt5
   # or ensure Tk is available; then re-run check_env.py
   ```

3. Confirm you are in the **noVNC desktop terminal**, not a host terminal without a display.

## Saving a figure yourself

In an interactive session, after a plot is open:

```python
# from a Python REPL in the same folder
import matplotlib.pyplot as plt
plt.savefig("my-capture.png", dpi=140)
```

Or use File → Save in the matplotlib window toolbar when available.

## Regenerating all docs figures

From the AD101 repo root (maintainers):

```bash
python3 scripts/build_figures.py
# → docs/assets/img/f01-….png … f15-….png
```

Noise figures use a fixed seed (`RNG_SEED = 42` in `labs/common/adsig.py`) so rebuilds do not churn git.

## Common errors

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: common` | Run from the lab folder via `python3 src/explore.py` (uses `_path.py`), or `mod ad101` first |
| `ModuleNotFoundError: numpy` | `pip install --user numpy matplotlib` |
| Blank / frozen window over noVNC | Reduce window count (`--figure f1`); close extras; check VNC bandwidth |
| `check.py` says not quite | Read the spectrum peak again; tolerance is ±5 Hz |

## Related

- [IC101 — Launch noVNC](https://uoftasic.com/ic101/#/guide/launch-novnc)
- [Getting started](guide/getting-started.md)
