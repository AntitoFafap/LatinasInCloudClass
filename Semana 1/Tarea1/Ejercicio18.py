def es_palindromo(cadena):
    # Convertir a minúsculas y eliminar espacios en blanco
    cadena_limpia = cadena.replace(" ", "").lower()
    # Comparar la cadena original con su reverso
    return cadena_limpia == cadena_limpia[::-1]

# Solicitar una cadena al usuario
cadena = input("Introduce una cadena para verificar si es un palíndromo: ")
if es_palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')
