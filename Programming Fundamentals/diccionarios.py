#tienen una llave o unkey y una definición o valor 
'''
diccionario = {
    'name': 'Michael',
    'apellido': 'Quintana',
    'edad': 28
}

print(diccionario)
print(len(diccionario)) #saber cuantos elementos hay ene le diccionario 

print(diccionario['edad']) #Ya no pregunto por la posición si no que utilizo una llave para obtener el valor
print(diccionario.get('edad')) #tambipen puedo utilizar get para hacer lo mismo
print(diccionario.get('un elemento que no está en el diccionario')) # la diferencia esque si no está no saltará error si no que pondrá None como respuesta

#también podemos evitar ese error si primero validamos con el in si es que ese elemento no está ene el diccionario 
print('name' in diccionario)  # true
print('otrooo' in diccionario) #false
'''

personas = {
    'name': 'Michael',
    'apellido': 'Quintana',
    'edad': 28,
    'lenguajes': ['Python', 'Html', 'C'],
    'random': 2
}
print(personas)

personas['name'] = 'MICHAEL'  #perimite reemplazar un valor
personas['edad'] =- 10 #podemos restar también dentro 
personas['lenguajes'].append('JS') #también podemos añadir elementos a las listas que están dentro 
del personas ['apellido'] #También podemos eliminar ese atributo
personas.pop('random') #también puede eliminar un elemento con pop 
personas['algo'] = 'algo' #puedes añadir a un diccionario más keys y más valores según gustes
print(personas)


#podemos imprimir por separado los items, keys y valores de los diccionarios
print('items')
print(personas.items())
print('keys')
print(personas.keys())
print('values')
print(personas.values())


