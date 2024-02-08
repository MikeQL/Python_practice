#Una tupla es lo mismo que una lista pero con parentesis 

numeros= (1,2,3,4,5)
strings=('hola', 'me', 'llamo', 'Michael', 'me')
print(numeros)
print(strings)

print('posición 0 de la tupla números: ', numeros[0])


#En laas tuplas no se pueden insertar más elementos ni editarlos, solo se puede hacer CRD no el update
#pero si podemos hacer lo siguiente: 
print(strings.index('me')) #podemos saber la posición de un elemento
print(strings.count('me')) #conocer cuantas veces está ese elemento en la tupla 

mi_lista= list(strings) #cambiar el tipo tupla a lista 
print(mi_lista)
#ahora si podemos trabajar con todas las acciones de una lista 
mi_lista[-1] = '!'
print(mi_lista)
#para cambiar de una lista a una tupla tenemos 
strings = tuple(mi_lista)
print(strings)

