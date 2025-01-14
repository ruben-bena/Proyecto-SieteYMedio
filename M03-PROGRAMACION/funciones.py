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

def mainMenu():
    '''Menú principal del juego. Para que empiece la partida, debe haber mínimo 2 jugadores
    y hay que escoger una baraja de cartas (en Settings).'''
    inputOptMainMenu = (
        '1) Add/Remove/Show Players',
        '2) Settings',
        '3) Play Game',
        '4) Ranking',
        '5) Reports',
        '6) Exit')
    validInputsMainMenu = (1,2,3,4,5,6)
    
    userInput = getOpt(strMainMenu, inputOptMainMenu, validInputsMainMenu)
        
    if userInput == 1:
        addRemovePlayers()
    elif userInput == 2:
        settings()
    elif userInput == 3:
        # TODO Poner condiciones necesarias para que el juego pueda comenzar (2 jugadores min, elegir baraja...)
        playGame()
    elif userInput == 4:
        ranking()
    elif userInput == 5:
        reports()
    elif userInput == 6:
        quit

def getOpt(textOpts="", inputOptText=[], rangeList=[], inputName='', errorName=''):
    '''Función para la gestión de menús.

    textOpts es un string que será el encabezado.
    inputOptText es un array de strings, que representarán las opciones que puede escoger el usuario.
    rangeList es un array que contiene las opciones válidas de input, ya sean números o strings.
    inputName es el nombre del input que pedimos al usuario.
    errorName es el mensaje de error que damos cuando el input es inválido.
    '''
    while True:

        # Imprimimr texto en pantalla
        clearScreen()
        print('~' * lineSize)
        print('')
        print(textOpts.center(lineSize))
        print('')
        print('~' * lineSize)
        print('')
        for option in inputOptText:
            print(initialString + option.ljust(lineSize - lineStart))
        
        # Pedir input
        inputText = 'Option'
        if inputName != '':
            inputText = inputName
        userInput = input(initialString + inputText + ': ')
        if userInput.isdigit():
            userInput = int(userInput)
        if userInput in rangeList or rangeList == []:
            break
        else:
            errorName = 'INVALID OPTION'
            if errorName != '':
                errorName = errorName
            print('INVALID OPTION'.center(lineSize, '='))
            _ = input('Press enter to continue'.center(lineSize))
    
    return userInput

def orderPlayersByPoints(listaJugadores):
    '''Función que ordena los jugadores según sus puntos.'''
    pass

def chanceExceedingSevenAndHalf(id, mazo):
    '''Función que calcula la probabilidad de pasarse de siete y medio'''
    pass

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
    pass

def logToFile(text):
    '''Esta función nos puede servir para enviar mensajes de texto al archivo
“logFileSevenAndHalf”, que puede sernos útil a modo de debug.
    
    f = open("logfileSevenAndHalf.txt", "a")
    f.write(text)
    f.close()'''
    pass

def baknOrderNewCard(id, mazo):
    '''Función que evalúa si la banca pedirá una nueva carta.'''
    pass

def newPlayer(dni, name, profile, human):
    '''Función que devuelve una tupla con dos elementos, el primero es el dni del nuevo
jugador, el segundo, un diccionario con las claves: name, human, bank, initialCard,
priority, type, bet, points, ards, roundPoints'''
    # TODO Arreglar función. No sé qué valores por defecto debo darle a algunos campos.
    player = (dni, {
        'name':name,
        'human': human,
        'bank': False,
        'initialCard': '',
        'priority': '',
        'type': profile,
        'bet': '',
        'points': 20,
        'ards': '',
        'roundPoints': ''})
    return player

def addRemovePlayers():
    '''Función que nos muestra el menú despues de escoger la opción 1 del menu principal:
1)New Human Player
2)New Boot
3)Show/Remove Players
4)Go back
Option:'''
    inputOptAddRemovePlayers = (
        '1) New Human Player',
        '2) New boot',
        '3) Show/Remove Players',
        '4) Go back')
    validInputsAddRemovePlayers = (1,2,3,4)
    
    userInput = getOpt(strAddRemovePlayers, inputOptAddRemovePlayers, validInputsAddRemovePlayers)

    if userInput == 1:
        setNewPlayer()
    elif userInput == 2:
        setNewPlayer(False)
    elif userInput == 3:
        removeBBDDPlayer()
    elif userInput == 4:
        mainMenu()

