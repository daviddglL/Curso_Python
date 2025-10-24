"""
Igual que el programa anterior, pero esta vez la pirámide debe aparecer invertida, con el vértice 
hacia abajo.
"""

def imprimir_estre_hueco_invertido(n):

    if n % 2 == 0:
        n += 1
    
    ancho_total = n 
    

    for num_actual in range(n, 0, -2):
        
        espacios_izq = (ancho_total - num_actual) // 2
        
        print(" " * espacios_izq, end="")
        
        if num_actual == n:
            print("*" * ancho_total)
        elif num_actual > 1:
            espacios_internos = num_actual - 2 

            print("*", end="")
            print(" " * espacios_internos, end="")
            print("*")
        else:
            
            print("*")

# Llamada a la función
imprimir_estre_hueco_invertido(9)