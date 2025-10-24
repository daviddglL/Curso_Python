"""
Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del 
primer carácter en la cadena por el segundo carácter.
"""

cad=input("introduzca una cadena: ")

cac1=input("Introduzca un solo caracter de la cadena anterior caracter: ")
if cac1.isalpha() and len(cac1)==1:
    pass
else:
    print("ha introducido mas de un caracter")

cac2=input("Introduzca un solo caracter por el que sustituir el anterior: ")

if cac2.isalpha() and len(cac2)==1:
    pass
else:
    print("ha introducido mas de un caracter")


cad2=cad.replace(cac1,cac2)
print(cad2)