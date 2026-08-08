# upper() — convierte a mayúsculas
my_str = 'hello world'
uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

# lower() — convierte a minúsculas
my_str = 'Hello World'
lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

# strip() — elimina espacios (u otros chars) al inicio y final
my_str = '  hello world  '
trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

# replace(old, new) — reemplaza todas las ocurrencias
my_str = 'hello world'
replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

# split(separator) — divide en lista (por defecto, espacios)
my_str = 'hello world'
split_words = my_str.split()
print(split_words)  # ['hello', 'world']

# join(iterable) — une elementos con un separador
my_list = ['hello', 'world']
joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

# startswith(prefix) — ¿empieza con...?
my_str = 'hello world'
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

# endswith(suffix) — ¿termina con...?
my_str = 'hello world'
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

# find(substring) — índice de la primera ocurrencia (-1 si no hay)
my_str = 'hello world'
world_index = my_str.find('world')
print(world_index)  # 6

# count(substring) — cuántas veces aparece
my_str = 'hello world'
o_count = my_str.count('o')
print(o_count)  # 2

# capitalize() — primera letra mayúscula, resto minúsculas
my_str = 'hello world'
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

# isupper() — ¿todas mayúsculas?
my_str = 'hello world'
is_all_upper = my_str.isupper()
print(is_all_upper)  # False

# islower() — ¿todas minúsculas?
my_str = 'hello world'
is_all_lower = my_str.islower()
print(is_all_lower)  # True

# title() — primera letra de cada palabra en mayúscula
my_str = 'hello world'
title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
