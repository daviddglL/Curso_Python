"""
Realiza un programa que pinte un triángulo relleno tal como se muestra en los ejemplos. El usuario
debe introducir la altura de la figura.
"""
def pintar_triangulo_relleno():
    """
    Dibuja un triángulo invertido y relleno de asteriscos, 
    donde la longitud de la fila disminuye con cada línea.
    """
    print("--- 🔽 DIBUJADOR DE TRIÁNGULO RELLENO INVERTIDO ---")

    # 1. Entrada de Datos y Validación
    while True:
        try:
            altura = int(input("Introduce la altura del triángulo (un número entero positivo): "))
            if altura > 0:
                break
            else:
                print("ERROR: La altura debe ser un número positivo.")
        except ValueError:
            print("ERROR: Por favor, introduce un número entero válido.")

    # 2. Construcción e Impresión del Triángulo
    
    print("\n--- Resultado ---")
    
    # Usamos range(altura, 0, -1) para ir desde 'altura' (incluida) hasta 1 (sin incluir 0), de forma descendente.
    for i in range(altura, 0, -1):
        # 'i' representa el número de asteriscos que tendrá la fila actual.
        linea = "*" * i
        print(linea)

    print("-----------------")

pintar_triangulo_relleno()