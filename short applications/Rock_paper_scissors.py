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
pc_wins= 0
user_wins=0
rounds=1
empates = 0

while over == False:
    print('*' * 10)
    print(' ROUND ', rounds)
    print('*' * 10)
    
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
        empates += 1

    #En caso de elegir piedra
    elif user_option == 'piedra':
        if pc_option == 'tijeras':
            print('Piedra gana a tijeras')
            print('Ganó el usuario')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('ganó la PC')
            pc_wins += 1

    #En caso de elegir papel        
    elif user_option == 'papel':
        if pc_option == 'tijeras':
            print('Tijeras gana a papel')
            print('Ganó el PC')
            pc_wins += 1
        else:
            print('Papel gana a piedra')
            print('ganó el usuario')
            user_wins += 1

    #En caso de elegir tijeras       
    elif user_option == 'tijeras':
        if pc_option == 'papel':
            print('Tijeras gana a papel')
            print('Ganó el usuario')
            user_wins += 1
        else:
            print('Piedra gana a tijeras')
            print('ganó el PC')
            pc_wins += 1
    print('\n')
    print('Así van las cuentas: ')
    print('Victorias del usuario: ', user_wins)
    print('Victorias de la PC: ', pc_wins)
    print('Empates: ', empates)
    print('\n')
    rounds += 1
    confirmation = input ('¿Quieres jugar otra vez? Y/N ')
    confirmation=confirmation.lower()
    while not confirmation in continua:
        confirmation = input ('Elija entre => Y/N ')
        confirmation=confirmation.lower()
    
    if confirmation == 'n':
        over= True
        if user_wins > pc_wins:
            print('*' * 35)
            print('El usuario es el ganador esta vez')
            print('*' * 35)
        elif user_wins < pc_wins:
            print('*' * 30)
            print('El PC es el ganador esta vez')
            print('*' * 30)
        else:
            print('*' * 20)
            print('Es un rotundo empate')
            print('*' * 20)
            
            

            
        

    




