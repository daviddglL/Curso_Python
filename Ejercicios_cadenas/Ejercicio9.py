"""
 Igual que el programa anterior, pero esta vez la pirámide estará hueca (se debe ver únicamente el 
contorno hecho con asteriscos).
"""

def imprimir_estre_centrado(n):
    ancho_total = n 
    
    for num_actual in range(1, n, 2):
            
            espacios_izq = (ancho_total - num_actual) // 2
            
            print(" " * espacios_izq, end="")
            
            if num_actual == 1:
                print("*")
            else:
                espacios_internos = num_actual - 2 
                
                print("*", end="")
                print(" " * espacios_internos, end="")
                print("*")

    print("*" * ancho_total)

    
imprimir_estre_centrado(9)

