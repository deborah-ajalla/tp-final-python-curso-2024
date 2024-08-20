# Trabajo Práctico Final - Curso Introductorio de Python
#------------------------------------------------------------
##  ⏩⏩ EJERCICIO 1: Números y Cadenas de Caracteres ⏪⏪
#-------------------------------------------------------------
#1.
"""
    1. Escribe un programa que pida al usuario dos números enteros y realice lo siguiente:
    - Muestra la suma de los dos números.
    - Muestra el producto de los dos números.
    - Muestra la concatenación de los dos números (como texto).
"""
print ("------------------------------------------")
print ("\n \t ▪▪▪▪▪▪▪▪ BIENVENIDO/A AL PROGRAMA ▪▪▪▪▪▪▪▪")

num_1 = int (input ("\n-> Ingrese un número entero: "))
num_2 = int (input ("-> Ingrese otro número entero: "))

suma = num_1 + num_2
producto = num_1 * num_2
concatenacion = str (num_1) + str (num_2)

print ("\n-----------------------------------------")
print (F"> La suma de {num_1} y {num_2} es: {suma} ✔\n")
print (F"> El producto de {num_1} y {num_2} es: {producto} ✔\n")
print (F"> Ambos números concatenados: {concatenacion} ✔")
print ("------------------------------------------")

#-------------------------------------------------------------
#2.
"""
    2. Pide al usuario una cadena de texto. Luego muestra:
    - La cadena en mayúsculas.
    - La longitud de la cadena.
    - La cadena invertida.
    - La cantidad de veces que aparece una letra específica (elige una letra y pídesela al usuario).
"""
cadena = input ("\n-> Ingrese una Cadena de Texto: ")
letra = input ("-> Elija una letra de la Cadena Ingresada: ")

cadena_invertida = cadena [::-1]

print ("------------------------------------------")
print (F"> La Cadena Ingresada en Mayúscula es: '{cadena.upper()}' ✔ \n")
print (F"> La Cadena Ocupa: {len(cadena)} caracteres ✔ \n")
print (F"> La Letra Elegida '{letra}' se repite: {cadena.count(letra)} veces ✔ \n")
print (F"> La Cadena Invertida Queda:'{cadena_invertida}' ✔ \n")

print ("------------------------------------------")
#-------------------------------------------------------------
#3.
"""
    3. Escribe un programa que convierta un número decimal a binario y viceversa.
"""
numero = int (input ("Ingrese un número decimal: "))
binario = input ("Ingrese un número binario: ")
numero_binario = bin (numero)
print ("------------------------------------------")
print (F"> El número decimal: '{numero}' en binario es: {numero_binario} ✔ \n")
print (F"> El Número binario: '{binario}' en decimal es: {int(binario, 2)} ✔ \n")

print ("------------------------------------------")
#-------------------------------------------------------------
#4.
"""
    4. Pide al usuario una cadena y un número entero. Muestra la cadena repetida el número de veces indicado por el número entero.
"""

cadena_usuario = input ("-> Ingrese una Cadena de Texto: ")
repeticiones = int (input ("-> Ingrese un Número Entero (del 1 al 10): "))

r = 0
while r < repeticiones:
    r+=1
    print(F" > {cadena_usuario}, repetición nº: {r}") 

#-------------------------------------------------------------
## ⏩⏩ EJERCICIO 2: Listas y Tuplas ⏪⏪
#-------------------------------------------------------------
# 1.
"""
    1. Crea una lista con los nombres de tres frutas. Luego:
    - Añade dos frutas más a la lista.
    - Ordena la lista alfabéticamente.
    - Muestra la lista completa.
    - Elimina una fruta de la lista y muestra el resultado.
"""
lista_frutas = ["cereza", "pera", "durazno"]
print ("\n------------------------------------------\n")
print (F"--> Listado de Frutas: {lista_frutas} ✔")

lista_frutas.append ("frutilla")
lista_frutas.append ("banana")
print (F"\n--> Listado Con dos Frutas más: {lista_frutas} ✔")

lista_frutas.sort()
print (F" \n--> Listado Ordenado: {lista_frutas} ✔")

lista_frutas.pop ()
print (F"\n--> Listado Actualizado Sin La Última Fruta: {lista_frutas} ✔")
print ("\n------------------------------------------\n")

#-------------------------------------------------------------
# 2.
"""
    2. Crea una tupla con los nombres de dos ciudades. Luego:
    - Muestra el primer y último elemento de la tupla.
    - Convierte la tupla en una lista, añade una nueva ciudad y muestra la lista resultante.
"""
ciudades = ("Roma", "Moscú")
print ("--> CIUDADES <--")
print (F"--> Primera de la Tupla: {ciudades[0]} ✔")
print (F"--> Última de la Tupla: {ciudades[1]} ✔")

lista_ciudades = []
lista_ciudades.append (ciudades[0])
lista_ciudades.append (ciudades[1])
lista_ciudades.append ("Las Vegas")
print (F"--> La Lista de Ciudades es: {lista_ciudades} ✔")
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 3.
"""
    3. Crea una lista de números enteros y muestra:
    - El número mayor de la lista.
    - El número menor de la lista.
    - El promedio de los números en la lista.
"""
lista_numeros = [3, 1, 6, 2]
print (F"--> Lista de Números: {lista_numeros} ✔ \n")

lista_numeros.sort()
print (F"--> El Número Mayor es: {lista_numeros[-1]} ✔ \n")
print (F"--> El Número Menor es: {lista_numeros[0]} ✔ \n")

suma_lista = sum(lista_numeros)                  # --> suma todos los elementos de la lista ✔
promedio_lista = suma_lista / len (lista_numeros)
print (F"--> El Promedio de los elementos de la Lista es: {promedio_lista} ✔")
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 4.
"""
    4. Escribe un programa que reciba una lista de cadenas y muestre la lista con todas las cadenas en mayúsculas.
"""
lista_cadenas = []
elemento_cadena = int (input ("Ingrese la Cantidad de Cadenas que desea cargar (del 1 al 9): "))

e = 0
while e < elemento_cadena:
    nuevo_elemento = input ("> Ingrese una Cadena: ")
    lista_cadenas.append(nuevo_elemento.upper())
    e+=1
print (F" --> La Lista está compuesta por: {lista_cadenas} ✔")    
print ("\n------------------------------------------\n")
#-------------------------------------------------------------