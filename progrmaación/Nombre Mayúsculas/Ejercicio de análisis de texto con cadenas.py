# Solicita al usuario un texto
texto = input("Ingresa un texto: ")

# 1. Contar la cantidad de oraciones en el texto
oraciones = texto.split('.')
# Removemos oraciones vacías causadas por puntos finales
oraciones = [oracion.strip() for oracion in oraciones if oracion.strip()]
cantidad_oraciones = len(oraciones)
print(f"Cantidad de oraciones: {cantidad_oraciones}")

# 2. Contar la cantidad de palabras en cada oración
print("\nCantidad de palabras en cada oración:")
for i, oracion in enumerate(oraciones):
    palabras = oracion.split()
    cantidad_palabras = len(palabras)
    print(f"Oración {i+1}: {cantidad_palabras} palabras")

# 3. Identificar la oración más larga y la más corta
oracion_mas_larga = ""
oracion_mas_corta = oraciones[0] if oraciones else ""
longitud_mas_larga = 0
longitud_mas_corta = len(oracion_mas_corta)

for oracion in oraciones:
    longitud_actual = len(oracion)
    # Actualizar oración más larga
    if longitud_actual > longitud_mas_larga:
        oracion_mas_larga = oracion
        longitud_mas_larga = longitud_actual
    # Actualizar oración más corta
    if longitud_actual < longitud_mas_corta:
        oracion_mas_corta = oracion
        longitud_mas_corta = longitud_actual

print("\nOración más larga:")
print(oracion_mas_larga)
print("\nOración más corta:")
print(oracion_mas_corta)

# 4. Calcular la longitud promedio de las oraciones
longitud_total = sum(len(oracion) for oracion in oraciones)
longitud_promedio = longitud_total / cantidad_oraciones if cantidad_oraciones else 0

print(f"\nLongitud promedio de las oraciones: {longitud_promedio:.2f} caracteres")
