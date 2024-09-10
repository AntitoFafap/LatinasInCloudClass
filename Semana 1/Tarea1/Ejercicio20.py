

def contar_palabras(frase):
    palabras = frase.split()  # Dividir la frase en palabras
    return len(palabras)

# Solicitar una frase al usuario
frase = input("Introduce una frase para contar sus palabras: ")
cantidad_palabras = contar_palabras(frase)
print(f"La frase tiene {cantidad_palabras} palabras.")
