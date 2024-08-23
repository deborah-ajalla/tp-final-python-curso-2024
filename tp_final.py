# Trabajo Práctico Final - Curso Introductorio de Python
#------------------------------------------------------------
##  ⏩⏩ EJERCICIO 1: Números y Cadenas de Caracteres ⏪⏪
#-------------------------------------------------------------
# 1.
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
print ("------------------------------------------\n")
#-------------------------------------------------------------
# 2.
"""
    2. Pide al usuario una cadena de texto. Luego muestra:
    - La cadena en mayúsculas.
    - La longitud de la cadena.
    - La cadena invertida.
    - La cantidad de veces que aparece una letra específica (elige una letra y pídesela al usuario).
"""
cadena = input ("-> Ingrese una Cadena de Texto: ")
letra = input ("-> Elija una letra de la Cadena Ingresada: ")

cadena_invertida = cadena [::-1]

print ("------------------------------------------")
print (F"> La Cadena Ingresada en Mayúscula es: '{cadena.upper()}' ✔ \n")
print (F"> La Cadena Ocupa: {len(cadena)} caracteres ✔ \n")
print (F"> La Letra Elegida '{letra}' se repite: {cadena.count(letra)} veces ✔ \n")
print (F"> La Cadena Invertida Queda:'{cadena_invertida}' ✔")

print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 3.
"""
    3. Escribe un programa que convierta un número decimal a binario y viceversa.
"""
numero = int (input ("Ingrese un número decimal: "))
binario = input ("Ingrese un número binario: ")
numero_binario = bin (numero)

print (F"\n> El número decimal: '{numero}' en binario es: {numero_binario} ✔")
print (F"> El Número binario: '{binario}' en decimal es: {int(binario, 2)} ✔")

print ("\n------------------------------------------\n")
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
print ("\n------------------------------------------\n")
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
print ("--> TUPLA DE CIUDADES <--")
print (F"> Primera Ciudad: {ciudades[0]} ✔")
print (F"> Última Ciudad: {ciudades[1]} ✔")

lista_ciudades = []
lista_ciudades.append (ciudades[0])
lista_ciudades.append (ciudades[1])
lista_ciudades.append ("Las Vegas")
print ("-> Se agrega una Nueva Ciudad...")
print (F"--> La Lista de Ciudades Final es: {lista_ciudades} ✔")
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
print (F"-> El Número Mayor es: {lista_numeros[-1]} ✔ \n")
print (F"-> El Número Menor es: {lista_numeros[0]} ✔ \n")

suma_lista = sum(lista_numeros)                  # --> suma todos los elementos de la lista ✔
promedio_lista = suma_lista / len (lista_numeros)
print (F"-> El Promedio de los elementos de la Lista es: {promedio_lista} ✔")
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 4.
"""
    4. Escribe un programa que reciba una lista de cadenas y muestre la lista con todas las cadenas en mayúsculas.
"""
print ("--> Armamos una Lista de Cadenas ...")
lista_cadenas = []
elemento_cadena = int (input ("Ingrese la Cantidad de Cadenas que desea cargar (del 1 al 9): "))

e = 0
while e < elemento_cadena:
    nuevo_elemento = input ("> Ingrese una Cadena: ")
    lista_cadenas.append(nuevo_elemento.upper())
    e+=1
print (F"--> La Lista está compuesta por: {lista_cadenas} ✔")    
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
## ⏩⏩ EJERCICIO 3: Controladores de Flujo ⏪⏪
#-------------------------------------------------------------
# 1.
"""
    1. Escribe un programa que pida un número al usuario. Muestra si el número es par o impar.
"""
print ("-> Analizamos si un nº es par o impar ...")
numero_usuario = int (input ("> Ingrese un Número: "))

if (numero_usuario % 2) == 0:
    print (F"> El Número '{numero_usuario}' es par ✔")
else:
    print (F"> El Número '{numero_usuario}' es impar ✔")
    print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 2.
"""
    2. Crea un programa que simule un menú simple con las siguientes opciones:
        1. Saludar
        2. Despedirse
        3. Salir
        - Dependiendo de la opción elegida, muestra un mensaje correspondiente. Si se elige 3, el programa debe terminar.
"""
print (" 🔸🔸🔸🔸🔸 BIENVENIDO/A 🔸🔸🔸🔸🔸\n")
  
