#------------------------- Versión 1 para piedra papel o tijera  -----------------------------------
'''
user_option=input('Elige => Piedra, papel o tijeras: ')
user_option=user_option.lower() #evito que por las mayusculas no las reconozca
pc_option='tijeras'  # opción de computador para siempre 

#Caso de Empate
if user_option == pc_option:
    print('Empate')

#En caso de elegir piedra
elif user_option == 'piedra':
    if pc_option == 'tijeras':
        print('Piedra gana a tijeras')
        print('Ganó el usuario')
    else:
        print('Papel gana a piedra')
        print('ganó la PC')

#En caso de elegir papel        
elif user_option == 'papel':
    if pc_option == 'tijeras':
        print('Tijeras gana a papel')
        print('Ganó el PC')
    else:
        print('Papel gana a piedra')
        print('ganó el usuario')

#En caso de elegir tijeras       
elif user_option == 'tijeras':
    if pc_option == 'papel':
        print('Tijeras gana a papel')
        print('Ganó el usuario')
    else:
        print('Piedra gana a tijeras')
        print('ganó el PC')
'''

 #------------------------------------ Versión 2 añadiendo tuplas y quitandole la opción al usuario de escribir lo que desea -------------------------------

'''
import random  #importa la función random al código

options = ('piedra', 'papel', 'tijeras') 
user_option=input('Elige => Piedra, papel o tijeras: ')
user_option=user_option.lower() #evito que por las mayusculas no las reconozca

#eliminando las pendejadas que escribe el usuario: 
if not user_option  in options:  #aqui preguntamos si lo que escribe el usuario no está dentro de mis opciones pues que lo mande a la gaver
    print('¿Qué le pasa, acaso es estúpido? xd')


pc_option= random.choice(options)  # añadiendo aleatoriedad con la funcion random que elije algo al azar de la tupla o lista

print('opción del usuario: ', user_option)
print('opción del pc: ', pc_option)

#Caso de Empate
if user_option == pc_option:
    print('Empate')

#En caso de elegir piedra
elif user_option == 'piedra':
    if pc_option == 'tijeras':
        print('Piedra gana a tijeras')
        print('Ganó el usuario')
    else:
        print('Papel gana a piedra')
        print('ganó la PC')

#En caso de elegir papel        
elif user_option == 'papel':
    if pc_option == 'tijeras':
        print('Tijeras gana a papel')
        print('Ganó el PC')
    else:
        print('Papel gana a piedra')
        print('ganó el usuario')

#En caso de elegir tijeras       
elif user_option == 'tijeras':
    if pc_option == 'papel':
        print('Tijeras gana a papel')
        print('Ganó el usuario')
    else:
        print('Piedra gana a tijeras')
        print('ganó el PC')
'''

 #------------------------------------ Versión 3 haciendo que se repita el juego  -------------------------------

import random  #importa la función random al código
over= False
confirmation = 'y'

while over == False:
    options = ('piedra', 'papel', 'tijeras') 
    continua = ('y','n')
    user_option=input('Elige => Piedra, papel o tijeras: ')
    user_option=user_option.lower() #evito que por las mayusculas no las reconozca

    #eliminando las pendejadas que escribe el usuario: 
    while not user_option  in options:  #aqui preguntamos si lo que escribe el usuario no está dentro de mis opciones pues que lo mande a la gaver
        print('Esa opción no existe')
        user_option=input('Elige => Piedra, papel o tijeras: ')
        user_option=user_option.lower() #evito que por las mayusculas no las reconozca

    pc_option= random.choice(options)  # añadiendo aleatoriedad con la funcion random que elije algo al azar de la tupla o lista

    print('opción del usuario: ', user_option)
    print('opción del pc: ', pc_option)

    #Caso de Empate
    if user_option == pc_option:
        print('Empate')

    #En caso de elegir piedra
    elif user_option == 'piedra':
        if pc_option == 'tijeras':
            print('Piedra gana a tijeras')
            print('Ganó el usuario')
        else:
            print('Papel gana a piedra')
            print('ganó la PC')

    #En caso de elegir papel        
    elif user_option == 'papel':
        if pc_option == 'tijeras':
            print('Tijeras gana a papel')
            print('Ganó el PC')
        else:
            print('Papel gana a piedra')
            print('ganó el usuario')

    #En caso de elegir tijeras       
    elif user_option == 'tijeras':
        if pc_option == 'papel':
            print('Tijeras gana a papel')
            print('Ganó el usuario')
        else:
            print('Piedra gana a tijeras')
            print('ganó el PC')
    
    confirmation = input ('¿Quieres jugar otra vez? Y/N ')
    confirmation=confirmation.lower()
    while not confirmation in continua:
        confirmation = input ('Elija entre => Y/N ')
        confirmation=confirmation.lower()
    
    if confirmation == 'n':
        over= True
        

    




