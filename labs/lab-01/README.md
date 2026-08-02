# Lab 01

Starter lab package for **{{COURSE_TITLE}}** (`uoftasic/{{COURSE_ID}}`).

## Docs writeup

- Site path: `/#/labs/lab-01-overview`
- Source: [`docs/labs/lab-01-overview.md`](../../docs/labs/lab-01-overview.md)
- Live: `https://uoftasic.com/{{COURSE_ID}}/#/labs/lab-01-overview`

## Layout

```text
labs/lab-01/
├── README.md
├── src/               # Python, SystemVerilog, or notebook entrypoints
├── data/              # lab-local inputs
├── results/           # optional baselines / local outputs
└── requirements.txt
```

## Quick start

```bash
cd labs/lab-01
pip install -r requirements.txt
python3 src/main.py
```

## Notes

- Prefer the team IIC-OSIC-TOOLS / SKY130 workbench for LibreLane flows when this course needs it.
- Keep large binaries out of git; use Git LFS when needed.
- Solution keys in `solutions/` only if policy allows; gitignore on student forks when appropriate.
