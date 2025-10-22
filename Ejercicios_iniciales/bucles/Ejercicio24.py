"""
Positivos-negativos. Escribe un programa que pida al usuario 10 números y muestre por pantalla cuantos son positivos y cuántos negativos.
"""

positivos=0
negativos=0

for i in range(10):
    n=int(input("introduca un numero: "))
    if n==0:
        print("inserte un numero diferente de cero")
    elif n>0:
        positivos=positivos+1
    else:
        negativos=negativos+1

print("El total de números positivos es de: ",positivos," y el de negativos es de: ",negativos)