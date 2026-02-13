# Création de listes
liste_vide = []
liste_nombres = [1, 22, 9, 5, 100]
liste_mixte = [1, "texte", 3.14, True]  # Types différents possibles

print(type([]))  # <class 'list'>

# Accès et modification (mutable)
liste_nombres[0] = 999
print(liste_nombres)  # [999, 22, 9, 5, 100]

# Méthodes principales
liste_nombres.append(200)  # Ajouter à la fin
print(liste_nombres)  # [999, 22, 9, 5, 100, 200]

liste_nombres.insert(0, 10)  # Insérer à l'index 0
print(liste_nombres)  # [10, 999, 22, 9, 5, 100, 200]

liste_nombres.remove(999)  # Retirer la première occurrence
print(liste_nombres)  # [10, 22, 9, 5, 100, 200]

dernier = liste_nombres.pop()  # Retirer et retourner le dernier
print(dernier)  # 200

# Tri
liste_nombres.sort()  # Trier en place
print(liste_nombres)  # [5, 9, 10, 22, 100]

liste_nombres.reverse()  # Inverser en place
print(liste_nombres)  # [100, 22, 10, 9, 5]

# Longueur
print(len(liste_nombres))  # 5

# Slicing
print(liste_nombres[1:3])  # [22, 10]
print(liste_nombres[:2])   # [100, 22]

# List comprehension (création rapide)
carres = [x**2 for x in range(5)]
print(carres)  # [0, 1, 4, 9, 16]

# Recherche (O(n) - peut être lent)
if 22 in liste_nombres:
    print("22 trouvé!")

index = liste_nombres.index(22)  # Trouver l'index
print(f"22 est à l'index {index}")  # 22 est à l'index 1
