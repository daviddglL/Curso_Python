"""
Una pastelería nos ha pedido realizar un programa que haga presupuestos de tartas. El programa
preguntará primero de qué sabor quiere el usuario la tarta: manzana, fresa o chocolate. La tarta de
manzana vale 18 euros y la de fresa 16. En caso de seleccionar la tarta de chocolate, el programa debe
preguntar además si el chocolate es negro o blanco; la primera opción vale 14 euros y la segunda 15.
Por último se pregunta si se añade nata y si se personaliza con un nombre; la nata suma 2.50 y la
escritura del nombre 2.75.
"""

def calcular_presupuesto_tarta():
    
    PRECIOS_SABOR = {
        'manzana': 18.00,
        'fresa': 16.00,
        'chocolate_negro': 14.00,
        'chocolate_blanco': 15.00
    }
    
    PRECIO_NATA = 2.50
    PRECIO_NOMBRE = 2.75
    
    precio_base = 0.00
    
    print("--- 🍰 PRESUPUESTADOR DE TARTAS ---")
    
    while True:
        sabor_elegido = input("¿De qué sabor quiere la tarta (Manzana, Fresa o Chocolate)? ").lower()
        
        if sabor_elegido == 'manzana':
            precio_base = PRECIOS_SABOR['manzana']
            sabor_final = "Manzana"
            break
            
        elif sabor_elegido == 'fresa':
            precio_base = PRECIOS_SABOR['fresa']
            sabor_final = "Fresa"
            break
            
        elif sabor_elegido == 'chocolate':
            while True:
                tipo_chocolate = input("¿Qué tipo de chocolate quiere (Negro o Blanco)? ").lower()
                if tipo_chocolate == 'negro':
                    precio_base = PRECIOS_SABOR['chocolate_negro']
                    sabor_final = "Chocolate Negro"
                    break
                elif tipo_chocolate == 'blanco':
                    precio_base = PRECIOS_SABOR['chocolate_blanco']
                    sabor_final = "Chocolate Blanco"
                    break
                else:
                    print("Opción de chocolate no válida. Intente con 'Negro' o 'Blanco'.")
            break
            
        else:
            print("Sabor no reconocido. Por favor, elija entre Manzana, Fresa o Chocolate.")
    
    # a. Nata
    while True:
        opcion_nata = input("¿Quiere añadir nata (Sí/No)? ").lower()
        if opcion_nata in ['si', 's', 'no', 'n']:
            con_nata = opcion_nata in ['si', 's']
            break
        else:
            print("Opción no válida. Por favor, escriba 'Sí' o 'No'.")

    # b. Nombre
    while True:
        opcion_nombre = input("¿Quiere personalizar con un nombre (Sí/No)? ").lower()
        if opcion_nombre in ['si', 's', 'no', 'n']:
            con_nombre = opcion_nombre in ['si', 's']
            break
        else:
            print("Opción no válida. Por favor, escriba 'Sí' o 'No'.")
                
    coste_nata = PRECIO_NATA if con_nata else 0.00
    coste_nombre = PRECIO_NOMBRE if con_nombre else 0.00
    
    precio_final = precio_base + coste_nata + coste_nombre

    separador = "=" * 40
    
    print("\n" + separador)
    print("        PRESUPUESTO DE SU TARTA")
    print(separador)
    
    print(f"Sabor Base ({sabor_final}):         {precio_base:10.2f} €")
    print("-" * 40)
    
    print("EXTRAS:")

    nata_display = f"{coste_nata:10.2f} €" if con_nata else "No"
    nombre_display = f"{coste_nombre:10.2f} €" if con_nombre else "No"
    
    print(f"   - Nata ({PRECIO_NATA:.2f} €):             {nata_display:>10}")
    print(f"   - Nombre ({PRECIO_NOMBRE:.2f} €):         {nombre_display:>10}")
    print("-" * 40)

    print(f"PRECIO FINAL TOTAL:         {precio_final:10.2f} €")
    print(separador)

calcular_presupuesto_tarta()