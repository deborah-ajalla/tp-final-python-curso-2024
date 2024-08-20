# Trabajo Práctico Final - Curso Introductorio de Python
#------------------------------------------------------------
##  ⏩ EJERCICIO 1: Números y Cadenas de Caracteres ⏪
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