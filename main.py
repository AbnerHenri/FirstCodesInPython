def Add(game, console, archive):
    try:
        myArchive = open(archive, 'at')
    except:
        print('Houve um erro')
    else:
        myArchive.write('{} : {} \r\n'.format(game, console))
        print('Arquivo cadastrado com sucesso')
    finally:
        myArchive.close()


def List(archive):
    try:
        a = open(archive, 'rt')
    except:
        print('Houve um erro')
    else:
        print('Redirecionando para arquivo...')
        print(a.read())
    finally:
        a.close()

def Validation():
    question = int(input('Seleciona uma das opções : '))
    while (question < 1) or (question > 3):
        question = int(input('Número inválido, selecione uma opção : '))
    return question

def FindArchive(archive):
    try:
        ar = open(archive, 'rt')
        ar.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CreateArchive(archive):
    try:
        ar = open(archive, 'at+')
        ar.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo Criado com sucesso')


# Principal Program

comand = ''
archive = 'games.txt'

if FindArchive(archive):
    print('Arquivo localizado')
else:
    print('Criando Arquivo...')
    CreateArchive(archive)

while comand != 'Sair' or 3:
    print('-' * 10 + 'Menu' + '-' * 10)
    print('1 - Adicionar novo Item')
    print('2 - Listar Cadastrados')
    print('3 - Sair')

    op = Validation()
    if op == 1 :
        gameName = str(input('Digite o nome do jogo : '))
        consoleName = str(input('Digite a plataforma do jogo: '))
        Add(gameName, consoleName, archive)
    elif op == 2 :
        List(archive)
    elif op == 3 :
        print('Encerrando ...\n\n')
        break
