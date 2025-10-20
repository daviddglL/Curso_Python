"""
Suma dos numeros Escribe un programa que pida dos numeros y calcule la suma de ellos. Mostrara en pantalla “La suma es mayor que cero” o “la suma no es mayor que cero” en funcion del resultado
"""
num1=int(input("Introduzca el primer número: "))
num2=int(input("Introduzca el segundo número: "))

sum=num1+num2

if sum >0 :
    print("La suma es mayor que cero")
else :
    print("La suma no es mayor que cero")