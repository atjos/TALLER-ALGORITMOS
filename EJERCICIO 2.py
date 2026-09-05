n = int(input("Ingrese un entero positivo n: "))

b = int(input("Ingrese la base b (2 <= b < 10): "))
while b < 2 or b >= 10:
    print("La base debe ser un entero mayor o igual a 2 y menor que 10.")
    b = int(input("Ingrese la base b (2 <= b < 10): "))

if n == 0:
    representacion = "0"
else:
    numero = n
    representacion = ""
    while numero > 0:
        digito = numero % b
        representacion = str(digito) + representacion
        numero = numero // b

print(f"El número {n} en base {b} se representa como: {representacion}")