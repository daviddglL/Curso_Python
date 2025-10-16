"""
Volumen de un cono. Diseña un algoritmo que calcule el volumen de un cono.
"""
from math import pi

h=float(input("Introduzca la altura "))
r=float(input("Introduzca el radio del cono "))
volumen=(pi*h*r**2)/3
print("El volumen del cono de altura: ",h, " y de radio: ",r, " es: ",volumen)

