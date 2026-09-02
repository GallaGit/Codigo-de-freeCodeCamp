Introducción a NumPy
NumPy es un juego de palabras que significa Python numérico (Numerical Python). Es una librería de código abierto que se utiliza para llevar a cabo tareas matemáticas con altísima eficiencia. Además, introduce estructuras de datos como los arrays multidimensionales, que se pueden operar entre ellos a alto nivel, sin meterse mucho en el detalle.

En concreto, las claves de esta librería son:

Array multidimensionales: Esta librería proporciona un objeto llamado ndarray, que permite almacenar y manipular grandes conjuntos de datos de forma eficiente. Los arrays pueden tener cualquier número de dimensiones.
Operaciones Vectorizadas: NumPy permite realizar operaciones matemáticas en arrays completos sin la necesidad de bucles explícitos en el código, lo que lo hace muy rápido y eficiente.
Funciones matemáticas: NumPy proporciona una amplia gama de funciones matemáticas para trabajar con arrays, incluyendo funciones trigonométricas, estadísticas, álgebra lineal, entre otras.
Eficiencia: Es mucho más rápido que la misma funcionalidad implementada directamente sobre Python nativo. Además, es muy flexible en términos de acceso y manipulación de elementos individuales o subconjuntos de arrays.
NumPy es una biblioteca fundamental para el Machine Learning y la ciencia de los datos en Python. Proporciona una amplia gama de herramientas y funciones para trabajar eficientemente con datos numéricos en forma de arrays y matrices.

Arrays
Un array de NumPy es una estructura de datos que permite almacenar una colección de elementos, generalmente números, en una o más dimensiones.

Array unidimensional
Un array unidimensional (1D) de NumPy es una estructura de datos que contiene una secuencia de elementos en una única dimensión. Es similar a una lista en Python, pero con las ventajas de rendimiento y funcionalidad que ofrece NumPy.

Array de una dimensión

Un array 1D puede ser creado usando la función array de la librería con una lista de elementos como argumento. Por ejemplo:

import numpy as np

array = np.array([1, 2, 3, 4, 5])
array
array([1, 2, 3, 4, 5])
Esto creará un array 1D con los elementos 1, 2, 3, 4 y 5. Los elementos del array deben ser del mismo tipo de datos. Si los elementos son de diferentes tipos, NumPy intentará convertirlos al mismo tipo si es posible.

En un array 1D, podemos acceder a los elementos usando índices (indexes), modificarlos y realizar operaciones matemáticas en el array completo de forma eficiente. A continuación se muestran algunas operaciones que se pueden realizar utilizando el array anterior:

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
3
[1 7 3 4 5]
[11 17 13 14 15]
70
Array N-dimensional
Un array multidimensional o n-dimensional en NumPy es una estructura de datos que organiza elementos en múltiples dimensiones (ejes). Estos arrays permiten representar estructuras de datos más complejas, como matrices (array 2D, 2 ejes), tensores (array 3D, 3 ejes) y estructuras de mayor dimensión.

Arrays de diferentes dimensiones

Un array N-dimensional puede ser creado también usando la función array de la librería. Por ejemplo, si queremos crear un array 2D:

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_2d
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
Si ahora quisiéramos crear un array 3D, tendríamos que pensar en él como una lista de matrices:

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
array_3d
array([[[1, 2],
        [3, 4]],

       [[5, 6],
        [7, 8]]])
Al igual que sucedía con los arrays 1D, los elementos en un array multidimensional son accesibles mediante índices, se pueden realizar operaciones con ellos, etcétera.

A medida que agregamos más dimensiones, el principio básico sigue siendo el mismo: cada dimensión adicional puede considerarse como un nivel adicional de anidamiento. Sin embargo, a nivel práctico, trabajar con arrays de más de 3 o 4 dimensiones puede volverse más complejo y menos intuitivo.

Los arrays n-dimensionales en NumPy permiten una gran flexibilidad y potencia para representar y manipular datos en formas más complejas, especialmente útiles en campos como la ciencia de los datos, procesamiento de imágenes y aprendizaje profundo.

Funciones
NumPy proporciona una gran cantidad de funciones predefinidas y que se pueden aplicar directamente sobre las estructuras de datos vistas anteriormente o las propias de Python (listas, matrices, etcétera). Algunas de las más utilizadas en el análisis de datos son:

import numpy as np

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
Suma: [ 6  7  8  9 10]
Producto: [ 3  6  9 12 15]
Logaritmo natural: [0.         0.69314718 1.09861229 1.38629436 1.60943791]
Exponencial: [  2.71828183   7.3890561   20.08553692  54.59815003 148.4131591 ]
Media: 3.0
Mediana: 3.0
Desviación estándar: 1.4142135623730951
Varianza: 2.0
Máximo valor: 5
Índice del máximo valor: 4
Mínimo valor: 1
Índice del mínimo valor: 0
Suma de todos los elementos: 15
Redondeo: [1. 2. 4. 5.]
Entero menor (floor): [1. 2. 3. 4.]
Entero mayor (ceil): [2. 3. 4. 5.]