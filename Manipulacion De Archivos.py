#ej1
def start_with(letra, arcchivo):
    count = 0 
    with open(archivo, "r") as file: 
        for line in line:
            if (line[0] != letra.lower() or line[0] != letra.upper())
                count +=1
    print("el numero de liner=as que empiezan con", letra, "es", count)

start_with("M", "archivo")

#ej 2
def imprimir(cantidad_de_filas, archivo):
    file = open(archivo, "r")
    for i in range(0, cantidad_de_filas)
        print(file.readline())

imprimir(3, archivo)

#ej 4
def cuantaspalabrasarchivo(archivo):
    """
    Leer archivo y cuantas palabras tiene
    """
    with open(archivo, "r") as f:
        linea = f.readline()
        palabras = linea.split()
        return len(palabras)

#ej7
def palabra_mas_larga(archivo):
    palabra = ""
    max_long = 0

with open(archivo, "r") as f:
    lista_palabra = f.read().split()
    for word in lista_palabra:
        if len(word) > max_long:
            max_long = len(word)
            palabra = word

print("la palabra mas larga es", palabra, "con", max_long, "caracteres")


#ej8
def join_files(file1, file2, file3):
    with open(file1, "r") as f1, open(file2, "r") as f2, open(file3, "a") as f3: 
        f3.write(f1.read() + f2.read())

join_files("documento", "documento2", "documento3")

#ej 9 
def frecuenciadecadapalabra(archivo, palabra):
    with open(archivo) as f:
        linea = f.readline()
        palabras = linea.split()
        contador = 0
        for i in range(len(palabras)):
            if palabras[i] == palabra:
                contador += 1
        return contador/len(palabras)

# ej 
import glob
import os 
def funcion1(archivo, ruta):
    os.chdir(ruta)
    lista_txt =  glob.glob("*.txt")

    with open (archivo, "a") as s:
        for f in lista_txt:
            file = open(f, "r")
            s.write(file.read())
            file.close()
