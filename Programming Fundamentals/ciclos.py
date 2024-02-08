#------------------- while -------------------------------------- 

# contador = 0
# while contador < 10:
#     contador += 1
#     print(contador)

'''
contador = 0 

while contador < 20:
    contador += 1
    if contador == 15:
        break    #esto es para cortar o parar forzadamente el ciclo
    print(contador)


contador = 0 

while contador < 20:
    contador += 1
    if contador < 15:
        continue    # aquí salta al siguiente ciclo ignorando las lineas de abajo es decir hasta la 15 no se va a ejecutar
    print(contador)
'''



#------------------------------ FOR ----------------------------------------

# for element in range (20):   # este incia en 0 , pero el último valor no entra '20'
#     print (element)
    
# for element in range (1, 20):   # este incia en 1 
#     print (element)
"""
mi_lista= [23,45,67,89,43]
for element in mi_lista:    #recorre los valores de la lista 
    print(element)
    
mi_tupla=('michael', 'william', 'quintana','lopez')

for element in mi_tupla:
    print(element)
""" 
""" 
productos = {
    'nombre':'Pantalon',
    'Precio':100,
    'stock':89
}


for element in productos:  #Aquí imprime solo las keys 
    print(element)
    
for key in productos:  #Aquí si imprime los valores de esas keys
    print(key, '=>', productos[key])
    
for key, value in productos.items(): #otra forma de hacer lo de arriba es recorriendo y transformando en tupla 
    print(key, '=>', value)
""" 



""" 
#Haremos una lista de diccionarios     
personas = [
    {
        'name': 'Michael',
        'edad': 28
    },     
    {
       'name': 'Agustin',
        'edad': 26 
    },
    {
         'name': 'William',
        'edad': 27
    }
]

for persona in personas:   #Aquí imprimimos los diccionarios que estan dentro de esa lista 
    print(persona)
    
    
for persona in personas:   #Aquí imprimimos uno de los valores dentro de esos diccionarios, como el nombre en este caso 
    print('El nombre de la persona en esa posicion de lista es: ', persona['name'])
"""


#----------------------------- CICLOS ANIDADOS ------------------------------------------
#esta es una lista de istas como con filas y columnas 
matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ] 

print(matriz[0])  #me devuelve la lista que está en la posición 0 

print(matriz[0][1]) #me devuelve el elemento en la posición 1 de la matriz 0 e decir el '2' como si fueran coordenadas o igual fila y columna 

#recorremos cada uno de los elementos de las sublistas
for fila in matriz:
    for columna in fila:
        print(columna)
 