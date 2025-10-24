def leer_entero ( mensaje ="Introduce un numero: ", error="No se introdujo un numero"):
    
    while True:
        try:
            num=int(input(mensaje))
            print(num)
        except ValueError:
            print(error)
            
print(leer_entero())


def leer_entero_minimo(minimo=0, mensaje="Intodue un numero:",error="No se introdujo un numero"):
    while (numero:=leer_entero(mensaje,error)<minimo):
        pass 
    return numero
numero=leer_entero_minimo(0,"introduce un numero >=0: ")
