# Python in the workbench

How to run the AD101 explorers and scripts inside the IIC-OSIC-TOOLS noVNC desktop from IC101, and what to do when something goes wrong. [Lab 01](labs/lab-01-signal-explorer-overview.md), Part 1, walks you through loading the course the first time.

## One-time setup

Start noVNC as in IC101 (`./scripts/start_vnc.sh` from your `workspace` folder), open a terminal in the desktop, then:

```bash
. /foss/designs/common/.designinit
mod add ad101                # first time only: clones into modules/ad101
mod ad101                    # → /foss/designs/modules/ad101
python3 scripts/check_env.py
```

Instead of `mod add`, you can clone on the host:

```bash
# on the host, inside your workspace clone
cd workspace/modules
git clone https://github.com/uoftasic/ad101.git
```

`check_env.py` should print `OK` for numpy, matplotlib and the `adsig` smoke line, then `=== All checks passed ===`.

## Running an explorer

```bash
cd labs/lab-01-signal-explorer
python3 src/explore.py              # interactive windows
python3 src/explore.py --figure f1  # one figure
python3 src/explore.py --headless   # PNGs into results/ (no GUI)
```

The terminal stays busy until you close the plot windows. Close a window with its × button, or press `q` while the figure has focus.

## Running the snippets

The short Python snippets in Labs 01–04 only import `numpy` and `matplotlib`. Unlike the explorers, they don't need `_path.py` or `mod ad101`, so they run in any Python 3 that has those two packages: the noVNC desktop, your host machine or your own laptop. Save each one as its own `.py` file and run it with `python3 <file>.py`. In the desktop, files you save under `/foss/designs` live in your `workspace` folder on the host and survive a container restart.

## GUI backend

Interactive explorers need a matplotlib GUI backend (Tk or Qt) and a display, which the noVNC desktop provides. A host machine without a display reports `Agg`. That's fine for `build_figures.py` and `--headless`. Inside IIC-OSIC-TOOLS and noVNC, re-run `check_env.py`; if it still warns, use one of the fixes below or `--headless`.

## If the GUI won't open

`check_env.py` may report `WARN no interactive GUI backend`. Your options:

1. Use headless mode. You can still learn from the exported PNGs:

   ```bash
   python3 src/explore.py --headless
   ```

2. Install a GUI backend inside the container:

   ```bash
   pip install --user PyQt5
   # or make sure Tk is available; then re-run check_env.py
   ```

3. Check that you're in the noVNC desktop terminal, not a host terminal without a display.

## Saving a figure

- From an explorer or snippet window: click the save icon (the floppy disk) in the window's toolbar.
- From an explorer, all figures at once: `python3 src/explore.py --headless` writes PNGs into the lab's `results/` folder.
- From your own snippet: add `plt.savefig("my-capture.png", dpi=140)` just before `plt.show()`.

## Listening to a filtered signal (Lab 05)

Lab 05 exports and plays audio so you can hear a filter change a chord. Live playback needs a sound device, which the noVNC desktop may not pass through from the host. The lab script uses the same fallback idea as the GUI backend above:

1. Try live playback with `sounddevice`. It isn't installed in the course image, and neither is `soundfile`; both are listed as optional in `labs/lab-05-signal-workshop/requirements.txt`. Install them with `pip install --user sounddevice soundfile`.
2. If playback fails, the script still writes `.wav` files into `results/` and prints their paths. Open them from your host machine's file manager or media player.

Either way you can compare the filtered and unfiltered chord.

## Regenerating the docs figures (maintainers)

From the AD101 repo root:

```bash
python3 scripts/build_figures.py
# → docs/assets/img/f01-….png … f15-….png
```

Noise figures use a fixed seed (`RNG_SEED = 42` in `labs/common/adsig.py`), so rebuilds don't churn git.

## Common errors

| Symptom | Fix |
|---------|-----|
| `ModuleNotFoundError: common` | Run from the lab folder as `python3 src/explore.py` (uses `_path.py`), or `mod ad101` first |
| `ModuleNotFoundError: numpy` | `pip install --user numpy matplotlib` |
| Blank or frozen window over noVNC | Open fewer windows (`--figure f1`), close extras, check VNC bandwidth |
| `check.py` says `Not quite` | Read the spectrum peak again; the tolerance is ±5 Hz |
| `NotImplementedError: TODO: …` in Lab 05 | Expected: fill in the function the message names, then re-run |

## Related

- [IC101: Launch noVNC](https://uoftasic.com/ic101/#/guide/launch-novnc)
- [Getting started](guide/getting-started.md)
