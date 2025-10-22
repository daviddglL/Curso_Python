"""
Fibonacci. Escribe un programa que muestre los n primeros términos de la serie de Fibonacci. El valor de n será introducido por teclado.
"""

n=0
iteraciones=0
max=int(input("inserte el numero maximo de la secuencia de Fibonacci: "))
suma=0
ant=0

while iteraciones<max:
    if n<0:
        print("numero invalido")
    elif n==0:
        print(n)
        ant=n
        n=n+1
    elif n==1:
        print(n)
        ant=n
        n=n+1
    else :
        suma=ant+n 
        print(ant)
        ant=n
        n=suma
    iteraciones=iteraciones+1