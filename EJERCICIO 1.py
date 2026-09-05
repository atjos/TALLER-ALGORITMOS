PI = 3.14159265358979323846

opcion = 0

while opcion != 4:
    print()
    print("--- Calculadora de funciones trigonométricas por series ---")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        x_grados = float(input("Ingrese el valor de x en grados: "))
        n_terminos = int(input("Ingrese el número de términos (n) a usar en la serie: "))

        x = x_grados * PI / 180

        resultado = 0
        for n in range(n_terminos):
            # Calcular (2n+1)!
            factorial = 1
            for i in range(2, 2 * n + 1 + 1):
                factorial *= i

            termino = ((-1) ** n) * (x ** (2 * n + 1)) / factorial
            resultado += termino

        print(f"sin({x_grados}°) ≈ {resultado:.6f}")

    elif opcion == 2:
        x_grados = float(input("Ingrese el valor de x en grados: "))
        n_terminos = int(input("Ingrese el número de términos (n) a usar en la serie: "))

        x = x_grados * PI / 180

        resultado = 0
        for n in range(n_terminos):
            # Calcular (2n)!
            factorial = 1
            for i in range(2, 2 * n + 1):
                factorial *= i

            termino = ((-1) ** n) * (x ** (2 * n)) / factorial
            resultado += termino

        print(f"cos({x_grados}°) ≈ {resultado:.6f}")

    elif opcion == 3:
        print("La tangente se podría hallar como sin(x)/cos(x) usando las series anteriores,")
        print("pero esta opción aún no ha sido implementada.")

    elif opcion == 4:
        print("Saliendo del programa. ¡Hasta luego!")

    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")