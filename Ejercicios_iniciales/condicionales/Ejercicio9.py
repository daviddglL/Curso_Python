"""
Asignatura escribe un programa que pida el dia de la semana y muestre que asignatura toca a primera hora
"""

dia=input("Escriba el dia de la semana: ")
dia=dia.lower()

if dia=="lunes":
    print("Programación")
elif dia=="martes":
    print("Desarrollo")
elif dia=="miercoles":
    print("Sitemas")
elif dia=="jueves":
    print("Interfaces")
elif dia=="viernes":
    print("Tutoria")
else:
    print("Día no valido")

