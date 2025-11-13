"""
Realiza un programa que pinte la letra U por pantalla hecha con asteriscos. El programa pedirá la
altura. Fíjate que el programa inserta un espacio y pinta dos asteriscos menos en la base para simular la
curvatura de las esquinas inferiores.
"""
def pintar_letra_u():
    """
    Dibuja la letra 'U' con asteriscos de una altura dada.
    La base simula una curvatura insertando un espacio inicial 
    y reduciendo el ancho de la línea de la base.
    """
    print("--- 🌟 DIBUJADOR DE LA LETRA 'U' ---")

    # 1. Entrada de Datos y Validación
    while True:
        try:
            # Pedimos la altura a la terminal
            altura = int(input("Introduce la altura de la 'U' (mínimo 3): "))
            if altura >= 3:
                break
            else:
                print("ERROR: La altura mínima debe ser 3 para formar la 'U' correctamente.")
        except ValueError:
            print("ERROR: Por favor, introduce un número entero válido.")

    # 2. Construcción de la 'U'

    print("\n--- Resultado ---")
    
    # El ancho es igual a (altura * 2) - 3. Por ejemplo, para altura 5, el ancho es 7.
    ancho_interior = (altura * 2) - 3 

    espacio_entre_brazos = " " * ancho_interior

    # Recorremos desde 1 hasta (altura - 1)
    for i in range(1, altura):
        # La cadena es: Asterisco + Espacios internos + Asterisco
        brazos = f"*{espacio_entre_brazos}*"
        print(brazos)
    
    # El ancho total de la U (incluyendo los dos asteriscos de los lados) es (ancho_interior + 2).
    ancho_total_brazos = ancho_interior + 2 
    
    # El número de asteriscos para la base es el ancho total - 2 (la instrucción lo pide).
    num_asteriscos_curvatura = ancho_total_brazos - 2 
    
    # Cadena de asteriscos para la base (los dos asteriscos menos)
    linea_curva = "*" * num_asteriscos_curvatura
    
    # Se añade el espacio inicial requerido para la simulación de la curva:
    base_final_curva = " " + linea_curva
    
    print(base_final_curva)
    
    print("-----------------")

pintar_letra_u()