"""
Realiza un programa que pinte una X hecha de asteriscos. El programa debe pedir la altura. Se debe
comprobar que la altura sea un número impar mayor o igual a 3, en caso contrario se debe mostrar un
mensaje de error.
"""
def pintar_letra_x():
    """
    Dibuja una letra 'X' de asteriscos en la terminal.
    Requiere que la altura sea un número impar >= 3.
    """
    print("--- ✖️ DIBUJADOR DE LA LETRA 'X' ---")

    # 1. Entrada de Datos y Validación
    while True:
        try:
            altura = int(input("Introduce la altura de la 'X' (debe ser un número impar >= 3): "))
            
            # Comprobar si la altura es impar (altura % 2 != 0) y mayor o igual a 3
            if altura >= 3 and altura % 2 != 0:
                break
            else:
                print("ERROR: La altura debe ser un número IMPAR mayor o igual a 3. Inténtalo de nuevo.")
        except ValueError:
            print("ERROR: Por favor, introduce un número entero válido.")

    # 2. Construcción de la 'X'
    
    print("\n--- Resultado ---")

    # El centro de la X (el índice de la fila donde se cruzan) es (altura // 2).
    centro = altura // 2
    
    # Recorrer cada fila, desde el inicio (i=0) hasta la base (i=altura-1)
    for i in range(altura):
        # Inicia en 0 y termina en el centro.
        pos_izq = i

        # Inicia en altura - 1 y termina en el centro.
        pos_der = altura - 1 - i

        linea = [" "] * altura
        
        # Caso A: Fila que no es el centro (donde pos_izq != pos_der)
        if pos_izq != pos_der:
            linea[pos_izq] = "*"
            linea[pos_der] = "*"
        
        # Caso B: Fila central (solo un asterisco, donde pos_izq == pos_der)
        else: 
            linea[centro] = "*"

        print("".join(linea))

    print("-----------------")

pintar_letra_x()