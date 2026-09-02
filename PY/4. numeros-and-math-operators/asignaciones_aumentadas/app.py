# Augmented assignment addition (+=)
my_var = 10
my_var += 5

print(my_var) # 15

# Without augmented assignment
my_var = 10
my_var = my_var + 5

print(my_var) # 15

# Augmented assignment subtraction (-=)
count = 14
count -= 3

print(count) # 11

# Augmented assignment multiplication (*=)
product = 65
product *= 7

print(product) # 455

# Augmented assignment division (/=)
price = 100
price /= 4

print(price) # 25.0

# Floor division (//=)
total_pages = 23
total_pages //= 5

print(total_pages) # 4

# Modulo (%=)
bits = 35
bits %= 2

print(bits) # 1

# Exponentiation (**=)
power = 2
power **= 3

print(power) # 8

# String concatenation with +=
greet = 'Hello'
greet += ' World'

print(greet) # Hello World

# String repetition with *=
greet = 'Hello'
greet *= 3

print(greet) # HelloHelloHello

# TypeError with -= on strings
# greet = 'Hello'
# greet -= ' World'
# print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'

# TypeError with /= on strings
# greet = 'Hello'
# greet /= 'World'
# print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str'

# Increment operators (++ and --) do not work in Python
my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1

print(my_var) # 6
