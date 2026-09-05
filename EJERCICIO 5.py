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
    print("No se ingresó ningún valor par, por lo tanto no se puede calcular la media.")
else:
    suma = 0
    for p in pares:
        suma += p
    media = suma / len(pares)
    print(f"Los valores pares ingresados fueron: {pares}")
    print(f"La media de los valores pares es: {media}")
