
def convertir_horas_a_segundos(horas):
    return horas * 3600  # 1 hora = 3600 segundos

# Solicitar el número de horas al usuario
try:
    horas = float(input("Cantidad de horas que deseas convertir a segundos: "))
    segundos = convertir_horas_a_segundos(horas)
    print(f"{horas} horas son {segundos} segundos.")
except ValueError:
    print("Por favor, introduce un número válido de horas.")
