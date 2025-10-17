"""
Saludo escribe un programa que pida una hora (0-23) y muestre “buenos dias”, “buenas tardes” o “buenas noches”, segun la hora. Se utilizaran los tramos 6 a 12, 13 a 20 y de 21 a 5, respectivamente.
"""

hora=int(input("Inserte la hora del día del 0 al 23: "))

if hora in  range(6,13,1):
    print("Buenos días")
elif hora in range(13,21,1):
    print("Buenas tardes")
elif hora in range(21,6,-1):
    print("Buenas noches")
else:
    print("Hora no valida")

print(hora)
