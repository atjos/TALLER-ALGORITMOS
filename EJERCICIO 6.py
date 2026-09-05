
cantidad_valores = int(input("¿Cuántos valores va a ingresar?: "))

valores = []
for i in range(cantidad_valores):
    valor = int(input(f"Ingrese el valor {i + 1}: "))
    valores.append(valor)

pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

if len(pares) == 0:
    print("No se ingresó ningún valor par, no se puede calcular la desviación estándar.")
else:
    n = len(pares)

    suma = 0
    for p in pares:
        suma += p
    media = suma / n

    suma_diferencias_cuadrado = 0
    for p in pares:
        suma_diferencias_cuadrado += (p - media) ** 2

    varianza_poblacional = suma_diferencias_cuadrado / n
    desviacion_poblacional = varianza_poblacional ** 0.5
    print(f"Valores pares: {pares}")
    print(f"Media: {media}")
    print(f"Desviación estándar poblacional: {desviacion_poblacional:.6f}")

    if n >= 2:
        varianza_muestral = suma_diferencias_cuadrado / (n - 1)
        desviacion_muestral = varianza_muestral ** 0.5
        print(f"Desviación estándar muestral: {desviacion_muestral:.6f}")
    else:
        print("La desviación estándar muestral no está definida con un solo valor (división entre n-1 = 0).")
