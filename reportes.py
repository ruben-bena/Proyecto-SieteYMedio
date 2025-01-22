
from funciones import *

jugadores_cartas_iniciales = [  # --> Vista Num1
    {"id_jugador": "1","palo_mas_repetido": "Copas",
        "carta_mas_repetida": "C11","veces_repetida": 4,
        "total_partidas": 5,
    },
    {"id_jugador": "2","palo_mas_repetido": "Espadas",
        "carta_mas_repetida": "E05","veces_repetida": 3,
        "total_partidas": 4,
    },
    {"id_jugador": "3","palo_mas_repetido": "Oros",
        "carta_mas_repetida": "O03","veces_repetida": 5,
        "total_partidas": 7,
    },
]

apuesta_mas_alta_por_partida = [ #--> Vista Num2
    {"id_partida": "P1", "id_jugador": "3", "apuesta_mas_alta": 17},
    {"id_partida": "P2", "id_jugador": "1", "apuesta_mas_alta": 9},
    {"id_partida": "P3", "id_jugador": "2", "apuesta_mas_alta": 8},
]

apuesta_mas_baja_por_partida = [ #--> Vista Num3
    {"id_partida": "P1", "id_jugador": "2", "apuesta_mas_baja": 1},
    {"id_partida": "P2", "id_jugador": "3", "apuesta_mas_baja": 4},
    {"id_partida": "P3", "id_jugador": "1", "apuesta_mas_baja": 5},
]

usuarios_banca_por_partida = [#Vista num7
    {"id_partida": "P1", "usuarios_banca": 1},
    {"id_partida": "P2", "usuarios_banca": 2},
    {"id_partida": "P3", "usuarios_banca": 1},
]

rondas_ganadas_banca = [ #Vista Num6
    {"id_partida": "P1", "rondas_ganadas": 2},
    {"id_partida": "P2", "rondas_ganadas": 0},
    {"id_partida": "P3", "rondas_ganadas": 1},
]

apuesta_media_por_partida = [ #Vista num8
    {"id_partida": "P1", "apuesta_media": 6},
    {"id_partida": "P2", "apuesta_media": 4},
    {"id_partida": "P3", "apuesta_media": 9},
]

apuesta_media_primera_ronda = [ #vista num9
    {"id_partida": "P1", "apuesta_media_primera_ronda": 3},
    {"id_partida": "P2", "apuesta_media_primera_ronda": 1},
    {"id_partida": "P3", "apuesta_media_primera_ronda": 7},
]

apuesta_media_ultima_ronda = [ #vista num10
    {"id_partida": "P1", "apuesta_media_ultima_ronda": 14},
    {"id_partida": "P2", "apuesta_media_ultima_ronda": 16},
    {"id_partida": "P3", "apuesta_media_ultima_ronda": 13},
]


