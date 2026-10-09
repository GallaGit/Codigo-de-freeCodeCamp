# Soluciones — Intro a NumPy (4GeeksAcademy)

Fuente: [02.1-Intro-to-Numpy_solutions.ipynb](https://github.com/4GeeksAcademy/machine-learning-prework/blob/main/02-numpy/02.1-Intro-to-Numpy_solutions.ipynb)

```python
import numpy as np

np.random.seed(42)
```

---

## Creación de arrays

### Exercise 01

```python
np.zeros(10)
```

Resultado: `array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])`

---

### Exercise 02

```python
np.ones(10)
```

Resultado: `array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])`

---

### Exercise 03

```python
# Create an array of 10 elements with numbers from 1 to 10

np.linspace(1, 10, 10)
```

Resultado: `array([ 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])`

---

### Exercise 04

```python
# np.random.rand: Random numbers from 0 to 1

np.random.rand(10)
```

```python
# np.random.randn: Random numbers from a Normal distribution which have mean = 0 and std = 1

np.random.randn(5, 5)
```

```python
# np.random.randint: Random numbers from given numbers (from included and to not included)

np.random.randint(1, 10, size = (2, 5))
```

---

### Exercise 05

```python
np.eye(5)
```

Resultado:

```text
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
```

---

### Exercise 06

```python
matrix = np.random.rand(3, 2)
print(matrix)

min_value = np.min(matrix)
max_value = np.max(matrix)
print(f"Min value: {min_value} \nMax value: {max_value}")

# Another way: matrix.min(), matrix.max()
```

---

### Exercise 07

```python
array = np.random.randint(5, 13, size = 30)
print(array)

mean_value = np.mean(array)
print(f"Mean value: {mean_value}")

# Another way: array.mean()
```

---

### Exercise 08

```python
l = [1, 2, 3]
array = np.asarray(l)
array

# Another way: np.array(l)
```

```python
t = (1, 2, 3)
array = np.asarray(t)
array

# Another way: np.array(t)
```

---

## Operaciones entre arrays

### Exercise 09

```python
np.flip(array)

# Another way: array[::-1]
```

Resultado: `array([3, 2, 1])`

---

### Exercise 10

```python
matrix = np.random.randn(5, 12)
matrix
```

```python
np.reshape(matrix, (12, 5))
```

---

### Exercise 11

```python
l = [1, 2, 0, 0, 4, 0]
array = np.array(l)
array
```

```python
indices = np.where(array != 0)
indices

# Another way: np.nonzero(array)
```

Resultado: `(array([0, 1, 4]),)`

---

### Exercise 12

```python
l = [0, 5, -1, 3, 15]
array = np.asarray(l)
array = array * -2

even_numbers = array[array % 2 == 0]
even_numbers
```

Resultado: `array([ 0, -10, 2, -6, -30])`

---

### Exercise 13

```python
array = np.random.random_sample(10)
array = np.sort(array)
array

# Another way: array.sort()
```

---

### Exercise 14

```python
array1 = np.random.randint(0, 10, 8)
array2 = np.random.randint(0, 10, 8)
print(f"Array 1: {array1} \nArray 2: {array2}")

# Sum
arr_sum = array1 + array2

# Subtraction
arr_sub = array1 - array2

# Product
arr_prod = array1 * array2

print(f"Sum: {arr_sum} \nSubtraction: {arr_sub} \nProduct: {arr_prod}")
```

---

### Exercise 15

```python
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
array = np.array(l)
array
```

```python
np.reshape(array, (4, 3))
```

Resultado:

```text
array([[ 1, 2, 3],
       [ 4, 5, 6],
       [ 7, 8, 9],
       [10, 11, 12]])
```
