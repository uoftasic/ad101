# Scripts — AD101

| Script | Purpose |
|--------|---------|
| `check_env.py` | Preflight: Python, numpy, matplotlib, GUI backend, `adsig` smoke |
| `check_site.py` | Check every local link and anchor in the rendered site; `site.yml` runs it on `docs/_site` |
| `build_figures.py` | Export every lab figure into `docs/assets/img/` (seeded RNG) |
| `hello.py` | Tiny sanity print (template leftover) |
| `init-template.py` | Already run; don't re-bootstrap |

```bash
python3 scripts/check_env.py
python3 scripts/check_site.py docs/_site    # after a quarto render
python3 scripts/build_figures.py
```
