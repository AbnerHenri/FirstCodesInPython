
games = []


def Add(game=str, console=str):
    global games

    data = game + ' : ' + console
    games.append(data)

def List():
    global games

    for i in games:
        print('-> {}' .format(i))

def Alg():

    name = ''
    console = ''

    while name != 'Listar' or console != 'Listar':
        name = str(input('Digite o nome de um game : '))
        if name == 'Listar': break

        console = str(input('Digite o nome de um console : '))
        if console == 'Listar': break

        Add(name, console)

    List()



Alg()

