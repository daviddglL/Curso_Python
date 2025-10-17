"""
Nota Programación. Escribe un programa que pide las notas de dos exámenes de programación. Si la media es mayor o igual a 5, el alumno estará aprobado y se mostrará la media. Si no, se preguntará al usuario ¿Cual ha sido el resultado de la recuperación?(apto/no apto). Si el resultado es apto la nota será 5, en caso contrario se mantendrá la media anterior.
"""

n1=float(input("Introduzca la nota del primer examen: "))
n2=float(input("Introduzca la nota del segundo examen: "))

media=(n1+n2)/2

if media>=5:
    print("Esta aprovado ",media)
else:
    rec=input("¿Cual ha sido el resultado de la recuperación?(apto/no apto)")
    if rec=="no apto":
        print("has suspendido, ",media)
    elif rec=="apto":
        print("has aprovado tu media es 5")