# Solicita al usuario una frase
frase = input("Ingresa una frase: ")

# 1. Contar la cantidad de palabras en la frase
palabras = frase.split()
cantidad_palabras = len(palabras)
print(f"Cantidad de palabras: {cantidad_palabras}")

# 2. Convertir la frase a minúsculas
frase_minusculas = frase.lower()
print(f"Frase en minúsculas: {frase_minusculas}")

# 3. Reemplazar una palabra específica por otra
palabra_a_reemplazar = input("Ingresa la palabra que deseas reemplazar: ")
palabra_nueva = input("Ingresa la nueva palabra: ")
frase_modificada = frase.replace(palabra_a_reemplazar, palabra_nueva)
print(f"Frase modificada: {frase_modificada}")

# 4. Encontrar la posición de una subcadena
subcadena = input("Ingresa una subcadena para buscar su posición: ")
posicion = frase.find(subcadena)

if posicion != -1:
    print(f"La subcadena se encuentra en la posición: {posicion}")
else:
    print("La subcadena no se encuentra en la frase.")

# Imprimir la frase modificada y la cantidad de palabras
print(f"Frase final: {frase_modificada}")
print(f"Cantidad de palabras: {cantidad_palabras}")
