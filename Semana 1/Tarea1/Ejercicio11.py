# Solicitar una cadena de texto
cadena = input("Introduce una cadena de texto: ")

# Definicion de  vocales
vocales = "aeiouAEIOU"

# Inicializa el contador de vocales
contador_vocales = 0

# Recorre la cadena y cuenta las vocales
for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

# Print del resultado
print(f"El número de vocales en la cadena es: {contador_vocales}")
