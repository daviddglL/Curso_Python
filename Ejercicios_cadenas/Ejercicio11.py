"""
 Escribe un programa que calcule el precio final de un producto según su base imponible (precio 
antes de impuestos), el tipo de IVA aplicado (general, reducido o superreducido) y el código 
promocional. Los tipos de IVA general, reducido y superreducido son del 21%, 10% y 4% 
respectivamente. Los códigos promocionales pueden ser nopro, mitad, meno5 o 5porc que significan 
respectivamente que no se aplica promoción, el precio se reduce a la mitad, se descuentan 5 euros o se 
descuenta el 5%. Mostrar los resultados tabulados.
"""

bip=int(input("Introduzca el precio en base imponible: "))
iva=input("Introduzca el IVA aplicado (general, reducido o superreducido): ")
des=input("Introduzca su codigo de descuento (nopro, mitad, meno5 o 5porc): ")

if iva !="general" and iva!="reducido" and iva!="superreducido":
    print("tipo no valido")
elif iva =="general":
    pre=(bip*0.21)
elif iva == "reducido":
    pre=(bip*0.1)
elif iva == "superreducido":
    pre=(bip*0.04)

if des != "nopro" and des!="mitad" and des!="meno5" and des!="5porc":
    print("codigo de descuento no valido")
elif des=="nopro":
    desc=0
elif des=="mitad":
    desc=(bip+pre)/2
elif des=="meno5":
    desc=5
elif des=="5porc":
    desc=((bip+pre)*0.05)


print("precio del producto con base imponible: ",bip)
print("IVA",pre)
print("precio del producto con IVA: ",bip+pre)
print("Descuento por promocion: ",desc)
print("Precio final del producto: ",(bip+pre)-desc)