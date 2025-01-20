import random
import datetime
from funciones import *
from parametros import *
from datos import *

def playGame():
    '''Esta es la función principal del proyecto. Una vez establecido el número de rondas, la
    baraja con la que se va a jugar, y los jugadores que participan en la partida, ésta será
    la función que gestione toda la partida. Para ello, hará uso de otras funciones.'''
    # Establecer prioridades de los jugadores:
    setGamePriority(mazo)

    # Resetear puntos:
    resetPoints(players)

    # Crear un id de partida
    game_id = getGameId()

    # Crear diccionarios cardgame,player_game,player_game_round:
    cardgame, player_game, player_game_round = generateBBDDvariables() # Crear diccionarios cardgame,player_game,player_game_round

    # Mientras hayan dos jugadores o más con puntos, y no nos pasemos del máximo de rondas:
    while checkMinimun2PlayerWithPoints():

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

        # Repartir puntos:
        newBankCandidates = distributionPointAndNewBankCandidates()

        # Eliminar los jugadores sin puntos:
        removeDefeatedPlayers()

        # Establecer nueva banca si es necesario:
        setNewBank(newBankCandidates)

    # Rellenar variables para BBDD
    fill_cardgame(cardgame)
    for id in context_game['game']: # Puede haber más de un jugador en partida si esta acaba por sobrepasar las rondas
        fill_player_game(player_game, playerID=id)

    # Insertar en BBDD los diccionarios creados para tal propósito:
    '''TODO Aquí van las funciones relacionadas con inserción de datos en BBDD.'''

    # Mostrar el ganador:
    printWinner()
    '''TODO Al acabar la partida, devolver jugador al menú principal.'''

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

def generateBBDDvariables():
    '''Crea y devuelve los diccionarios: cardgame, player_game, player_game_round'''
    cardgame = {
        'cardgame_id': context_game['id_game'],
        'players': len(context_game['game']),
        'start_hour': datetime.datetime.now(),
        'rounds': 0, # Esta variable se actualiza al final de la partida, con el valor de context_game['rounds']
        'end_hour': '' # Esta variable se actualiza al final de la partida, con el valor de datetime.datetime.now()
    }

    player_game = {}

    player_game_round = {}

    return cardgame, player_game, player_game_round

def fill_cardgame(cardgame):
    '''Función para insertar datos en el diccionario cardgame'''
    cardgame['rounds'] = context_game['rounds']
    cardgame['end_hour'] = datetime.datetime.now()

def fill_player_game(player_game,playerID):
    '''Función para insertar datos en el diccionario player_game'''
    gameID = context_game['id_game']
    player_game[gameID]['initial_card_id'] = players[playerID]['initialCard']
    player_game[gameID]['starting_points'] = 20
    player_game[gameID]['ending_points'] = players[id]['points']
    

def fill_player_game_round(player_game_round,round,*fields):
    '''Función para insertar datos en el diccionario player_game_round'''
    pass

def checkMinimun2PlayerWithPoints():
    '''Función que verifica que al menos haya dos jugadores con puntos.'''
    nPlayersWithPoints = 0
    for player_id in context_game['game']:
        if players[player_id]['points'] > 0:
            nPlayersWithPoints += 1
            if nPlayersWithPoints >= 2:
                return True
    return False

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
        orderCard(id, mazo)
        humanRound(id, mazo)
    elif userInput == 5:
        standarRound(id, mazo)
    elif userInput == 6:
        pass
    
def orderCard(id, mazo):
    '''Pide una carta al jugador.'''
    print(initialString + ' Order Card')

    # Variables bloque condicional
    jugadorQuiereCarta = False
    jugadorSinCartas = len(players[id]['cards']) == 0

    # Si jugador ya tiene cartas, preguntar si quiere pedir carta
    if not jugadorSinCartas:
        posibilidadDePasarse = chanceExceedingSevenAndHalf(id, mazo)
        print(initialString + f'Chance of exceed 7,5 = {posibilidadDePasarse:.02} %')
        userInput = input(initialString + 'Do you want another card? Y/y = yes, any other key = Not')
        if userInput == 'Y' or userInput == 'y':
            jugadorQuiereCarta = True

    if jugadorQuiereCarta or jugadorSinCartas:
        # Sacar carta del mazo. Añadirla carta y puntos a jugador
        idCarta = mazo.pop[0]
        players[id]['cards'].append(idCarta)

        # Imprimir info por pantalla
        nombreCarta = context_game['cards_deck']['literal']
        print(initialString + f'The new card is {nombreCarta}')
        playerCardPoints = getPlayerCardPoints(id)
        print(initialString + f'Now you have {playerCardPoints} points')

    _ = input(initialString + 'Enter to Continue')

def getPlayerCardPoints(id):
    '''Retorna los puntos de cartas de un jugador.'''
    playerCardPoints = 0
    for idCard in players[id]['cards']:
        playerCardPoints += context_game['cards_deck']['value']
    return playerCardPoints

def distributionPointAndNewBankCandidates():
    '''Función que realiza el reparto de puntos una vez finalizada una ronda y devuelve
una lista con los candidatos a la banca ( los que tienen 7,5)'''
    pass

def printStats(idPlayer="", titulo=""):
    '''Imprime los stats de todos los jugadores de la partida.'''
    if titulo == '':
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
