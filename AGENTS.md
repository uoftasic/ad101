# Agent guide — UofT ASIC course repos

You are working in a course repository for the UofT ASIC Team (`uoftasic`): pedagogical materials for IC / RTL / FPGA / open-source ASIC flows. The site under `docs/` is built with Quarto and published on GitHub Pages by `.github/workflows/site.yml`. Runnable work lives outside `docs/`.

Optimize for clear student learning paths, not template maintenance. Prefer concrete labs and notes students can follow end-to-end over meta documentation.

## Goals

- Teach IC development skills: RTL (SystemVerilog/Verilog), simulation, synthesis, FPGA bring-up, and/or open ASIC flows (e.g. Yosys, LibreLane, SKY130) as the course requires.
- Keep each lab self-contained: what you'll build, before you start (guide pages to read, setup), a time estimate, numbered parts that each open with the question they answer and end in a "You should see …" check, and Finishing.
- In every lab, at least one required part has the student produce something: edit a file, write code, or work out a number and write it down before a script prints it. Ask for predictions wherever a student can make one.
- Keep observed numbers in the "You should see …" checks. When a check would also explain *why*, make the explanation a question at that step, with the answer in a collapsed `<details><summary>Answer</summary> … </details>` block (blank lines inside, so Markdown and math render).
- Put optional parts at the end of the lab, mark them "(optional)" in the header, and leave them out of the time estimate or give their time separately. No required part may depend on an optional one.
- Separate what students read (`docs/`) from what they run (`labs/`, `scripts/`, `notebooks/`). Inside `docs/`, guide pages are reading only; every command a student runs belongs in a lab writeup.
- Keep the Course path table on `docs/index.md` current, in the order a student should work, and in the format every course uses:

  ```
  | # | | What | Time |
  |---|---|---|---|
  | 1 | Read | [Page](guide/page.md) · [Page](guide/page.md) | 45 min |
  | 2 | Do | [Lab 01: Title](labs/lab-01-...-overview.md). One sentence on what you'll do. | 1.5 h |
  ```

  Read and Do are plain text, lab titles use a colon, every Do row ends with one sentence on what the student will do, and the row times add up to the total on the home page. Lab page titles (`# Lab 01: Title`) and the sidebar entries in `docs/_quarto.yml` use the same "Lab 01: Title" form. The sidebar and the chapter list in `docs/_quarto-pdf.yml` both follow the Course path order.
- Never publish grades, solution keys, or PII under `docs/`. Put keys in `labs/**/solutions/` and gitignore them on student forks when policy requires.

## Layout (do not fight this)

| Path | Published? | Put here |
|------|------------|----------|
| `docs/` | Yes | Guides, lab writeups, figures for the site |
| `docs/guide/` | Yes | Conceptual notes (flows, tools, theory) |
| `docs/labs/` | Yes | Lab writeups only (`lab-NN-*-overview.md`) |
| `docs/assets/img/` | Yes | Small diagrams / waveforms for docs |
| `labs/<lab-id>/` | No | HDL, Python, testbenches, local data, graders |
| `scripts/` | No | Course utilities / automation |
| `notebooks/` | No | Exploratory or assignment notebooks |
| `data/`, `figures/` | No | Shared datasets / source figures |

Site wiring: `docs/_quarto.yml` (site, sidebar, navbar, per-page PDFs), `docs/_quarto-pdf.yml` (the whole course as one PDF) and `docs/_filters/course.lua` (turns `<details>` answers into collapsible callouts, and moves them to an Answers section at the end of each page in PDFs). The home page is `docs/index.md`. Math: `$inline$`, `$$display$$`.

## Adding a lab (preferred unit of coursework)

Lab IDs: `lab-NN-short-name` (e.g. `lab-02-counter-sv`).

1. Create `labs/<lab-id>/` with at least:
   - `README.md` — points at the writeup on the site and how to run
   - `src/` — HDL / Python / entrypoints
   - `data/` — small inputs (large binaries → Git LFS or external)
   - `requirements.txt` or tool notes when needed
