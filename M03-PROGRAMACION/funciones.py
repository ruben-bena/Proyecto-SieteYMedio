import os
import random
import string
from parametros import *
from datos import *

def clearScreen() -> None:
    '''Limpiamos la pantalla de la terminal.

    Retorna: No retorna nada'''
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

def generarBaraja():
    numeros = []
    for n in range(1,13):
        numeros.append(n)
    palos = ['Bastos', 'Espadas', 'Copas', 'Oros']

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
                tmp = 'Sota'
            elif n == 11:
                tmp = 'Caballo'
            elif n == 12:
                tmp = 'Rey'
            cartas[clave]['literal'] = f'{tmp} de {palo}'

            if n >= 8:
                cartas[clave]['value'] = 0.5
            else:
                cartas[clave]['value'] = n

            cartas[clave]['priority'] = priority + 1

            cartas[clave]['realValue'] = n

def validaInput(inputUsuario, posiblesInputs):
    if inputUsuario not in posiblesInputs:

        print('INVALID OPTION'.center(lineSize, '='))
        _ = input('Press enter to continue'.center(lineSize))
        return False
    return True

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
        validOption = validaInput(userInput, validInputs)
        if validOption:
            break

    if userInput == 1:
        addRemovePlayers()
    elif userInput == 2:
        settings()
    elif userInput == 3: # Falta poner condiciones para que el juego pueda comenzar
        playGame()
    elif userInput == 4:
        ranking()
    elif userInput == 5:
        reports()
    elif userInput == 6:
        quit



        
def playGame():
    '''Esta es la función principal del proyecto. Una vez establecido el número de rondas, la
    baraja con la que se va a jugar, y los jugadores que participan en la partida, ésta será
    la función que gestione toda la partida. Para ello, hará uso de otras funciones.
    
    Una posible estrategia para esta función sería:
    Establecer prioridades de los jugadores
    Resetear puntos
    Crear diccionarios cardgame,player_game,player_game_round
    Crear un id de partida
    Mientras hayan dos jugadores o más con puntos, y no nos pasemos del máximo de
    rondas:
    ordenar jugadores, banca al final y resto de prioridad menor a mayor.
    Crear una lista con los id’s de cartas ( mazo).
    Barajar el mazo.
    Establecer apuestas
    Ejecutar jugadas de cada jugador.
    Repartir puntos.
    Eliminar los jugadores sin puntos.
    Establecer nueva banca si es necesario.
    Insertar en BBDD los diccionarios creados para tal propósito.
    Mostrar el ganador.'''

def setGamePriority(mazo):
    '''Esta función establece las prioridades de los jugadores.
Se recibe una lista con los id’s de la baraja (mazo), se mezclan, se reparte una
carta a cada jugador, se ordenan la lista de jugadores de la partida
(contextGame[“game”]) según la carta que han recibido, y se establecen las
prioridades.'''

def resetPoints():
    '''Función que establece los 20 puntos iniciales en todos los jugadores.'''

def fill_player_game(player_game,gameID,*fields):
    '''Función para insertar datos en el diccionario player_game'''

def fill_player_game_round(player_game_round,round,*fields):
    '''Función para insertar datos en el diccionario player_game_round'''

def checkMinimun2PlayerWithPoints():
    '''Función que verifica que al menos haya dos jugadores con puntos.'''

def orderAllPlayers():
    '''Función que ordena los jugadores de la partida (contextGame[“game”]) de forma
que pone la banca al principio y el resto de jugadores después, ordenados según
prioridad'''

def setBets():
    '''Función que establece las apuestas de cada jugador en función del tipo de
jugador.'''

def standarRound(id, mazo):
    '''Función que realiza la tirada de cartas de un jugador en función del tipo de
jugador que es y teniendo en cuenta si el jugador es banca o no.'''

def humanRound(id, mazo):
    '''Función que gestiona la tirada de un jugador humano. Nos muestra el menú de
opciones:
1)View Stats
2)View Game Stats
3)Set Bet
4)Order Card
5)Automatic Play
6)Stand
Option:
Y ejecuta la acción que elijamos'''

def distributionPointAndNewBankCandidates():
    '''Función que realiza el reparto de puntos una vez finalizada una ronda y devuelve
una lista con los candidatos a la banca ( los que tienen 7,5)'''

def printStats(idPlayer="", titulo=""):
    '''Esta función nos imprime los stats de todos los jugadores de la partida.'''

def orderPlayersByPriority(listaJugadores):
    '''Ordenamos la lista de jugadores de la partida (contextGame[“game”]) según
prioridad.'''

def printWinner():
    '''Función que muestra el ganador de la partida:'''

def insertBBDDCardgame(cardgame):
    '''Función que guarda un nuevo registro en la tabla cardgame.
Esta función debería llamarse justo después de acabar una partida.'''

def insertBBDD_player_game(player_game,cardgame_id):
    '''Función que guarda en la tabla player_game de la BBDD el diccionario
player_game.
Esta función debería llamarse justo después de acabar una partida'''

def insertBBDD_player_game_round(player_game_round,cardgame_id):
    '''Función que guarda en la tabla player_game_round de la BBDD el diccionario
player_game_round.
Esta función debería llamarse justo después de acabar una partida.'''

'''FIN FUNCIONES DE playGame()'''





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
        validOption = validaInput(userInput, validInputs)
        if validOption:
            break

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

    while True:
        print('Select your Profile:')
        print('1)Cautios')
        print('2)Moderated')
        print('3)Bold')
        userInput = input('Option: ')
        if userInput.isdigit():
            userInput = int(userInput)
        else:
            userInput = -1
        if validaInput(userInput, [1,2,3]):
            break
    if userInput == 1:
        profile = 'Cautios'
    elif userInput == 2:
        profile = 'Moderated'
    elif userInput == 3:
        profile = 'Bold'

    while True:
        userInput = input('Is ok? Y/n: ')
        if userInput.lower() == 'y':
            newPlayer()
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

if __name__ == '__main__':
    menuPrincipal()