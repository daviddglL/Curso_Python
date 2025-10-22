"""
 Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena resultado 
de invertir la primera.
"""
cad=""
while True:

    car=input("Introduzca el caracter de la cadena: ")
    if car=="*":
        break
    else:
        cad=cad+car
        inv=cad[-1::-1]

print(inv," , ",cad)