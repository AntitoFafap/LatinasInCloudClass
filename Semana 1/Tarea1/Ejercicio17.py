def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))

# Solicitar un número entero al usuario
try:
    numero = int(input("Introduce un número entero: "))
    suma = suma_digitos(numero)
    print(f"La suma de los dígitos de {numero} es {suma}.")
except ValueError:
    print("Por favor, introduce un número entero válido.")
