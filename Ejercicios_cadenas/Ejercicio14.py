"""
Realiza un programa que calcule el precio de unas entradas de cine en función del número de
personas y del día de la semana. El precio base de una entrada son 8 euros. El miércoles (día del
espectador), el precio base es de 5 euros. Los jueves son el día de la pareja, por lo que la entrada para
dos cuesta 11 euros. Con la tarjeta CineCampa se obtiene un 10% de descuento. Si un jueves, un
grupo de 6 personas compran entradas, el precio total sería de 33 euros ya que son 3 parejas; pero si es
un grupo de 7, pagarán 3 entradas de pareja más 1 individual que son 41 euros (33 + 8).
"""
def calcular_precio_entradas():
    """
    Calcula el precio final de las entradas de cine basado en el día, 
    número de personas y el uso de la tarjeta CineCampa.
    """
    
    # Precios y constantes
    PRECIO_BASE = 8.00
    PRECIO_MIERCOLES = 5.00
    PRECIO_PAREJA = 11.00 
    DESCUENTO_TARJETA = 0.10 
    
    print("--- 🎬 CALCULADORA DE ENTRADAS DE CINE ---")
    
    # Días de la semana para la entrada
    dias_validos = {
        'lunes': 1, 'martes': 2, 'miercoles': 3, 'jueves': 4, 
        'viernes': 5, 'sabado': 6, 'domingo': 7
    }

    # a. Día de la semana
    while True:
        dia_str = input("Introduce el día de la semana (Ej: Lunes, Miércoles, Jueves): ").lower()
        if dia_str in dias_validos:
            dia = dias_validos[dia_str]
            break
        else:
            print("ERROR: Día no válido. Por favor, usa el nombre completo del día.")

    # b. Número de personas
    while True:
        try:
            num_personas = int(input("Introduce el número de personas: "))
            if num_personas > 0:
                break
            else:
                print("ERROR: El número de personas debe ser positivo.")
        except ValueError:
            print("ERROR: Introduce un número entero válido.")

    # c. Tarjeta CineCampa
    while True:
        tarjeta_str = input("¿Tiene tarjeta CineCampa? (Sí/No): ").lower()
        if tarjeta_str in ['si', 's', 'no', 'n']:
            con_tarjeta = tarjeta_str in ['si', 's']
            break
        else:
            print("Opción no válida. Por favor, escriba 'Sí' o 'No'.")

    
    precio_base_sin_descuento = 0.00
    concepto_aplicado = ""

    # Caso Especial: Jueves (Día de la Pareja)
    if dia == 4: # Jueves
        num_parejas = num_personas // 2  
        entradas_individuales = num_personas % 2 
        
        coste_parejas = num_parejas * PRECIO_PAREJA
        coste_individuales = entradas_individuales * PRECIO_BASE
        
        precio_base_sin_descuento = coste_parejas + coste_individuales
        concepto_aplicado = (f"Día de la Pareja ({num_parejas}x{PRECIO_PAREJA:.2f}€ + "
                             f"{entradas_individuales}x{PRECIO_BASE:.2f}€)")

    # Caso Especial: Miércoles (Día del Espectador)
    elif dia == 3:
        precio_base_sin_descuento = num_personas * PRECIO_MIERCOLES
        concepto_aplicado = f"Día del Espectador ({num_personas}x{PRECIO_MIERCOLES:.2f}€)"
        
    # Caso General: Resto de días
    else:
        precio_base_sin_descuento = num_personas * PRECIO_BASE
        concepto_aplicado = f"Precio Base ({num_personas}x{PRECIO_BASE:.2f}€)"

    
    descuento_aplicado = 0.00
    
    if con_tarjeta:
        descuento_aplicado = precio_base_sin_descuento * DESCUENTO_TARJETA
    
    precio_final = precio_base_sin_descuento - descuento_aplicado

    
    separador = "=" * 50
    
    print("\n" + separador)
    print("              RESUMEN DE LA COMPRA")
    print(separador)
    
    print(f"Día de la semana:         {dia_str.capitalize()}")
    print(f"Número de personas:       {num_personas}")
    print("-" * 50)
    
    # Desglose de Costes
    print("I. COSTES BASE (Subtotal)")
    print(f"   - Cálculo Aplicado:         {concepto_aplicado}")
    print(f"   SUBTOTAL:                   {precio_base_sin_descuento:10.2f} €")
    print("-" * 50)

    # Descuentos
    print("II. DESCUENTOS")
    descuento_display = f"Sí ({DESCUENTO_TARJETA*100:.0f}%)" if con_tarjeta else "No"
    print(f"   - Tarjeta CineCampa ({descuento_display}): {descuento_aplicado:10.2f} €")
    print("-" * 50)
    
    # Precio Final
    print(f"   PRECIO FINAL A PAGAR:       {precio_final:10.2f} €")
    print(separador)


calcular_precio_entradas()