def reports():
    '''Función que nos muestra el menú de reportes, y una vez elegida una opción, el reporte
correspondiente'''
    #pass
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
    for n in range(1,12):
        validInputReports.append(n)
    userInput = getOpt(strReports, inputOptReports, validInputReports)
    #mainMenu()
    # TODO Todas las opciones de la función
    if userInput == 1:
        cabecera = (" CARTA MÁS REPETIDA ".center(125, "=") + "\n" + "ID".ljust(10) + "Palo Más Repetido".rjust(20)
                    + "Carta Más Repetida".rjust(30) + "Veces Repetidas".rjust(30) + "Total Partidas".rjust(30)
                    + "\n" + "*".center(125, "="))
        #print(cabecera)

        datos = ""
        for jugador in jugadores_cartas_iniciales:
            datos += (jugador["id_jugador"].ljust(10) + jugador["palo_mas_repetido"].rjust(20) + jugador["carta_mas_repetida"].rjust(30) +
                    str(jugador["veces_repetida"]).rjust(30) + str(jugador["total_partidas"]).rjust(30) + "\n")

        tabla = cabecera + "\n" + datos
        print(tabla)

        input("Enter para continuar.")
        reports()

    elif userInput == 2:
        cabecera = (" APUESTA MÁS ALTA POR PARTIDA ".center(85, "=") + "\n" + "ID Partida".ljust(15) +  "ID Jugador".rjust(15) +
                "Apuesta Más Alta".rjust(30) +   "\n" + "*".center(85, "="))

        datos = ""
        for partida in apuesta_mas_alta_por_partida:
            datos += (partida["id_partida"].ljust(15) +partida["id_jugador"].rjust(15) + str(partida["apuesta_mas_alta"]).rjust(30) + "\n")

        tabla = cabecera + "\n" + datos
        print(tabla)

        input("Enter para continuar.")
        reports()

    elif userInput == 3:
        cabecera = (" APUESTA MÁS BAJA POR PARTIDA ".center(85, "=") + "\n" + "ID Partida".ljust(
            15) + "ID Jugador".rjust(15) + "Apuesta Más Baja".rjust(30) + "\n" + "*".center(85, "="))

        datos = ""
        for partida in apuesta_mas_baja_por_partida:
            datos += (partida["id_partida"].ljust(15) + partida["id_jugador"].rjust(15) + str( partida["apuesta_mas_baja"]).rjust(30) + "\n")

        tabla = cabecera + "\n" + datos
        print(tabla)

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

        cabecera = (" USUARIOS BANCAS POR PARTIDA ".center(60, "=") + "\n" + "ID Partida".ljust(20) +
                "Usuarios Banca".rjust(30) + "\n" +"*".center(60, "="))

        datos = ""
        for partida in usuarios_banca_por_partida:
            datos += (partida["id_partida"].ljust(20) +str(partida["usuarios_banca"]).rjust(30) + "\n")

        tabla = cabecera + "\n" + datos
        print(tabla)

        input("Enter para continuar")
        reports()

    elif userInput == 7:

        cabecera = (" RONDAS GANADAS POR LA BANCA ".center(60, "=") + "\n" +"ID Partida".ljust(20) +
                "Rondas Ganadas".rjust(30) + "\n" +"*".center(60, "="))

        datos = ""
        for partida in rondas_ganadas_banca:
            datos += (partida["id_partida"].ljust(20) + str(partida["rondas_ganadas"]).rjust(30) + "\n")

        tabla = cabecera + "\n" + datos
        print(tabla)

        input("Enter para continuar")
        reports()

    elif userInput == 8:

        cabecera = (" APUESTA MEDIA POR PARTIDA ".center(60, "=") + "\n" +"ID Partida".ljust(20) +
                "Apuesta Media".rjust(30) +"\n" +"*".center(60, "="))

        datos = ""
        for partida in apuesta_media_por_partida:
            datos += ( partida["id_partida"].ljust(20) + str(partida["apuesta_media"]).rjust(30) + "\n")


        tabla = cabecera + "\n" + datos
        print(tabla)

        input("Enter para continuar")
        reports()

    elif userInput == 9:

        cabecera = ( " APUESTA MEDIA PRIMERA RONDA ".center(60, "=") + "\n" + "ID Partida".ljust(20) +"Apuesta Media Primera Ronda".rjust(30) +
                "\n" +"*".center(60, "=") )
        datos = ""
        for partida in apuesta_media_primera_ronda:
            datos += ( partida["id_partida"].ljust(20) + str(partida["apuesta_media_primera_ronda"]).rjust(30) + "\n")

        tabla = cabecera + "\n" + datos
        print(tabla)

        input("Enter para continuar")
        reports()

    elif userInput == 10:

        cabecera = (" APUESTA MEDIA ÚLTIMA RONDA ".center(60, "=") + "\n" +"ID Partida".ljust(20) +
                "Apuesta Media Última Ronda".rjust(30) +"\n" +"*".center(60, "="))
        datos = ""
        for partida in apuesta_media_ultima_ronda:
            datos += ( partida["id_partida"].ljust(20) +str(partida["apuesta_media_ultima_ronda"]).rjust(30) +"\n")

        tabla = cabecera + "\n" + datos
        print(tabla)

        input("Enter para continuar")
        reports()

    elif userInput == 11:
        pass
        #mainMenu()

reports()