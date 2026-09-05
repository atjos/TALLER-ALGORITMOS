import math

epsilon = float(input("Ingrese la tolerancia (épsilon), por ejemplo 0.0001: "))

n = 0
signo = 1
suma = 0
termino = 1  # valor inicial cualquiera > epsilon, para entrar al bucle

while True:
    termino = signo / (2 * n + 1)
    suma += termino

    if abs(termino) < epsilon:
        break

    signo = -signo
    n += 1

num_terminos = n + 1
pi_aproximado = suma * 4
error = abs(pi_aproximado - math.pi)

print(f"Aproximación de π obtenida: {pi_aproximado}")
print(f"Número de términos utilizados: {num_terminos}")
print(f"Valor real de math.pi: {math.pi}")
print(f"Error absoluto: {error}")