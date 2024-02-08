text = 'Sé programar en python'
'''
print ('Javascript' in text ) # Evalua si una cadena se encuentra dentro del texto
print ('python' in text) #Este es True

if 'phyton' in text:
    print('Si se encuentra')
else:
    print('La palabra no se encuentra en el texto')
'''

''' 
size= len('amor') #para saber el número de caracteres tiene un texto 
print(size)

print(text)
print(text.upper()) #pasa todo a mayúsculas
print(text.lower()) #pasa todo a minúsculas
print(text.count('a')) #cuantas veces se repite un caracter
print(text.swapcase()) #cambia las mayusculas por minusculas y viceversa
print(text.startswith('Sé')) #analiza si empieza por esa cadena 
print(text.endswith('thon')) #analiza si termina por esa cadena 
print(text.replace('python','Go')) #reemplaza una palabra por otra

text2= 'este es un título'
print(text2)
print(text2.capitalize()) #cambia la primera letra a mayúsculas
print(text2.title()) #cambia cada inicio de la palabra a mayúsculas 
print(text2.isdigit()) #Nos dice si el texto es un dígito
print('398'.isdigit()) #Aquí por ejemplo sabemos que aunque es un string si es un dígito
'''


'''
#----------------------------- INDEXING -----------------------------------------------
# los textos tienen un indicador que funcionan con posiciones

text='Michael sabe python'
print(text[0]) #me refleja el valor del primer caracter
print(text[-1]) #me refleja el último caracter del string
print(text[len(text)-1]) #esta es otra forma de conseguir el último caracter

#------------------------------- Slicing ----------------------------------------------
#sacar varias partes del texto 

print(text[0:7])
print(text[:7]) #esta es otra forma de tomar lo mismo pero en una forma abreviada para no escribir el 0
print(text[5:-1]) #no incluye el último caracter
print(text[5:]) #esto si incluye el final 
print(text[:]) #imprime todo
print(text[0:7:2]) #va a tomar la primera letra luego salta una y toma la que esta 2 posiciones despues de esa y así sucesivamente
'''