2. Add `docs/labs/<lab-id>-overview.md`, titled `# Lab NN: Title`, with: a 2–3 line summary of what the student builds or measures, Before you start, Time, Part 1…N (each opening with the question it answers, with numbered steps and a "You should see …" check), and Finishing. Finishing has three things, in this order:
   1. "You're done when …": one checkable line tied to the student's own work, not to output the shipped package prints anyway.
   2. Questions, if there are any: each with a collapsed answer or a pointer to the step that answers it.
   3. Submit: what to submit, or "Nothing to submit."

   After those come Going further (optional), if any, and last a `Next on the [Course path](../index.md#course-path): …` line.
3. Add a Do row to the Course path in `docs/index.md`, in the format above, and add the writeup to the sidebar in `docs/_quarto.yml` and the chapters in `docs/_quarto-pdf.yml`, in the same position (and to the navbar in `_quarto.yml` only if it belongs in top nav).
4. Cross-link: writeup → GitHub `labs/<lab-id>/`; package README → `docs/labs/<lab-id>-overview.md`.

Writeups teach; packages execute. Don't dump long HDL into site pages; reference files under `labs/` instead. Keep package READMEs short: a link to the writeup, how to run, the commands or make targets, and the file list.

## Adding a guide page

1. Add kebab-case Markdown under `docs/guide/` (e.g. `yosys-synth.md`).
2. Keep it reading only: concepts, figures, worked examples. If the student should run something, put it in the matching lab as a numbered step and leave a one-line pointer on the guide page.
3. Add it to the right Read row of the Course path in `docs/index.md`, and to the sidebar in `docs/_quarto.yml` and the chapters in `docs/_quarto-pdf.yml` in the same position.
4. Images under `docs/assets/img/`, linked with paths relative to the page you are writing in (`../assets/img/x.png` from a guide or lab page).
5. Write links between pages as paths relative to the page you are writing in (`../guide/x.md` from a lab), because that is how Quarto resolves them. Use GitHub URLs for `labs/` and `scripts/`.

## Pedagogy checklist (use when authoring)

- State learning objectives in student language (“You will synthesize a counter and inspect the netlist”).
- Assume a clone of this repo and the course’s documented workbench; do not bundle Docker in every lab unless the course already does.
- For EDA-heavy work (LibreLane / SKY130 / IIC-OSIC-TOOLS), document the team workbench steps in-course rather than inventing a one-off container story.
- Keep procedures copy-pasteable (`cd`, install, simulate/synth, check artifact).
- Define expected results (printout, waveform check, area/timing ballpark, golden hash) so students know they succeeded.
- Progress difficulty across labs; reuse naming and directory conventions so later labs feel familiar.
- Prefer small, inspectable designs over opaque blobs; when using IP or PDK artifacts, keep secrets and huge binaries out of git.

## Tooling norms

- Python helpers and graders: under `labs/<id>/src/` or `scripts/`; list entry points in the nearest `README.md`.
- SystemVerilog/Verilog: under `labs/<id>/src/` (or `rtl/`, `tb/` if you split — stay consistent within the course).
- Heavy outputs (GDS, large FSDB/VCD, PDK caches): local `results/` or LFS — never under `docs/`.
- Preview docs locally: `quarto preview docs` → http://localhost:4200
- Check links after a render: `python3 scripts/check_site.py docs/_site` (the site workflow runs it too).

## What not to do

- Do not add maintainer-only pages to the published site (contributing guides, template notes, notation stubs “for debugging”).
- Do not put solution keys or rubrics in `docs/`.
- Do not replace student-facing content with template/bootstrap instructions; point humans at `CONTRIBUTING.md` / `TEMPLATE.md` only when they are bootstrapping or changing repo conventions.
- Do not change org assumptions: GitHub org is `uoftasic`; course id matches the repo name.

## Quick references

- Repo conventions: `CONTRIBUTING.md`
- Bootstrap tokens / Pages checklist: `TEMPLATE.md`
- Sample lab shape: `labs/lab-01-signal-explorer/` + `docs/labs/lab-01-signal-explorer-overview.md`
