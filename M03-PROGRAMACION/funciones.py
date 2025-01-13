import os
import random
import string

from parametros import *
from datos import *
from playGame import *

def clearScreen() -> None:
    '''Limpiamos la pantalla de la terminal.

    Retorna: No retorna nada'''
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

def setCarddeck(esp=True):
    '''Genera el contenido de la variable "cartas". Por defecto es baraja española; si el parámetro es False,
    iniciamos una baraja de poker.'''
    if esp:
        palos = ['Bastos', 'Espadas', 'Copas', 'Oros']
        nCartas = 12
    else:
        palos = ['Tréboles', 'Picas', 'Corazones', 'Diamantes']
        nCartas = 13

    numeros = []
    for n in range(1, nCartas + 1):
        numeros.append(n)

    for priority, palo in enumerate(palos):
        for n in numeros:
            clave = palo[0] + f'{n:02}'
            cartas[clave] = {}

            if n == 1:
                tmp = 'Uno'
            elif n == 2:
                tmp = 'Dos'
            elif n == 3:
                tmp = 'Tres'
            elif n == 4:
                tmp = 'Cuatro'
            elif n == 5:
                tmp = 'Cinco'
            elif n == 6:
                tmp = 'Seis'
            elif n == 7:
                tmp = 'Siete'
            elif n == 8:
                tmp = 'Ocho'
            elif n == 9:
                tmp = 'Nueve'
            elif n == 10:
                tmp = 'Diez'
            elif n == 11:
                tmp = 'Once'
            elif n == 12:
                tmp = 'Doce'
            elif n == 13:
                tmp = 'Trece'

            cartas[clave]['literal'] = f'{tmp} de {palo}'

            if n >= 8:
                cartas[clave]['value'] = 0.5
            else:
                cartas[clave]['value'] = n

            cartas[clave]['priority'] = priority + 1

            cartas[clave]['realValue'] = n

def invalidInput():
    print('INVALID OPTION'.center(lineSize, '='))
    _ = input('Press enter to continue'.center(lineSize))

def menuPrincipal():
    '''Menú principal del juego. Para que empiece la partida, debe haber mínimo 2 jugadores
    y hay que escoger una baraja de cartas (en Settings).'''
    validInputs = (1,2,3,4,5,6)
    options = (
        '1) Add/Remove/Show Players',
        '2) Settings',
        '3) Play Game',
        '4) Ranking',
        '5) Reports',
        '6) Exit')
    while True:
        clearScreen()
        print('MENÚ PRINCIPAL'.center(lineSize))
        for option in options:
            print(initialString + option.ljust(lineSize - lineStart))
        userInput = input(initialString + 'Option: ')
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput in validInputs:
                break
        invalidInput()
        
    if userInput == 1:
        addRemovePlayers()
    elif userInput == 2:
        settings()
    elif userInput == 3: # Falta poner condiciones necesarias para que el juego pueda comenzar (2 jugadores min, baraja...)
        playGame()
    elif userInput == 4:
        ranking()
    elif userInput == 5:
        reports()
    elif userInput == 6:
        quit

def getOpt(textOpts="", inputOptText="", rangeList=[], exceptions=[]):
    '''Función para la gestión de menús. Le pasamos un texto, que nos mostrará un menú,
un rango de opciones válidas, y una lista de excepciones, y nos devuelve la opción
elegida por el usuario'''

def orderPlayersByPoints(listaJugadores):
    '''Función que ordena los jugadores según sus puntos.'''

def chanceExceedingSevenAndHalf(id, mazo):
    '''Función que calcula la probabilidad de pasarse de siete y medio'''

def printPlayerStats(id):
    '''Esta función nos muestra los stats de un jugador humano.
name Mario
type 40
human True
bank True
initialCard E11
priority 3
bet 8
points 20
cards C07
roundPoints 0'''

def logToFile(text):
    '''Esta función nos puede servir para enviar mensajes de texto al archivo
“logFileSevenAndHalf”, que puede sernos útil a modo de debug.
    
    f = open("logfileSevenAndHalf.txt", "a")
    f.write(text)
    f.close()'''

def baknOrderNewCard(id, mazo):
    '''Función que evalúa si la banca pedirá una nueva carta.'''

def newPlayer(dni, name, profile, human):
    '''Función que devuelve una tupla con dos elementos, el primero es el dni del nuevo
jugador, el segundo, un diccionario con las claves: name, human, bank, initialCard,
priority, type, bet, points, ards, roundPoints'''

