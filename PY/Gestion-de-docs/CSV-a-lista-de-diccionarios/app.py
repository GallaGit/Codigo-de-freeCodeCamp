import csv

with open("users.csv", "r", encoding="utf-8") as f:
    users = list(csv.DictReader(f))

# aquí: filtra / modifica
adults = [user for user in users if int(user['age']) > 18]

for user in users:
    user['is_adult'] = 'sí' if int(user['age']) > 18 else 'no'

# aquí: escribe users_modified.csv
fieldnames = ['name', 'age', 'email', 'is_adult']

with open('users_modified.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # Escribe la fila de encabezado
    writer.writerows(users)  # Escribe las filas de datos