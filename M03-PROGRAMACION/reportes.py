
from funciones import *

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
        print("En proceso")
        input("Enter para continuar")
        reports()

    elif userInput == 2:
        cabecera = (" APUESTA MÁS ALTA POR PARTIDA ".center(85, "=") + "\n" + "ID Partida".ljust(15) +  "ID Jugador".rjust(15) +
                "Apuesta Más Alta".rjust(30) +   "\n" + "*".center(85, "="))

        cursor = BBDDconnect()
        cursor.execute("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));")
        cursor.execute("select * from informe_2")
        results = cursor.fetchall()
        print(cabecera)
        for row in results:
            print(str(row[0]).ljust(15) + str(row[1]).rjust(15)+str(row[2]).rjust(30))

        
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
                "Rondas Ganadas".rjust(30) + "\n" +"*".center(60, "="))

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

        cabecera = (" USUARIOS BANCAS POR PARTIDA".center(60, "=") + "\n" +"ID Partida".ljust(20) +
                "Usuarios Banca".rjust(30) + "\n" +"*".center(60, "="))

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

        cabecera = (" APUESTA MEDIA POR PARTIDA ".center(60, "=") + "\n" +"ID Partida".ljust(20) +
                "Apuesta Media".rjust(30) +"\n" +"*".center(60, "="))

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

        cabecera = ( " APUESTA MEDIA PRIMERA RONDA ".center(60, "=") + "\n" + "ID Partida".ljust(20) +"Apuesta Media Primera Ronda".rjust(30) +
                "\n" +"*".center(60, "=") )

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

        cabecera = (" APUESTA MEDIA ÚLTIMA RONDA ".center(60, "=") + "\n" +"ID Partida".ljust(20) +
                "Apuesta Media Última Ronda".rjust(30) +"\n" +"*".center(60, "="))

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
        #mainMenu()

reports()