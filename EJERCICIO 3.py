frase = input("Ingrese una frase: ")

palabras = frase.split()

frase_palabras_invertidas = " ".join(palabras[::-1])

frase_letras_invertidas = " ".join(palabra[::-1] for palabra in palabras)

print(f"Frase original: {frase}")
print(f"Frase con las palabras invertidas: {frase_palabras_invertidas}")
print(f"Frase con las letras de cada palabra invertidas: {frase_letras_invertidas}")