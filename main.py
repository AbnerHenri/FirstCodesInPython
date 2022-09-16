print('R - Residências')
print('C - Comércio')
print('I - Indústria')

instalation_type = input('Qual é o seu tipo de instalação? : ')
kWh = int(input('Qual a quantidade do kWh? : '))

if(instalation_type == 'R'):
    if(kWh <= 500):
        calc = kWh * 0.40
        print('O valor da sua conta é {:.2f}' .format(calc))
    else:
        calc = kWh * 0.65
        print('O valor da sua conta é {:.2f}'.format(calc))
elif(instalation_type == 'C'):
    if(kWh <= 100):
        calc = kWh * 0.55
        print('O valor da sua conta é {:.2f}'.format(calc))
    else:
        calc = kWh * 0.60
        print('O valor da sua conta é {:.2f}'.format(calc))
elif(instalation_type == 'I'):
    if(kWh <= 5000):
        calc = kWh * 0.55
        print('O valor da sua conta é {:.2f}'.format(calc))
    else:
        calc = kWh * 0.60
        print('O valor da sua conta é {:.2f}'.format(calc))
else:
    print('O tipo de instalação é inválido')

