
def verifyString(palavra_tamanho, max, min):
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
