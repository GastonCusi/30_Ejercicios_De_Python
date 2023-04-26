#Importando math para conseguir PI
import math

#Declarando variables
radio = 0.0
pi = math.pi
area = 0.0

#Iniciando el programa
print("Calcular el área de un círculo")

#Pidiendo datos al usuario
print("Ingrese radio del círculo")
radio = float(input("> "))

#Calculando el área del círculo
area = pi * (radio ** 2)

#redondeando el resultado para que muestre solo dos decimales
numero_redondeado = round(area, 2)

#Imprimiendo el resultado obtenido
print(f"El área del círculo es de {numero_redondeado}")