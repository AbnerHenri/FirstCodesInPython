dias_alugados = int(input('Por quantos dias o carro foi alugado?'))
km_percorridos = int(input('Quantos Kilometros foram percorridos?'))

calc = (dias_alugados * 60) + (km_percorridos * 0.15)

print('O valor correspondente aos dias alugados e km percorridos é R${}' .format(calc))