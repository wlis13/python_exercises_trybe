import random

dates = {
    "pt-BR": {
        "first_part": random.choice(["AYT", "SAW", "NYG", "PKI"]),
        "second_part": random.choice(["7Y45", "2L54", "0N26", "1U20"]),
    },
    "es-AR": {
        "first_part": random.choice(["AA", "AB", "AC", "AD", "AE"]),
        "half_part": random.randint(1000, 9999),
        "second_part": random.choice(["ES", "RS", "LS"]),
    },
    "fr-FR": {
        "first_part": random.randint(1000, 9999),
        "half_part": random.choice(["AA", "AB", "AC", "AD", "AE"]),
        "second_part": random.randint(10, 99),
    },
}
