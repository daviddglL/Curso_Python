"""
Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena 
introducida por teclado
"""

cad=input("Introduzca una cadena por teclado: ")

sub=input("Introduzca una subcadena por teclado: ")

if cad[0]==sub[0]:
    print("la cadena y la subcadena empiezan igual")
else:
    print("La cadena y la sumbacena no empiezan igual")