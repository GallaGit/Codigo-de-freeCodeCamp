email = 'alice.johnson@company.com'
print(f'Email: {email}')
# Llama al método .find() en email con '@' para encontrar la posición del arroba, guárdala en at_position e imprímela como 'Position of @: 13'
at_position = email.find('@')
print(f'Position of @: {at_position}')
# Usa slicing en email para extraer todo lo anterior a at_position, guárdalo en username e imprímelo como 'Username: alice.johnson'
username = email[:at_position]
print(f'Username: {username}')
# Crea has_at para comprobar si el carácter '@' está en email e imprímelo como 'Has @ symbol: True'
has_at = '@' in email
print(f'Has @ symbol: {has_at}')
# Crea has_com para comprobar si '.com' está en email e imprímelo como 'Has .com: True'
has_com = '.com' in email
print(f'Has .com: {has_com}')
# Crea messy_name con 'sARaH dAVis' con dos espacios delante y dos detrás e imprímelo como Original name
messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")
# Crea clean_name con el resultado de llamar a .title() en messy_name
# Actualiza clean_name llamando a .strip() en messy_name antes de .title() e imprímelo como 'Cleaned name: Sarah Davis'
clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")
# Crea messy_email con 'SARAH.DAVIS@COMPANY.COM' con dos espacios delante y dos detrás y crea clean_email con .strip().lower() sobre messy_email
messy_email = '  SARAH.DAVIS@COMPANY.COM  '
# Imprime messy_email como "Original email: '  SARAH.DAVIS@COMPANY.COM  '"
print(f"Original email: '{messy_email}'")
clean_email = messy_email.strip().lower()
# Imprime clean_email como "Cleaned email: 'sarah.davis@company.com'"
print(f"Cleaned email: '{clean_email}'")
# Crea name_badge con .upper() sobre clean_name e imprímelo como 'Name badge: SARAH DAVIS'
name_badge = clean_name.upper()
print(f'Name badge: {name_badge}')
# Encuentra la posición de '@' en clean_email en at_pos, extrae con slicing lo anterior en email_user e imprime Email y Username de sarah.davis
at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]
print(f'Email: {clean_email}')
print(f'Username: {email_user}')
# Reemplaza '.' por un espacio en email_user y aplica .title(), guárdalo en display_name e imprímelo como 'Display name: Sarah Davis'
display_name = email_user.replace('.', ' ').title()
print(f'Display name: {display_name}')
# Crea phone con '123-456-7890' y crea phone_clean reemplazando '-' por cadena vacía
phone = '123-456-7890'
# Imprime phone como 'Phone with dashes: 123-456-7890'
print(f'Phone with dashes: {phone}')
phone_clean = phone.replace('-', '')
# Imprime phone_clean como 'Phone without dashes: 1234567890'
print(f'Phone without dashes: {phone_clean}')
# Crea full_address con '123 Main Street, Springfield, IL' y crea address_parts separando por coma + espacio e imprímelo como lista
full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f'Address parts: {address_parts}')
# Une address_parts con ' | ' en rejoined e imprímelo como 'Rejoined: 123 Main Street | Springfield | IL'
rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')
# Crea employee_code con 'EMP-2024-SD' y crea starts_with_emp comprobando si empieza con EMP
employee_code = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')
# Crea ends_with_com comprobando si clean_email termina con .com
ends_with_com = clean_email.endswith('.com')
# Imprime employee_code, starts_with_emp, clean_email y ends_with_com como Code / Starts with EMP / Clean email / Ends with .com
print(f'Code: {employee_code}')
print(f'Starts with EMP: {starts_with_emp}')
print(f'Clean email: {clean_email}')
print(f'Ends with .com: {ends_with_com}')
# Crea dot_count contando '.' en clean_email y dash_count contando '-' en employee_code
dot_count = clean_email.count('.')
dash_count = employee_code.count('-')
# Imprime dot_count y dash_count como 'Dots in email: 2' y 'Dashes in code: 2'
print(f'Dots in email: {dot_count}')
print(f'Dashes in code: {dash_count}')
