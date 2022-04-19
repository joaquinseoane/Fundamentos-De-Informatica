# ej 1
cadena=(input("palabra: "))
if cadena[0] == str.upper(cadena[0]):
    print("Es mayuscula") 
else:
    print("Es minuscula") 

#ej 2
def par_impar(numero):
    if numero % 2 == 0:
      print("Es par")
    else:
        print ("Es impar")
numero = int(input("Numero: "))
if numero>0:
    print("Es positivo",par_impar(numero))
elif numero<0:
    print("Es negativo",par_impar(numero))
else:
    print("El numero es 0",par_impar(numero))

#ej 3 
def cara_dado(numero):
    if numero==1:
        print("6")
    elif numero==2:
        print("5")
    elif numero ==3:
        print("4")
    elif numero==4:
        print("3")
    elif numero==5:
        print("2")
    elif numero==6:
        print("1")
    else:
        print("Numero incorrecto ingresado, tiene que ser del 1 al 6")
numero=int(input("Numero: "))
print(cara_dado(numero))

#ej 7
lista=[]
numero =int(input("Ingrese numero:"))
while numero>=0:
    lista.append(numero)
    numero =int(input("Ingrese numero:"))
if numero<0:
    print(lista)


#ej 11
contadores = {}
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto + alfabeto.upper():
    contadores[letra] = 0

cadena = input('escribi una cadena:')

for caracter in cadena: 
    if caracter.lower() in alfabeto:
        contadores[caracter] += 1


for campo, valor in contadores.items():
    print(campo, valor)


#ej 12

cantidad =  int(input("introducir cantidad de alumnos: "))
alumnos = {}

for num in range(0, cantidad):
alumno = input ("alumno: ")
notas = []
nota = int(input("nota: "))
while nota >= 0:
    notas.append(nota)
    nota = int(input("nota: "))
alumnos[alumno] = notas

for alumno in alumnos:
    print(alumno, sum(alumnos[alumno])/len(alumnos[alumno]))

#ej 15

def cargarSocios(socios):
    numero = int(input("Número de socio: "))
    while numero != 0:
        nombre = input("Nombre y apellido: ")
        fecha = input("Fecha de ingreso: ")
        cuota = input("¿Cuota al día? s/n: ")
        pago = cuota.lower() == "s"
        socios[numero] = [nombre, fecha, pago]
        numero = int(input("Número de socio: "))
    return socios
    
def modificarFecha(socios, fechaAnterior, fechaNueva):
    for datos in socios.values():
        if datos[1] == fechaAnterior:
            datos[1] = fechaNueva
    return socios
    
def numeroSocio(socios, nombre):
    for numero,datos in socios.items():
        if datos[0].lower() == nombre.lower():
            return numero
    return 0

def formatoFecha(fecha):
    return fecha[:2] + "/" + fecha[2:4] + "/" + fecha[4:]
    
def imprimirListado(socios):
    for numero,datos in socios.items():
        print("Número: ", numero)
        print("Nombre: ", datos[0])
        print("Fecha de ingreso ", formatoFecha(datos[1]))
        if datos[2]:
            print("Cuota al día")
        else:
            print("En deuda")
            print("---------------")
    return None
    
socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}

print("Cargar socios")
socios_activos = cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")
print("Registrar pago de cuotas")
numero = int(input("Numero de socio: "))
socios_activos[numero][2] = True

print("Modificando fecha de ingreso...")
socios_activos = modificarFecha(socios_activos, "21102017", "22102017")

print("Eliminar socio:")
nombre = input("Nombre y apellido: ")
numero = numeroSocio(socios_activos, nombre)
del socios_activos[numero]

imprimirListado(socios_activos)
