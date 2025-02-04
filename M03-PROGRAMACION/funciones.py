import os
import random
import string
import datetime
import math
import mysql.connector
from mysql.connector import Error
import pymysql

from parametros import *
from datos import *
from setPlayers import *
#from playGame import *

#region funciones
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

    while True:
        userInput = getOpt(strSevenAndHalf, inputOptMainMenu, validInputsMainMenu)

        if userInput == 1:
            addRemovePlayers()
        elif userInput == 2:
            settings()
        elif userInput == 3:
            # TODO Poner condiciones necesarias para que el juego pueda comenzar (2 jugadores min, elegir baraja...)
            if gameCanStart():
                playGame()
            else:
                print(initialString + 'Cannot start game yet! Need at least 2 players and one deck selected.')
                _ = input(initialString + 'Enter to Continue')
        elif userInput == 4:
            ranking()
        elif userInput == 5:
            reports()
        elif userInput == 6:
            break

def gameCanStart():
    '''Retorna True si se cumplen las condiciones para que comience la partida:
    - Al menos 2 jugadores
    - Mazo de cartas seleccionado'''
    atLeast2Players = (len(context_game['game']) >= 2)
    deckIsSelected = (len(context_game['cards_deck']) > 0)
    if atLeast2Players and deckIsSelected:
        return True
    return False

def getOpt(textOpts="", inputOptText=[], rangeList=[], inputName='', errorName='', playerId=''):
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
        if round != '' and playerId != '':
            print(f'Round {context_game['round']}, Turn of {players[playerId]['name']}'.center(lineSize, '~'))
        else:
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
            errorText = 'INVALID OPTION'
            if errorName != '':
                errorText = errorName
            print(errorText.center(lineSize, '='))
            _ = input('Press enter to continue'.center(lineSize))
    
    return userInput

def orderPlayersByPoints(listaJugadores):
    '''Función que ordena los jugadores según sus puntos.'''
    pass

def chanceExceedingSevenAndHalf(id, mazo):
    '''Función que calcula la probabilidad (en %) de pasarse de siete y medio.'''
    nCartasTotales = len(mazo)
    nCartasExceder = 0
    puntosActuales = getPlayerCardPoints(id)
    for idCarta in mazo:
        puntosCarta = context_game['cards_deck'][idCarta]['value']
        pasamosSieteYMedio = (puntosActuales + puntosCarta) > 7.5
        if pasamosSieteYMedio:
            nCartasExceder += 1
    probabilidadPasarSieteYMedio = (nCartasExceder / nCartasTotales) * 100
    return probabilidadPasarSieteYMedio

def printPlayerStats(id):
    '''Esta función nos muestra los stats de un jugador humano.'''
    clearScreen()
    print('~' * lineSize)
    print()
    print(strPlayerStats)
    print()
    print('~' * lineSize)
    playerName = players[id]['name']
    print(f'Stats of {playerName}'.center(lineSize, '~'))
    print()
    for nombreClave in players[id].keys():
        valorClave = str(players[id][nombreClave])
        print(initialString + nombreClave.ljust(20) + valorClave)
    print()
    _ = input(initialString + 'Enter to continue')

def logToFile(text):
    '''Esta función nos puede servir para enviar mensajes de texto al archivo
“logFileSevenAndHalf”, que puede sernos útil a modo de debug.
    
    f = open("logfileSevenAndHalf.txt", "a")
    f.write(text)
    f.close()'''
    pass

def newPlayer(dni, name, profile, human):
    '''Función que devuelve una tupla con dos elementos, el primero es el dni del nuevo
    jugador, el segundo, un diccionario con las claves: name, human, bank, initialCard,
    priority, profile, bet, points, cards, roundPoints.'''
    # TODO Arreglar función. No sé qué valores por defecto debo darle a algunos campos.
    player = (
        dni,
        {
        'name':name,
        'human': human,
        'bank': False,
        'initialCard': '',
        'priority': 0,
        'profile': profile,
        'bet': 0,
        'points': 20,
        'cards': [],
        'roundPoints': ''
        }
    )
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
    
    while True:
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
    validInputsSetMaxRounds = []
    for n in range(1, 11): # Máximo de 10 rondas
        validInputsSetMaxRounds.append(n)
    nRounds = getOpt(strSetMaxRounds, inputOptText=[], rangeList=validInputsSetMaxRounds, inputName='Max Rounds', errorName='Please, enter only numbers between 1 and 10')
    context_game['maxRounds'] = nRounds
    print(initialString + f'Established maximum of rounds to {nRounds}')
    _ = input(initialString + 'Enter to continue')
    settings()

def newRandomDNI():
    '''Función que devuelve un dni válido con números aleatorios'''
    dni = ''
    for i in range(8):
        dni += str(random.randint(0,9))
    dni += random.choice(string.ascii_letters).upper()
    return dni

def validName(name):
    '''Retorna True si un nombre de jugador es válido.
    Un nombre es válido si sólo contiene letras (1 mínimo) y números, y no es un string vacío.'''
    if name == '':
        return False
    elif type(name) == int:
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
        _ = input('Invalid name! Only characters (1 at least) and numbers allowed\nEnter to Continue')

    # Pedir DNI
    if human:
        while True:
            dni = getOpt(strNewPlayer, inputOptText=[f'name = {name}'], rangeList=[], inputName='DNI')
            if validDNI(dni):
                break
            _ = input('Invalid DNI! 8 numbers and 1 upper letter required\nEnter to Continue')
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
        profile = 50
    elif userInput == 2:
        profile = 40
    elif userInput == 3:
        profile = 30

    # Confirmar jugador
    inputOptPlayerData = (
        f'name = {name}',
        f'DNI = {dni}',
        f'Profile = {profile}'
    )
    userInput = getOpt(strNewPlayer, inputOptPlayerData, rangeList=['y','Y','n','N'], inputName='Is ok? Y/n')
    if userInput.lower() == 'y':
        # Insertar jugador en BBDD
        insertBBDD_player(dni, name, not human, profile)

        # Asignar jugador a variable 'players'
        player = newPlayer(dni, name, profile, human)
        players[player[0]] = player[1]
        
        # Asignar jugador a partida actual
        context_game['game'].append(dni)

