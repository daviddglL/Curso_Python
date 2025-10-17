"""
Piedra, papel, tijera. Escribe un programa que implemente este juego para dos usuarios. Si alguien introduce una opción incorrecta se mostrará un mensaje de error.
"""

n1=input("Inserte su elección: (piedra,papel,tijera): ")
n2=input("Inserte su elección: (piedra,papel,tijera): ")

if n1=="piedra" and n2=="papel":
    print("El ganador es el jugador 2")
elif n1=="piedra" and n2=="tijera":
    print("El ganador es el jugador 1")
elif n1=="papel" and n2=="piedra":
    print("El ganador es el jugador 1")
elif n1=="tijera" and n2=="papel":
    print("El ganador es el jugador 1")
elif n1=="tijera" and n2=="piedra":
    print("El ganador es el jugador 2")
elif n1=="papel" and n2=="tijera":
    print("El ganador es el jugador 2")
else:
    print("Error")