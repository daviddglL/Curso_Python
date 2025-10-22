"""
Caja fuerte. realiza un programa que pida un número de 4 cifras. Si no acertamos se mostrará el mensaje “Lo siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se ha abierto”. Disponemos de 4 intentos.
"""
import random

codigo=random.randint(1111,9999)
numint=0
for i in range(1,5):
        intt=int(input("Inserte su codigo de cuatro numeros: "))
        if codigo==intt :
            print("Has acertado el codigo es: ",codigo)
            break
        else:
            print("Has fallado vuelve a intentarlo")
            numint=numint+1

print("Has fallado todos los intentos, el codigo era: ",codigo)