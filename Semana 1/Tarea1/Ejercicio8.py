# Solicitar numeros
numeros = list(map(int, input("Introduce los números separados por espacios: ").split()))

# Sumar todos los números con sum()
suma_total = sum(numeros)

# Print del resultado2
print(f"La suma de los números de la lista es: {suma_total}")
