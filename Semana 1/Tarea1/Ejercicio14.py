# Solicita al usuario que ingrese una lista de números separados por espacios
numeros = list(map(int, input("Introduce los números separados por espacios: ").split()))

# Recorre la lista e imprime los números pares
print("Los números pares en la lista son:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
