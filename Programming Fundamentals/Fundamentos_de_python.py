#-------------------------- Funciones más básicas de python ---------------------------------------
#print ("Mi primer mensaje en python será: ¡Obtendré todo lo que me proponga!") 
#print (12+5-8*5/2) #puedes usar el print con valores numéricos y operaciones matemáticas.

"""
Esto es 
un comentario
de varias líneas
"""
#------------------------------- TIPOS DE DATOS -----------------------------------------------------
# my_name = "Michael"  #String
# my_name = 'Michael'  #String con comillas simples funciona igual
# my_age = 12          #Variable tipo Int

# print(type(my_name),type(my_age)) #imprime el tipo de la variable

#-----------------------------  CLASE SOBRE VARIABLES  --------------------------------------------

# my_name = "Michael" #Variables tipo string 
# print(my_name) #Imprime el nombre 
# my_age = 28 #Variables tipo int
# print(my_age) #imprime la edad
# #Puedes cambiar el valor de una variable por otro, pero si hay una linea anterior que imprima ese valor desactualizado, lo hará antes de ser cambiado
# my_name = "William"
# print("Aquí cambió el nombre a: ", my_name)

# #Función input para ingresar valores de variables por teclado
# my_name = input("¿Cuál es tu nombre?")
# print("Usando input tu nombre es: ", my_name)

#--------------------------------- TRANSFORMACIÓN DE TIPOS ------------------------------------------

# print("Mi edad es " + str(my_age)) #transformacción con la función str de un entero a una cadena de texto, no puedes concatenar un entero con un string
# print(f"Mi edad es {my_age}") #transformación más directa 

# #Introducir un valor desde el terminal 
# age=input("Escribe tu edad => ")
# age=int(age) #tranformación de un string a un int 
# age += 10
# print(f"Tu edad en 10 años será {age}" )

#-------------------------------- Ejercicio 1 ------------------------------------
# name = "Michael"
# print(name)
# age = "12"
# print(age)
# total = int(age) +10


# template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años"
# print(template)

#----------------------------------- Operadores aritmeticos  --------------------------------

# print(10+10)
# print(10-10)
# print(5*2)
# print(10/2)
# print(10 // 3) # solo toma el entero en la división
# print (10 % 2) #modulo, muestra el residuo 
# print (2 ** 3) #potenciación 2 elevado a 3


# print("hola"+" mundo")
# print(" hola" * 5)


#-------------------------------- Operadores de comparación ------------------------------------

# print(10 > 3) #mayor que 
# print(10 < 3) #menor que 
# print(5>=5) #mayor o igual que
# print(5<=5) #menor o igual que 
# print(5.0000000001 == 5) #exactamente igual.... aquí es false
# print(5.000001 != 5) #operador diferente
# print("Apple" == "apple") #falso porque el ascii de la A no es el mismo que el ascii de la a 
# print("1" == 1) #falso porque tienen tipos de datos distintos
# age = 17
# print(age >= 18) #no lo dejo entrar porque es menor de edad.


#-------------------------------- comparando flotantes -------------------------------------------

# x = 3.3
# y = 1.1 + 2.2
# print(x)
# print(y)
# print(x == y) # no es igual por la precision decimal 1.1 +2.2 es 3.30000000000003


# #si quieres que sean iguales como string 
# y_str = format(y, ".2g") #transforma la precision a 2 digitos y lo convierte a str
# print(type(y_str))
# print(y_str == str (x))


# #si quieres que sean iguales de forma matematica

# tolerance = 0.000001 #definimos una tolerancia para que si el resutado es menor que ese entonces son iguales 
# print(abs(x-y)< tolerance) # aquí lo restamos y si la tolerancia es más grnade entonces los dos numeros son iguales


#------------------------------------- operadores lógicos --------------------------------------
# #operador y 
# print("1 y 1 es: ", True and True) 
# print(10 > 5 and 6 < 10) #true ambas se cumplen

# #programa para determinar si el stock se encuentra dentro de un rango
# stock =input("ingrese el numero en stock: ")
# stock = int(stock)
# print(stock >= 100 and stock <= 1000)

# #operador O
# print("1 o 0 es: ", True or False) 
# print(10<5 or 9>8) #con una que sea verdadera basta 

# #programa para probar el operador or 
# role=input("digita el valor: ")
# print(role == "admin" or role == "seller")

#Operador not 
# print(not True)
# #tambien puedes usarlo para negar un operador 
# print("El opuesto de AND en 1 y 1 es: ", not (True and True))
#ahora usando el programa de stocks encontraremos lo que está fuera de ese rango
# stock =input("ingrese el numero en stock: ")
# stock = int(stock)
# print(not(stock >= 100 and stock <= 1000)) #saldrá true si está fuera del rango 100 a 1000


#---------------------------- CONDICIONALES ------------------------------------------------

#if
# if True:
#     print('Debería ejecutarse')
    
# if False:
#     print('Esto no debería aparecer...')

'''
pet = input('¿Cuál es tu mascota favorita? ')
if pet == 'perro':
    print('genial')
if pet == 'gato':
    print('ya valiste')
'''

'''
stock = int(input('Digita el stock => '))
if stock >= 100 and stock <= 1000:
    print('El stock entra en el rango deseado')
else:
    print('El stock no se encuentra en el rango')
'''

'''
pet = input('¿Cuál es tu mascota favorita? ')
if pet == 'perro':
    print('genial')
elif pet == 'gato':    #es un else if
    print('ya valiste')
elif pet == 'pez':
    print('Aburrido')
else:
    print('No tienes la mascota que se encuentran en mi lista..')
'''    

# Código para saber si un número es par o impar
# number = int(input('Ingresa un número para saber si es par o impar: '))
# if number % 2 == 0:
#     print('el número es par')
# else:
#     print("El número es impar")









