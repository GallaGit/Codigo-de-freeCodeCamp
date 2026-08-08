¿Cuáles son algunos métodos comunes de cadenas?
Un método es una función que pertenece a un objeto o clase específicos. Aprenderás más sobre clases, objetos, funciones y métodos más adelante. Por ahora, ten en cuenta que los métodos deben ser llamados en el objeto al que pertenecen escribiendo el objeto seguido de un punto y la llamada al método. Python ofrece varios métodos integrados que puedes usar para manipular cadenas. Incluyen, pero no se limitan a, los siguientes:

upper(): Devuelve una nueva cadena con todos los caracteres convertidos a mayúsculas.
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
lower(): Devuelve una nueva cadena con todos los caracteres convertidos a minúsculas.
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
strip(): Devuelve una nueva cadena con los caracteres especificados de inicio y final eliminados. Si no se pasa ningún argumento, elimina los espacios en blanco de inicio y final.
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"
replace(old, new): Devuelve una nueva cadena con todas las ocurrencias de old reemplazadas por new.
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
split(separator): Divide una cadena en un separador especificado en una lista de cadenas. Si no se especifica separador, divide en espacios.
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
join(iterable): Une elementos de un iterable en una cadena con un separador.
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
startswith(prefix): Devuelve un booleano que indica si una cadena comienza con el prefijo especificado.
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
endswith(suffix): Devuelve un booleano que indica si una cadena termina con el sufijo especificado.
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
find(substring): Devuelve el índice de la primera ocurrencia de substring, o -1 si no la encuentra.
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
count(substring): Devuelve el número de veces que una subcadena aparece en una cadena.
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
capitalize(): Devuelve una nueva cadena con el primer carácter en mayúscula y los demás caracteres en minúscula.
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
isupper(): Devuelve True si todas las letras en la cadena están en mayúsculas y False si no.
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
islower(): Devuelve True si todas las letras en la cadena están en minúsculas y False si no.
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
title(): Devuelve una nueva cadena con la primera letra de cada palabra en mayúscula.
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
