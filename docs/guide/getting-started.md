# Getting started

How to use this **UofT ASIC** Docsify template after **Use this template** under [`uoftasic`](https://github.com/uoftasic).

## 1. Create the course repo

1. Open [uoftasic/course-template](https://github.com/uoftasic/course-template) → **Use this template**.
2. Name the new repo after the course id (e.g. `dd103`, `ic101`).
3. Clone:

```bash
git clone https://github.com/uoftasic/{{COURSE_ID}}.git
cd {{COURSE_ID}}
```

4. Fill course fields (org is fixed to `uoftasic`):

```bash
python3 scripts/init-template.py \
  --id {{COURSE_ID}} \
  --title "{{COURSE_TITLE}}" \
  --description "{{DESCRIPTION}}"
```

Details: [TEMPLATE.md](https://github.com/uoftasic/{{COURSE_ID}}/blob/main/TEMPLATE.md).

## 2. Enable GitHub Pages

1. Push to `main`.
2. **Settings → Pages → Build and deployment**
3. Source: **Deploy from a branch** → `main` / `/docs`
4. Site URL:

```text
https://uoftasic.com/{{COURSE_ID}}/
```

No Actions workflow is required for the baseline Docsify site.

## 3. Preview docs locally

```bash
npx docsify-cli serve docs
```

Open [http://localhost:3000](http://localhost:3000).

## 4. Add a documentation page

1. Create kebab-case Markdown under `docs/` (e.g. `docs/guide/yosys-basics.md`).
2. Link it from `docs/_sidebar.md`.
3. Prefer relative links: `guide/yosys-basics.md`.
4. Put figures in `docs/assets/img/`.

Conventions for docs and labs: [CONTRIBUTING.md](https://github.com/uoftasic/{{COURSE_ID}}/blob/main/CONTRIBUTING.md).

## 5. Add a lab

1. Create `labs/<lab-id>/` with `README.md`, `src/`, `data/`, …
2. Add `docs/labs/<lab-id>-overview.md` and a sidebar entry.
3. Link the Docsify writeup from `labs/<lab-id>/README.md`.

**Separation:** `docs/labs/` = theory / procedure. `labs/` = HDL, Python, data (not published by Pages).

For LibreLane / SKY130 / IIC-OSIC-TOOLS workflows, follow the course-specific workbench instructions (do not bundle Docker in every course repo).

## 6. Smoke checks

```bash
python3 scripts/hello.py
python3 labs/lab-01/src/main.py
```
