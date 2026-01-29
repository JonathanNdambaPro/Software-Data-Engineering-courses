# Manifest : on déclare explicitement le type
age: int = 25
name: str = "Alice"

# Inferred : mypy/pyright déduit le type automatiquement
age = 25      # mypy sait que c'est un int
name = "Alice"  # mypy sait que c'est un str

# L'inférence fonctionne aussi pour les retours de fonction
def get_age():
    return 25  # mypy infère que le retour est int
