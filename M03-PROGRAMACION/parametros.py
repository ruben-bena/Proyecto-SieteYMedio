lineSize = 140
lineStart = lineSize // 2 - 10
initialString = ' ' * lineStart
PRUEBAS = True

# Variables para pruebas:
playersPrueba = {
    '11111111A': {
        'name': 'pepe',
        'human': True,
        'bank': '',
        'initialCard': '',
        'priority': 0,
        'profile': 40,
        'bet': 0,
        'points': 0,
        'cards': [],
        'roundPoints': 0
    },
    '22222222B': {
        'name': 'luis',
        'human': True,
        'bank': '',
        'initialCard': '',
        'priority': 0,
        'profile': 30,
        'bet': 0,
        'points': 0,
        'cards': [],
        'roundPoints': 0
    },
    '33333333C': {
        'name': 'lola',
        'human': True,
        'bank': '',
        'initialCard': '',
        'priority': 0,
        'profile': 50,
        'bet': 0,
        'points': 0,
        'cards': [],
        'roundPoints': 0
    },
    '44444444D': {
        'name': 'bot1',
        'human': False,
        'bank': '',
        'initialCard': '',
        'priority': 0,
        'profile': 30,
        'bet': 0,
        'points': 0,
        'cards': [],
        'roundPoints': 0
    },
}

# Página para generar ASCII: https://patorjk.com/software/taag/#p=display&f=Big%20Money-ne&t=Type%20Something%20
strSevenAndHalf = '''
  /$$$$$$                                                                          /$$       /$$   /$$           /$$  /$$$$$$ 
 /$$__  $$                                                                        | $$      | $$  | $$          | $$ /$$__  $$
| $$  \__/  /$$$$$$  /$$    /$$ /$$$$$$  /$$$$$$$         /$$$$$$  /$$$$$$$   /$$$$$$$      | $$  | $$  /$$$$$$ | $$| $$  \__/
|  $$$$$$  /$$__  $$|  $$  /$$//$$__  $$| $$__  $$       |____  $$| $$__  $$ /$$__  $$      | $$$$$$$$ |____  $$| $$| $$$$    
 \____  $$| $$$$$$$$ \  $$/$$/| $$$$$$$$| $$  \ $$        /$$$$$$$| $$  \ $$| $$  | $$      | $$__  $$  /$$$$$$$| $$| $$_/    
 /$$  \ $$| $$_____/  \  $$$/ | $$_____/| $$  | $$       /$$__  $$| $$  | $$| $$  | $$      | $$  | $$ /$$__  $$| $$| $$      
|  $$$$$$/|  $$$$$$$   \  $/  |  $$$$$$$| $$  | $$      |  $$$$$$$| $$  | $$|  $$$$$$$      | $$  | $$|  $$$$$$$| $$| $$      
 \______/  \_______/    \_/    \_______/|__/  |__/       \_______/|__/  |__/ \_______/      |__/  |__/ \_______/|__/|__/      
'''

strAddRemovePlayers = '''
 /$$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$$        /$$$$$$$  /$$                                                  
| $$__  $$| $$__  $$| $$__  $$| $$__  $$      | $$__  $$| $$                                                  
| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$      | $$  \ $$| $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$$
| $$$$$$$ | $$$$$$$ | $$  | $$| $$  | $$      | $$$$$$$/| $$ |____  $$| $$  | $$ /$$__  $$ /$$__  $$ /$$_____/
| $$__  $$| $$__  $$| $$  | $$| $$  | $$      | $$____/ | $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/|  $$$$$$ 
| $$  \ $$| $$  \ $$| $$  | $$| $$  | $$      | $$      | $$ /$$__  $$| $$  | $$| $$_____/| $$       \____  $$
| $$$$$$$/| $$$$$$$/| $$$$$$$/| $$$$$$$/      | $$      | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$       /$$$$$$$/
|_______/ |_______/ |_______/ |_______/       |__/      |__/ \_______/ \____  $$ \_______/|__/      |_______/ 
                                                                       /$$  | $$                              
                                                                      |  $$$$$$/                              
                                                                       \______/                               
'''

