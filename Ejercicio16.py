"""
Ordenar 3. Escribe un programa que ordene 3 números enteros introducidos por teclado
"""

num1=int(input("Introduce un número entero: "))
num2=int(input("introduce un número entero: "))
num3=int(input("Introduce un número entero: "))

if num1>num2 and num1>num3 and num2>num3:
    print(num1,num2,num3)
elif num1>num2 and num1>num3 and num3>num2:
    print(num1,num3,num2)
elif num2>num1 and num2>num3 and num1>num3:
    print(num2,num1,num3)
elif num2>num1 and num2>num3 and num3>num1:
    print(num2,num3,num1)
elif num3>num1 and num3>num2 and num1>num2:
    print(num3,num1,num2)
elif num3>num1 and num3>num2 and num2>num1:
    print(num3,num2,num1)