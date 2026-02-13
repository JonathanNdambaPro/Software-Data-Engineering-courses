# Entiers normaux
x = 42
y = -100
print(x + y)  # -58

# Python peut gérer des entiers très grands (qui dépasseraient Java/C#)
# En Java, le max int est 2,147,483,647 (32 bits)
# En Java, le max long est 9,223,372,036,854,775,807 (64 bits)
tres_grand_nombre = 999999999999999999999999999999999999999999999999
print(tres_grand_nombre)  # Fonctionne sans problème!

# Opérations avec de très grands nombres
a = 10 ** 100  # 1 suivi de 100 zéros
b = 10 ** 101
resultat = a * b
print(f"Résultat a {len(str(resultat))} chiffres")

# Démonstration de l'impact sur la performance
import time

# Opération rapide avec de petits nombres
start = time.time()
petit = 1000 ** 10
end = time.time()
print(f"Petit nombre: {(end - start) * 1000:.4f} ms")

# Opération plus lente avec de très grands nombres
start = time.time()
grand = 1000 ** 1000
end = time.time()
print(f"Grand nombre: {(end - start) * 1000:.4f} ms")
