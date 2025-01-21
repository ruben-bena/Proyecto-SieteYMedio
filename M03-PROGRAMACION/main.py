from parametros import *
from datos import *
#from playGame import *
from funciones import *

def main():
    context_game['game'] = []
    context_game['cards_deck'] = {}
    players = loadBBDD_players()
    mainMenu()

if __name__ == '__main__':
    main()