strNewHumanPlayer = '''
 /$$   /$$                               /$$   /$$ /$$   /$$ /$$      /$$  /$$$$$$  /$$   /$$       /$$$$$$$  /$$                                        
| $$$ | $$                              | $$  | $$| $$  | $$| $$$    /$$$ /$$__  $$| $$$ | $$      | $$__  $$| $$                                        
| $$$$| $$  /$$$$$$  /$$  /$$  /$$      | $$  | $$| $$  | $$| $$$$  /$$$$| $$  \ $$| $$$$| $$      | $$  \ $$| $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$ 
| $$ $$ $$ /$$__  $$| $$ | $$ | $$      | $$$$$$$$| $$  | $$| $$ $$/$$ $$| $$$$$$$$| $$ $$ $$      | $$$$$$$/| $$ |____  $$| $$  | $$ /$$__  $$ /$$__  $$
| $$  $$$$| $$$$$$$$| $$ | $$ | $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$  $$$$      | $$____/ | $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/
| $$\  $$$| $$_____/| $$ | $$ | $$      | $$  | $$| $$  | $$| $$\  $ | $$| $$  | $$| $$\  $$$      | $$      | $$ /$$__  $$| $$  | $$| $$_____/| $$      
| $$ \  $$|  $$$$$$$|  $$$$$/$$$$/      | $$  | $$|  $$$$$$/| $$ \/  | $$| $$  | $$| $$ \  $$      | $$      | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|__/  \__/ \_______/ \_____/\___/       |__/  |__/ \______/ |__/     |__/|__/  |__/|__/  \__/      |__/      |__/ \_______/ \____  $$ \_______/|__/      
                                                                                                                            /$$  | $$                    
                                                                                                                           |  $$$$$$/                    
                                                                                                                            \______/                     
'''

strNewBotPlayer = '''
 /$$   /$$                               /$$$$$$$   /$$$$$$  /$$$$$$$$       /$$$$$$$  /$$                                        
| $$$ | $$                              | $$__  $$ /$$__  $$|__  $$__/      | $$__  $$| $$                                        
| $$$$| $$  /$$$$$$  /$$  /$$  /$$      | $$  \ $$| $$  \ $$   | $$         | $$  \ $$| $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$ 
| $$ $$ $$ /$$__  $$| $$ | $$ | $$      | $$$$$$$ | $$  | $$   | $$         | $$$$$$$/| $$ |____  $$| $$  | $$ /$$__  $$ /$$__  $$
| $$  $$$$| $$$$$$$$| $$ | $$ | $$      | $$__  $$| $$  | $$   | $$         | $$____/ | $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/
| $$\  $$$| $$_____/| $$ | $$ | $$      | $$  \ $$| $$  | $$   | $$         | $$      | $$ /$$__  $$| $$  | $$| $$_____/| $$      
| $$ \  $$|  $$$$$$$|  $$$$$/$$$$/      | $$$$$$$/|  $$$$$$/   | $$         | $$      | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|__/  \__/ \_______/ \_____/\___/       |_______/  \______/    |__/         |__/      |__/ \_______/ \____  $$ \_______/|__/      
                                                                                                     /$$  | $$                    
                                                                                                    |  $$$$$$/                    
                                                                                                     \______/                     
'''

strSettings = '''
  /$$$$$$              /$$     /$$     /$$                              
 /$$__  $$            | $$    | $$    |__/                              
| $$  \__/  /$$$$$$  /$$$$$$ /$$$$$$   /$$ /$$$$$$$   /$$$$$$   /$$$$$$$
|  $$$$$$  /$$__  $$|_  $$_/|_  $$_/  | $$| $$__  $$ /$$__  $$ /$$_____/
 \____  $$| $$$$$$$$  | $$    | $$    | $$| $$  \ $$| $$  \ $$|  $$$$$$ 
 /$$  \ $$| $$_____/  | $$ /$$| $$ /$$| $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$/|  $$$$$$$  |  $$$$/|  $$$$/| $$| $$  | $$|  $$$$$$$ /$$$$$$$/
 \______/  \_______/   \___/   \___/  |__/|__/  |__/ \____  $$|_______/ 
                                                     /$$  \ $$          
                                                    |  $$$$$$/          
                                                     \______/           
'''

strSetCardsdeck = '''
 /$$$$$$$                      /$$                        /$$$$$$         /$$$$$$                            /$$          
| $$__  $$                    | $$                       /$$__  $$       /$$__  $$                          | $$          
| $$  \ $$  /$$$$$$   /$$$$$$$| $$   /$$        /$$$$$$ | $$  \__/      | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$$
| $$  | $$ /$$__  $$ /$$_____/| $$  /$$/       /$$__  $$| $$$$          | $$       |____  $$ /$$__  $$ /$$__  $$ /$$_____/
| $$  | $$| $$$$$$$$| $$      | $$$$$$/       | $$  \ $$| $$_/          | $$        /$$$$$$$| $$  \__/| $$  | $$|  $$$$$$ 
| $$  | $$| $$_____/| $$      | $$_  $$       | $$  | $$| $$            | $$    $$ /$$__  $$| $$      | $$  | $$ \____  $$
| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$ \  $$      |  $$$$$$/| $$            |  $$$$$$/|  $$$$$$$| $$      |  $$$$$$$ /$$$$$$$/
|_______/  \_______/ \_______/|__/  \__/       \______/ |__/             \______/  \_______/|__/       \_______/|_______/ 
'''

