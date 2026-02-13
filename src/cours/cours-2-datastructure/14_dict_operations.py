# Création de dictionnaires
dict_vide = {}
personne = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 30
}

# Accès (O(1) - très rapide!)
print(personne["nom"])  # Dupont
print(personne.get("age"))  # 30
print(personne.get("ville", "Paris"))  # Paris (défaut si clé absente)

# Modification et ajout
personne["age"] = 31  # Modifier
personne["ville"] = "Lyon"  # Ajouter nouvelle clé
print(personne)

# Suppression
del personne["ville"]
age = personne.pop("age")  # Retirer et retourner
print(age)  # 31

# Vérifier l'existence d'une clé (O(1) - très rapide!)
if "nom" in personne:
    print("Nom présent!")

# Itération
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")

# Méthodes utiles
print(personne.keys())    # dict_keys(['nom', 'prenom'])
print(personne.values())  # dict_values(['Dupont', 'Jean'])

# Dict comprehension
carres = {x: x**2 for x in range(5)}
print(carres)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Fusion de dictionnaires (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
fusion = dict1 | dict2
print(fusion)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Comptage rapide avec get()
mots = ["chat", "chien", "chat", "oiseau", "chat"]
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1
print(compteur)  # {'chat': 3, 'chien': 1, 'oiseau': 1}
