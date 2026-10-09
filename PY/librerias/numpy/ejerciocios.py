"""
Ejercicios Intro a NumPy (4GeeksAcademy)
Fuente ejercicios:
https://colab.research.google.com/github/4GeeksAcademy/machine-learning-prework/blob/main/02-numpy/02.1-Intro-to-Numpy.es.ipynb
Fuente soluciones:
https://github.com/4GeeksAcademy/machine-learning-prework/blob/main/02-numpy/02.1-Intro-to-Numpy_solutions.ipynb

Las celdas In [ ]: del notebook de ejercicios vienen vacías (espacio para practicar).
Aquí centralizo: instrucciones en comentarios + solución oficial lista para ejecutar.
Si quieres practicar: comenta el bloque de solución y escribe el tuyo debajo del enunciado.
"""

import numpy as np

np.random.seed(42)


# =============================================================================
# Creación de arrays
# =============================================================================


# -----------------------------------------------------------------------------
# Ejercicio 01: Crea un vector nulo (null vector) que tenga 10 elementos (★☆☆)
# Un vector nulo es un array de una dimensión compuesto por ceros (0).
# NOTA: Revisa np.zeros
# https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
# -----------------------------------------------------------------------------
# In [ ]:  (celda vacía en el notebook de ejercicios)

print("Ejercicio 01:")
print(np.zeros(10))


# -----------------------------------------------------------------------------
# Ejercicio 02: Crea un vector de unos que tenga 10 elementos (★☆☆)
# NOTA: Revisa np.ones
# https://numpy.org/doc/stable/reference/generated/numpy.ones.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 02:")
print(np.ones(10))


# -----------------------------------------------------------------------------
# Ejercicio 03: Investiga linspace de NumPy y crea un array con 10 elementos (★☆☆)
# NOTA: Revisa np.linspace
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 03:")
# Create an array of 10 elements with numbers from 1 to 10
print(np.linspace(1, 10, 10))


# -----------------------------------------------------------------------------
# Ejercicio 04: Busca varias formas de generar un array con números aleatorios
# y crea un array 1D y dos arrays 2D (★★☆)
# NOTA: Revisa np.random.rand, np.random.randint y np.random.randn
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 04:")
# np.random.rand: Random numbers from 0 to 1
print(np.random.rand(10))

# np.random.randn: Normal distribution (mean = 0, std = 1)
print(np.random.randn(5, 5))

# np.random.randint: Random integers (from included, to not included)
print(np.random.randint(1, 10, size=(2, 5)))


# -----------------------------------------------------------------------------
# Ejercicio 05: Crea una matriz (array 2D) identidad de 5x5 (★☆☆)
# NOTA: Revisa np.eye
# https://numpy.org/devdocs/reference/generated/numpy.eye.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 05:")
print(np.eye(5))


# -----------------------------------------------------------------------------
# Ejercicio 06: Crea una matriz con números aleatorios de 3x2 y calcula
# el valor mínimo y máximo (★☆☆)
# NOTA: Revisa np.min y np.max
# https://numpy.org/devdocs/reference/generated/numpy.min.html
# https://numpy.org/devdocs/reference/generated/numpy.max.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 06:")
matrix = np.random.rand(3, 2)
print(matrix)

min_value = np.min(matrix)
max_value = np.max(matrix)
print(f"Min value: {min_value} \nMax value: {max_value}")
# Another way: matrix.min(), matrix.max()


# -----------------------------------------------------------------------------
# Ejercicio 07: Crea un vector con números aleatorios de 30 elementos
# y calcula la media (★☆☆)
# NOTA: Revisa np.mean
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 07:")
array = np.random.randint(5, 13, size=30)
print(array)

mean_value = np.mean(array)
print(f"Mean value: {mean_value}")
# Another way: array.mean()


# -----------------------------------------------------------------------------
# Ejercicio 08: Convierte la lista [1, 2, 3] y la tupla (1, 2, 3) en arrays (★☆☆)
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 08:")
l = [1, 2, 3]
array = np.asarray(l)
print(array)
# Another way: np.array(l)

t = (1, 2, 3)
array = np.asarray(t)
print(array)
# Another way: np.array(t)


# =============================================================================
# Operaciones entre arrays
# =============================================================================


# -----------------------------------------------------------------------------
# Ejercicio 09: Invierte el vector del ejercicio anterior (★☆☆)
# NOTA: Revisa np.flip
# https://numpy.org/doc/stable/reference/generated/numpy.flip.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 09:")
print(np.flip(array))
# Another way: array[::-1]


# -----------------------------------------------------------------------------
# Ejercicio 10: Cambia el tamaño de un array aleatorio de dimensiones 5x12
# en 12x5 (★☆☆)
# NOTA: Revisa np.reshape
# https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 10:")
matrix = np.random.randn(5, 12)
print(matrix)
print(np.reshape(matrix, (12, 5)))


# -----------------------------------------------------------------------------
# Ejercicio 11: Convierte la lista [1, 2, 0, 0, 4, 0] en un array y obtén
# el índice de los elementos que no son cero (★★☆)
# NOTA: Revisa np.where
# https://numpy.org/devdocs/reference/generated/numpy.where.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 11:")
l = [1, 2, 0, 0, 4, 0]
array = np.array(l)
print(array)

indices = np.where(array != 0)
print(indices)
# Another way: np.nonzero(array)


# -----------------------------------------------------------------------------
# Ejercicio 12: Convierte la lista [0, 5, -1, 3, 15] en un array,
# multiplica sus valores por -2 y obtén los elementos pares (★★☆)
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 12:")
l = [0, 5, -1, 3, 15]
array = np.asarray(l)
array = array * -2

even_numbers = array[array % 2 == 0]
print(even_numbers)


# -----------------------------------------------------------------------------
# Ejercicio 13: Crea un vector aleatorio de 10 elementos y ordénalo
# de menor a mayor (★★☆)
# NOTA: Revisa np.sort
# https://numpy.org/doc/stable/reference/generated/numpy.sort.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 13:")
array = np.random.random_sample(10)
array = np.sort(array)
print(array)
# Another way: array.sort()


# -----------------------------------------------------------------------------
# Ejercicio 14: Genera dos vectores aleatorios de 8 elementos y aplica
# las operaciones de suma, resta y multiplicación entre ellos (★★☆)
# NOTA: Funciones matemáticas
# https://numpy.org/doc/stable/reference/routines.math.html
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 14:")
array1 = np.random.randint(0, 10, 8)
array2 = np.random.randint(0, 10, 8)
print(f"Array 1: {array1} \nArray 2: {array2}")

arr_sum = array1 + array2
arr_sub = array1 - array2
arr_prod = array1 * array2

print(f"Sum: {arr_sum} \nSubtraction: {arr_sub} \nProduct: {arr_prod}")


# -----------------------------------------------------------------------------
# Ejercicio 15: Convierte la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# en un array y transfórmalo en una matriz con filas de 3 columnas (★★★)
# -----------------------------------------------------------------------------
# In [ ]:

print("\nEjercicio 15:")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
array = np.array(l)
print(array)
print(np.reshape(array, (4, 3)))
