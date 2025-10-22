"""
Escribe un programa que muestre tu horario de clase. Cada módulo o asignatura debe mostrarse en 
un color diferente.
"""
import colorama 

colorama.init()
dia=["lunes","martes"]
clase=[["\x1b[41mMatematicas\x1b[0m","\x1b[44mLengua\x1b[0m","\x1b[45mHistoria\x1b[0m"],["\x1b[42mCiencia\x1b[0m","\x1b[44mLengua\x1b[0m","\x1b[47mArte\x1b[0m"]]

for i in range (2):
    print("\n",dia[i],"\n")
    for n in range(3):
        print(clase[i][n])
