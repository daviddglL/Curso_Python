"""
Operaciones aritméticas Escribe un programa que sume, reste, multiplique, y divida dos números introducidos por teclado.

"""
num=float(input("Introduzca un número: "))
num2=float(input("Introduzca un número: "))

suma=num+num2
resta1=num-num2
resta2=num2-num
multi=num*num2
div=num/num2
div2=num2/num

print("El resultado de la suma es ",suma, 
      " los resultados de la resta posibles son ",resta1, " y ",resta2,
      " el resultado de la multiplicación es ", multi, " y los resultados posible de la division son ",div," y ",div2)