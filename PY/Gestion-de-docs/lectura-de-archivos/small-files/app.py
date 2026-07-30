# ============================================================
# 5 formas comunes de leer texto en Python
# Descomenta SOLO una sección a la vez y ejecuta: py app.py
# ============================================================


# --- 1) read() → todo el archivo en un solo string ---
#with open("log.txt", "r", encoding="utf-8") as f:
#    contenido = f.read()
#    print(contenido)


# --- 2) readlines() → lista con todas las líneas ---
#with open("log.txt", "r", encoding="utf-8") as f:
#    lineas = f.readlines()
#    print(lineas)          # lista con \n al final de cada línea
#    for linea in lineas:
#        print(linea.strip())


# --- 3) for línea en archivo → leer línea por línea (recomendado) ---
with open("log.txt", "r", encoding="utf-8") as f:
    for linea in f:
        if "ERROR" in linea:
            print(linea.strip())

#o si queremos buscar una palabra específica
with open("log.txt", "r", encoding="utf-8") as f:
    for linea in f:
        if "conexión" in linea:
            print(linea.strip())


# --- 4) readline() → una línea a la vez, a mano ---
# with open("log.txt", "r", encoding="utf-8") as f:
#     linea = f.readline()
#     while linea:
#         print(linea.strip())
#         linea = f.readline()


# --- 5) Path.read_text() → lectura rápida con pathlib ---
# from pathlib import Path
# contenido = Path("log.txt").read_text(encoding="utf-8")
# print(contenido)
