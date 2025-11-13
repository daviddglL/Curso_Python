"""
. Escribe un programa que genere la nómina (bien desglosada) de un empleado según las siguientes 
condiciones:
 • Se pregunta el cargo del empleado (1 - Prog. junior, 2 - Prog. senior, 3 – Jefe de proyecto), los 
días que ha estado de viaje visitando clientes durante el mes y su estado civil (1 - Soltero, 2 - 
Casado).
 • El sueldo base según el cargo es de 950, 1200 y 1600 euros según si se trata de un prog. junior, 
un prog. senior o un jefe de proyecto respectivamente.
 • Por cada día de viaje visitando clientes se pagan 30 euros extra en concepto de dietas. Al sueldo 
neto hay que restarle el IRPF, que será de un 25% en caso de estar soltero y un 20% en caso de 
estar casado.
"""

def generar_nomina_terminal():
    """
    Genera la nómina desglosada de un empleado, interactuando por terminal.
    """
    print("--- GENERADOR DE NÓMINA ---")

    
    # Preguntar y validar Cargo
    while True:
        try:
            cargo = int(input("Introduzca el cargo (1 - Prog. junior, 2 - Prog. senior, 3 – Jefe de proyecto): "))
            if 1 <= cargo <= 3:
                break
            else:
                print("ERROR: Opción de cargo no válida (debe ser 1, 2 o 3). Inténtelo de nuevo.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")

    # Preguntar y validar Días de Viaje
    while True:
        try:
            dias_viaje = int(input("Introduzca los días que ha estado de viaje visitando clientes durante el mes: "))
            if dias_viaje >= 0:
                break
            else:
                print("ERROR: Los días de viaje no pueden ser negativos.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")

    # Preguntar y validar Estado Civil
    while True:
        try:
            estado_civil = int(input("Introduzca el estado civil (1 - Soltero, 2 - Casado): "))
            if 1 <= estado_civil <= 2:
                break
            else:
                print("ERROR: Opción de estado civil no válida (debe ser 1 o 2). Inténtelo de nuevo.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")

    # Asignación de Sueldo Base y Descripción
    cargos_map = {
        1: (950.00, "Programador Junior"),
        2: (1200.00, "Programador Senior"),
        3: (1600.00, "Jefe de Proyecto"),
    }
    sueldo_base, descripcion_cargo = cargos_map.get(cargo, (0.00, "Desconocido"))

    # Cálculo de Dietas
    TARIFA_DIETA = 30.00
    dietas = dias_viaje * TARIFA_DIETA

    # Cálculo del Sueldo Bruto
    sueldo_bruto = sueldo_base + dietas

    # Cálculo de IRPF y Descripción
    if estado_civil == 1:
        irpf_porcentaje = 0.25
        descripcion_estado_civil = "Soltero"
    else: 
        irpf_porcentaje = 0.20
        descripcion_estado_civil = "Casado"
    
    retencion_irpf = sueldo_bruto * irpf_porcentaje
    
    sueldo_neto = sueldo_bruto - retencion_irpf

    # 3. Desglose de la Nómina (Salida con formato de Cadenas)
    
    separador = "=" * 50
    linea_devengo = "-" * 40
    
    print("\n" + separador)
    print("========== NÓMINA MENSUAL DEL EMPLEADO ==========")
    print(separador)
    print(f"Cargo:             {descripcion_cargo}")
    print(f"Estado Civil:      {descripcion_estado_civil}")
    print(f"Días de Viaje:     {dias_viaje} días")
    print(linea_devengo)

    # I. DEVENGOS (Ingresos)
    print("I. DEVENGOS (TOTAL INGRESOS)")
    print(f"   - Sueldo Base:              {sueldo_base:10.2f} €")
    print(f"   - Dietas ({dias_viaje} días * {TARIFA_DIETA:.2f} €): {dietas:10.2f} €")
    print(f"   {linea_devengo}")
    print(f"   SUELDO BRUTO (A):           {sueldo_bruto:10.2f} €")
    print(linea_devengo)

    # II. DEDUCCIONES (Descuentos)
    print("II. DEDUCCIONES (TOTAL DESCUENTOS)")
    irpf_display = irpf_porcentaje * 100
    print(f"   - Retención IRPF ({irpf_display:.0f}%):  {retencion_irpf:10.2f} €")
    print(linea_devengo)

    # III. LÍQUIDO A PERCIBIR (Sueldo Neto)
    print("III. LÍQUIDO A PERCIBIR")
    print(f"TOTAL NETO (A - DEDUCCIONES):  {sueldo_neto:10.2f} €")
    print(separador)

generar_nomina_terminal()