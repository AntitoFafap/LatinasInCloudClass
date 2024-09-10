# Solicita al usuario que ingrese un número
numero = int(input("Introduce un número para calcular su factorial: "))

# Inicializa la variable factorial
factorial = 1

# Verifica si el número es negativo, cero o positivo
if numero < 0:
    print("El factorial no está definido para números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    # Calcula el factorial
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}.")
