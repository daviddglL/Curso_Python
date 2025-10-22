"""
números. Escribe un programa que pida números hasta que se introduzca un número negativo. Se mostrará cuántos números se han introducido, la media de los impares y el mayot de los pares. El número negativo solo se utiliza para finalizar.
"""

cantidad=1
suma_imp=0
cont_imp=0
may_par=-1
num=int(input("introduzca un número superior a 0: "))

while num>=0:
    num=int(input("introduzca un número superior a 0: "))
    if num>=0:
        cantidad=cantidad+1
    if num %2 == 0:
        if num > may_par:
            may_par=num
    else:
        suma_imp=suma_imp+num
        cont_imp=cont_imp+1

if cont_imp>0:
    media_impar=suma_imp/cont_imp
else:
    media_impar=0

print("la cantidad de numeros introducidos es: ",cantidad)
print("La media de los números impares es: ",media_impar)

if may_par !=-1:
    print("El mayor de los numeros pares es: ",may_par)
else:
    print("no se introdujeron números pares")

    