# Python est dynamiquement typé : on peut changer le type d'une variable
x = 5        # x est un int
x = "hello"  # x devient un str → aucune erreur !

# Avec mypy, on peut détecter les erreurs de type AVANT l'exécution
def greet(name: str) -> str:
    return "Hello " + name

# greet(123)  # ❌ mypy détecte l'erreur, mais Python l'exécute quand même
