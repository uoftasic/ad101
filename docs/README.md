# {{COURSE_TITLE}}

{{DESCRIPTION}}

Part of the **UofT ASIC Team** education materials. This site is the published documentation; runnable labs and scripts live in the [GitHub repo](https://github.com/uoftasic/{{COURSE_ID}}) (not under `docs/`).

Education hub: [edu.uoftasic.com](https://edu.uoftasic.com/).

## Quick links

| What | Where |
|------|--------|
| Getting started | [guide/getting-started.md](guide/getting-started.md) |
| Lab 01 writeup | [labs/lab-01-overview.md](labs/lab-01-overview.md) |
| Lab packages | [labs/](https://github.com/uoftasic/{{COURSE_ID}}/tree/main/labs) |
| Scripts | [scripts/](https://github.com/uoftasic/{{COURSE_ID}}/tree/main/scripts) |

## Math

Inline: $E = mc^2$. Display:

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

## Figures

Images used in docs live under `docs/assets/img/`:

![Sample figure](assets/img/sample-figure.png)

## Local preview

```bash
npx docsify-cli serve docs
# → http://localhost:3000
```
