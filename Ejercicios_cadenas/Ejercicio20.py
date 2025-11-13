"""
Realiza un programa que pinte un triángulo hueco tal como se muestra en los ejemplos. El usuario
debe introducir la altura de la figura.
"""
def pintar_triangulo_hueco_invertido():
    """
    Dibuja un triángulo invertido y hueco de asteriscos en la terminal.
    La altura debe ser un número entero positivo.
    """
    print("--- 🔽 DIBUJADOR DE TRIÁNGULO HUECO INVERTIDO ---")

    # 1. Entrada de Datos y Validación
    while True:
        try:
            altura = int(input("Introduce la altura del triángulo (un número entero positivo, mínimo 3): "))
            if altura >= 3:
                break
            else:
                print("ERROR: La altura debe ser 3 o mayor para que el patrón se aprecie.")
        except ValueError:
            print("ERROR: Por favor, introduce un número entero válido.")

    # 2. Construcción e Impresión del Triángulo
    
    print("\n--- Resultado ---")
    
    for i in range(altura):
        
        longitud_fila = altura - i
        
        # 2.1. FILA SUPERIOR (Solo se ejecuta para i = 0)
        if i == 0:
            print("*" * longitud_fila)
            
        # 2.2. FILAS INTERMEDIAS (Para 0 < i < altura - 1)
        elif i < altura - 1:

            espacios = " " * (longitud_fila - 2)
            linea_hueca = "*" + espacios + "*"
            print(linea_hueca)
            
        # 2.3. FILA INFERIOR (Solo se ejecuta para i = altura - 1)
        else:
            print("*")

    print("-----------------")


pintar_triangulo_hueco_invertido()