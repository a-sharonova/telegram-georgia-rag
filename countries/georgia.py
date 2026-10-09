"""Georgia country profile — the default (COUNTRY unset or "georgia").

Every value here is the literal that used to live directly in config.py /
src/rag.py before the multi-country refactor — moved here verbatim, not
changed, so the live prod deployment's behavior is unaffected.
"""
from __future__ import annotations

from countries._profile import CountryProfile

PROFILE = CountryProfile(
    key="georgia",
    name_nom="Грузия",
    name_prep="Грузии",
    wide_rx_root="Грузи",
    city_examples=("Тбилиси", "Батуми", "Кутаиси"),
    example_city_prep="в Тбилиси",
    non_country_city_noise=frozenset(
        {"Ереван", "Москва", "Владикавказ", "Санкт-Петербург", "Стамбул"}
    ),
    ingest_since="2024-01-01",
    support_min_text="От 3₾ / ~$1.",
    # `username` builds t.me/<username>/<msg_id> source links (and is the
    # internal slug for data/raw/<username>.jsonl etc.); `chat_id` is what
    # Telethon uses to actually fetch history. `private: True` marks a
    # closed chat with no public @username (source links become
    # t.me/c/<internal_id>/<msg_id>, openable only by members — see
    # src/ingest.py::_chat_link). See config.py's original CHATS docstring
    # for the full explanation, preserved there.
    chats=[
        {"username": "helpgeorgia", "chat_id": -1001452236047, "title": "Взаимопомощь. Грузия"},
        {"username": "ipgeorgiachat", "chat_id": -1001670908431, "title": "ИП/Бизнес Грузия"},
        {"username": "nogotochki", "chat_id": -1001318697228, "title": "Ноготочки", "private": True},
        {"username": "paravaingeorgia", "chat_id": -1001512786455, "title": "Получение водительских прав в Грузии"},
        {"username": "mygeorgia_chat", "chat_id": -1001486751358, "title": "ГРУЗИЯ ЧАТ"},
        {"username": "tbilisi_girl", "chat_id": -1001549075106, "title": "Женский чат Тбилиси"},
        {"username": "georgia_it", "chat_id": -1001688709586, "title": "Грузия IT чат"},
        {"username": "gruzia_medicina", "chat_id": -1001781403833, "title": "Грузия медицина"},
        {"username": "georgia_woman", "chat_id": -1001276829180, "title": "Тбилиси женский чат"},
        {"username": "Gruziya_Mastera", "chat_id": -1001896208901, "title": "Грузия мастера услуги Батуми Тбилиси"},
    ],
)
