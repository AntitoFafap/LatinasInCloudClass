import random

# Generador de números aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Solicitar al usuario que adivine el número
adivina = int(input("Adivina el número (entre 1 y 10): "))

# Bucle para seguir solicitando mientras no adivine correctamente
while adivina != numero_secreto:
    if adivina < numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    else:
        print("Demasiado alto, intenta de nuevo.")
    
    adivina = int(input("Adivina el número (entre 1 y 10): "))

# Mensaje de victoria
print(f"¡Adivinaste el numero!  {numero_secreto}.")
