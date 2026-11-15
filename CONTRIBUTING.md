# Contributing

Thanks for improving materials for the UofT ASIC Team.

## After creating a course from this template

1. Run `scripts/init-template.py` with `--id`, `--title`, and `--description` (org is always `uoftasic`).
2. Enable GitHub Pages with Source set to GitHub Actions, so that `.github/workflows/site.yml` can build `docs/` with Quarto and deploy it.
3. Prefer repo names that match course ids (`dd103`, `ic101`, …).

See [TEMPLATE.md](TEMPLATE.md).

## Course fields

The init script fills only these three fields. This repo's values, with an example from another course:

| This repo | Example |
|-------|---------|
| `ad101` | `dd103` |
| `AD101 — Signals` | `DD103 — RTL on FPGAs & ASICs` |
| `Signals in time and frequency: waveforms, spectra, and Bode plots.` | `RTL synthesis intro with Yosys` |

## Conventions

| Item | Convention |
|------|------------|
| Org | `uoftasic` |
| Default branch | `main` |
| Docs pages | kebab-case `.md` under `docs/` |
| Lab IDs | `lab-NN-short-name` |
| Adding a doc page | add `.md` under `docs/`, add it to the sidebar in `docs/_quarto.yml` and the chapters in `docs/_quarto-pdf.yml` |
| Adding a lab | `labs/<id>/` + `docs/labs/<id>-overview.md` + sidebar entry in `docs/_quarto.yml` + chapter in `docs/_quarto-pdf.yml` + a Do row in the Course path on `docs/index.md` (`[Lab NN: Title](labs/...). One sentence on what you'll do.`) |
| Links between pages | relative to the page they are written in (`../guide/x.md` from a lab) |
| Binaries | small images in `docs/assets/`; large data → Git LFS or external |

## Docs vs labs

- `docs/` is the published site. Guide pages in `docs/guide/` are for reading only; every command a student runs belongs in a lab writeup in `docs/labs/`.
- Lab writeups follow the shape in [AGENTS.md](AGENTS.md): numbered parts, at least one where the student produces something, optional parts last, and a Finishing section with "You're done when", Questions (collapsed answers) and Submit, in that order, then the "Next on the Course path" line.
- Course path rows on `docs/index.md` use the shared format `| # | | What | Time |`, plain Read and Do, and row times that add up to the course total.
- `labs/` holds runnable HDL, Python and data. Each `labs/<id>/README.md` links to its writeup on the site.
- `scripts/` holds utilities; list entry points in `scripts/README.md`.

Do not put grades, solution keys, or PII under `docs/`. Prefer `labs/**/solutions/` and gitignore them on student forks when needed.

## Local docs preview

```bash
quarto preview docs
```

The preview runs at http://localhost:4200.

## Pull requests

Keep changes focused. For doc-only PRs, check navigation and math in the local preview when you can. Two workflows run on any PR that touches `docs/**`: `.github/workflows/site.yml` renders the site and the course PDF and runs `scripts/check_site.py` on every local link and anchor, and `.github/workflows/docs-link-check.yml` checks the links in the Markdown sources with lychee and checks that every image a page references exists.