def insertBBDD_player(player_id, name, is_ai, risk_level):
    '''Inserta un jugador en la BBDD.'''
    try:
        conn = pymysql.connect(
            host='proyectosetimitge.mysql.database.azure.com',
            user='adminproyecto',
            password='proyecto1234!',
            database='siete_y_medio')
        
        cursor = conn.cursor()
        consulta = """
            INSERT INTO players (player_id, name, is_ai, risk_level)
            VALUES (%s, %s, %s, %s);
        """
        cursor.execute(consulta, (player_id, name, is_ai, risk_level))

        # Cerrar cursor y conexión
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f'Error al conectar con la BBDD en la función insertBBDD_player(): {e}')
        _ = input('Enter to Continue')

def loadBBDD_players():
    '''Carga los jugadores de la BBDD en la variable 'players'.'''
    try:
        conn = pymysql.connect(
            host='proyectosetimitge.mysql.database.azure.com',
            user='adminproyecto',
            password='proyecto1234!',
            database='siete_y_medio')
        
        cursor = conn.cursor()
        consulta = "SELECT player_id, name, is_ai, risk_level FROM players;"
        cursor.execute(consulta)
        resultados = cursor.fetchall()

        # Crear diccionario de players
        players = {}
        for fila in resultados:
            player = newPlayer(dni=fila['player_id'], name=fila['name'], profile=fila['risk_level'], human=not bool(fila['is_ai']))
            players[player[0]] = player[1]

        # Cerrar cursor y conexión
        conn.commit()
        cursor.close()
        conn.close()

        return players

    except Exception as e:
        print(f'Error al conectar con la BBDD en la función loadBBDD_players(): {e}')
        _ = input('Enter to Continue')
        return None

def showPlayersGame():
    '''Función que muestra los jugadores seleccionados cuando estamos añadiendo
jugadores a la partida. (Hay una foto en el PDF que muestra cómo debería quedar)'''
    pass

def setPlayersGame():
    '''Función para establecer los jugadores que conformarán la partida siguiente'''
    clearScreen()
    ya_seleccionados(players, context_game['game'])
    clearScreen()
    print_jugadores(players)
    menu_principal(players, context_game['game'])

def removeBBDDPlayer():
    '''Función que nos muestra los jugadores disponibles en BBDD, y elimina el que
seleccionemos'''
    pass

