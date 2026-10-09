# Ejemplos de notes.md — Intro a NumPy
# Fuente: notebook 4GeeksAcademy Intro to NumPy

import numpy as np


# =============================================================================
# Array unidimensional (1D)
# =============================================================================

array = np.array([1, 2, 3, 4, 5])
print(array)  # array([1, 2, 3, 4, 5])

# Acceder al tercer elemento
print(array[2])

# Cambiar el valor del segundo elemento
array[1] = 7
print(array)

# Sumar 10 a todos los elementos
array += 10
print(array)

# Calcular la suma de los elementos
sum_all = np.sum(array)
print(sum_all)


# =============================================================================
# Array N-dimensional
# =============================================================================

# Array 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array_2d)

# Array 3D (lista de matrices)
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(array_3d)


# =============================================================================
# Funciones de NumPy
# =============================================================================

# Crear un array para el ejemplo
arr = np.array([1, 2, 3, 4, 5])

# Operaciones Aritméticas
print("Suma:", np.add(arr, 5))
print("Producto:", np.multiply(arr, 3))

# Logarítmicas y Exponenciales
print("Logaritmo natural:", np.log(arr))
print("Exponencial:", np.exp(arr))

# Funciones Estadísticas
print("Media:", np.mean(arr))
print("Mediana:", np.median(arr))
print("Desviación estándar:", np.std(arr))
print("Varianza:", np.var(arr))
print("Máximo valor:", np.max(arr))
print("Índice del máximo valor:", np.argmax(arr))
print("Mínimo valor:", np.min(arr))
print("Índice del mínimo valor:", np.argmin(arr))
print("Suma de todos los elementos:", np.sum(arr))

# Funciones de Redondeo
arr_decimal = np.array([1.23, 2.47, 3.56, 4.89])
print("Redondeo:", np.around(arr_decimal))
print("Entero menor (floor):", np.floor(arr_decimal))
print("Entero mayor (ceil):", np.ceil(arr_decimal))
