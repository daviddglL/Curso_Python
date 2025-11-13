"""
La tienda online BanderaDeEspaña.es vende banderas personalizadas de la máxima calidad y nos
ha pedido hacer un configurador que calcule el precio según el alto y el ancho. El precio base de una 
bandera es de un céntimo de euro el centímetro cuadrado. Si la queremos con un escudo bordado, el
precio se incrementa en 2.50 € independientemente del tamaño. Los gastos de envío son 3.25 €. El IVA
ya está incluido en todas las tarifas.
"""

def calcular_precio_bandera():
    """
    Calcula el precio de una bandera personalizada basado en sus dimensiones,
    la opción de escudo bordado y los gastos de envío fijos.
    """
    PRECIO_BASE_CM2 = 0.01  
    COSTE_ESCUDO = 2.50      
    GASTOS_ENVIO = 3.25      
    
    print("--- 🇪🇸 CONFIGURADOR DE BANDERAS PERSONALIZADAS ---")

    
    # Validar el Alto
    while True:
        try:
            alto = float(input("Introduce el ALTO de la bandera en centímetros (cm): "))
            if alto > 0:
                break
            else:
                print("El alto debe ser un valor positivo.")
        except ValueError:
            print("ERROR: Introduce un número válido para el alto.")

    # Validar el Ancho
    while True:
        try:
            ancho = float(input("Introduce el ANCHO de la bandera en centímetros (cm): "))
            if ancho > 0:
                break
            else:
                print("El ancho debe ser un valor positivo.")
        except ValueError:
            print("ERROR: Introduce un número válido para el ancho.")
            
    
    # Validar la opción de Escudo Bordado
    while True:
        opcion_escudo = input("¿Quiere la bandera con escudo bordado? (Sí/No): ").lower()
        if opcion_escudo in ['si', 's', 'no', 'n']:
            con_escudo = opcion_escudo in ['si', 's']
            break
        else:
            print("Opción no válida. Por favor, escriba 'Sí' o 'No'.")


    # A. Precio por Superficie (Base)
    superficie = alto * ancho
    precio_superficie = superficie * PRECIO_BASE_CM2

    # B. Precio del Escudo Bordado
    precio_escudo = COSTE_ESCUDO if con_escudo else 0.00
    
    # C. Cálculo del Subtotal
    subtotal = precio_superficie + precio_escudo
    
    # D. Cálculo del Total (incluye el IVA y gastos de envío)
    precio_final = subtotal + GASTOS_ENVIO

    # 4. Desglose del Precio (Salida con formato de Cadenas)
    
    separador = "=" * 40
    
    print("\n" + separador)
    print("           RESUMEN DEL PEDIDO")
    print(separador)
    
    # Dimensiones
    print(f"Dimensiones:         {alto:.2f} cm x {ancho:.2f} cm")
    print(f"Superficie:          {superficie:.2f} cm²")
    print(f"Escudo Bordado:      {'Sí' if con_escudo else 'No'}")
    print("-" * 40)
    
    # Desglose de Costes
    print("I. COSTE BASE")
    print(f"   - Precio por superficie ({PRECIO_BASE_CM2:.2f} €/cm²): {precio_superficie:10.2f} €")
    
    print("II. EXTRAS")
    print(f"   - Escudo Bordado:                     {precio_escudo:10.2f} €")
    print("-" * 40)

    # Subtotal
    print(f"   SUBTOTAL (IVA Incluido):              {subtotal:10.2f} €")
    
    print("III. ENVÍO")
    print(f"   - Gastos de Envío Fijos:              {GASTOS_ENVIO:10.2f} €")
    print(separador)
    
    # Precio Final
    print(f"   PRECIO FINAL TOTAL:                   {precio_final:10.2f} €")
    print(separador)

calcular_precio_bandera()