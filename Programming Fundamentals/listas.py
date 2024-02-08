numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
print(type(numeros))

tareas = ['lavar','jugar','cursos']
print(tareas)

tipos = [1, True, 'texto']
print(tipos)

print(numeros[0])
print(tareas[0])
print(tipos[0])

# text = 'Hola'
# text[0] = 'W' # los strings no se pueden cambiar o conmutables pero con una lista si 

tareas[0]= 'ya no hagas nada'
print(tareas)

print(numeros[:3]) #imprimir un rango de valores en la lista
print(True in tipos) #para saber si un elemento se encuentra dentro de esa lista 
print('texto' in tipos)
