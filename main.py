def Soma(*number):
    soma = 0
    print('Tupla : {}'.format(number))

    for i in number:
        soma += i
    return soma


print('Resultado : {}'  .format(Soma(1, 4, 7, 15,28)))
