"""
Tabla de multiplicar. Escribe un programa que muestre la tabla de multiplicar de un número introducido por teclado.
"""
num=int(input("Introduzca el número del que desee ver su tabla: "))



for i in range(10):
    resultado=num*i 
    print("El resultado de ",num,"x",i," es: ",resultado)
    i=i+1