# Interpolation de base
nom = "Alice"
age = 25
message = f"Bonjour, je m'appelle {nom} et j'ai {age} ans."
print(message)  # Bonjour, je m'appelle Alice et j'ai 25 ans.

# Expressions dans les f-strings
x = 10
y = 5
print(f"{x} + {y} = {x + y}")  # 10 + 5 = 15
print(f"{x} * {y} = {x * y}")  # 10 * 5 = 50

# Appeler des méthodes
nom = "alice"
print(f"Bonjour {nom.upper()}!")  # Bonjour ALICE!
print(f"Bonjour {nom.capitalize()}!")  # Bonjour Alice!

# Formatage de nombres
prix = 19.99
print(f"Prix: {prix:.2f}€")  # Prix: 19.99€

pi = 3.14159265359
print(f"Pi: {pi:.2f}")  # Pi: 3.14
print(f"Pi: {pi:.5f}")  # Pi: 3.14159

# Formatage de grands nombres avec séparateur
population = 67000000
print(f"Population: {population:,}")  # Population: 67,000,000

# Alignement et padding
nom = "Alice"
print(f"{nom:>10}")   # "     Alice" - aligné à droite, 10 caractères
print(f"{nom:<10}")   # "Alice     " - aligné à gauche
print(f"{nom:^10}")   # "  Alice   " - centré

# Afficher des pourcentages
taux = 0.157
print(f"Taux: {taux:.1%}")  # Taux: 15.7%

# Notation scientifique
grand_nombre = 1234567890
print(f"{grand_nombre:e}")  # 1.234568e+09

# Comparaison avec anciennes méthodes
# ❌ Ancienne méthode (moins lisible):
print("Bonjour, je m'appelle %s et j'ai %d ans." % (nom, age))
print("Bonjour, je m'appelle {} et j'ai {} ans.".format(nom, age))

# ✅ F-string (moderne et lisible):
print(f"Bonjour, je m'appelle {nom} et j'ai {age} ans.")

# Debug: afficher variable et valeur (Python 3.8+)
x = 42
print(f"{x=}")  # x=42
