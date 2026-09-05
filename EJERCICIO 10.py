# PRUEBA EJERCICIO 10

n = int(input("Ingrese un entero positivo n: "))

cantidad_primos = 0
mayor_primo = None

for numero in range(2, n + 1):
    es_primo = True

    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1

    if es_primo:
        print(numero)
        cantidad_primos += 1
        mayor_primo = numero

print()
print(f"Cantidad de números primos encontrados: {cantidad_primos}")
if mayor_primo is not None:
    print(f"El mayor número primo encontrado es: {mayor_primo}")
else:
    print("No se encontró ningún número primo en ese rango.")