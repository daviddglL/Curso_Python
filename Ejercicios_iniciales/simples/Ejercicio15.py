"""
Medianoche Escribe un programa que dada una hora determinada(horas y minutos), calcule el numero de segundos que faltan para llegar a la medianoche
"""

horas=int(input("Escriba la hora determinada: "))
mins=int(input("Introduzca los minutos: "))

min=60
hora=min*60
dia=hora*24

m=dia-((mins*min)+(horas*hora))

print("El tiempo que falta en segundos hasta la media noche es de: ",m)