def settings():
    '''Función que gestiona el menú settings, donde podemos establecer los jugadores que
participarán en una partida, la baraja con la que se va a jugar y el número máximo de
rondas.'''
    inputOptSettings = (
        '1) Set Game Players',
        "2) Set Card's Deck",
        '3) Set Max Rounds (Default 5 Rounds)',
        '4) Go Back'
    )
    validInputsSettings = (1,2,3,4)

    userInput = getOpt(strSettings, inputOptSettings, validInputsSettings)

    if userInput == 1:
        setPlayersGame()
    elif userInput == 2:
        selectCardsDeck()
    elif userInput == 3:
        setMaxRounds()
    elif userInput == 4:
        mainMenu()

def selectCardsDeck():
    '''Menú en el que se escoge qué baraja se utilizará durante la partida.'''
    inputOptSeletCardsDeck = (
        '1) ESP',
        '2) POK',
        '3) Go Back'
    )
    validInputSelectCardsDeck = (1,2,3)

    userInput = getOpt(strSetCardsdeck, inputOptSeletCardsDeck, validInputSelectCardsDeck)

    if userInput == 1:
        esp = True
        baraja = 'ESP, Baraja Española'
    elif userInput == 2:
        esp = False
        baraja = 'POK, Baraja de Poker'
    elif userInput == 3:
        settings()
    setCardsDeck(esp)
    print(initialString + f'Established Card Deck {baraja}')
    _ = input(initialString + 'Enter to continue'.ljust(lineSize - lineStart))
    settings()

def setMaxRounds():
    '''Función que pide al usuario el número de rondas de la siguiente partida y lo establece
en el diccionario contextGame, contextGame[“maxRounds”]'''
    pass

def newRandomDNI():
    '''Función que devuelve un dni válido con números aleatorios'''
    dni = ''
    for i in range(8):
        dni += str(random.randint(0,9))
    dni += random.choice(string.ascii_letters).upper()
    return dni

def validName(name):
    '''Retorna True si un nombre de jugador es válido.
    Un nombre es válido si sólo contiene letras y números, y no es un string vacío.'''
    if name is '':
        return False
    for letter in name:
        esLetra = letter in string.ascii_letters
        esNumero = letter in '0123456789'
        if not esLetra and not esNumero:
            return False
    return True

def validDNI(dni):
    '''Retorna True si un DNI es válido.
    Un DNI es válido si contiene 8 números seguidos de una letra mayúscula, y no está repetido en la BBDD'''
    if len(dni) != 9:
        return False
    elif not dni[:-1].isdigit():
        return False
    elif not dni[-1] in string.ascii_uppercase:
        return False
    
    #TODO Comprobar si el DNI está en la BBDD
    
    return True

def setNewPlayer(human=True):
    '''Función que gestiona la creación de un nuevo jugador que insertaremos en la BBDD'''

    # Definir encabezado en función del tipo de jugador
    strNewPlayer = strNewHumanPlayer
    if not human:
        strNewPlayer = strNewBotPlayer

    # Pedir nombre
    while True:
        name = getOpt(strNewPlayer, inputOptText=[], rangeList=[], inputName='Name')
        if validName(name):
            break
        _ = input('Invalid name! Only characters and numbers allowed\nEnter to Continue')

    # Pedir DNI
    if human:
        while True:
            dni = getOpt(strNewPlayer, inputOptText=[f'name = {name}'], rangeList=[], inputName='DNI')
            if validDNI(dni):
                break
            _ = input('Invalid DNI! 8 letters and 1 number required\nEnter to Continue')
    else:
        dni = newRandomDNI()

    # Pedir perfil de riesgo
    inputOptProfile = (
        f'name = {name}',
        f'DNI = {dni}',
        '',
        'Select your Profile:',
        '1) Cautios',
        '2) Moderated',
        '3) Bold'
    )
    validInputsProfile = [1,2,3]
    userInput = getOpt(strNewPlayer, inputOptProfile, validInputsProfile)
    if userInput == 1:
        profile = 'Cautios'
    elif userInput == 2:
        profile = 'Moderated'
    elif userInput == 3:
        profile = 'Bold'

    # Confirmar jugador
    inputOptPlayerData = (
        f'name = {name}',
        f'DNI = {dni}',
        f'Profile = {profile}'
    )
    userInput = getOpt(strNewPlayer, inputOptPlayerData, rangeList=['y','Y','n','N'], inputName='Is ok? Y/n')
    if userInput.lower() == 'y':
        #TODO Guardar al jugador en la BBDD
        #TODO Guardar al jugador en la partida actual
        pass

    # Volver al menú anterior
    addRemovePlayers()

