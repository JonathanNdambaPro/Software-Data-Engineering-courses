# Opérations de base avec les flottants
x = 3.14
y = 2.71
print(x * y)  # 8.5094

# Problème classique de précision: 0.1 + 0.2
resultat = 0.1 + 0.2
print(resultat)  # 0.30000000000000004 au lieu de 0.3 !
print(resultat == 0.3)  # False - problème pour les comparaisons

# Perte de précision avec de grands nombres
grand_float = 1.0e16  # 10 000 000 000 000 000
petit_ajout = grand_float + 1.0
print(petit_ajout == grand_float)  # True - le +1 est perdu!

# Troncature des décimales
nombre_long = 1.123456789012345678901234567890
print(nombre_long)  # Environ ~15-17 chiffres de précision seulement

# Propagation d'erreur dans les calculs
# Exemple: calcul itératif qui accumule les erreurs
somme = 0.0
for i in range(10):
    somme += 0.1
print(f"Résultat: {somme}")  # ~0.9999999999999999 au lieu de 1.0
print(f"Erreur: {abs(somme - 1.0)}")

# Comparaison correcte de flottants avec une tolérance
def floats_egaux(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance

print(floats_egaux(0.1 + 0.2, 0.3))  # True - bonne pratique!

# Éviter les comparaisons directes
a = 0.1 + 0.2
# Mauvais:
# if a == 0.3:
# Bon:
if abs(a - 0.3) < 1e-9:
    print("Les nombres sont égaux (avec tolérance)")
