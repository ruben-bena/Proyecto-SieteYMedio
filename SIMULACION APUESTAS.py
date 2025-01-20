import random

cartas = {
    "O01": {"nombre": "As de Oros", "value": 1, "priority": 4, "RealValue": 1},
    "O02": {"nombre": "Dos de Oros", "value": 2, "priority": 4, "RealValue": 2},
    "O03": {"nombre": "Tres de Oros", "value": 3, "priority": 4, "RealValue": 3},
    "O04": {"nombre": "Cuatro de Oros", "value": 4, "priority": 4, "RealValue": 4},
    "O05": {"nombre": "Cinco de Oros", "value": 5, "priority": 4, "RealValue": 5},
    "O06": {"nombre": "Seis de Oros", "value": 6, "priority": 4, "RealValue": 6},
    "O07": {"nombre": "Siete de Oros", "value": 7, "priority": 4, "RealValue": 7},
    "O08": {"nombre": "Ocho de Oros", "value": 0.5, "priority": 4, "RealValue": 8},
    "O09": {"nombre": "Nueve de Oros", "value": 0.5, "priority": 4, "RealValue": 9},
    "O10": {"nombre": "Sota de Oros", "value": 0.5, "priority": 4, "RealValue": 10},
    "O11": {"nombre": "Caballo de Oros", "value": 0.5, "priority": 4, "RealValue": 11},
    "O12": {"nombre": "Rey de Oros", "value": 0.5, "priority": 4, "RealValue": 12},
    "C01": {"nombre": "As de Copas", "value": 1, "priority": 3, "RealValue": 1},
    "C02": {"nombre": "Dos de Copas", "value": 2, "priority": 3, "RealValue": 2},
    "C03": {"nombre": "Tres de Copas", "value": 3, "priority": 3, "RealValue": 3},
    "C04": {"nombre": "Cuatro de Copas", "value": 4, "priority": 3, "RealValue": 4},
    "C05": {"nombre": "Cinco de Copas", "value": 5, "priority": 3, "RealValue": 5},
    "C06": {"nombre": "Seis de Copas", "value": 6, "priority": 3, "RealValue": 6},
    "C07": {"nombre": "Siete de Copas", "value": 7, "priority": 3, "RealValue": 7},
    "C08": {"nombre": "Ocho de Copas", "value": 0.5, "priority": 3, "RealValue": 8},
    "C09": {"nombre": "Nueve de Copas", "value": 0.5, "priority": 3, "RealValue": 9},
    "C10": {"nombre": "Sota de Copas", "value": 0.5, "priority": 3, "RealValue": 10},
    "C11": {"nombre": "Caballo de Copas", "value": 0.5, "priority": 3, "RealValue": 11},
    "C12": {"nombre": "Rey de Copas", "value": 0.5, "priority": 3, "RealValue": 12},
    "E01": {"nombre": "As de Espadas", "value": 1, "priority": 2, "RealValue": 1},
    "E02": {"nombre": "Dos de Espadas", "value": 2, "priority": 2, "RealValue": 2},
    "E03": {"nombre": "Tres de Espadas", "value": 3, "priority": 2, "RealValue": 3},
    "E04": {"nombre": "Cuatro de Espadas", "value": 4, "priority": 2, "RealValue": 4},
    "E05": {"nombre": "Cinco de Espadas", "value": 5, "priority": 2, "RealValue": 5},
    "E06": {"nombre": "Seis de Espadas", "value": 6, "priority": 2, "RealValue": 6},
    "E07": {"nombre": "Siete de Espadas", "value": 7, "priority": 2, "RealValue": 7},
    "E08": {"nombre": "Ocho de Espadas", "value": 0.5, "priority": 2, "RealValue": 8},
    "E09": {"nombre": "Nueve de Espadas", "value": 0.5, "priority": 2, "RealValue": 9},
    "E10": {"nombre": "Sota de Espadas", "value": 0.5, "priority": 2, "RealValue": 10},
    "E11": {"nombre": "Caballo de Espadas", "value": 0.5, "priority": 2, "RealValue": 11},
    "E12": {"nombre": "Rey de Espadas", "value": 0.5, "priority": 2, "RealValue": 12},
    "B01": {"nombre": "As de Bastos", "value": 1, "priority": 1, "RealValue": 1},
    "B02": {"nombre": "Dos de Bastos", "value": 2, "priority": 1, "RealValue": 2},
    "B03": {"nombre": "Tres de Bastos", "value": 3, "priority": 1, "RealValue": 3},
    "B04": {"nombre": "Cuatro de Bastos", "value": 4, "priority": 1, "RealValue": 4},
    "B05": {"nombre": "Cinco de Bastos", "value": 5, "priority": 1, "RealValue": 5},
    "B06": {"nombre": "Seis de Bastos", "value": 6, "priority": 1, "RealValue": 6},
    "B07": {"nombre": "Siete de Bastos", "value": 7, "priority": 1, "RealValue": 7},
    "B08": {"nombre": "Ocho de Bastos", "value": 0.5, "priority": 1, "RealValue": 8},
    "B09": {"nombre": "Nueve de Bastos", "value": 0.5, "priority": 1, "RealValue": 9},
    "B10": {"nombre": "Sota de Bastos", "value": 0.5, "priority": 1, "RealValue": 10},
    "B11": {"nombre": "Caballo de Bastos", "value": 0.5, "priority": 1, "RealValue": 11},
    "B12": {"nombre": "Rey de Bastos", "value": 0.5, "priority": 1, "RealValue": 12}
}

players = {
    "11115555A": {"name": "Bot1", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": "", "points": 20, "cards": [], "roundsPoints": 0},
    "22224444B": {"name": "Pedro", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": "", "points": 20, "cards": [], "roundsPoints": 0},
    "55557777C": {"name": "Bot2", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": "", "points": 15, "cards": [], "roundsPoints": 0},
    "66668888D": {"name": "Pablo", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": "", "points": 25, "cards": [], "roundsPoints": 0},
}
def resetPoints(players):
    for player_id in players:
        players[player_id]["points"] = 20
resetPoints(players)

import random

def setBets(players):
    '''Función que establece las apuestas de cada jugador en función del tipo de jugador.'''
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
setBets(players)

print("\nEstado final de las apuestas:")
for player_id, player_data in players.items():
    print(f"{player_data['name']} ha apostado {player_data['bet']} puntos.")
input("Enter to continue")

cabecera = ("DATOS POR PARTIDA".center(115, "=") + "\n" + "Name".rjust(10) + "Human".rjust(10) + "Priority".rjust(15)
    + "Type".rjust(10) + "Bank".rjust(10) + "Bet".rjust(10) + "Points".rjust(10) + "Cards".rjust(20)
    + "Roundpoints".rjust(15) + "\n" + "*".center(115, "="))


datos = ""
keys = list(players.keys())
for i in range(len(keys)):
    player_id = keys[i]
    player = players[player_id]
    cards = ""
    for j in range(len(player["cards"])):
        if j > 0:
            cards += ";"
        cards += player["cards"][j]

    datos += (player["name"].rjust(10) + str(player["human"]).rjust(10) + str(player["priority"]).rjust(15)
        + str(player["type"]).rjust(10) + str(player["bank"]).rjust(10) + str(player["bet"]).rjust(10)
        + str(player["points"]).rjust(10) + cards.rjust(20)+ str(player["roundsPoints"]).rjust(15) + "\n")

tabla = cabecera + "\n" + datos
print(tabla)




