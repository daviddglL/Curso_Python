"""
Media numeros. Escribe un programa que calcule la media de una serie de números positivos. El usuario indicará que ha terminado de introducir datos cuando introduzca un número negativo.
"""

num=0
suma=0
contador=0
while num>=0:
    num=float(input("Introduzca el valor de la nota: "))
    if num>=0:
        suma=suma+num
        contador=contador+1
    media=suma/contador
print(media)