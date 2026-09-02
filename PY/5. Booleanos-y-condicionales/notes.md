# ¿Cómo funcionan las declaraciones condicionales y los operadores lógicos?

Las declaraciones condicionales, o condicionales, te permiten controlar el flujo de tu programa basándote en si ciertas condiciones son verdaderas o falsas.

Pero, antes de entrar en todo eso, repasemos los bloques de construcción básicos de las declaraciones condicionales, comenzando con los operadores de comparación. Los operadores de comparación son operadores que te permiten comparar dos o más valores y devolver un valor booleano.

En una lección anterior, aprendiste que los booleanos son uno de los tipos de datos en Python, y solo pueden ser `True` o `False`.

Aquí hay una tabla con los operadores de comparación en Python:

| Operador | Nombre | Descripción |
| --- | --- | --- |
| `==` | Igual | Verifica si dos valores son iguales |
| `!=` | Distinto | Verifica si dos valores no son iguales |
| `>` | Mayor que | Verifica si el valor de la izquierda es mayor que el valor de la derecha |
| `<` | Menor que | Verifica si el valor de la izquierda es menor que el valor de la derecha |
| `>=` | Mayor o igual que | Verifica si el valor de la izquierda es mayor o igual que el valor de la derecha |
| `<=` | Menor o igual que | Verifica si el valor de la izquierda es menor o igual que el valor de la derecha |

Aquí algunas de esas expresiones que evalúan a `True` o `False`:

```python
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
```

Estos operadores se pueden usar en condicionales para comparar valores y ejecutar cierto código basado en si el condicional evalúa a `True` o `False`.

En Python, el condicional más básico es la declaración `if`. Aquí está la sintaxis básica:

```python
if condition:
    pass # Code to execute if condition is True
```

Las sentencias `if` comienzan con la palabra clave `if`.

`condition` es una expresión que se evalúa como `True` o `False`, seguida de dos puntos (`:`).

El cuerpo de la sentencia `if` constituye un bloque de código, que es un grupo de sentencias que pertenecen juntas. En Python, el nivel de indentación es lo que define un bloque de código.

En el ejemplo anterior, el cuerpo de la sentencia `if` contiene una sentencia `pass`. Cuando se ejecuta una sentencia `pass`, no sucede nada. Esta es una palabra clave especial que puede usarse como marcador de posición para código futuro y es útil cuando no se permiten bloques de código vacíos.

El código dentro del cuerpo de la sentencia `if` se ejecuta solo cuando la condición evalúa a `True`. Por ejemplo:

```python
age = 18

if age >= 18:
    print('You are an adult') # You are an adult
```

Observa la indentación antes de `print('You are an adult')`. Mientras que otros lenguajes de programación usan caracteres como llaves para definir bloques de código, y solo usan la indentación para mejorar la legibilidad, en Python, los bloques de código se determinan por la indentación.

El siguiente código generaría un `IndentationError`, que es la forma en que Python indica que se requiere indentación en un punto determinado del código:

```python
age = 18

if age >= 18:
print('You are an adult') # IndentationError: expected an indented block after 'if' statement on line 3
```

Aunque puedes usar cualquier número de espacios (siempre que seas consistente) para determinar cada nivel de sangría, la guía de estilo de Python recomienda usar cuatro espacios.

Los bloques también se encuentran en bucles y funciones, que aprenderás en lecciones futuras.

Volviendo a nuestro ejemplo, si `age` es menor que 18, no se imprime nada en el terminal:

```python
age = 12

if age >= 18:
    print('You are an adult') # Nothing shows up in the terminal
```

Pero, ¿qué pasa si también quieres imprimir algo si `age` es menor que 18? Ahí es donde entra la cláusula `else`. La cláusula `else` se ejecuta cuando la condición `if` es falsa. Aquí está la sintaxis para una sentencia `if…else`:

```python
if condition:
   pass # Code to execute if condition is True
else:
   pass # Code to execute if condition is False
```

Por ejemplo:

```python
age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet') # You are not an adult yet
```

Ten en cuenta que no puedes colocar ninguna instrucción entre el bloque `if` y la cláusula `else`. El siguiente código generaría un `SyntaxError`:

```python
age = 12

if age >= 18:
    print('You are an adult')
print('Almost there!')
else: # SyntaxError: invalid syntax
    print('You are not an adult yet')
```

Puede haber situaciones en las que quieras tener en cuenta múltiples condiciones. Para hacer eso, Python te permite extender tu declaración `if` con la palabra clave `elif` (else if).

Aquí está la sintaxis:

```python
if condition1:
   pass # Code to execute if condition1 is True
elif condition2:
   pass # Code to execute if condition1 is False and condition2 is True
else:
   pass # Code to execute if all conditions are False
```

Por ejemplo:

```python
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child') # You are a child
```

Ten en cuenta que puedes usar tantas cláusulas `elif` como quieras:

```python
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant
```

Ahora que entiendes cómo funcionan los operadores de comparación y las declaraciones condicionales en Python, puedes empezar a escribir programas que tomen decisiones basadas en la lógica y la entrada. Ya sea comparando valores o bifurcándose a través de múltiples condiciones, estas herramientas son la base para escribir código flexible y sensible.

