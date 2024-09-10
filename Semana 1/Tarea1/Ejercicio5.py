# Ingrese dos valores
a = input("Introduce el valor de la variable a: ")
b = input("Introduce el valor de la variable b: ")

# Valores antes del intercambio
print(f"Antes del intercambio: a = {a}, b = {b}")

# Intercambia los valores de las variables
a, b = b, a

#Valores después del intercambio
print(f"Después del intercambio: a = {a}, b = {b}")
