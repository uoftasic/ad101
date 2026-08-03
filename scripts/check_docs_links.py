#!/usr/bin/env python3
"""Validate Docsify links under docs/.

Docsify quirk (default relativePath=false):
  - Page links go through the hash router → use docs-root paths
    (guide/foo.md, labs/bar.md) so the URL becomes #/guide/foo
  - Images are fetched relative to the current route directory → nested
    pages must use ../assets/img/... (bare assets/img 404s as guide/assets/…)

Root pages (_sidebar.md, _navbar.md, README.md) use docs-root paths for both.

Usage (repo root):
    python3 scripts/check_docs_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")
ROOT_STYLE = {"_sidebar.md", "_navbar.md", "README.md"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def main() -> int:
    errors: list[str] = []

    for md in sorted(DOCS.rglob("*.md")):
        rel_md = md.relative_to(DOCS)
        nested = md.name not in ROOT_STYLE

        for m in LINK_RE.finditer(md.read_text(encoding="utf-8")):
            is_image_markup = m.group(1) == "!"
            url = m.group(3).strip()
            if url.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path = url.split("#", 1)[0].split("?", 1)[0]
            if not path:
                continue

            suffix = Path(path).suffix.lower()
            is_image = is_image_markup or suffix in IMAGE_SUFFIXES
            is_page = suffix == ".md" or path == "README.md"

            if nested and is_image:
                if not path.startswith("../"):
                    errors.append(
                        f"{rel_md}: image {url!r} must be file-relative "
                        f"(../assets/img/…)"
                    )
                    continue
                target = (md.parent / path).resolve()
            elif nested and is_page:
                if path.startswith("../") or path.startswith("./"):
                    errors.append(
                        f"{rel_md}: page link {url!r} must be docs-root "
                        f"(guide/…, labs/…) — '../' breaks the hash router"
                    )
                    continue
                if "/" not in path and path != "README.md":
                    # bare sibling like building-signals.md → #/building-signals (wrong)
                    errors.append(
                        f"{rel_md}: page link {url!r} needs a folder prefix "
                        f"(e.g. guide/{path})"
                    )
                    continue
                target = (DOCS / path).resolve()
            else:
                # Root-style page
                target = (DOCS / path.lstrip("/")).resolve()

            try:
                target.relative_to(DOCS.resolve())
            except ValueError:
                errors.append(f"{rel_md}: escapes docs/ → {url!r}")
                continue
            if not target.exists():
                errors.append(f"{rel_md}: missing {url!r}")

    if errors:
        print(f"FAIL — {len(errors)} docs link issue(s):")
        for e in errors:
            print(f"  {e}")
        return 1

    print("OK — Docsify links follow image=file-relative / page=docs-root rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
