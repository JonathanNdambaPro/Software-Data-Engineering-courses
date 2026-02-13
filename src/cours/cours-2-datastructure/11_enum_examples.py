from enum import Enum, auto, IntEnum, StrEnum

# Enum de base
class Couleur(Enum):
    ROUGE = 1
    VERT = 2
    BLEU = 3

# Accéder aux membres
print(Couleur.ROUGE)        # Couleur.ROUGE
print(Couleur.ROUGE.name)   # 'ROUGE'
print(Couleur.ROUGE.value)  # 1

# Comparaison
favori = Couleur.BLEU
if favori == Couleur.BLEU:
    print("C'est bleu!")  # S'exécute

# ❌ Comparaison par valeur ne fonctionne pas!
print(Couleur.ROUGE == 1)  # False

# Itération
print("Toutes les couleurs:")
for couleur in Couleur:
    print(f"{couleur.name} = {couleur.value}")

# ---

# auto() - génération automatique de valeurs
class Statut(Enum):
    EN_ATTENTE = auto()   # 1
    EN_COURS = auto()     # 2
    TERMINE = auto()      # 3
    ANNULE = auto()       # 4

print(Statut.EN_COURS.value)  # 2

# ---

# StrEnum - Enum basé sur des strings (Python 3.11+)
class Environnement(StrEnum):
    DEV = "development"
    STAGING = "staging"
    PROD = "production"

# Avec StrEnum, on peut comparer directement avec des strings
env = Environnement.PROD
print(env == "production")  # True
print(env)  # 'production' (pas Environnement.PROD)

# Utile pour les configurations
config_env = "production"
if config_env == Environnement.PROD:
    print("Mode production!")  # S'exécute

# ---

# StrEnum avec auto() - génère automatiquement les valeurs
class Direction(StrEnum):
    HAUT = auto()     # 'haut'
    BAS = auto()      # 'bas'
    GAUCHE = auto()   # 'gauche'
    DROITE = auto()   # 'droite'

print(Direction.HAUT)        # 'haut'
print(Direction.HAUT.value)  # 'haut'

# ---

# IntEnum - Enum compatible avec les entiers
class Code(IntEnum):
    SUCCES = 200
    NON_TROUVE = 404
    ERREUR_SERVEUR = 500

# IntEnum peut être utilisé comme un entier
code = Code.SUCCES
print(code == 200)  # True
print(code + 1)     # 201

# ---

# Cas d'usage réel: remplacer les "magic strings"
# ❌ Mauvais (strings magiques, sujets aux typos):
def traiter_commande(statut):
    if statut == "en_cours":  # Typo possible!
        print("Traitement...")

traiter_commande("en cours")  # Bug silencieux!

# ✅ Bon (avec Enum):
class StatutCommande(StrEnum):
    EN_ATTENTE = auto()
    EN_COURS = auto()
    TERMINE = auto()

def traiter_commande_safe(statut: StatutCommande):
    if statut == StatutCommande.EN_COURS:
        print("Traitement...")

traiter_commande_safe(StatutCommande.EN_COURS)  # Type-safe!
