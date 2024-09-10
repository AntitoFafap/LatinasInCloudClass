
def generar_tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar el número al usuario
try:
    numero = int(input("Introduce un número para la tabla de multiplicar: "))
    generar_tabla_multiplicar(numero)
except ValueError:
    print("Introduce un numero del 1 al 10.")
