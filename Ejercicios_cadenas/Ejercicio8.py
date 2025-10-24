"""
 Escribe un programa que pinte por pantalla una pirámide rellena a base de asteriscos. La base de la pirámide debe estar formada por 9 asteriscos
 """

def imprimir_estre_centrado(n):
    ancho_total = n 
    
    for num_estrellas in range(1, n + 1, 2):
        espacios = (ancho_total - num_estrellas) // 2
        
        print(" " * espacios, end="")
        
        print("*" * num_estrellas) 

imprimir_estre_centrado(11)