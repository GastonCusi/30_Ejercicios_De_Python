#Declaración de variables
nombre = ""
apellido = ""

#Solicitud de datos
print("Ingrese su nombre: ")
nombre = input("> ")
print("Ingrese su appelido: ")
apellido = input("> ")

#Mensaje en pantalla: Operador en formato %
print("Hola %s %s, gusto en conocerte!" % (nombre, apellido))