soma = 0
cont = 1

while cont <= 5:
    nota = float(input('Digite a nota {}º : ' .format(cont)))
    soma += nota
    cont += 1

media = soma / 5
print('O valor total da média foi : {}' .format(media))
