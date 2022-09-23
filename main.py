
def FatorialNumber(num):
    """
    A função recebe um número inteiro, após isso
    a função multiplica o número por todos os seu antecessores
    até 1
    """
    for i in range(1, num, 1):
        num *= i
    print(num)

number = int(input('Digite um número para ver o seu fatorial : '))
FatorialNumber(number)

help(FatorialNumber)