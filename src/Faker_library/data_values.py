import random

dates_locales = {
    "pt-BR": {
        "first_part": random.choice(["BRA", "SAW", "NYG", "PKI"]),
        "second_part": random.choice(["7Y45", "2L54", "0N26", "1U20"]),
    },
    "es-AR": {
        "first_part": random.choice(["AR", "AB", "AC", "AD", "AE"]),
        "half_part": random.randint(1000, 9999),
        "second_part": random.choice(["ES", "RS", "LS"]),
    },
    "fr-FR": {
        "first_part": random.randint(1000, 9999),
        "half_part": random.choice(["FR", "AB", "AC", "AD", "AE"]),
        "second_part": random.randint(10, 99),
    },
    "en-UA": {
        "first_part": random.choice(["AUS", "TRS", "CXS", "VZX"]),
        "second_part": random.randint(100, 999),
    },
    "de-DE": {
        "first_part": random.choice(["ALM", "IUB", "MNC", "MMC"]),
        "second_part": random.randint(100, 999),
    },
    "en-US": {
        "first_part": random.choice(["ALM", "IUB", "MNC", "MMC"]),
        "second_part": random.randint(100, 999),
    },
}
