# Scripts — AD101

| Script | Purpose |
|--------|---------|
| `check_env.py` | Preflight: Python, numpy, matplotlib, GUI backend, `adsig` smoke |
| `check_docs_links.py` | Validate Docsify local links (nested pages must use `../`) |
| `build_figures.py` | Export every lab figure into `docs/assets/img/` (seeded RNG) |
| `hello.py` | Tiny sanity print (template leftover) |
| `init-template.py` | Already run — do not re-bootstrap |

```bash
python3 scripts/check_env.py
python3 scripts/check_docs_links.py
python3 scripts/build_figures.py
```
