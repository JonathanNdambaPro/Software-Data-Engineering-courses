texte = "Python"

# Indexing (comme les listes)
print(texte[0])    # 'P' - premier caractère
print(texte[-1])   # 'n' - dernier caractère
print(texte[2])    # 't' - troisième caractère

# Slicing (comme les listes)
print(texte[0:3])   # 'Pyt' - du début à l'index 3 (exclus)
print(texte[2:])    # 'thon' - de l'index 2 jusqu'à la fin
print(texte[:4])    # 'Pyth' - du début à l'index 4 (exclus)
print(texte[::2])   # 'Pto' - un caractère sur deux
print(texte[::-1])  # 'nohtyP' - inversion de la string

# Concaténation (comme les listes)
salut = "Bonjour"
nom = "Alice"
message = salut + " " + nom
print(message)  # 'Bonjour Alice'

# Répétition (comme les listes)
print("Ha" * 3)  # 'HaHaHa'
separateur = "-" * 20
print(separateur)  # '--------------------'

# Longueur (comme les listes)
print(len("Python"))  # 6

# Itération (comme les listes)
for lettre in "Python":
    print(lettre)  # P, y, t, h, o, n (un par ligne)

# Appartenance (comme les listes)
print("th" in "Python")      # True
print("java" in "Python")    # False
print("P" not in "Python")   # False

# Différence importante: les strings sont IMMUTABLES!
# texte[0] = 'J'  # ❌ ERREUR! TypeError
# Il faut créer une nouvelle string:
nouveau_texte = 'J' + texte[1:]
print(nouveau_texte)  # 'Jython'
