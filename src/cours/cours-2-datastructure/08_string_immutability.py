# STRING (immutable) - ne peut PAS être modifiée
texte = "Python"

# ❌ Tentative de modification -> ERREUR
try:
    texte[0] = 'J'  # TypeError
except TypeError as e:
    print(f"Erreur: {e}")

# ✅ Pour "modifier", on crée une NOUVELLE string
nouveau_texte = 'J' + texte[1:]
print(nouveau_texte)  # 'Jython'
print(texte)  # 'Python' - l'original n'a pas changé!

# LIST (mutable) - modification directe possible
lettres = ['P', 'y', 't', 'h', 'o', 'n']
lettres[0] = 'J'  # ✅ Fonctionne!
print(lettres)  # ['J', 'y', 't', 'h', 'o', 'n']

# Performance: éviter la concaténation répétée
# ❌ Lent (crée une nouvelle string à chaque itération):
resultat = ""
for i in range(1000):
    resultat += str(i)

# ✅ Rapide (une seule opération finale):
morceaux = [str(i) for i in range(1000)]
resultat = ''.join(morceaux)
