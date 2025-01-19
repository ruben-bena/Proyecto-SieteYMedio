import random
from funciones import *
from parametros import *
from datos import *

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
    # Establecer prioridades de los jugadores:
    setGamePriority(mazo)

    # Resetear puntos:
    resetPoints(players)

    # Crear diccionarios cardgame,player_game,player_game_round:
    cardgame, player_game, player_game_round = generateBBDDvariables() # Crear diccionarios cardgame,player_game,player_game_round

    # Crear un id de partida
    gameId = getGameId()

    # Mientras hayan dos jugadores o más con puntos, y no nos pasemos del máximo de rondas:
    while checkMinimun2PlayerWithPoints():

        # ordenar jugadores, banca al final y resto de prioridad menor a mayor:
        orderPlayersByPriority()

        # Crear una lista con los id’s de cartas (mazo):
        mazo = [] 
        for cardId in context_game['cards_deck'].keys():
            mazo.append(cardId)

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

        # Repartir puntos:
        newBankCandidates = distributionPointAndNewBankCandidates()

        # Eliminar los jugadores sin puntos:
        playersToRemove = []
        for id in context_game['game']:
            if players[id]['points'] <= 0:
                playersToRemove.append(id)
        if len(playersToRemove) != 0:
            for id in playersToRemove:
                context_game['game'].remove(id)

        # Establecer nueva banca si es necesario:
        setNewBank(newBankCandidates)

    # Insertar en BBDD los diccionarios creados para tal propósito:
    '''TODO Aquí van las funciones relacionadas con inserción de datos en BBDD.'''

    # Mostrar el ganador:
    printWinner()
    '''TODO Al acabar la partida, devolver jugador al menú principal.'''

def generateBBDDvariables():
    '''Crea y devuelve los diccionarios: cardgame, player_game, player_game_round'''
    pass

def setNewBank(newBankCandidates):
    '''Se comprueba si hay una nueva banca entre los posibles candidatos. En caso
    afirmativo, se realiza el cambio de banca.'''
    pass

def setGamePriority(mazo):
    '''Esta función establece las prioridades de los jugadores.
Se recibe una lista con los id’s de la baraja (mazo), se mezclan, se reparte una
carta a cada jugador, se ordenan la lista de jugadores de la partida
(contextGame[“game”]) según la carta que han recibido, y se establecen las
prioridades.'''
    # Mezclar el mazo
    random.shuffle(mazo)

    # Repartir una carta a cada jugador para decidir prioridades
    for id in context_game['game']:
        players[id]['initialCard'] = mazo.pop[0]
        ###player_game[context_game['id_game']][id]['initial_card_id'] = mazo.pop[0]

    # Ordenar lista jugadores en función de carta inicial usando método de la burbuja
    for pasada in range(len(context_game['game']) - 1):
        for i in range(len(context_game['game']) - pasada - 1):
            # Comprobar que el número de la carta es mayor
            idJugadorActual = context_game[i]
            idCartaJugadorActual = players[idJugadorActual]['initialCard']
            idJugadorSiguiente = context_game[i+1]
            idCartaJugadorSiguiente = players[idJugadorActual]['initialCard']

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

def resetPoints(players):
    '''Función que establece los 20 puntos iniciales en todos los jugadores.'''
    for player_id in players:
        players[player_id]['points'] = 20

def fill_player_game(player_game,gameID,*fields):
    '''Función para insertar datos en el diccionario player_game'''
    pass

def fill_player_game_round(player_game_round,round,*fields):
    '''Función para insertar datos en el diccionario player_game_round'''
    pass

def checkMinimun2PlayerWithPoints():
    '''Función que verifica que al menos haya dos jugadores con puntos.'''
    pass

def orderAllPlayers():
    '''Función que ordena los jugadores de la partida (contextGame[“game”]) de forma
que pone la banca al principio y el resto de jugadores después, ordenados según
prioridad'''
    pass

def setBets():
    '''Función que establece las apuestas de cada jugador en función del tipo de
jugador.'''
    for player_id in players:
        player = players[player_id]

        #humano
        if player["human"]:
            while True:
                print(f"\nHumano: {player['name']} tienes {player['points']} puntos disponibles.")

                bet = int(input(f"{player['name']}, ingresa tu apuesta (1 a {player['points']}): "))
                if 1 <= bet <= player["points"]:
                    player["bet"] = bet
                    print(f"{player['name']} ha apostado {player['bet']} puntos.")
                    break
                else:
                    print("La apuesta debe estar entre 1 y tus puntos disponibles.")

        #bot
        else:
            if player["points"] > 0:
                max_bet = player["points"]
            else:
                max_bet = 1
            bet = random.randint(1, max_bet)

            player["bet"] = bet
            print(f"Bot: {player['name']} ha apostado {player['bet']} puntos.")

def standarRound(id, mazo):
    '''Función que realiza la tirada de cartas de un jugador en función del tipo de
jugador que es y teniendo en cuenta si el jugador es banca o no.'''
    pass

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

    userInput = getOpt(strSevenAndHalf, inputOptHumanRounds, validInputsHumanRound, playerId=id)

    if userInput == 1:
        printPlayerStats(id)
    elif userInput == 2:
        printStats(id, strSevenAndHalf)
    elif userInput == 3:
        validInputsBet = []
        for n in range(1,21):
            validInputsBet.append(n)
        bet = getOpt(strSevenAndHalf, rangeList=validInputsBet, inputName='Set the new Bet', errorName='The New Bet has to be a number between 1 and  20')
        players[id]['bet'] = bet
        humanRound(id, mazo)
    elif userInput == 4:
        orderNewCard()
    elif userInput == 5:
        standarRound(id, mazo)
    elif userInput == 6:
        endTurn()
    

def distributionPointAndNewBankCandidates():
    '''Función que realiza el reparto de puntos una vez finalizada una ronda y devuelve
una lista con los candidatos a la banca ( los que tienen 7,5)'''
    pass

def printStats(idPlayer="", titulo=""):
    '''Imprime los stats de todos los jugadores de la partida.'''
    print('~' * lineSize)
    print()
    print(strGameStats)
    print()
    print('~' * lineSize)
    if idPlayer != '':
        playerName = players[idPlayer]['name']
        print(f'Round {context_game['round']}, Turn of {playerName}'.center(lineSize, '~'))
    print()
    for nombreClave in players[idPlayer]:
        line = ''
        line += nombreClave.ljust(20)
        for id in context_game['game']:
            valorClave = players[id][nombreClave]
            line += f'{valorClave}'.ljust(40)
        print(line)
    print()
    _ = input(initialString + 'Enter to Continue')

def orderPlayersByPriority(listaJugadores):
    '''Ordenamos la lista de jugadores de la partida (contextGame[“game”]) según
prioridad.'''
    pass

def printWinner():
    '''Función que muestra el ganador de la partida:'''
    pass

def insertBBDDCardgame(cardgame):
    '''Función que guarda un nuevo registro en la tabla cardgame.
Esta función debería llamarse justo después de acabar una partida.'''
    pass

def insertBBDD_player_game(player_game,cardgame_id):
    '''Función que guarda en la tabla player_game de la BBDD el diccionario
player_game.
Esta función debería llamarse justo después de acabar una partida'''
    pass

def insertBBDD_player_game_round(player_game_round,cardgame_id):
    '''Función que guarda en la tabla player_game_round de la BBDD el diccionario
player_game_round.
Esta función debería llamarse justo después de acabar una partida.'''
    pass
