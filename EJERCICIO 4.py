n = input("Ingrese un entero positivo: ")

resultado = ""
for i in range(len(n)):
    resultado += n[i]
    if i < len(n) - 1:
        resultado += "0"

print(f"El número con ceros intercalados es: {resultado}")