nombre_usuario = input ("Ingrese su Nombre: ")
nombre_usuario = nombre_usuario.title()

while True:
    print ("-----------------------")
    print ("\n   ✨ MENÚ ✨")
    print (" > 1. Saludar")
    print (" > 2. Despedirse")
    print (" > 3. Salir")

    opcion = input ("\n >> Ingrese una opción del 1 al 3: ")
   
    if opcion == "1":
         print ("-----------------------")
         print (F"   -> Hola {nombre_usuario} 😊")

    elif opcion == "2":
         print ("-----------------------")
         print (F"   -> Adiós {nombre_usuario} 🤗")
    elif opcion == "3":
        print ("-----------------------")
        print (F"   -> Hasta Luego {nombre_usuario} 😊")
        break
    else:
        print ("-----------------------")
        print (F"  ❌❌ Por Favor {nombre_usuario} ingresá una opción correcta ❌❌")
print ("\n  😊 Gracias Vuelva Pronto!!😊")

print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 3.
"""
    3. Escribe un programa que pida un número al usuario y determine si es positivo, negativo o cero.
"""
print ("-> Analizamos si un nº es positivo/negativo ...")
un_numero =  int (input ("> Ingrese un número entero: "))
    
if un_numero > 0: 
     print (F" --> El Número '{un_numero}' es Positivo ✔")
elif un_numero < 0:
     print (F"--> El Número '{un_numero}' es Negativo ✔")    
else:
     print ("--> El Número Ingresado es Cero ✔" ) 
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 4.
"""
     4. Escribe un programa que muestre los números del 1 al 10 utilizando un bucle `for`.
"""
print("--> Se Muestran Números del 1 al 10 usando 'for':")
for i in range(1, 11): 
    print("- ",i)
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 5.
"""
    5. Escribe un programa que calcule la suma de los números del 1 al 100 utilizando un bucle `while`.
"""
print("--> Se Muestran Suma de Números del 1 al 100 usando 'while':")
x = 1
suma_while = 0
print (" ✨ Números que se recorren: ")
while x <= 100:
    print(F" > {x}")
    suma_while = suma_while + x
    # x = x + 1
    x += 1
      
print (F"\n --> El Resultado de La Suma es: {suma_while} ✔") 
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
## ⏩⏩ EJERCICIO 4: Conjuntos y Diccionarios ⏪⏪
#-------------------------------------------------------------
# 1.
"""
    1. Crea dos conjuntos con algunos números. Luego:
    - Muestra la unión de los dos conjuntos.
    - Muestra la diferencia entre los dos conjuntos.
    - Muestra los elementos comunes en ambos conjuntos.
"""
print ("🔸🔸🔸 CONJUNTOS 🔸🔸🔸")
conjunto_1 = {10, 10, 20, 30, 40, 50}
conjunto_2 = { 60, 70, 80, 90, 100, 10, 20}

print (F" --> Conjunto 1: {conjunto_1}")
print (F" --> Conjunto 2: {conjunto_2} ")

union_conjunto = conjunto_1.union (conjunto_2)
diferencia_1 = conjunto_1.difference(conjunto_2) 
diferencia_2 = conjunto_2.difference (conjunto_1)
diferencia_conjuntos = diferencia_1.union(diferencia_2) 
interseccion_conjuntos = conjunto_1.intersection(conjunto_2)

print (F"\n > La unión de Ambos Conjuntos: {union_conjunto} ✔")
print (F"\n > La diferencia de Ambos Conjuntos: {diferencia_conjuntos} ✔")
print (F"\n > Los elementos Comunes en Ambos Conjuntos: {interseccion_conjuntos} ✔")
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 2.
"""
    2. Crea un diccionario con tres nombres como claves y edades como valores. Luego:
    - Muestra la edad del primer nombre en el diccionario.
    - Añade un nuevo nombre y edad al diccionario.
    - Elimina un nombre del diccionario y muestra el resultado.
    - Muestra todas las claves y todos los valores del diccionario.
"""
print ("🔸🔸🔸 DICCIONARIO NOMBRES 🔸🔸🔸\n")
diccionario = {"Simón": 2, "Erika": 3, "Ramona": 6}
print (diccionario)
print ("\n-> Edad del primer elemento: ", diccionario ["Simón"])

