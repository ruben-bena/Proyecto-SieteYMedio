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