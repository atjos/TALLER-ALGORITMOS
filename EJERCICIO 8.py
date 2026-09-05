# Criterio de fin de lectura: se usa como valor centinela un 0 en la
# primera longitud (lado a). Como una longitud de lado igual a 0 nunca
# sería válida para un triángulo real, sirve perfectamente para
# indicar "el usuario terminó" sin ambigüedad con un dato real.

while True:
    a = float(input("Ingrese la longitud del lado a (0 para salir): "))
    if a == 0:
        print("Fin del programa.")
        break

    # Validar que a sea positivo
    while a < 0:
        print("La longitud debe ser un número positivo.")
        a = float(input("Ingrese la longitud del lado a (0 para salir): "))
        if a == 0:
            break
    if a == 0:
        print("Fin del programa.")
        break

    b = float(input("Ingrese la longitud del lado b: "))
    while b <= 0:
        print("La longitud debe ser un número positivo.")
        b = float(input("Ingrese la longitud del lado b: "))

    c = float(input("Ingrese la longitud del lado c: "))
    while c <= 0:
        print("La longitud debe ser un número positivo.")
        c = float(input("Ingrese la longitud del lado c: "))

    # Desigualdad triangular: la suma de dos lados cualesquiera debe
    # ser mayor que el tercero
    if a + b > c and a + c > b and b + c > a:
        print(f"Los lados {a}, {b}, {c} SÍ forman un triángulo.")

        # a) Clasificación por lados
        if a == b and b == c:
            print("Clasificación por lados: equilátero")
        elif a == b or b == c or a == c:
            print("Clasificación por lados: isósceles")
        else:
            print("Clasificación por lados: escaleno")

        # b) Clasificación por ángulos: se compara el cuadrado del
        # lado mayor con la suma de los cuadrados de los otros dos
        # (Teorema de Pitágoras generalizado)
        mayor = a
        if b > mayor:
            mayor = b
        if c > mayor:
            mayor = c

        suma_cuadrados_otros = a ** 2 + b ** 2 + c ** 2 - mayor ** 2

        if mayor ** 2 == suma_cuadrados_otros:
            print("Clasificación por ángulos: rectángulo")
        elif mayor ** 2 > suma_cuadrados_otros:
            print("Clasificación por ángulos: obtusángulo")
        else:
            print("Clasificación por ángulos: acutángulo")

    else:
        print(f"Los lados {a}, {b}, {c} NO forman un triángulo (no cumplen la desigualdad triangular).")

    print()  # línea en blanco para separar cada iteración