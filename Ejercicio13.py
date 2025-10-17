"""
Caida Escribe un programa que calcule el tiempo que tardara en caer un objeto desde una altura h. Aplica la formula t=Raiz 2h/g siendo g = 9.81m/s*2
"""
from math import sqrt

h=float(input("Inserte la altura desde la que cae el objeto: "))
g=9.81

t=sqrt(2*h/g)

print("El tiempo que tarda un objeto en caer es: ",t,"m/s")