diccionario ["Antonia"] = 10
print (" > Se agrega un nuevo elemento ...")
print ("\n--> Diccionario Actualizado: ", diccionario)

del diccionario ["Ramona"]
print ("\n--> Diccionario Sin Elemento 'Ramona': ", diccionario)
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 3.
"""
    3. Crea un diccionario con los nombres de cinco productos como claves y sus precios como valores. Luego:
    - Muestra el precio de un producto específico.
    - Incrementa el precio de todos los productos en un 10%.
    - Muestra el diccionario actualizado.
"""
print ("🔸🔸🔸 DICCIONARIO PRODUCTOS 🔸🔸🔸\n")
dict_productos = {"Cuaderno": 3000, "Lapicera": 1000, "Corrector": 600, "Resaltador": 800, "Regla": 200}
print (F"Listado Total:\n{dict_productos}")

print ("\n--> El Precio de un Cuaderno es: $", dict_productos["Cuaderno"])

valores = dict_productos.values()
print (F"\n❌ Lista de Precios Anterior: {valores} ❌")

mi_lista = []

for valor in valores:
    aumento = valor * 0.10
    nuevo_valor = int (valor + aumento) 
    mi_lista.append(nuevo_valor)
   
print (F"❗❗ Hay Cambio de Precios ❗❗ ")

nuevos_datos = {"Cuaderno": 3300, "Lapicera": 1000, "Corrector": 660, "Resaltador": 880, "Regla": 220}

dict_productos.update(nuevos_datos)

print (F"\n--> Lista Actualizada: {dict_productos}")
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 4.
"""
    4. Crea un conjunto con los números del 1 al 5 y otro conjunto con los números del 4 al 8. Muestra:
    - La intersección de los dos conjuntos.
    - La diferencia simétrica entre los dos conjuntos.
"""
print ("🔸🔸🔸 CONJUNTOS 🔸🔸🔸")
conjunto_num_1 = {1, 2, 3, 4, 5}
conjunto_num_2 = { 4, 5, 6, 7, 8}

print (F" -> Conjunto 1: {conjunto_num_1}")
print (F" -> Conjunto 2: {conjunto_num_2}")


interseccion = conjunto_num_1.intersection(conjunto_num_2)
print ("\n--> La INTERSECCIÓN de Ambos Conjuntos está dada por los elementos: ", interseccion)

diferencia_a = conjunto_num_1.difference(conjunto_num_2) 
diferencia_b = conjunto_num_2.difference (conjunto_num_1)
diferencias = diferencia_a.union(diferencia_b) 
print ("\n--> La DIFERENCIA de Ambos Conjuntos está dada por los elementos: ", diferencias)
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
## ⏩⏩ EJERCICIO 5: Funciones ⏪⏪
#-------------------------------------------------------------
# 1.
"""
    1. Define una función `saludar(nombre)` que reciba un nombre y muestre un saludo. Luego llama a esta función con tu propio nombre.
"""
print ("🔸🔸🔸 FUNCIONES 🔸🔸🔸\n")
def saludar (nombre):
    print (F"--> Hola {nombre} 💜")

nombre = "Debh"
saludar(nombre)
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 2.
"""
    2. Define una función `suma(a, b)` que reciba dos números y retorne su suma. Luego prueba la función con dos números diferentes.
"""
def suma (a,b):
    return a + b

a = 10
b = 20

print (F" -> {a} + {b} es igual a = {suma (a,b)}")
print ("\n------------------------------------------\n")
#-------------------------------------------------------------
# 3.
"""
    3. Define una función `es_mayor_de_edad(edad)` que reciba una edad y retorne `True` si la edad es mayor o igual a 18 y `False` en caso contrario. Prueba la función con diferentes edades.
"""
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

print ("🔸🔸 ANALIZAMOS SI UD ES MAYOR DE EDAD: ")
edad = int (input ("--> Ingrese Su Edad: "))
print (es_mayor_de_edad(edad))
print ("------------------------------------------\n")
print ("\t>>>>>>>>>> FIN <<<<<<<<<<< ")
print ("\n------------------------------------------\n")
