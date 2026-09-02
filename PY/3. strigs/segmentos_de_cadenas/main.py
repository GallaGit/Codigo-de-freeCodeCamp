# Acceso por índice
my_str = "Hello world"
print(my_str[0])   # H
print(my_str[6])   # w
print(my_str[-1])  # d

# Slicing básico: string[start:stop] (stop no incluido)
my_str = 'Hello world'
print(my_str[1:4])  # ell

# Omitir start → desde el inicio
my_str = 'Hello world'
print(my_str[:7])   # Hello w

# Omitir stop → hasta el final
my_str = 'Hello world'
print(my_str[8:])   # rld

# El slicing no modifica la cadena original
my_str = 'Hello world'
print(my_str[8:])   # rld
print(my_str)       # Hello world

# Omitir start y stop → toda la cadena
my_str = 'Hello world'
print(my_str[:])    # Hello world

# Con step: string[start:stop:step]
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

# Invertir cadena con step = -1
my_str = 'Hello world'
print(my_str[::-1])    # dlrow olleH
