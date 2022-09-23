
def verifyString(palavra_tamanho, max, min):
    """
    Verifica se a o tamanho da palavra
    está entre o número correto ou não

    -> palavra_tamanho : A palavra digitada
    -> max : Tamanho máximo da String
    -> min : Tamanho minimo da String
    """

    if palavra_tamanho > min and palavra_tamanho < max:
        print('O tamanho da palavra está conforme o esperado')
    else:
        print('O tamanho da palavra não é aceitavel')




min = int(input('Qual o mínimo de caracteres? : '))
max = int(input('Qual o máximo de caracteres? : '))

while max < min :
    max = int(input('O valor máximo deve ser maior que o valor mínimo, digite outro número : '))


palavra = input('Digite uma palavra entre {} e {} caracteres : ' .format(min, max))
palavra_tam = len(palavra)

verifyString(palavra_tam, max, min)

help(verifyString)