strSetMaxRounds = '''
  /$$$$$$              /$$           /$$      /$$                           /$$$$$$$                                      /$$          
 /$$__  $$            | $$          | $$$    /$$$                          | $$__  $$                                    | $$          
| $$  \__/  /$$$$$$  /$$$$$$        | $$$$  /$$$$  /$$$$$$  /$$   /$$      | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$$  /$$$$$$$
|  $$$$$$  /$$__  $$|_  $$_/        | $$ $$/$$ $$ |____  $$|  $$ /$$/      | $$$$$$$/ /$$__  $$| $$  | $$| $$__  $$ /$$__  $$ /$$_____/
 \____  $$| $$$$$$$$  | $$          | $$  $$$| $$  /$$$$$$$ \  $$$$/       | $$__  $$| $$  \ $$| $$  | $$| $$  \ $$| $$  | $$|  $$$$$$ 
 /$$  \ $$| $$_____/  | $$ /$$      | $$\  $ | $$ /$$__  $$  >$$  $$       | $$  \ $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$ \____  $$
|  $$$$$$/|  $$$$$$$  |  $$$$/      | $$ \/  | $$|  $$$$$$$ /$$/\  $$      | $$  | $$|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$ /$$$$$$$/
 \______/  \_______/   \___/        |__/     |__/ \_______/|__/  \__/      |__/  |__/ \______/  \______/ |__/  |__/ \_______/|_______/ 
'''

strRanking = '''
 /$$$$$$$                      /$$       /$$                    
| $$__  $$                    | $$      |__/                    
| $$  \ $$  /$$$$$$  /$$$$$$$ | $$   /$$ /$$ /$$$$$$$   /$$$$$$ 
| $$$$$$$/ |____  $$| $$__  $$| $$  /$$/| $$| $$__  $$ /$$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$/ | $$| $$  \ $$| $$  \ $$
| $$  \ $$ /$$__  $$| $$  | $$| $$_  $$ | $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$| $$ \  $$| $$| $$  | $$|  $$$$$$$
|__/  |__/ \_______/|__/  |__/|__/  \__/|__/|__/  |__/ \____  $$
                                                       /$$  \ $$
                                                      |  $$$$$$/
                                                       \______/ 
'''

strReports = '''
 /$$$$$$$                                            /$$             
| $$__  $$                                          | $$             
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$$$$$$
| $$$$$$$/ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/  /$$_____/
| $$__  $$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \__/  | $$   |  $$$$$$ 
| $$  \ $$| $$_____/| $$  | $$| $$  | $$| $$        | $$ /$$\____  $$
| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$/| $$        |  $$$$//$$$$$$$/
|__/  |__/ \_______/| $$____/  \______/ |__/         \___/ |_______/ 
                    | $$                                             
                    | $$                                             
                    |__/                                             
'''

strPlayerStats = '''
 /$$$$$$$  /$$                                                /$$$$$$   /$$                 /$$             
| $$__  $$| $$                                               /$$__  $$ | $$                | $$             
| $$  \ $$| $$  /$$$$$$  /$$   /$$  /$$$$$$   /$$$$$$       | $$  \__//$$$$$$    /$$$$$$  /$$$$$$   /$$$$$$$
| $$$$$$$/| $$ |____  $$| $$  | $$ /$$__  $$ /$$__  $$      |  $$$$$$|_  $$_/   |____  $$|_  $$_/  /$$_____/
| $$____/ | $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/       \____  $$ | $$      /$$$$$$$  | $$   |  $$$$$$ 
| $$      | $$ /$$__  $$| $$  | $$| $$_____/| $$             /$$  \ $$ | $$ /$$ /$$__  $$  | $$ /$$\____  $$
| $$      | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$            |  $$$$$$/ |  $$$$/|  $$$$$$$  |  $$$$//$$$$$$$/
|__/      |__/ \_______/ \____  $$ \_______/|__/             \______/   \___/   \_______/   \___/ |_______/ 
                         /$$  | $$                                                                          
                        |  $$$$$$/                                                                          
                         \______/                                                                           
'''

strGameStats = '''
  /$$$$$$                                           /$$$$$$   /$$                 /$$             
 /$$__  $$                                         /$$__  $$ | $$                | $$             
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \__//$$$$$$    /$$$$$$  /$$$$$$   /$$$$$$$
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      |  $$$$$$|_  $$_/   |____  $$|_  $$_/  /$$_____/
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$       \____  $$ | $$      /$$$$$$$  | $$   |  $$$$$$ 
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/       /$$  \ $$ | $$ /$$ /$$__  $$  | $$ /$$\____  $$
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/ |  $$$$/|  $$$$$$$  |  $$$$//$$$$$$$/
 \______/  \_______/|__/ |__/ |__/ \_______/       \______/   \___/   \_______/   \___/ |_______/ 
'''

strGameOver = '''
  /$$$$$$                                           /$$$$$$                               
 /$$__  $$                                         /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$       | $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ 
| $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$      | $$  | $$|  $$  /$$//$$__  $$ /$$__  $$
| $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$      | $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/      | $$  | $$  \  $$$/ | $$_____/| $$      
|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$      |  $$$$$$/   \  $/  |  $$$$$$$| $$      
 \______/  \_______/|__/ |__/ |__/ \_______/       \______/     \_/    \_______/|__/      
'''