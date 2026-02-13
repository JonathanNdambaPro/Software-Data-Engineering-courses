# Valeurs booléennes de base
vrai = True
faux = False
print(vrai)  # True
print(faux)  # False

# Équivalence avec les entiers
print(True == 1)   # True
print(False == 0)  # True
print(True + True)  # 2 (1 + 1)
print(True * 5)     # 5 (1 * 5)

# Conversion bool vers int
print(int(True))   # 1
print(int(False))  # 0

# Conversion int vers bool
print(bool(1))     # True
print(bool(0))     # False
print(bool(42))    # True (tout nombre non-zéro est True)
print(bool(-5))    # True

# Opérations booléennes
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(False or False)   # False
print(not True)         # False
print(not False)        # True

# Comparaisons retournent des booléens
print(5 > 3)      # True
print(10 == 10)   # True
print(7 < 2)      # False
print("a" == "a") # True

# Truthiness et Falsiness - autres types évalués comme bool
# Falsy (évalués comme False):
print(bool(0))         # False
print(bool(""))        # False - string vide
print(bool([]))        # False - liste vide
print(bool({}))        # False - dict vide
print(bool(None))      # False

# Truthy (évalués comme True):
print(bool(1))         # True
print(bool("texte"))   # True - string non-vide
print(bool([1, 2]))    # True - liste non-vide
print(bool({"a": 1}))  # True - dict non-vide

# Utilisation dans les conditions
age = 18
if age >= 18:
    print("Majeur")  # S'exécute car True
else:
    print("Mineur")

# Court-circuit (short-circuit evaluation)
def fonction_lente():
    print("Fonction appelée")
    return True

# and: si le premier est False, le second n'est pas évalué
result = False and fonction_lente()  # fonction_lente() n'est PAS appelée
print(result)  # False

# or: si le premier est True, le second n'est pas évalué
result = True or fonction_lente()  # fonction_lente() n'est PAS appelée
print(result)  # True
