#SET GAME PLAYERS

# Variables de prueba
'''player = {"22223333H":{"name":"Anna","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundsPoints":0},
          "11115555A":{"name":"B_Mario","human":False,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundsPoints":0},
          "22224444B":{"name":"Pedro","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundsPoints":0},
          "55557777C":{"name":"B_Alberto","human":False,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundsPoints":0},
          "66668888D":{"name":"Sara","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundsPoints":0},
          "77774444E":{"name":"B_Pablo","human":False,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundsPoints":0,
          "44448888F":{"name":"Milán","human":True,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundsPoints":0},
          "11114444G":{"name":"B_Isabella","human":False,"bank":False,"initialCard":"","priority":0,"type":40,"bet":4,"points":0,"cards":[],"roundsPoints":0},
           }}

seleccionados = {
    "11114444Z": {"name": "Bot1", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4, "points": 0, "cards": [], "roundsPoints": 0},
    "22229999V": {"name": "Bot2", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4, "points": 0, "cards": [], "roundsPoints": 0},
    "17172525A": {"name": "Poveda", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4, "points": 0, "cards": [], "roundsPoints": 0},
}

player = {
    "22223333H": {"name": "Anna", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4,
                  "points": 0, "cards": [], "roundsPoints": 0},
    "11115555A": {"name": "B_Mario", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": 4, "points": 0, "cards": [], "roundsPoints": 0},
    "22224444B": {"name": "Pedro", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4,
                  "points": 0, "cards": [], "roundsPoints": 0},
    "55557777C": {"name": "B_Alberto", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": 4, "points": 0, "cards": [], "roundsPoints": 0},
    "66668888D": {"name": "Sara", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4,
                  "points": 0, "cards": [], "roundsPoints": 0},
    "77774444E": {"name": "B_Pablo", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": 4, "points": 0, "cards": [], "roundsPoints": 0},
    "44448888F": {"name": "Milán", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4,
                  "points": 0, "cards": [], "roundsPoints": 0},
    "11114444G": {"name": "B_Isabella", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": 4, "points": 0, "cards": [], "roundsPoints": 0},
}

seleccionados = {
    "11114444Z": {"name": "Bot1", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4,
                  "points": 0, "cards": [], "roundsPoints": 0},
    "22229999V": {"name": "Bot2", "human": False, "bank": False, "initialCard": "", "priority": 0, "type": 40, "bet": 4,
                  "points": 0, "cards": [], "roundsPoints": 0},
    "17172525A": {"name": "Poveda", "human": True, "bank": False, "initialCard": "", "priority": 0, "type": 40,
                  "bet": 4, "points": 0, "cards": [], "roundsPoints": 0},
}'''

def ya_seleccionados(players, seleccionados):
    cabecera2 = "Jugadores Dentro Del Juego".center(60, "=") + "\n"
    datos = ""
    '''for key, jugador in seleccionados.items():
        datos += (jugador["name"].ljust(20) + str(jugador["human"]).center(20)+ str(jugador["type"]).rjust(20) + "\n")'''
    for player_id in seleccionados:
        name = players[player_id]['name']
        human = str(players[player_id]['human'])
        type = str(players[player_id]['profile'])
        datos += (name.ljust(20) + human.center(20)+ type.rjust(20) + "\n")

    total = cabecera2 + datos
    print(total)
    input("Enter Para Continuar")
    '''return total'''
'''print(ya_seleccionados(seleccionados))
input("Enter Para Continuar")'''

def print_jugadores(player):
    cabecera = (((" SELECT PLAYER ".center(140, "=") + "\n" + "Bot Players".center(60) + "||".center(20)
                  + "Human Players".center(60) + "\n" + " || ".center(140, "-")) + "\n"
                 + "ID".ljust(20)) + "Name".center(20) + "Type".rjust(20) + "||".center(20)
                + "ID".ljust(20) + "Name".center(20) + "Type".rjust(20)) + "\n" + " || ".center(140, "=")

    bots = []
    humans = []

    for id in player:
        info = player[id]
        if info["human"]:
            humans.append((id, info))
        else:
            bots.append((id, info))

    bots_len = len(bots)
    humans_len = len(humans)

    if bots_len > humans_len:
        for i in range(bots_len - humans_len):
            humans.append(("", {"name": "", "type": ""}))
    elif humans_len > bots_len:
        for i in range(humans_len - bots_len):
            bots.append(("", {"name": "", "type": ""}))

    print(cabecera)

    i = 0
    while i < len(bots):
        bot_id, bot_info = bots[i]
        human_id, human_info = humans[i]

        bot_line = bot_id.ljust(20) + bot_info['name'].center(20) + str(bot_info['profile']).rjust(20)
        human_line = human_id.ljust(20) + human_info["name"].center(20) + str(human_info['profile']).rjust(20)

        print(bot_line + "||".center(20) + human_line)
        i += 1

'''print_jugadores(player)
input("Enter Para Continuar")'''

def agregar_jugador(seleccionados, player, key):
    if key in player and key not in seleccionados:
        seleccionados.append(key)
        print("Jugador", player[key]['name']," agregado a seleccionados.\nJugador ID:",key)
        ya_seleccionados(seleccionados)
        input("Enter Para Continuar")
    else:
        print("Error: Jugador con ID", key,"no existe")

def eliminar_jugador(seleccionados, player, key):
    if key in seleccionados:
        eliminado = seleccionados.pop(key)
        nombreJugadorEliminado = player[eliminado]['name']
        print("Jugador", nombreJugadorEliminado, "eliminado de seleccionados.")
        ya_seleccionados(seleccionados)
        input("Enter Para Continuar")
    else:
        print("Error: Jugador con ID" ,key ,"no está en 'seleccionados'.")

def menu_principal(player, seleccionados):
    while True:
        menu = "- Escribe el ID del jugador para agregarlo." + "\n- Escribe '-ID' para eliminar un jugador. " + ("\n- Escribe '-1' para salir.")
        print(menu)

        opcion = input("Tu elección: ")

        if opcion == "-1":
            '''print("Menú Principal")'''
            break
        elif opcion.startswith("-"):
            key = opcion[1:]
            eliminar_jugador(seleccionados, key)
        else:
            agregar_jugador(seleccionados, player, opcion)

if __name__ == '__main__':
    menu_principal()