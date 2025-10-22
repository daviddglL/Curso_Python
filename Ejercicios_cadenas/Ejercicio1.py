"""
 Escribe un programa que muestre por pantalla 10 palabras en inglés junto a su correspondiente 
traducción al castellano. Las palabras deben estar distribuidas en dos columnas y alineadas a la 
izquierda.
"""

cad_en=["computer","student","cat","penguin","machine","nature","light","green","book","pyramid"]
cad_esp=["ordenador","alumno/a","gato","pingüino","máquina","naturaleza","luz","verde","libro","pirámide"]

for i in range(10):
    print(cad_en[i],"  ",cad_esp[i],"\n")
    