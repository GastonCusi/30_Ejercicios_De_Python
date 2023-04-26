#Declarando variables
farenheit = 0.0
celcius = 0.0

#iniciando el programa
print("Pasar grados Farenheit a grados Celcius")

#pidiendo datos al usuario
print("Ingrese los grados farenheit a calcular")
farenheit = float(input("°"))

#Pasando de grados Farenheit a Celcius
celcius = (farenheit - 32.0) * (5.0 / 9.0)

#Acortando a dos decimales
grados_redondeados = round(celcius, 2)

#Imprimiendo los datos obtenidos
print(f"La conversión es de {grados_redondeados}°C")