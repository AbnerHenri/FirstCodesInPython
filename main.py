number1 = int(input('Primeiro dado : '))
number2 = int(input('Segundo Dado : '))

equacao = input('Qual a operação : ')

if equacao == 'Soma' :
    soma = number1 + number2
    print('A soma dos dados é {}' .format(soma))
elif equacao == 'Subtração' :
    sub = number1 - number2
    print('A subtração dos dados é {}' .format(sub))
elif equacao == 'Multiplicação' :
    mult = number1 * number2
    print('A multiplicação dos dados é {}' .format(mult))
elif equacao == 'Divisão' :
    div = number1 / number2
    print('A divisão dos dados é {}' .format(div))
else :
    print('Não conseguimos entender o tipo da operação')
