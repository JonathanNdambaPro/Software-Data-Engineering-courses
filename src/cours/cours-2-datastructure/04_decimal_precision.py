from decimal import Decimal, getcontext

# Créer des Decimal à partir de strings (recommandé)
# IMPORTANT: Utiliser des strings, pas des floats!
prix1 = Decimal('10.50')
prix2 = Decimal('20.30')
total = prix1 + prix2
print(f"Total: {total}")  # 30.80 - précis!

# Comparaison: Float vs Decimal
# Avec float (imprécis):
float_result = 0.1 + 0.2
print(f"Float: {float_result}")  # 0.30000000000000004

# Avec Decimal (précis):
decimal_result = Decimal('0.1') + Decimal('0.2')
print(f"Decimal: {decimal_result}")  # 0.3 - exactement!
print(decimal_result == Decimal('0.3'))  # True

# Problème: créer Decimal à partir de float (à éviter!)
mauvais_decimal = Decimal(0.1)  # Hérite l'imprécision du float
print(f"Mauvais: {mauvais_decimal}")  # 0.1000000000000000055511151231257827021181583404541015625

bon_decimal = Decimal('0.1')  # Parfaitement précis
print(f"Bon: {bon_decimal}")  # 0.1

# Définir la précision
getcontext().prec = 6  # 6 chiffres significatifs
result = Decimal('1') / Decimal('3')
print(f"1/3 avec précision 6: {result}")  # 0.333333

getcontext().prec = 28  # Précision par défaut
result = Decimal('1') / Decimal('3')
print(f"1/3 avec précision 28: {result}")  # Plus de chiffres

# Cas d'usage: calculs financiers
# Les banques ne peuvent pas tolérer les erreurs de précision!
montant = Decimal('100.00')
taux_taxe = Decimal('0.20')  # 20%
taxe = montant * taux_taxe
total_ttc = montant + taxe
print(f"Montant HT: {montant}")
print(f"Taxe (20%): {taxe}")
print(f"Total TTC: {total_ttc}")  # 120.00

# Arrondir correctement pour l'argent
from decimal import ROUND_HALF_UP
prix = Decimal('10.555')
prix_arrondi = prix.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(f"Prix arrondi: {prix_arrondi}")  # 10.56
