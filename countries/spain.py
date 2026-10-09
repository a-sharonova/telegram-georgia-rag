"""Spain country profile (COUNTRY=spain).

Seeded with the 6 Spain-related Telegram chats found and subscribed to
during the initial research pass (2026-10-09) — the general ExpatFM/OFF MAP
network chats plus the two Barcelona-specific ones. Not yet run through
src.ingest/src.knowledge, so this is a starting point, not a tuned config:
ingest_since/support_min_text are placeholders, non_country_city_noise is
empty (no real corpus yet to reveal what leaks in), and the chat list itself
may need pruning/expanding once real volume and content quality are visible.
"""
from __future__ import annotations

from countries._profile import CountryProfile

PROFILE = CountryProfile(
    key="spain",
    name_nom="Испания",
    name_prep="Испании",
    wide_rx_root="Испан",
    city_examples=("Мадрид", "Барселона", "Валенсия"),
    example_city_prep="в Мадриде",
    # Empty until a real knowledge base exists — same role as Georgia's
    # Ереван/Москва/... list (nearby-country cities that leak into
    # retrieval as noise), just nothing observed yet to put here.
    non_country_city_noise=frozenset(),
    # Placeholder — revisit once ingest actually runs and real message
    # volume/history depth for these chats is known.
    ingest_since="2024-01-01",
    # Placeholder currency line — adjust once real SUPPORT_BANK_* values
    # for a Spain deployment exist (config.py reads those from .env).
    support_min_text="От 1€ / ~$1.",
    chats=[
        {"username": "russians_in_spain", "chat_id": -1002020533312, "title": "Все русские в Испании"},
        {"username": "spain4ru", "chat_id": -1001101727718, "title": "Русская Испания"},
        {"username": "women_in_spain", "chat_id": -1002153985905, "title": "Женский чат. Испания"},
        {"username": "nedvizhimost_spain", "chat_id": -1002164725134, "title": "Недвижимость. Испания"},
        {"username": "russians_in_barcelona", "chat_id": -1002071220069, "title": "Русские в Барселоне"},
        {"username": "spain_granitsa", "chat_id": -1001745587210, "title": "Испания Барселона Чат"},
    ],
)