def showPlayersGame():
    '''Función que muestra los jugadores seleccionados cuando estamos añadiendo
jugadores a la partida. (Hay una foto en el PDF que muestra cómo debería quedar)'''
    pass

def setPlayersGame():
    '''Función para establecer los jugadores que conformarán la partida siguiente'''
    pass

def removeBBDDPlayer():
    '''Función que nos muestra los jugadores disponibles en BBDD, y elimina el que
seleccionemos'''
    pass

def printStats(idPlayer="", titulo=""):
    '''Esta función nos imprime los stats de todos los jugadores de la partida.
    (Hay una foto en el PDF que muestra cómo debería quedar)'''
    pass

def reports():
    '''Función que nos muestra el menú de reportes, y una vez elegida una opción, el reporte
correspondiente'''
    pass

def getPlayers():
    '''Función que extrae los jugadores definidos en la BBDD y los almacena en el diccionario
contextGame[“players”]'''
    pass

def setCardsDeck(esp=True):
    '''Elegimos una baraja, y a partir de esa baraja, establecemos el diccionario de cartas
contextGame["cards_deck"]'''

    # Definir parámetros iniciales en función de la baraja
    if esp:
        palos = ['Bastos', 'Espadas', 'Copas', 'Oros']
        nCartas = 12
    else:
        palos = ['Tréboles', 'Picas', 'Corazones', 'Diamantes']
        nCartas = 13
    numeros = []
    for n in range(1, nCartas + 1):
        numeros.append(n)

    # Generar diccionario baraja
    deck = {}
    for priority, palo in enumerate(palos):
        for n in numeros:
            clave = palo[0] + f'{n:02}'
            deck[clave] = {}

            if n == 1:
                cardinal = 'Uno'
            elif n == 2:
                cardinal = 'Dos'
            elif n == 3:
                cardinal = 'Tres'
            elif n == 4:
                cardinal = 'Cuatro'
            elif n == 5:
                cardinal = 'Cinco'
            elif n == 6:
                cardinal = 'Seis'
            elif n == 7:
                cardinal = 'Siete'
            elif n == 8:
                cardinal = 'Ocho'
            elif n == 9:
                cardinal = 'Nueve'
            elif n == 10:
                cardinal = 'Diez'
            elif n == 11:
                cardinal = 'Once'
            elif n == 12:
                cardinal = 'Doce'
            elif n == 13:
                cardinal = 'Trece'

            deck[clave]['literal'] = f'{cardinal} de {palo}'

            if n >= 8:
                deck[clave]['value'] = 0.5
            else:
                deck[clave]['value'] = n

            deck[clave]['priority'] = priority + 1

            deck[clave]['realValue'] = n
    
    context_game["cards_deck"] = deck

def savePlayer(nif,name,risk,human):
    '''Función que guarda en BBDD un nuevo jugador.'''
    pass

def delBBDDPlayer(nif):
    '''Función que elimina un jugador de la BBDD'''
    pass

def getGameId():
    '''Función que devuelve un id no existente en la tabla cardgame.'''
    pass

def getBBDDRanking():
    '''Función que crea la vista player_earnings, y retorna un diccionario con los datos de
ésta,
player_id | earnings | games_played | minutes_played.'''
    pass

def ranking():
    '''Función que muestra el menú del ranking y el ranking según la opción elegida'''
    pass

def returnListRanking(field="earnings"):
    '''Función que retorna una lista con los id de jugadores del diccionario que retorna la
función getBBDDRanking(), ordenados según la opción del ranking elegida'''
    pass