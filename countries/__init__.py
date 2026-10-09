"""Country profile loader — the COUNTRY env var (georgia|spain) picks which
profile config.py and everything downstream of it (src/rag.py,
src/knowledge.py, the eval judges, src/bot.py, scripts/dedupe_knowledge.py)
uses. Each deployment is its own OS process/checkout with its own .env (see
README's Deployment section / CLAUDE.local.md) — this is read once, the same
way every other env-driven setting in config.py is.

Unset or unrecognized COUNTRY -> "georgia": the live prod deployment's .env
has no COUNTRY key today and must keep behaving exactly as before — this
loader never raises for a missing/bad value, only warns.
"""
from __future__ import annotations

import os
import sys

from dotenv import load_dotenv

# Idempotent — config.py also calls this, but countries/ is imported FROM
# config.py before config.py's own load_dotenv() line has necessarily run
# in every possible import order, so this makes the package self-sufficient.
load_dotenv()

from countries import georgia as _georgia  # noqa: E402
from countries import spain as _spain  # noqa: E402

_PROFILES = {_georgia.PROFILE.key: _georgia.PROFILE, _spain.PROFILE.key: _spain.PROFILE}

_raw = (os.getenv("COUNTRY") or "georgia").strip().lower()
if _raw not in _PROFILES:
    print(
        f"[countries] COUNTRY={_raw!r} not recognized (known: {sorted(_PROFILES)}) "
        "— falling back to 'georgia'.",
        file=sys.stderr,
    )
    _raw = "georgia"

PROFILE = _PROFILES[_raw]
