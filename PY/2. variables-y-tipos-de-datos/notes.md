## ¿Cómo declaras variables y cuáles son las convenciones de nomenclatura para nombrar variables?

En Python, las variables son como una caja etiquetada para almacenar y referenciar datos de diferentes tipos. Para declarar variables en Python, asignas un valor a un identificador con el operador de asignación (=). No necesitas usar palabras clave especiales como let o const en JavaScript, o char en C#.

En Python, simplemente escribes el nombre de la variable a la izquierda, seguido del operador de asignación, y el valor que deseas asignar a la variable a la derecha. Aquí hay un ejemplo de cómo declarar las variables name y age:

name = 'John Doe'
age = 25
En el ejemplo anterior, la variable name contiene el valor 'John Doe'. Este valor es una cadena, que es una serie de caracteres usados para representar texto. Las cadenas se escriben con comillas simples o dobles, por ejemplo 'Hello' o "Hello". En lecciones futuras, aprenderás más sobre cómo trabajar con cadenas en Python.

Al nombrar variables en Python, hay algunas reglas importantes que debes tener en cuenta:

Los nombres de las variables sólo pueden comenzar con una letra o un guión bajo (_), no un número.
Los nombres de las variables sólo pueden contener caracteres alfanuméricos (a-z, A-Z, 0-9) y guiones bajos (_).
Los nombres de las variables son sensibles a mayúsculas — age, Age, y AGE se consideran únicos.
Los nombres de las variables no pueden ser una de las palabras reservadas de Python como if, class, o def.
Si rompes alguna de esas reglas, tu programa de Python lanzará un SyntaxError:

    5variable_name = 5
     ^
SyntaxError: invalid syntax
Ahora repasemos algunas convenciones comunes de nomenclatura para variables en Python.

Primero, los nombres de las variables deben estar en minúsculas, con palabras separadas por un guión bajo. Esto se llama snake case:

my_variable_name = 'freeCodeCamp'
A continuación, debes usar nombres descriptivos para las variables. Por ejemplo, si deseas guardar la edad de un usuario como variable, user_age es mejor que age o una abreviatura como ua:

user_age = 30
De esta manera, puedes comunicar fácilmente el propósito de una variable a otros miembros del equipo (o a tu futuro yo) en una gran base de código.

Otra convención es evitar usar nombres de variables de una sola letra. Esto es muy común en Python, pero se debe evitar porque los nombres de variables de una sola letra no comunican propósito o significado:

