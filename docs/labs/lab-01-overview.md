# Lab 01 overview

Short writeup for the published docs site. Full runnable content: [`labs/lab-01/`](https://github.com/uoftasic/{{COURSE_ID}}/tree/main/labs/lab-01).

## Prerequisites

- Python 3.10+ on your machine
- Clone of `uoftasic/{{COURSE_ID}}`
- For EDA-heavy follow-ons: course workbench / IIC-OSIC-TOOLS (not required for this starter)

## Objectives

- Confirm the UofT ASIC lab package layout
- Run the starter under `labs/lab-01/src/`
- Optionally capture baselines in `labs/lab-01/results/`

## Theory (stub)

Replace with course-specific notes. Example discrete convolution:

$$
y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k]\, h[n-k]
$$

## Procedure

1. Open the lab package:

```bash
cd labs/lab-01
```

2. Install dependencies if needed:

```bash
pip install -r requirements.txt
```

3. Run the starter:

```bash
python3 src/main.py
```

4. Keep large GDS / waveform dumps out of `docs/` — use `results/` locally or Git LFS when sharing.

## Expected results

- Starter prints a greeting and a trivial checksum (replace with course goldens).

## Links

- [Lab package](https://github.com/uoftasic/{{COURSE_ID}}/tree/main/labs/lab-01)
- [Scripts](https://github.com/uoftasic/{{COURSE_ID}}/tree/main/scripts)