def delBBDDPlayer(nif):
    '''Función que elimina un jugador de la BBDD'''
    cursor=BBDDconnect()
    cursor.execute(f"SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute(f"delete from players where player_id like {nif}")
    print("Eliminado jugador/a "+ str(nif))

def returnListRanking(field='earnings'):
    '''Función que retorna una lista ordenada según la opción del ranking elegida'''
    cursor=BBDDconnect()
    if field=='earnings':
        cursor.execute('select * from player_statistics order by earnings desc')
    elif field=='games':
        cursor.execute('select * from player_statistics order by games_played desc')
    elif field=='minutes':
        cursor.execute('select * from player_statistics order by minutes_played desc')
    results = cursor.fetchall()
    table_ranking = ("*" * 60 + "\n" + "Player ID".ljust(12) + "Name".ljust(10) + "Earnings".ljust(10)
                     + "Games Played".ljust(13) + "Minutes Played".ljust(15) + "\n" + "*" * 60)
    print(table_ranking)
    # Filas de datos
    for row in results:
        print(
            str(row[0]).ljust(12) +
            str(row[1]).ljust(10) +
            str(row[2]).ljust(10) +
            str(row[3]).ljust(13) +
            str(row[4]).ljust(15)
        )

def BBDDconnect():
    '''Función que conecta con la base de datos para insertar, borrar y modificar valores.'''
    conn = pymysql.connect(
        host='proyectosetimitge.mysql.database.azure.com',
        user='adminproyecto',
        password='proyecto1234!',
        database='siete_y_medio')
    cursor = conn.cursor()
    return cursor

def reports():
    '''Función que nos muestra el menú de reportes, y una vez elegida una opción, el reporte
correspondiente'''
    # pass
    inputOptReports = (
        '1)  Initial card more repeated by each user, only users who have played a minimum of 3 games.',
        '2)  Player who makes the highest bet per game, find the round with the highest bet.',
        '3)  Player who makes the lowest bet per game.',
        '4)  Percentage of rounds won per player in each game (%), as well as their average bet for the game.',
        '5)  List of games won by Bots.',
        '6)  Number of users have been the bank in each game.',
        '7)  Rounds won by the bank in each game.',
        '8)  Average bet per game.',
        '9)  Average bet of the first round of each game.',
        '10) Average bet of the last round of each game.',
        '11) Go back'
    )
    validInputReports = []
    for n in range(1, 12):
        validInputReports.append(n)
    userInput = getOpt(strReports, inputOptReports, validInputReports)
    # mainMenu()
    # TODO Todas las opciones de la función
    if userInput == 1:
        print("En proceso")
        input("Enter para continuar")
        reports()

    elif userInput == 2:
        cabecera = (" APUESTA MÁS ALTA POR PARTIDA ".center(85, "=") + "\n" + "ID Partida".ljust(
            15) + "ID Jugador".rjust(15) +
                    "Apuesta Más Alta".rjust(30) + "\n" + "*".center(85, "="))

        cursor = BBDDconnect()
        cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute("select * from informe_2")
        results = cursor.fetchall()
        print(cabecera)
        for row in results:
            print(str(row[0]).ljust(15) + str(row[1]).rjust(15) + str(row[2]).rjust(30))

        input("Enter para continuar.")
        reports()

    elif userInput == 3:
        cabecera = (" APUESTA MÁS BAJA POR PARTIDA ".center(85, "=") + "\n" + "ID Partida".ljust(
            15) + "ID Jugador".rjust(15) + "Apuesta Más Baja".rjust(30) + "\n" + "*".center(85, "="))

        cursor = BBDDconnect()
        cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute("select * from informe_3")
        results = cursor.fetchall()
        print(cabecera)
        for row in results:
            print(str(row[0]).ljust(15) + str(row[1]).rjust(15) + str(row[2]).rjust(30))

        input("Enter para continuar.")
        reports()

    elif userInput == 4:
        print("En proceso")
        input("Enter para continuar")
        reports()
    elif userInput == 5:
        print("En proceso")
        input("Enter para continuar")
        reports()

    elif userInput == 6:

        cabecera = (" RONDAS GANADAS POR BANCA ".center(60, "=") + "\n" + "ID Partida".ljust(20) +
                    "Rondas Ganadas".rjust(30) + "\n" + "*".center(60, "="))

        cursor = BBDDconnect()
        cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute("select * from informe_6")
        results = cursor.fetchall()
        print(cabecera)
        for row in results:
            print(str(row[0]).ljust(20) + str(row[1]).rjust(30))

        input("Enter para continuar")
        reports()

    elif userInput == 7:

        cabecera = (" USUARIOS BANCAS POR PARTIDA".center(60, "=") + "\n" + "ID Partida".ljust(20) +
                    "Usuarios Banca".rjust(30) + "\n" + "*".center(60, "="))

        cursor = BBDDconnect()
        cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute("select * from informe_7")
        results = cursor.fetchall()
        print(cabecera)
        for row in results:
            print(str(row[0]).ljust(20) + str(row[1]).rjust(30))

        input("Enter para continuar")
        reports()

    elif userInput == 8:

        cabecera = (" APUESTA MEDIA POR PARTIDA ".center(60, "=") + "\n" + "ID Partida".ljust(20) +
                    "Apuesta Media".rjust(30) + "\n" + "*".center(60, "="))

        cursor = BBDDconnect()
        cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute("select * from informe_8")
        results = cursor.fetchall()
        print(cabecera)
        for row in results:
            print(str(row[0]).ljust(20) + str(row[1]).rjust(30))

        input("Enter para continuar")
        reports()

    elif userInput == 9:

        cabecera = (" APUESTA MEDIA PRIMERA RONDA ".center(60, "=") + "\n" + "ID Partida".ljust(
            20) + "Apuesta Media Primera Ronda".rjust(30) +
                    "\n" + "*".center(60, "="))

        cursor = BBDDconnect()
        cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute("select * from informe_2")
        results = cursor.fetchall()
        print(cabecera)
        for row in results:
            print(str(row[0]).ljust(20) + str(row[1]).rjust(30))

        input("Enter para continuar")
        reports()

    elif userInput == 10:

        cabecera = (" APUESTA MEDIA ÚLTIMA RONDA ".center(60, "=") + "\n" + "ID Partida".ljust(20) +
                    "Apuesta Media Última Ronda".rjust(30) + "\n" + "*".center(60, "="))

        cursor = BBDDconnect()
        cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute("select * from informe_2")
        results = cursor.fetchall()
        print(cabecera)
        for row in results:
            print(str(row[0]).ljust(20) + str(row[1]).rjust(30))

        input("Enter para continuar")
        reports()

    elif userInput == 11:
        pass
        # mainMenu()

def reports():
    '''Función que nos muestra el menú de reportes, y una vez elegida una opción, el reporte
correspondiente'''
    # TODO Hacer que se muestre cada string segmentado si este es demasiado largo (para que quede más bonico)
    inputOptReports = (
        '1)  Initial card more repeated by each user, only users who have played a minimum of 3 games.',
        '2)  Player who makes the highest bet per game, find the round with the highest bet.',
        '3)  Player who makes the lowest bet per game.',                                      
        '4)  Percentage of rounds won per player in each game (%), as well as their average bet for the game.',                                      
        '5)  List of games won by Bots.',                                      
        '6)  Rounds won by the bank in each game.',                                      
        '7)  Number of users have been the bank in each game.',                                      
        '8)  Average bet per game.',                                      
        '9)  Average bet of the first round of each game.',                                      
        '10) Average bet of the last round of each game.',                                      
        '11) Go back'
    )
    validInputReports = []
    for n in range(1,12):
        validInputReports.append(n)

    userInput = getOpt(strReports, inputOptReports, validInputReports)

    mainMenu()
    # TODO Todas las opciones de la función
    if userInput == 1:
        pass
    elif userInput == 2:
        pass
    elif userInput == 3:
        pass
    elif userInput == 4:
        pass
    elif userInput == 5:
        pass
    elif userInput == 6:
        pass
    elif userInput == 7:
        pass
    elif userInput == 8:
        pass
    elif userInput == 9:
        pass
    elif userInput == 10:
        pass
    elif userInput == 11:
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

def getGameID():
    '''Función que devuelve un id no existente en la tabla cardgame.'''
    try:
        conn = pymysql.connect(
            host='proyectosetimitge.mysql.database.azure.com',
            user='adminproyecto',
            password='proyecto1234!',
            database='siete_y_medio')

        cursor = conn.cursor()
        consulta = "SELECT MAX(game_id) FROM games;"
        cursor.execute(consulta)
        resultado = cursor.fetchone()

        # Obtener el siguiente ID
        max_id = resultado[0]  # Esto puede valer 'None' si no hay datos en la tabla de la BBDD
        if max_id is None:
            game_id = 1
        else:
            game_id = max_id + 1

        # Cerrar cursor y conexión
        conn.commit()
        cursor.close()
        conn.close()

        return game_id

    except Exception as e:
        print(f'Error al conectar con la BBDD en la función getGameId(): {e}')
        _ = input('Enter to Continue')
        return None

def getBBDDRanking():
    '''Función que crea la vista player_earnings, y retorna un diccionario con los datos de
ésta,
player_id | earnings | games_played | minutes_played.'''
    pass

def ranking():
    '''Función que muestra el menú del ranking y el ranking según la opción elegida'''
    inputOptRanking = (
        '1) Players With More Earnings',
        '2) Players With More Games Played',
        '3) Players With More Minutes Playerd',
        '4) Go Back'
    )
    validInputRanking = (1,2,3,4)

    userInput = getOpt(strRanking, inputOptRanking, validInputRanking)

    if userInput == 1:
        returnListRanking(field='earnings')
    elif userInput == 2:
        returnListRanking(field='games')
    elif userInput == 3:
        returnListRanking(field='minutes')
    elif userInput == 4:
        mainMenu()

def returnListRanking(field="earnings"):
    '''Función que retorna una lista con los id de jugadores del diccionario que retorna la
función getBBDDRanking(), ordenados según la opción del ranking elegida'''
    pass
#endregion funciones

#region playGame

def playGame():
    '''Esta es la función principal del proyecto. Una vez establecido el número de rondas, la
    baraja con la que se va a jugar, y los jugadores que participan en la partida, ésta será
    la función que gestione toda la partida. Para ello, hará uso de otras funciones.'''
    # Crear una lista con los id’s de cartas (mazo):
    mazo = []
    for card_id in context_game['cards_deck'].keys():
        mazo.append(card_id)

    context_game['round'] = 0

    # Establecer prioridades iniciales de los jugadores:
    setGamePriority(mazo)

    # Resetear puntos:
    resetPoints(players)

    # Crear un id de partida
    if PRUEBAS:
        game_id = 1
    else:
        game_id = getGameID()
    context_game['id_game'] = game_id

    # Crear diccionarios cardgame,player_game,player_game_round:
    cardgame, player_game, player_game_round = generateBBDDvariables() # Crear diccionarios cardgame,player_game,player_game_round

    # Mientras hayan dos jugadores o más con puntos, y no nos pasemos del máximo de rondas:
    while checkMinimun2PlayerWithPoints() and checkRounds():

        # Establecer prioridad de los jugadores, SIN DAR CARTA INICIAL
        setGamePriority(mazo, giveInitialCard=False, setBank=False)

        # ordenar jugadores, banca al final y resto de prioridad menor a mayor:
        orderPlayersByPriority()

        # Crear una lista con los id’s de cartas (mazo):
        mazo = [] 
        for card_id in context_game['cards_deck'].keys():
            mazo.append(card_id)

        # Barajar el mazo:
        random.shuffle(mazo)

        # Establecer apuestas:
        setBets()

        # Ejecutar jugadas de cada jugador:
        for id in context_game['game']:
            playerIsHuman = players[id]['human']
            if playerIsHuman:
                humanRound(id, mazo)
            else:
                standarRound(id, mazo)
            fill_player_game_round(player_game_round, round=context_game['round'], playerID=id)  
            printStats(idPlayer=id)

        # Repartir puntos:
        newBankCandidates = distributionPointAndNewBankCandidates()

        # Eliminar los jugadores sin puntos:
        removeDefeatedPlayers()

        # Establecer nueva banca si es necesario:
        setNewBank(newBankCandidates)

        printStats(titulo=True)

        # Actualizar variables
        context_game['round'] += 1
        for id in context_game['game']:
            players[id]['cards'] = []
            players[id]['roundPoints'] = 0

    # Rellenar variables para BBDD
    fill_cardgame(cardgame)
    for id in context_game['game']: # Puede haber más de un jugador en partida si esta acaba por sobrepasar las rondas
        fill_player_game(player_game, playerID=id)

    # Insertar en BBDD los diccionarios creados para tal propósito:
    if not PRUEBAS:
        insertBBDDCardgame(cardgame)
        '''No se ejecuta inserción de 'player_game' porque no se ha creado la tabla para ello en la BBDD.'''
        #insertBBDD_player_game(player_game, context_game['id_game'])
        insertBBDD_player_game_round(player_game_round)

    # Mostrar el ganador:
    printWinner()

def removeDefeatedPlayers():
    '''Elimina a los jugadores sin puntos de la partida.'''
    playersToRemove = []
    for id in context_game['game']:
        if players[id]['points'] == 0:
            playersToRemove.append(id)
    if len(playersToRemove) != 0:
        for id in playersToRemove:
            # Añadir jugador a player_game
            fill_player_game(player_game, playerID=id)
            # Borrar jugador de partida
            context_game['game'].remove(id)

def getHighestPriorityID(playerList):
    '''Retorna el ID del jugador con más prioridad de la lista.'''
    highestPriorityID = ''
    highestPriorityValue = len(context_game['game']) + 1
    for player_id in playerList:
        playerPriorityValue = players[player_id]['priority']
        hasMorePriority = playerPriorityValue < highestPriorityValue
        if hasMorePriority:
            highestPriorityID = player_id
            highestPriorityValue = playerPriorityValue
    return highestPriorityID

def setNewBank(newBankCandidates):
    '''Evalúa si es necesario realizar un cambio de banca a partir de una lista de candidatos.'''
    bank_id = getBankId()
    # Variables de control
    gameHasBank = (bank_id is not None)
    thereAreCandidates = (len(newBankCandidates) != 0)
    needNewBank = False
    if gameHasBank:
        # Si hay candidatos, asignar nueva banca
        if thereAreCandidates:
            needNewBank = True
            # Borrar anterior banca
            players[bank_id]['bank'] = False
        # Si ya hay banca y no hay candidatos, no hacer nada
        else:
            pass
    else:
        needNewBank = True

    if needNewBank:
        # Si no hay candidatos, mirar todos los jugadores
        if thereAreCandidates:
            newBankID = getHighestPriorityID(playerList=newBankCandidates)
        else:
            newBankID = getHighestPriorityID(playerList=context_game['game'])
        players[newBankID]['bank'] = True

def setGamePriority(mazo, giveInitialCard=True, setBank=True):
    '''Esta función establece las prioridades de los jugadores.
    Se recibe una lista con los id’s de la baraja (mazo), se mezclan, se reparte una
    carta a cada jugador, se ordenan la lista de jugadores de la partida
    (contextGame[“game”]) según la carta que han recibido, y se establecen las
    prioridades.'''
    if giveInitialCard:
        # Mezclar el mazo
        random.shuffle(mazo)

        # Repartir una carta a cada jugador para decidir prioridades
        for id in context_game['game']:
            players[id]['initialCard'] = mazo.pop(0)

    # Ordenar lista jugadores en función de carta inicial usando método de la burbuja
    orderAllPlayers()

    # Asignar banca y prioridad a primer jugador lista ordenada (si es necesario)
    if setBank:
        id_banca = context_game['game'][0]
        players[id_banca]['bank'] = True
    else:
        id_banca = getBankId()
    
    players[id_banca]['priority'] = len(context_game['game'])

    # Asignar prioridad al resto de jugadores lista ordenada
    priority = 1
    for id in context_game['game'][1:]:
        players[id]['priority'] = priority
        priority += 1

def resetPoints(players):
    '''Función que establece los 20 puntos iniciales en todos los jugadores.'''
    for player_id in players:
        players[player_id]['points'] = 20

def generateBBDDvariables():
    '''Crea y devuelve los diccionarios: cardgame, player_game, player_game_round'''
    if len(context_game['cards_deck']) == 48:
        deck_id = 'ESP'
    else:
        deck_id = 'POKER'
    cardgame = {
        'cardgame_id': context_game['id_game'],
        'players': len(context_game['game']),
        'deck_id': deck_id,
        'start_hour': datetime.datetime.now(),
        'rounds': 0, # Esta variable se actualiza al final de la partida, con el valor de context_game['rounds']
        'end_hour': '' # Esta variable se actualiza al final de la partida, con el valor de datetime.datetime.now()
    }

    player_game = {}

    player_game_round = {}

    return cardgame, player_game, player_game_round

def fill_cardgame(cardgame):
    '''Función para insertar datos en el diccionario cardgame'''
    cardgame['rounds'] = context_game['round']
    cardgame['end_hour'] = datetime.datetime.now()

def fill_player_game(player_game,playerID):
    '''Función para insertar datos en el diccionario player_game'''
    gameID = context_game['id_game']
    if len(player_game) == 0:
        player_game[gameID] = {}
    player_game[gameID][playerID] = {}
    player_game[gameID][playerID]['initial_card_id'] = players[playerID]['initialCard']
    player_game[gameID][playerID]['starting_points'] = 20
    player_game[gameID][playerID]['ending_points'] = players[id]['points']
    

def fill_player_game_round(player_game_round,round,playerID):
    '''Función para insertar datos en el diccionario player_game_round'''
    if round not in player_game_round.keys():
        player_game_round[round] = {}
    player_game_round[round][playerID] = {}
    player_game_round[round][playerID]['is_bank'] = players[playerID]['bank']
    player_game_round[round][playerID]['bet_points'] = players[playerID]['bet']
    if round == 0:
        starting_points = 20
    else:
        starting_points = player_game_round[round - 1][playerID]['ending_round_points']
    player_game_round[round][playerID]['starting_round_points'] = starting_points
    player_game_round[round][playerID]['cards_value'] = getPlayerCardPoints(playerID)
    player_game_round[round][playerID]['ending_round_points'] = players[playerID]['points']

def checkRounds():
    '''Retorna True si no hemos sobrepasado el máximo de rondas de la partida.'''
    if context_game['round'] < context_game['maxRounds']:
        return True
    return False

def checkMinimun2PlayerWithPoints():
    '''Función que verifica que al menos haya dos jugadores con puntos.'''
    nPlayersWithPoints = 0
    for player_id in context_game['game']:
        if players[player_id]['points'] > 0:
            nPlayersWithPoints += 1
            if nPlayersWithPoints >= 2:
                return True
    return False

def setBets():
    '''Función que establece las apuestas de cada jugador en función del tipo de
jugador.'''
    for player_id in context_game['game']:
        puntos_actuales = players[player_id]['points']
        perfil = players[player_id]['profile']
        puntos_apostados = math.floor(puntos_actuales * (perfil / 100)) # math.floor redondea a un número entero por abajo
        
        # Si el jugador tiene pocos puntos y puntos_apostados le da 0, que apueste como mínimo 1 punto
        if puntos_apostados == 0:
            players[player_id]['bet'] = 1
        else:
            players[player_id]['bet'] = puntos_apostados

        # Si el jugador es banca, no puede apostar
        playerIsBank = players[player_id]['bank']
        if playerIsBank:
            players[player_id]['bet'] = 0

def bankOrderNewCard(id, mazo):
    '''Función que evalúa si la banca pedirá una nueva carta.'''
    pass

def checkBankWonRound(bank_id):
    '''Retorna True si la banca gana la ronda con sus cartas actuales.'''
    bankRoundPoints = players[bank_id]['roundPoints']
    for player_id in context_game['game']:
        if player_id != bank_id:
            playerRoundPoints = players[player_id]['roundPoints']
            playerWinsToBank = (playerRoundPoints > bankRoundPoints) and (playerRoundPoints <= 7.5)
            if playerWinsToBank:
                return False
    return True

def checkBankIsDefeated(bank_id):
    '''Retorna True si la banca pierde la partida (0 puntos) con sus cartas actuales.'''
    bankPoints = players[bank_id]['points']
    bankRoundPoints = players[bank_id]['roundPoints']
    # Calcular puntos que quedarían a la banca con cartas actuales
    for player_id in context_game['game']:
        if player_id != bank_id:
            # Comprobar si jugador gana a banca
            playerRoundPoints = players[player_id]['roundPoints']
            playerWinsToBank = (playerRoundPoints > bankRoundPoints) and (playerRoundPoints <= 7.5)

            # Dar o quitar puntos dependiendo de quién gane
            playerBetPoints = players[player_id]['bet']
            if playerWinsToBank:
                bankPoints -= playerBetPoints
            else:
                bankPoints += playerBetPoints

    # Comprobar si banca pierde partida
    if bankPoints <= 0:
        return True
    return False

def checkBankLosesRound(bank_id):
    '''Retorna True si la banca pierde la ronda contra TODOS los jugadores con sus cartas actuales.'''
    bankRoundPoints = players[bank_id]['roundPoints']
    for player_id in context_game['game']:
        if player_id != bank_id:
            playerRoundPoints = players[player_id]['roundPoints']
            bankWinsToPlayer = (playerRoundPoints < bankRoundPoints) and (bankRoundPoints <= 7.5)
            if bankWinsToPlayer:
                return False
    return True

def standarRound(id, mazo):
    '''Función que realiza la tirada de cartas de un jugador en función del tipo de
jugador que es y teniendo en cuenta si el jugador es banca o no.'''
    playerIsBank = players[id]['bank']
    playerProfile = players[id]['profile']

    if playerIsBank:
        while True:
            players[id]['roundPoints'] = getPlayerCardPoints(id)
            bankWonRound = checkBankWonRound(id) # Banca gana la ronda, sin necesitar más cartas
            if bankWonRound:
                break

            bankOrdersCard = False
            bankIsDefeated = checkBankIsDefeated(id) # Banca pierde partida (<= 0 puntos) si no pide más cartas
            bankLosesRound = checkBankLosesRound(id) # Banca no gana a NINGÚN jugador esta ronda
            if bankIsDefeated or bankLosesRound:
                bankOrdersCard = True

            # Comprobar si pide carta según perfil de riesgo
            chanceExceeding = chanceExceedingSevenAndHalf(id, mazo)
            bankCannotWin = players[id]['roundPoints'] > 7.5
            if (chanceExceeding > playerProfile and not bankOrdersCard) or bankCannotWin:
                break
            else:
                idCarta = mazo.pop(0)
                players[id]['cards'].append(idCarta)

    else:
        while True:
            chanceExceeding = chanceExceedingSevenAndHalf(id, mazo)
            if chanceExceeding > playerProfile:
                break
            else:
                idCarta = mazo.pop(0)
                players[id]['cards'].append(idCarta)
                players[id]['roundPoints'] = getPlayerCardPoints(id)

def setPlayerBet(id):
    '''Pide al jugador un valor de apuesta. Si el valor es válido, lo asigna.'''
    playerIsBank = players[id]['bank']
    if playerIsBank:
        print(initialString + 'Bank cannot bet points!')
        _ = input(initialString + 'Enter to Continue')
    else:
        validInputsBet = []
        maxBet = min(20, players[id]['points'])
        for n in range(1, maxBet + 1):
            validInputsBet.append(n)
        bet = getOpt(strSevenAndHalf, rangeList=validInputsBet, inputName='Set the new Bet', errorName=f'The New Bet has to be a number between 1 and {maxBet}')
        players[id]['bet'] = bet

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
    inputOptHumanRounds = (
        '1) View Stats',
        '2) View Game Stats',
        '3) Set Bet',
        '4) Order Card',
        '5) Automatic Play',
        '6) Stand')
    validInputsHumanRound = (1,2,3,4,5,6)

    while True:
        userInput = getOpt(strSevenAndHalf, inputOptHumanRounds, validInputsHumanRound, playerId=id)

        if userInput == 1:
            printPlayerStats(id)
        elif userInput == 2:
            printStats(id, strSevenAndHalf)
        elif userInput == 3:
            setPlayerBet(id)
        elif userInput == 4:
            orderCard(id, mazo)
            if players[id]['roundPoints'] > 7.5:
                break
        elif userInput == 5:
            standarRound(id, mazo)
            break
        elif userInput == 6:
            break
    
def orderCard(id, mazo):
    '''Pide una carta al jugador.'''
    print(initialString + ' Order Card')

    # Variables bloque condicional
    jugadorQuiereCarta = False
    jugadorSinCartas = len(players[id]['cards']) == 0

    # Si jugador ya tiene cartas, preguntar si quiere pedir carta
    if not jugadorSinCartas:
        posibilidadDePasarse = chanceExceedingSevenAndHalf(id, mazo)
        print(initialString + f'Chance of exceed 7,5 = {posibilidadDePasarse:.2f} %')
        userInput = input(initialString + 'Do you want another card? Y/y = yes, any other key = Not')
        if userInput == 'Y' or userInput == 'y':
            jugadorQuiereCarta = True

    if jugadorQuiereCarta or jugadorSinCartas:
        # Sacar carta del mazo. Añadirla carta y puntos a jugador
        idCarta = mazo.pop(0)
        players[id]['cards'].append(idCarta)

        # Imprimir info por pantalla
        nombreCarta = context_game['cards_deck'][idCarta]['literal']
        print(initialString + f'The new card is {nombreCarta}')
        playerCardPoints = getPlayerCardPoints(id)
        players[id]['roundPoints'] = playerCardPoints
        print(initialString + f'Now you have {playerCardPoints} points')
        if playerCardPoints > 7.5:
            print(initialString + 'You passed from 7.5...No more options for you')

    _ = input(initialString + 'Enter to Continue')

def getPlayerCardPoints(id):
    '''Retorna los puntos de cartas de un jugador.'''
    playerCardPoints = 0
    for idCard in players[id]['cards']:
        playerCardPoints += context_game['cards_deck'][idCard]['value']
    return playerCardPoints

def getBankId():
    '''Retorna el ID de la banca.'''
    for player_id in context_game['game']:
        playerIsBank = players[player_id]['bank']
        if playerIsBank:
            return player_id
    return None

def distributionPointAndNewBankCandidates():
    '''Función que realiza el reparto de puntos una vez finalizada una ronda y devuelve
    una lista con los candidatos a la banca ( los que tienen 7,5)'''
    # Repartir puntos a cada jugador
    bank_id = getBankId()
    bankRoundPoints = players[bank_id]['roundPoints']
    for player_id in context_game['game']:
        if player_id != bank_id:

            # Declarar variables para bucle condicional
            playerRoundPoints = players[player_id]['roundPoints']
            bankWonToPlayer = ((bankRoundPoints >= playerRoundPoints) and (bankRoundPoints <= 7.5)) or ((bankRoundPoints <= 7.5) and (playerRoundPoints > 7.5))
            playerWonToBank = (bankRoundPoints < playerRoundPoints) and (playerRoundPoints <= 7.5) or ((playerRoundPoints <= 7.5) and (bankRoundPoints > 7.5))
            deltaPoints = 0 # Si no ha ganado ni banca ni jugador (ambos han pasado 7.5), se mantendrá este valor
            
            # Si jugador gana a banca
            if playerWonToBank:
                if playerRoundPoints == 7.5:
                    deltaPoints += players[player_id]['bet'] * 2
                else:
                    deltaPoints += players[player_id]['bet']
            if deltaPoints > players[bank_id]['points']:
                deltaPoints = players[bank_id]['points']

            # Si banca gana a jugador
            elif bankWonToPlayer:
                deltaPoints -= players[player_id]['bet']

            # Realizar transacción de puntos
            players[player_id]['points'] += deltaPoints
            players[bank_id]['points'] -= deltaPoints

    # Comprobar si hay nuevos candidatos a banca
    newBankCandidates = []
    bankGotSevenAndHalf = False
    for player_id in context_game['game']:
        # Comprobar si jugador ha sacado 7.5, y comprobar si es banca
        playerIsBank = players[player_id]['bank']
        playerGotSevenAndHalf = (players[player_id]['roundPoints'] == 7.5)
        if playerGotSevenAndHalf and playerIsBank:
            bankGotSevenAndHalf = True
            break
        elif playerGotSevenAndHalf and not playerIsBank:
            newBankCandidates.append(player_id)

    # Borrar lista candidatos si banca saca 7.5
    if bankGotSevenAndHalf:
        newBankCandidates = []

    return newBankCandidates

def printStats(idPlayer="", titulo=False):
    '''Imprime los stats de todos los jugadores de la partida.'''
    # TODO Implementar funcionalidad para que imprima 3 jugadores máximo por fila
    clearScreen()
    if not titulo:
        print('~' * lineSize)
    else:
        print(f' STATS AFTER ROUND {context_game['round'] }'.center(lineSize, '~'))
    print()
    print(strGameStats)
    print()
    print('~' * lineSize)
    if idPlayer != '':
        playerName = players[idPlayer]['name']
        print(f'Round {context_game['round']}, Turn of {playerName}'.center(lineSize, '~'))
    print()
    for nombreClave in playersKeysForID:
        line = ''
        line += nombreClave.ljust(20)
        for id in context_game['game']:
            # Si miramos la clave 'cards', hacemos una variación ya que estamos mirando una lista y no un único valor
            if nombreClave == 'cards':
                valorClave = ','.join(players[id][nombreClave])
            else:
                valorClave = players[id][nombreClave]
            line += f'{valorClave}'.ljust(40)
        print(line)
    print()
    _ = input(initialString + 'Enter to Continue')

def orderAllPlayers():
    '''Función que ordena los jugadores de la partida (contextGame[“game”]) de forma
    que pone la banca al principio y el resto de jugadores después, ordenados según prioridad.

    Es decir, se ordena la lista teniendo en cuenta sólo la carta inicial, y no quién es la banca.'''
    # Ordenar lista utilizando método de la burbuja
    for pasada in range(len(context_game['game']) - 1):
        for i in range(len(context_game['game']) - pasada - 1):
            # Comprobar que el número de la carta es mayor
            idJugadorActual = context_game['game'][i]
            idCartaJugadorActual = players[idJugadorActual]['initialCard']
            idJugadorSiguiente = context_game['game'][i+1]
            idCartaJugadorSiguiente = players[idJugadorSiguiente]['initialCard']

            seDebeOrdenar = False
            valorEsMayor = context_game['cards_deck'][idCartaJugadorActual]['value'] > context_game['cards_deck'][idCartaJugadorSiguiente]['value']
            if valorEsMayor:
                seDebeOrdenar = True
            else: # Si valor carta no es más alto, miramos si es igual
                valorEsIgual = context_game['cards_deck'][idCartaJugadorActual]['value'] == context_game['cards_deck'][idCartaJugadorSiguiente]['value']
                if valorEsIgual: # Si es igual, miramor la prioridad (marcada por el palo de la carta)
                    prioridadPalo = context_game['cards_deck'][idCartaJugadorActual]['priority'] < context_game['cards_deck'][idCartaJugadorSiguiente]['priority']
                    if prioridadPalo:
                        seDebeOrdenar = True

            if seDebeOrdenar:
                tmp = context_game['game'][i + 1]
                context_game['game'][i + 1] = context_game['game'][i]
                context_game['game'][i] = tmp

def orderPlayersByPriority(listaJugadores=context_game):
    '''Ordenamos la lista de jugadores de la partida (contextGame[“game”]) según prioridad.'''
    # Ordenar lista utilizando método de la burbuja
    for pasada in range(len(context_game['game']) - 1):
        for i in range(len(context_game['game']) - pasada - 1):
            # Comprobar que el valor de prioridad es más pequeño
            idCurrentPlayer = context_game['game'][i]
            priorityCurrentPlayer = players[idCurrentPlayer]['priority']
            idNextPlayer = context_game['game'][i+1]
            priorityNextPlayer = players[idNextPlayer]['priority']

            isOrdered = False
            currentPlayerHasPriority = priorityCurrentPlayer < priorityNextPlayer
            if currentPlayerHasPriority:
                isOrdered = True

            # Si no están ordenados los pares de valores, se ordenan
            if not isOrdered:
                tmp = context_game['game'][i + 1]
                context_game['game'][i + 1] = context_game['game'][i]
                context_game['game'][i] = tmp
    

def printWinner():
    '''Función que muestra el ganador de la partida:'''
    print('~' * lineSize)
    print()
    print(strGameOver)
    print()
    print('~' * lineSize)
    print()

    id_winner = max(context_game['game'], key=lambda x:players[x]['points'])
    name_winner = players[id_winner]['name']
    points_winner = players[id_winner]['points']
    print(initialString + f'The winner is {id_winner} - {name_winner}, in {context_game['round']} rounds, with {points_winner} points!')

    _ = input(initialString + 'Enter to continue')

def insertBBDDCardgame(cardgame):
    '''Función que guarda un nuevo registro en la tabla cardgame.
Esta función debería llamarse justo después de acabar una partida.'''
    try:
        conn = pymysql.connect(
            host='proyectosetimitge.mysql.database.azure.com',
            user='adminproyecto',
            password='proyecto1234!',
            database='siete_y_medio')
        
        cursor = conn.cursor()

        # Definir primer round_id a partir de los guardados en BBDD
        consulta = """
            INSERT INTO games 
            (game_id, start_time, end_time, deck_id, number_players, number_rounds)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        valores = (
            cardgame['cardgame_id'], 
            cardgame['start_hour'], 
            cardgame['end_hour'], 
            cardgame['deck_id'], 
            cardgame['players'], 
            cardgame['rounds']
        )
        cursor.execute(consulta, valores)    

        # Cerrar cursor y conexión
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f'Error al conectar con la BBDD en la función insertBBDDCardgame(): {e}')
        _ = input('Enter to Continue')

def insertBBDD_player_game(player_game,cardgame_id):
    '''Función que guarda en la tabla player_game de la BBDD el diccionario
player_game.
Esta función debería llamarse justo después de acabar una partida'''
    pass

def insertBBDD_player_game_round(player_game_round):
    '''Función que guarda en la tabla player_game_round de la BBDD el diccionario
player_game_round.
Esta función debería llamarse justo después de acabar una partida.'''
    try:
        conn = pymysql.connect(
            host='proyectosetimitge.mysql.database.azure.com',
            user='adminproyecto',
            password='proyecto1234!',
            database='siete_y_medio')
        
        cursor = conn.cursor()

        # Definir primer round_id a partir de los guardados en BBDD
        consulta = "SELECT MAX(round_id) FROM rounds_players;"
        cursor.execute(consulta)
        resultado = cursor.fetchone()

        max_id = resultado[0]  # Esto puede valer 'None' si no hay datos en la tabla de la BBDD
        if max_id is None:
            round_id = 1
        else:
            round_id = max_id + 1
        
        # Recorrer las rondas y jugadores para preparar las inserciones
        for round_number, players in player_game_round.items():
            for player_id, player_data in players.items():
                # Preparar valores para inserción
                is_bank = player_data['is_bank']
                bet_points = player_data['bet_points']
                starting_round_points = player_data['starting_round_points']
                cards_value = player_data['cards_value']
                ending_round_points = player_data['endind_round_points']

                # Consulta SQL para insertar
                consulta = """
                    INSERT INTO rounds_players 
                    (round_id, game_id, round_number, player_id, first_cart_in_hand, player_start_points, 
                     player_end_points, player_bet, player_bank)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                valores = (
                    round_id,
                    context_game['id_game'],
                    round_number,
                    player_id,
                    players[player_id]['initialCard'], 
                    starting_round_points,
                    ending_round_points,
                    bet_points,
                    is_bank
                )

                # Ejecutar la inserción
                cursor.execute(consulta, valores)

        # Cerrar cursor y conexión
        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print(f'Error al conectar con la BBDD en la función insertBBDD_player_game_round(): {e}')
        _ = input('Enter to Continue')

if PRUEBAS:
    players = playersPrueba
    for id in players:
        context_game['game'].append(id)

    print('Iniciando MODO PRUEBA')
    print()
    print('Los jugadores serán cargados desde la variable "playersPrueba" dentro del archivo "parametros.py".')
    print('No se cargara ni insertará ningún dato en la BBDD.')
    print()
    print('Para iniciar el juego de forma normal:')
    print('1) Ir a parametros.py y cambiar variable PRUEBAS=False')
    print('2) Volver a ejecutar el archivo main.py')
    input('Enter to Continue')
else:
    players = loadBBDD_players()

# endregion playGame