"""Path bootstrap — add labs/ to sys.path so `from common.adsig import ...` works."""

from __future__ import annotations

import sys
from pathlib import Path

_LABS = Path(__file__).resolve().parents[2]  # .../labs
if str(_LABS) not in sys.path:
    sys.path.insert(0, str(_LABS))
