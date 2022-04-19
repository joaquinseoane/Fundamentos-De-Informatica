
#desafio IX
from logging.config import dictConfig


pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
lista_comensales =  pedido.keys()
lista_comensales = ["Ana", "Paul", "luz"]
lista_valores = pedido.values()
dict1 = {"no veggie": 0, "gusto2": 0....., "gustoN": 0}
dict1["gusto1"]
dict1["gusto1"] = dict1["gusto1"] + 1


lista_comensales = pedidos.keys()

def: empanadas_por_gusto():
   for i in lista_comensales:
      dict1[pedido[comensal]] += 1

# ej 2
print('palabra que queres')
palabra = input()
print(str.upper(f"{palabra}"[4])) 
print(str.upper(f"{palabra}"[5]))

# ej 3 
print("Cual es tu nombre y apellido?")
nombre = input()
print(f"Hola, {nombre}")

#ej 6
Datos = int(input("Minutos: "))
hora= Datos//60
minutos= Datos - (hora* 60)
print("Horas:", hora,"Minutos:", minutos)

#ej 8
def nota_final(correctas, incorrectas):
    return print("nota final:", correctas*4-incorrectas*1)

# ej 9
costo_total= int(input("Costo de la casa:"))
porcentaje_sueldo= float(input(f"Que porcentaje de sueldo quiere ahorrar por mes:"))
sueldo_anual=int(input(f"Cual es su sueldo anual:"))
cantidad_ahorro= 0
deposito=costo_total*0.25
cantidad_ahorro_mes=(sueldo_anual/12)*porcentaje_sueldo
print(deposito/cantidad_ahorro_mes)