"""
 Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en 
mayúsculas.
"""
 
nombre=input("Introduzca su nombre: ")
apellido=input("Introduzca su apellido: ")
nombre=nombre[0].upper()+nombre[1:]
apellido=apellido[0].upper()+apellido[1:]
print(nombre,"",apellido)
# End-of-file (EOF)