def addRemovePlayers():
    '''Función que nos muestra el menú despues de escoger la opción 1 del menu principal:
1)New Human Player
2)New Boot
3)Show/Remove Players
4)Go back
Option:'''
    validInputs = (1,2,3,4)
    options = (
        '1) New Human Player',
        '2) New boot',
        '3) Show/Remove Players',
        '4) Go back')
    while True:
        clearScreen()
        print('ADD/REMOVE/SHOW PLAYERS'.center(lineSize))
        for option in options:
            print(initialString + option.ljust(lineSize - lineStart))
        userInput = input(initialString + 'Option: ')
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput in validInputs:
                break
        invalidInput()

    if userInput == 1:
        setNewPlayer()
    elif userInput == 2:
        setNewPlayer(False)
    elif userInput == 3:
        removeBBDDPlayer()
    elif userInput == 4:
        menuPrincipal()

def settings():
    '''Función que gestiona el menú settings, donde podemos establecer los jugadores que
participarán en una partida, la baraja con la que se va a jugar y el número máximo de
rondas.'''

def setMaxRounds():
    '''Función que pide al usuario el número de rondas de la siguiente partida y lo establece
en el diccionario contextGame, contextGame[“maxRounds”]'''

def newRandomDNI():
    '''Función que devuelve un dni válido con números aleatorios'''
    dni = ''
    for i in range(8):
        dni += str(random.randint(0,9))
    dni += random.choice(string.ascii_letters).upper()
    return dni

def setNewPlayer(human=True):
    '''Función que gestiona la creación de un nuevo jugador que insertaremos en la BBDD'''
    clearScreen()
    if human:
        print('NUEVO JUGADOR HUMANO'.center(lineSize))
    else:
        print('NUEVO BOT'.center(lineSize))

    name = input('Name: ')

    if human:
        nif = input('NIF: ')
    else:
        nif = newRandomDNI()

    validInputs = [1,2,3]
    while True:
        print('Select your Profile:')
        print('1)Cautios')
        print('2)Moderated')
        print('3)Bold')
        userInput = input('Option: ')
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput in validInputs:
                break
        invalidInput()

    if userInput == 1:
        profile = 'Cautios'
    elif userInput == 2:
        profile = 'Moderated'
    elif userInput == 3:
        profile = 'Bold'

    while True:
        userInput = input('Is ok? Y/n: ')
        if userInput.lower() == 'y':
            newPlayer(nif, name, profile, human)
        elif userInput.lower() == 'n':
            break
        else:
            print('Error, introduce un input válido.')

    addRemovePlayers()

def showhPlayersGame():
    '''Función que muestra los jugadores seleccionados cuando estamos añadiendo
jugadores a la partida. (Hay una foto en el PDF que muestra cómo debería quedar)'''

def setPlayersGame():
    '''Función para establecer los jugadores que conformarán la partida siguiente'''

def removeBBDDPlayer():
    '''Función que nos muestra los jugadores disponibles en BBDD, y elimina el que
seleccionemos'''

def printStats(idPlayer="", titulo=""):
    '''Esta función nos imprime los stats de todos los jugadores de la partida.
    (Hay una foto en el PDF que muestra cómo debería quedar)'''

def reports():
    '''Función que nos muestra el menú de reportes, y una vez elegida una opción, el reporte
correspondiente'''

def getPlayers():
    '''Función que extrae los jugadores definidos en la BBDD y los almacena en el diccionario
contextGame[“players”]'''

def setCardsDeck():
    '''Elegimos una baraja, y a partir de esa baraja, establecemos el diccionario de cartas
contextGame["cards_deck"]'''

def savePlayer(nif,name,risk,human):
    '''Función que guarda en BBDD un nuevo jugador.'''

def delBBDDPlayer(nif):
    '''Función que elimina un jugador de la BBDD'''

def getGameId():
    '''Función que devuelve un id no existente en la tabla cardgame.'''

def getBBDDRanking():
    '''Función que crea la vista player_earnings, y retorna un diccionario con los datos de
ésta,
player_id | earnings | games_played | minutes_played.'''

def ranking():
    '''Función que muestra el menú del ranking y el ranking según la opción elegida'''

def returnListRanking(field="earnings"):
    '''Función que retorna una lista con los id de jugadores del diccionario que retorna la
función getBBDDRanking(), ordenados según la opción del ranking elegida'''