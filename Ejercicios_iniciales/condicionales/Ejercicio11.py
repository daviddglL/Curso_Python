"""
Salario semanal 2 Ampliaremos el ejercicio anterior para considerar las horas extras. Las primeras 40 h se pagan a 12 euros. Las siguientes se pagan a 16 euros
"""

horas=int(input("inserte las horas trabajadas: "))


if horas <=40:
   salario=horas*12
else:
   horas_extra=horas-40
   salario=40*12+horas_extra*16

total=salario

print("para las horas trabajadas: ",horas," y las horas extras de ",horas_extra," el salario es de ",total,"€")