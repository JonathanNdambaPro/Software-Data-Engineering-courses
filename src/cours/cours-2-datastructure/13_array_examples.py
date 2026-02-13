from array import array
import numpy as np

# Array Python standard (un seul type)
arr = array('i', [1, 2, 3, 4, 5])  # 'i' = entiers signés
print(arr)  # array('i', [1, 2, 3, 4, 5])

# Modification
arr[0] = 10
print(arr)  # array('i', [10, 2, 3, 4, 5])

# ❌ Tous les éléments doivent être du même type
# arr.append(3.14)  # TypeError!

# NumPy arrays (plus puissants et populaires)
np_arr = np.array([1, 2, 3, 4, 5])
print(np_arr)  # [1 2 3 4 5]

# Opérations vectorisées (très rapides!)
print(np_arr * 2)  # [ 2  4  6  8 10]
print(np_arr + 10)  # [11 12 13 14 15]

# Opérations mathématiques
print(np_arr.mean())  # 3.0
print(np_arr.sum())   # 15
print(np_arr.max())   # 5

# Arrays multidimensionnels
matrice = np.array([[1, 2, 3], [4, 5, 6]])
print(matrice)
print(matrice.shape)  # (2, 3)
