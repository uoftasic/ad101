# Contributing

Thanks for improving materials for the UofT ASIC Team.

## After creating a course from this template

1. Run `scripts/init-template.py` with `--id`, `--title`, and `--description` (org is always `uoftasic`).
2. Enable GitHub Pages: branch `main`, folder `/docs`.
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
| Adding a doc page | add `.md` under `docs/`, link in `docs/_sidebar.md` |
| Adding a lab | `labs/<id>/` + `docs/labs/<id>-overview.md` + sidebar entry + a row in the Course path on `docs/README.md` |
| Binaries | small images in `docs/assets/`; large data → Git LFS or external |

## Docs vs labs

- `docs/` is the published site. Guide pages in `docs/guide/` are for reading only; every command a student runs belongs in a lab writeup in `docs/labs/`.
- `labs/` holds runnable HDL, Python and data. Each `labs/<id>/README.md` links to its Docsify writeup.
- `scripts/` holds utilities; list entry points in `scripts/README.md`.

Do not put grades, solution keys, or PII under `docs/`. Prefer `labs/**/solutions/` and gitignore them on student forks when needed.

## Local docs preview

```bash
npx docsify-cli serve docs
```

## Pull requests

Keep changes focused. For doc-only PRs, check navigation and math locally when practical. Optional CI may link-check `docs/**`.
