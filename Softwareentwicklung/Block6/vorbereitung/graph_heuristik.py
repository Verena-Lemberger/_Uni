sld = {
    "Ulm": {
        "Basel": 204,
        "Bayreuth": 207,
        "Bern": 247,
        "Frankfurt": 215,
        "Innsbruck": 163,
        "Karlsruhe": 137,
        "Landeck": 143,
        "Linz": 318,
        "München": 120,
        "Mannheim": 164,
        "Memmingen": 47,
        "Nürnberg": 132,
        "Passau": 257,
        "Rosenheim": 168,
        "Stuttgart": 75,
        "Salzburg": 236,
        "Würzburg": 153,
        "Zürich": 157,
        "Ulm": 0
    }
}

def h1(state):
    return sld.get("Ulm").get(state)