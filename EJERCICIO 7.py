cantidad_valores = int(input("¿Cuántos valores va a ingresar?: "))

valores = []
for i in range(cantidad_valores):
    valor = int(input(f"Ingrese el valor {i + 1}: "))
    valores.append(valor)

# Contar cuántas veces aparece cada valor distinto, usando dos listas
# paralelas: una con los valores únicos y otra con sus frecuencias.
valores_unicos = []
frecuencias = []
for v in valores:
    if v in valores_unicos:
        indice = valores_unicos.index(v)
        frecuencias[indice] += 1
    else:
        valores_unicos.append(v)
        frecuencias.append(1)

# Buscar la frecuencia máxima
frecuencia_maxima = 0
for f in frecuencias:
    if f > frecuencia_maxima:
        frecuencia_maxima = f

if frecuencia_maxima == 1:
    # Ningún valor se repite: no hay una moda propiamente dicha,
    # ya que todos los valores tienen la misma frecuencia (1).
    print("Ningún valor se repite (todas las frecuencias son 1).")
    print("Por lo tanto, no existe una moda propiamente dicha para este conjunto.")
else:
    # Buscar todos los valores que tengan la frecuencia máxima
    modas = []
    for i in range(len(valores_unicos)):
        if frecuencias[i] == frecuencia_maxima:
            modas.append(valores_unicos[i])

    if len(modas) == 1:
        print(f"La moda es: {modas[0]} (aparece {frecuencia_maxima} veces)")
    else:
        # Conjunto multimodal: varios valores comparten la frecuencia máxima
        print(
            f"El conjunto es multimodal: hay {len(modas)} valores con la frecuencia máxima ({frecuencia_maxima} veces).")
        print(f"Las modas son: {modas}")
