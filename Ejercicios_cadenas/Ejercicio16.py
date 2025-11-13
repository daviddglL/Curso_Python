"""
Escribe un programa que lea un número n e imprima una pirámide de números con n filas como en
la siguiente figura:
    1
   121
  12321
 1234321
"""
def imprimir_piramide_numeros():
    """
    Lee un número N y genera una pirámide de números centrada con N filas.
    Ejemplo (N=4):
              1
            121
          12321
        1234321
    """
    
    print("--- 🔢 GENERADOR DE PIRÁMIDE DE NÚMEROS ---")

    # 1. Entrada de Datos y Validación
    while True:
        try:
            n = int(input("Introduce el número de filas (N): "))
            if n > 0:
                break
            else:
                print("ERROR: El número de filas debe ser un entero positivo.")
        except ValueError:
            print("ERROR: Por favor, introduce un número entero válido.")

    # 2. Generación e Impresión de la Pirámide
    
    # El ancho máximo de la pirámide es el de la última fila.
    # Para N=4, la última fila es '1234321', que tiene 7 caracteres.
    # El ancho máximo es 2*N - 1.
    ancho_maximo = 2 * n - 1

    print("\n--- Resultado ---")
    
    # Recorrer cada fila desde 1 hasta N
    for i in range(1, n + 1):
        # Parte ascendente de la cadena (1, 12, 123, ...)
        parte_ascendente = ""
        for j in range(1, i + 1):
            parte_ascendente += str(j)
        
        # Parte descendente de la cadena (vacío, 21, 321, ...)
        # Empezamos desde i-1 y vamos hasta 1
        parte_descendente = ""
        for k in range(i - 1, 0, -1):
            parte_descendente += str(k)
        
        # La cadena completa de la fila
        cadena_fila = parte_ascendente + parte_descendente
        
        # Imprimir la cadena centrada usando el ancho_maximo
        # str.center(width) añade espacios a la izquierda y derecha para centrar la cadena.
        print(cadena_fila.center(ancho_maximo))

    print("-----------------")
imprimir_piramide_numeros()