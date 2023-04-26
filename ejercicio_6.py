#declarando las variables
base = 0
altura = 0
area = 0.0

#Inicio del programa
print("Calcular el área de un triángulo")

#Pidiendo los datos al usuario
print("Ingrese la base del triángulo")
base = int(input("> "))
print("Ingrese la altura del triángulo")
altura = int(input("> "))

#Calculando el área del triángulo
area = (base * altura) / 2

#imprimiendo en pantalla el resultado
print(f"El área del triángulo es de {area}")