x = 56 # What do you mean by x?
El símbolo de libra (#) y el texto que sigue en el ejemplo anterior se llama comentario. Ya podrías estar familiarizado con los comentarios, así que revisémoslos rápidamente y expliquemos cómo funcionan.

En Python, los comentarios empiezan con un símbolo de libra (#), y el lenguaje ignora todo lo que siga después del símbolo # en esa línea:

(#) This is a single-line comment
Los comentarios de varias líneas se pueden crear usando comentarios de una sola línea consecutivos:

- (#) This is a
- (#) multi-line
- (#) comment

Puedes usar comentarios para explicar tu código, dejar recordatorios para ti mismo, o aclarar por qué existe una línea. Los comentarios son especialmente útiles cuando estás aprendiendo o trabajando en equipos.

Sin embargo, no debes usar comentarios para explicar lo que significan tus nombres de variables. En su lugar, los nombres que elijas para tus variables deben ser descriptivos y comunicar para qué son, y seguir las otras reglas de nomenclatura mencionadas anteriormente para evitar errores de sintaxis.

---

## ¿Cómo funciona la función de impresión?

Cada lenguaje de programación tiene alguna forma de mostrar datos en el terminal con un método incorporado, función, propiedad o palabra clave. En Python, puedes usar la función print para imprimir datos en el terminal. Echemos un vistazo más de cerca a la función print para que puedas comenzar a usarla con confianza.

Una de las primeras cosas que haces cuando estás aprendiendo cualquier lenguaje de programación es escribir un programa simple de Hello world!. Puedes hacer eso muy fácilmente en Python con solo la función print.

Para hacer eso, solo necesitas poner el string Hello world! entre los paréntesis de apertura y cierre que usas para llamar a la función print:

print('Hello world!') # Hello world!
Aprenderás más sobre cadenas y funciones en Python en lecciones futuras. Por ahora, solo considera las cadenas como una secuencia de caracteres rodeada por comillas simples (') o dobles (").

En el ejemplo print('Hello world!'), la cadena 'Hello world!' es un argumento pasado a la función print. También puedes usar la función print para mostrar múltiples valores, o argumentos, a la vez separándolos con comas. Por ejemplo:

print('My favorite colors are', 'blue', 'green', 'red')

 Output: My favorite colors are blue green red

Python agrega automáticamente un espacio entre cada elemento cuando los separas con comas. Esto es útil cuando quieres imprimir varias piezas de información juntas.

---

# Cuáles son los tipos de datos comunes en Python

Antes de trabajar con variables de Python, es importante entender los tipos de datos. Un tipo de dato describe el tipo de valor que una variable contiene. Por ejemplo, un número, un texto o una lista de elementos. Los lenguajes de programación usan tipos de datos para saber cómo almacenar y trabajar con diferentes tipos de información.

Python es un lenguaje de tipado dinámico como JavaScript, lo que significa que no es necesario declarar explícitamente tipos para las variables. El lenguaje sabe qué tipo de dato es una variable basado en lo que le asignes.

Aquí hay algunos ejemplos:

name = 'John Doe' # Python knows this is a string
age = 25 # Python knows this is an integer
Esto contrasta con algunos lenguajes de tipado estático como C#, Java y C++, donde tienes que declarar tipos con variables, como esto:

string name = 'John Doe'
int age = 25
La naturaleza de tipado dinámico de Python hace que la codificación sea realmente rápida y más flexible, pero puede llevar a errores inesperados porque los errores de tipo solo se detectan cuando se ejecuta un programa, no cuando se compila.

Como Python determina los tipos de datos mientras tu programa está ejecutándose, los errores relacionados con tipos solo se descubren en ese momento. Cuando un programa se ejecuta, Python procesa tu código línea por línea. Si llega a una línea donde se espera que un cierto objeto se comporte de una manera que no puede, Python se detendrá y mostrará un error.

En contraste, algunos lenguajes compilan tu programa antes de que se ejecute. Compilar significa que la computadora verifica tu código con anticipación y lo prepara para ejecutarse. Durante este paso, esos lenguajes pueden detectar errores de tipo antes de que el programa siquiera comience.

No necesitas conocer esos lenguajes todavía. La idea importante es simplemente:

En Python, los errores de tipo pueden revelarse durante la ejecución, cuando el programa está realmente corriendo y usando tu código.

Los lenguajes compilados detectan errores de tipo durante el paso de compilación, antes de que se permita ejecutar el programa.

Debido a esto, puede que no te des cuenta de un error de tipo en Python hasta que el programa llegue a esa línea específica de código mientras se ejecuta.

Estos son los tipos de datos más comunes que usarás en Python:

Entero: Un número entero sin decimales, por ejemplo, 10 o -5.
my_integer_var = 10
print('Integer:', my_integer_var) # Integer: 10
Flotante: Un número con un punto decimal, como 4.41 o -0.4.
my_float_var = 4.50
print('Float:', my_float_var) # Float: 4.5
Cadena: Una secuencia de caracteres encerrados en comillas simples o dobles como 'Hello world!'.
my_string_var = 'hello'
print('String:', my_string_var) # String: hello
Booleano: Un tipo verdadero o falso, escrito como True o False.
my_boolean_var = True
print('Boolean:', my_boolean_var) # Boolean: True
Conjunto: Una colección no ordenada de elementos únicos, como {0.5, 4, 'apple'}.
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5}
Diccionario: Una colección de pares clave-valor encerrados en llaves, como {'name': 'John Doe', 'age': 28}.
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
Tupla: Una colección ordenada e inmutable, encerrada entre paréntesis, como ('apple', 4.5, 7).
my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var) # Tuple: (7, 'hello', 8.5)
Rango: Una secuencia de números, a menudo usada en bucles, por ejemplo, range(5).
my_range_var = range(5)
print('Range:', my_range_var) # Range: range(0, 5)
Lista: Una colección ordenada de elementos que admite diferentes tipos de datos.
my_list = [22, 'Hello world', 3.14, True]
print(my_list) # [22, 'Hello world', 3.14, True]
Ninguno: Un valor especial que representa la ausencia de un valor.
my_none_var = None
print('None:', my_none_var) # None: None
En lecciones futuras, aprenderás más sobre cómo trabajar con todos estos tipos de datos.

---

# Cómo funcionan las funciones type() y isinstance()

En la lección anterior, aprendiste sobre los tipos de datos comunes en Python, incluyendo los tipos cadena, entero y float. A medida que desarrolles tus programas, necesitarás aprender cómo ver el tipo de una variable.

Aquí tienes una variable de ejemplo:

developer = 'Devin'
Para ver qué tipo es developer, puedes usar la función type() así:

developer = 'Devin'

print(type(developer)) # <class 'str'>
La salida de <class 'str'> significa que developer es un tipo cadena.

Si no proporcionas ningún argumento a la función type(), recibirás el siguiente mensaje de error:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
Aquí están todos los tipos de datos que has aprendido hasta ahora junto con sus tipos en la terminal:

my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>
Habrá momentos en tu programa en los que necesitarás verificar que una variable en particular sea de un tipo específico antes de realizar operaciones sobre ella. Aquí es donde la función isinstance() resulta útil.

Aquí tienes una variable de ejemplo con una cadena asignada:

account_balance = '12'
Si intentas hacer expresiones matemáticas como división usando la variable account_balance, recibirás un mensaje de error.

account_balance = '12'

account_balance / 2

(#) Traceback (most recent call last):
(#)   File "<stdin>", line 1, in <module>
(#) TypeError: unsupported operand type(s) for /: 'str' and 'int'
Para ver si account_balance es un entero, puedes verificarlo usando la función isinstance() así:

account_balance = '12'

isinstance(account_balance, int) # False
La función integrada isinstance() te permite comprobar si una variable coincide con un tipo de dato específico. Recibe un objeto y el tipo contra el que quieres verificarlo, y devuelve un booleano. En este caso, como account_balance es una cadena, devolverá False.

La función isinstance() también te permite verificar múltiples tipos a la vez.

Aquí tienes un ejemplo verificando si account_balance es un int o float:

account_balance = 12
isinstance(account_balance, (int, float)) # True
En este ejemplo, account_balance es un entero, por lo que isinstance() devuelve True. Si account_balance fuera 12.0, isinstance() aún devolvería True porque estás verificando enteros o floats.

En futuros talleres y laboratorios, usarás las funciones type() y isinstance() para asegurarte de que tus variables contienen los tipos de datos correctos antes de realizar operaciones sobre ellas.

# Cómo funcionan las funciones type() y isinstance()

En la lección anterior, aprendiste sobre los tipos de datos comunes en Python, incluyendo los tipos cadena, entero y float. A medida que desarrolles tus programas, necesitarás aprender cómo ver el tipo de una variable.

Aquí tienes una variable de ejemplo:

developer = 'Devin'
Para ver qué tipo es developer, puedes usar la función type() así:

developer = 'Devin'

print(type(developer)) # <class 'str'>
La salida de <class 'str'> significa que developer es un tipo cadena.

Si no proporcionas ningún argumento a la función type(), recibirás el siguiente mensaje de error:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: type() takes 1 or 3 arguments
Aquí están todos los tipos de datos que has aprendido hasta ahora junto con sus tipos en la terminal:

---
⚠️

my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>

⚠️
---

Habrá momentos en tu programa en los que necesitarás verificar que una variable en particular sea de un tipo específico antes de realizar operaciones sobre ella. Aquí es donde la función isinstance() resulta útil.

Aquí tienes una variable de ejemplo con una cadena asignada:

account_balance = '12'
Si intentas hacer expresiones matemáticas como división usando la variable account_balance, recibirás un mensaje de error.

account_balance = '12'

account_balance / 2

"""text
 Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
 TypeError: unsupported operand type(s) for /: 'str' and 'int'
"""
Para ver si account_balance es un entero, puedes verificarlo usando la función isinstance() así:

account_balance = '12'

isinstance(account_balance, int) # False
La función integrada isinstance() te permite comprobar si una variable coincide con un tipo de dato específico. Recibe un objeto y el tipo contra el que quieres verificarlo, y devuelve un booleano. En este caso, como account_balance es una cadena, devolverá False.

La función isinstance() también te permite verificar múltiples tipos a la vez.

Aquí tienes un ejemplo verificando si account_balance es un int o float:

account_balance = 12
isinstance(account_balance, (int, float)) # True
En este ejemplo, account_balance es un entero, por lo que isinstance() devuelve True. Si account_balance fuera 12.0, isinstance() aún devolvería True porque estás verificando enteros o floats.

En futuros talleres y laboratorios, usarás las funciones type() y isinstance() para asegurarte de que tus variables contienen los tipos de datos correctos antes de realizar operaciones sobre ellas.
