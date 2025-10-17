"""
Horoscopo Escribe un programa que nos muestre el horoscopo a partir del dia y mes de nacimiento
"""

dia=int(input("Inserte su día de nacimiento: "))
mes=int(input("Indique su mes de nacimiento: "))

if dia > 31 or dia < 1:
    print("Día no válido")
if mes > 12 or mes < 1:
    print("Mes no válido")


if mes == 1:
    if dia >= 1 and dia <= 19:
        print("Tu signo es Capricornio")
    elif dia >= 20 and dia <= 31:
        print("Tu signo es Acuario")
    else:
        print("Día no válido para este mes")

elif mes == 2:
    if dia >= 1 and dia <= 18:
        print("Tu signo es Acuario")
    elif dia >= 19 and dia <= 29:
        print("Tu signo es Piscis")
    else:
        print("Día no válido para este mes")

elif mes == 3:
    if dia >= 1 and dia <= 20:
        print("Tu signo es Piscis")
    elif dia >= 21 and dia <= 31:
        print("Tu signo es Aries")
    else:
        print("Día no válido para este mes")

elif mes == 4:
    if dia >= 1 and dia <= 19:
        print("Tu signo es Aries")
    elif dia >= 20 and dia <= 30:
        print("Tu signo es Tauro")
    else:
        print("Día no válido para este mes (Abril solo tiene 30 días)")

elif mes == 5:
    if dia >= 1 and dia <= 20:
        print("Tu signo es Tauro")
    elif dia >= 21 and dia <= 31:
        print("Tu signo es Géminis")
    else:
        print("Día no válido para este mes")

elif mes == 6:
    if dia >= 1 and dia <= 20:
        print("Tu signo es Géminis")
    elif dia >= 21 and dia <= 30:
        print("Tu signo es Cáncer")
    else:
        print("Día no válido para este mes (Junio solo tiene 30 días)")

elif mes == 7:
    if dia >= 1 and dia <= 22:
        print("Tu signo es Cáncer")
    elif dia >= 23 and dia <= 31:
        print("Tu signo es Leo")
    else:
        print("Día no válido para este mes")

elif mes == 8:
    if dia >= 1 and dia <= 22:
        print("Tu signo es Leo")
    elif dia >= 23 and dia <= 31:
        print("Tu signo es Virgo")
    else:
        print("Día no válido para este mes")

elif mes == 9:
    if dia >= 1 and dia <= 22:
        print("Tu signo es Virgo")
    elif dia >= 23 and dia <= 30:
        print("Tu signo es Libra")
    else:
        print("Día no válido para este mes (Septiembre solo tiene 30 días)")

elif mes == 10:
    if dia >= 1 and dia <= 22:
        print("Tu signo es Libra")
    elif dia >= 23 and dia <= 31:
        print("Tu signo es Escorpio")
    else:
        print("Día no válido para este mes")

elif mes == 11:
    if dia >= 1 and dia <= 21:
        print("Tu signo es Escorpio")
    elif dia >= 22 and dia <= 30:
        print("Tu signo es Sagitario")
    else:
        print("Día no válido para este mes (Noviembre solo tiene 30 días)")

elif mes == 12:
    if dia >= 1 and dia <= 21:
        print("Tu signo es Sagitario")
    elif dia >= 22 and dia <= 31:
        print("Tu signo es Capricornio")
    else:
        print("Día no válido para este mes")