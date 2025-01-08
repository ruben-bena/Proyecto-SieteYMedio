import os

def clearScreen() -> None:
    '''Limpiamos la pantalla de la terminal.

    Retorna: No retorna nada'''
    if os.name == 'nt':     # Si estàs a Windows
        os.system('cls')
    else:                   # Si estàs a Linux o macOS
        os.system('clear')

def validaInput(inputUsuario, posiblesInputs):
    if inputUsuario not in posiblesInputs:

        print('INVALID OPTION'.center(140, '='))
        _ = input('Press enter to continue'.center(140))
        return False
    return True
'''
def imprimeNombreJuego():
    stringg = "
    ____  ____  _  _  ____  __ _         __   __ _  ____        _  _   __   __    ____                                                 
    / ___)(  __)/ )( \(  __)(  ( \       / _\ (  ( \(    \      / )( \ / _\ (  )  (  __)                                                
    \___ \ ) _) \ \/ / ) _) /    /      /    \/    / ) D (      ) __ (/    \/ (_/\ ) _)                                                 
    (____/(____) \__/ (____)\_)__)      \_/\_/\_)__)(____/      \_)(_/\_/\_/\____/(__)                                                  
    ____  ____  ____  ____  _  _  ____        ____  ____  ____  ____   __   ____   __   ____         __          __   __    __     __  
    (  __)/ ___)(_  _)(  __)/ )( \(  __)      (_  _)(  __)(  _ \(  _ \ / _\ (    \ / _\ / ___)       (  )        (  ) (  )  (  )   / _\ 
    ) _) \___ \  )(   ) _) \ \/ / ) _)         )(   ) _)  )   / )   //    \ ) D (/    \\___ \        )(          )(  / (_/\/ (_/\/    \
    (____)(____/ (__) (____) \__/ (____)       (__) (____)(__\_)(__\_)\_/\_/(____/\_/\_/(____/       (__)        (__) \____/\____/\_/\_/
    "
    print(stringg)'''

def menuPrincipal():
    '''Menú principal del juego. Para que empiece la partida, debe haber mínimo 2 jugadores
    y hay que escoger una baraja de cartas (en Settings).
    
    Ancho de texto: 140'''
    validInputs = (1,2,3,4,5,6)
    initialString = ' ' * 60
    options = (
        '1) Add/Remove/Show Players',
        '2) Settings',
        '3) Play Game',
        '4) Ranking',
        '5) Reports',
        '6) Exit')
    while True:
        clearScreen()
        print('AQUÍ IRÁ EL ENCABEZADO')
        for option in options:
            print(initialString + option.ljust(80))
        userInput = input(initialString + 'Option: ')
        if userInput.isdigit():
            userInput = int(userInput)
        validOption = validaInput(userInput, validInputs)
        if validOption:
            break
        

if __name__ == '__main__':
    menuPrincipal()