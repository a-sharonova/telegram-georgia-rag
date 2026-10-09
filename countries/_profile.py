"""CountryProfile schema — the one explicit place that says what's actually
country-specific in this codebase (chat list + a handful of Russian-grammar
forms + a few tuning values). Everything else in config.py stays a single
shared source of truth across every deployment.

See countries/__init__.py for how one profile gets selected at runtime via
the COUNTRY env var, and countries/georgia.py / countries/spain.py for the
actual data.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CountryProfile:
    key: str  # "georgia" / "spain" — matches the COUNTRY env var value

    # Russian grammar: nominative ("Грузия"/"Испания") and prepositional
    # ("Грузии"/"Испании" — for -ия nouns this form also covers genitive/
    # dative, so these two fields are enough for every place this codebase
    # needs the country name inflected).
    name_nom: str
    name_prep: str

    # Regex root for "is this question about the WHOLE country" matching
    # (src/rag.py's _COUNTRY_WIDE_RX) — hand-picked, not derived from
    # name_nom/name_prep, because it must also catch adjective forms
    # ("грузинский") while avoiding false positives on unrelated words
    # (bare "Груз" would also match "груз"/"грузовик" — that's why the
    # Georgia root is "Грузи", not "Груз"; Spain's is "Испан", matching
    # Испания/Испании/испанский/испанцы but not shorter unrelated words).
    wide_rx_root: str

    # A few representative cities, used as examples inside the distillation
    # prompt (src/knowledge.py) so the model knows what "a specific city"
    # looks like for this country.
    city_examples: tuple[str, str, str]

    # A single precomposed example phrase like "в Тбилиси"/"в Мадриде" for
    # src/bot.py's EXAMPLES text — city names decline unpredictably in
    # Russian (Тбилиси is indeclinable, Мадрид needs "в Мадриде"), so this
    # is stored ready-made rather than built from city_examples[0] at runtime.
    example_city_prep: str

    # Nearby-country cities that leak into retrieval as noise (e.g. Yerevan/
    # Moscow showing up in Georgia chats) — src/rag.py's city-options filter.
    # Empty is safe (just means no filtering happens yet); fill in once a
    # real knowledge base reveals what actually leaks for this country.
    non_country_city_noise: frozenset[str]

    # config.INGEST_SINCE for this country's chats.
    ingest_since: str

    # Trailing line of config.SUPPORT_BANK_INFO (currency/minimum-amount
    # text) — the one part of that template that isn't already env-driven.
    support_min_text: str

    # config.CHATS for this country — same dict shape as the original
    # literal (username/chat_id/title, optional private).
    chats: list[dict]

    @property
    def prep_o(self) -> str:
        """'о' before a consonant, 'об' before a vowel — the standard
        Russian elision rule. Грузии -> 'о' (Г is a consonant); Испании ->
        'об' (И is a vowel). Computed once here so no prompt call site has
        to remember the rule (getting it wrong reads as a jarring typo —
        "о Испании" instead of "об Испании")."""
        return "об" if self.name_prep[0].upper() in "АЕЁИОУЭЮЯ" else "о"

    @property
    def about(self) -> str:
        """'о Грузии' / 'об Испании'."""
        return f"{self.prep_o} {self.name_prep}"

    @property
    def in_country(self) -> str:
        """'в Грузии' / 'в Испании' — 'в' never elides, unlike 'о'/'об'."""
        return f"в {self.name_prep}"
