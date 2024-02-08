#Crud es crear, leer, actualizar y eliminar (create, read, update, delete)

numbers=[0,1,2,3,4,5] #crear
print(numbers[0]) #leer 
numbers[-1] = 10 #actualizar
numbers.append(6) #agrega un elemento al final de la lista
numbers.insert(0, 7) #inserta un valor en una posicion definida el primer valor es la posicion y el segundo es lo que vas a agregar
numbers.insert(2,'hola') #no elimina el elemento en esa posicion sino que lod esplaza hacia la derecha
numbers2=[8,9,10]
nuevalista=numbers+numbers2 #fusiona dos listas 
print(nuevalista.index('hola')) #arroja la posicion en la que se encuentra ese parametro 
nuevalista.remove('hola') #elimina ese elemnto de la lista 
nuevalista.pop() #elimina el ultimo elemento de una lista 
nuevalista.pop(5) #elimina el elemento en esa posicion
nuevalista.reverse() #invierte el orden de todos los elementos de la lista
print(nuevalista)
numeros = [1 ,4 , 3, 5]
numeros.sort() #ordena los valores de la lista de menor a mayor solo funciona cuando no hay elementos de tipos distintos
print(numeros)
silabas = ['re','do','la']
silabas.sort() #ordena alfabeticamente, no ordena si tiene elementos de tipos distintos
print(silabas)


