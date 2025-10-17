"""
Desayuno. Escribe un programa que calcule el precio de un desayuno. Primero pregunta al usuario que ha tomado para comer: tostada, churros o donuts. Los churros valen 1,5€ y el donut 1€. En caso de tomar tostada, debe preguntar si es básica (1,2€) o especial (1,6€). Por último preguntara la bebida zumo o cafe a 1,8 y 1,2 respectivamente.
"""

desayuno=input("Que ha tomado para comer: (tostada/donuts/churros) ")

precio=0

if desayuno=="donuts":
    precio=precio+1
elif desayuno=="churros":
    precio=precio+1.5
elif desayuno=="tostada":
    tos=input("basica o especial: ")
    if tos=="basica":
        precio=precio+1.2
    elif tos=="especial":
        precio=precio+1.6

bebido=input("Que ha tomado para beber: (zumo/cafe)")

if bebido=="zumo":
    precio=precio+1.8
elif bebido=="cafe":
    precio=precio+1.2