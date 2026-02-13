# Création de tuples
tuple_vide = ()
coordonnees = (10, 20)
personne = ("Jean", "Dupont", 30)
tuple_un_element = (42,)  # Virgule obligatoire!

# Accès (comme les listes)
print(coordonnees[0])  # 10
print(personne[1])     # Dupont

# ❌ Immutable - ne peut pas être modifié
# coordonnees[0] = 15  # TypeError!

# Unpacking (déballage)
x, y = coordonnees
print(f"x={x}, y={y}")  # x=10, y=20

prenom, nom, age = personne
print(f"{prenom} {nom}, {age} ans")

# Packing (emballage)
point = 5, 10  # Les parenthèses sont optionnelles
print(point)  # (5, 10)

# Échange de variables (grâce au unpacking)
a, b = 1, 2
a, b = b, a  # Échange!
print(f"a={a}, b={b}")  # a=2, b=1

# Fonction retournant plusieurs valeurs
def get_min_max(nombres):
    return min(nombres), max(nombres)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Tuple comme clé de dictionnaire (car immutable)
positions = {}
positions[(0, 0)] = "Origine"
positions[(1, 2)] = "Point A"
print(positions[(0, 0)])  # Origine

# Unpacking étendu (Python 3+)
premier, *milieu, dernier = (1, 2, 3, 4, 5)
print(premier)  # 1
print(milieu)   # [2, 3, 4]
print(dernier)  # 5

# Named tuples (pour plus de lisibilité)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
print(p[0], p[1])  # 10 20 - accès par index aussi
