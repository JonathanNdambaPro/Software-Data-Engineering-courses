# Création de sets
set_vide = set()  # ❌ PAS {} car c'est un dict!
nombres = {1, 2, 3, 4, 5}
lettres = set(['a', 'b', 'c', 'a', 'b'])  # Doublons automatiquement retirés
print(lettres)  # {'a', 'b', 'c'}

# Dédoublonnage rapide
liste_avec_doublons = [1, 2, 2, 3, 3, 3, 4]
liste_unique = list(set(liste_avec_doublons))
print(liste_unique)  # [1, 2, 3, 4] (ordre peut varier)

# Ajout et suppression
nombres.add(6)  # Ajouter
print(nombres)  # {1, 2, 3, 4, 5, 6}

nombres.remove(3)  # Retirer (erreur si absent)
nombres.discard(10)  # Retirer (pas d'erreur si absent)

# Appartenance (O(1) - très rapide!)
if 5 in nombres:
    print("5 est présent")

# Opérations ensemblistes
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (tous les éléments)
print(set1 | set2)  # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))  # Équivalent

# Intersection (éléments communs)
print(set1 & set2)  # {3, 4}
print(set1.intersection(set2))  # Équivalent

# Différence (dans set1 mais pas set2)
print(set1 - set2)  # {1, 2}
print(set1.difference(set2))  # Équivalent

# Différence symétrique (dans l'un ou l'autre, pas les deux)
print(set1 ^ set2)  # {1, 2, 5, 6}

# Sous-ensemble et sur-ensemble
set_petit = {1, 2}
print(set_petit.issubset(set1))  # True
print(set1.issuperset(set_petit))  # True

# Frozenset (immutable)
fs = frozenset([1, 2, 3])
# fs.add(4)  # ❌ AttributeError - immutable!

# Frozenset peut être clé de dictionnaire
sets_dict = {
    frozenset([1, 2]): "Ensemble A",
    frozenset([3, 4]): "Ensemble B"
}
print(sets_dict[frozenset([1, 2])])  # Ensemble A

# Cas d'usage: filtrer doublons tout en gardant ordre
def unique_ordered(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

liste = [1, 2, 2, 3, 1, 4, 3, 5]
print(unique_ordered(liste))  # [1, 2, 3, 4, 5]