---

# ¿Qué son los valores truthy y falsy, y cómo funcionan los operadores booleanos y el cortocircuito?

En la lección anterior, aprendiste cómo usar operadores de comparación y sentencias condicionales para controlar el flujo de tus programas.

Aunque son muy poderosos, a menudo te encontrarás en situaciones en las que necesitas comparar múltiples valores a la vez. Esto puede llevar a sentencias condicionales anidadas, por ejemplo:

```python
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

El ejemplo anterior primero verificará si `is_citizen` es `True`. Si es así, pasará a la sentencia `if` anidada y verificará si `age` es mayor o igual a 18. Dado que `age` es mayor o igual a 18, el mensaje que se imprimirá en la terminal será `You are eligible to vote`. Si `is_citizen` fuera `False`, el mensaje que se imprimiría en la terminal habría sido `You are not eligible to vote`.

Si estás trabajando con sentencias condicionales más complejas, puedes usar los operadores de Python `and`, `or` y `not`.

Pero antes de profundizar en esos operadores, veamos qué son los valores truthy y falsy.

En Python, cada valor tiene un valor booleano inherente, o un sentido incorporado de si debe ser tratado como `True` o `False` en un contexto lógico. Muchos valores se consideran **truthy**, es decir, evalúan a `True` en un contexto lógico. Otros son **falsy**, lo que significa que evalúan a `False`.

Aquí hay unos pocos valores falsy:

- `None`
- `False`
- Entero `0`
- Flotante `0.0`
- Cadenas vacías `""`

Otros valores como números distintos de cero y cadenas no vacías son truthy.

Si deseas verificar si un valor es truthy o falsy, puedes usar la función incorporada `bool()`. Esta convierte explícitamente un valor a su equivalente booleano y devuelve `True` para valores truthy y `False` para valores falsy. Aquí hay algunos ejemplos:

```python
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True
```

Ahora que entiendes los valores truthy y falsy, podemos echar un vistazo a los operadores booleanos, que también se conocen como operadores lógicos. Estos son operadores especiales que te permiten combinar múltiples expresiones para crear una lógica de toma de decisiones más compleja en tu código.

Hay tres operadores booleanos en Python: `and`, `or` y `not`.

## Operador `and`

El operador `and` toma dos operandos y devuelve el primer operando si es falsy, de lo contrario, devuelve el segundo operando. Ambos operandos deben ser truthy para que una expresión resulte en un valor truthy.

Aquí hay un ejemplo:

```python
is_citizen = True
age = 25

print(is_citizen and age) # 25
```

En el ejemplo anterior, el número `25` se imprime en la terminal porque el operador `and` evaluará el segundo operando si el primer operando es `True`. El operador `and` se conoce como un operador de cortocircuito. El cortocircuito significa que Python verifica los valores de izquierda a derecha y se detiene tan pronto como determina el resultado final.

A menudo usarás `and` dentro de las sentencias `if` para verificar si se cumplen múltiples condiciones. Aquí te mostramos cómo puedes refactorizar el ejemplo anterior para usar el operador `and` en lugar de sentencias `if` anidadas:

```python
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

En el ejemplo anterior, `is_citizen` es `True`, y `age >= 18` se evalúa como `True`. Dado que ambos operandos del operador `and` son verdaderos, la condición `is_citizen and age >= 18` se evalúa como `True`, y se ejecuta la llamada a `print` dentro del bloque `if`.

## Operador `or`

Este operador devuelve el primer operando si es truthy, de lo contrario, devuelve el segundo operando. Una expresión con `or` resulta en un valor truthy si al menos un operando es truthy. El operador `or` también se conoce como un operador de cortocircuito. Aquí hay un ejemplo:

```python
age = 19
is_employed = False

print(age or is_employed) # 19
```

El siguiente código imprimirá el número `19` porque el primer operando `age` es truthy.

Si necesitas verificar si una o más expresiones son `True`, entonces puedes usar el operador `or` en una condición así:

```python
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
```

En este caso, `age < 18` es `False`, pero `is_student` es `True`. Dado que al menos una condición es verdadera, toda la expresión `or` se evalúa como `True`, y se imprime el mensaje de descuento en el bloque `if`.

## Operador `not`

El último operador que veremos es el operador `not`, que toma un solo operando e invierte su valor booleano. Convierte valores truthy en `False` y valores falsy en `True`. A diferencia de los operadores anteriores que vimos, `not` siempre devuelve `True` o `False`.

Aquí hay algunos ejemplos:

```python
print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy
```

Es común usar el operador `not` en condiciones para verificar si algo no es `True` o `False`, así:

```python
is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
```

Dado que `is_admin` es `False`, entonces `not is_admin` está diciendo no `False`, lo cual es `True`. Así que el mensaje `Access denied for non-administrators.` será impreso.

Ahora que entiendes los valores truthy y falsy, los operadores `and`, `or` y `not`, y cómo funciona el cortocircuito, puedes escribir lógica condicional más flexible y legible.
