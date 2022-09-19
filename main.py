valor = int(input('Qual o valor desejado? : '))

print('Cédulas disponiveis')
print('1 - $100,00')
print('2 - $50,00')
print('3 - $20,00')
print('4 - $10,00')
print('5 - $1,00')

cedula = int(input('Escolha o número que contenha o valor da cédula desejada : '))

if (cedula == 1):
    calc = valor // 100
    print('O valor desejado pode ser pago com {} cédulas de $100' .format(calc))
elif (cedula == 2):
    calc = valor // 50
    print('O valor desejado pode ser pago com {} cédulas de $50' .format(calc))
elif (cedula == 3):
    calc = valor // 20
    print('O valor desejado pode ser pago com {} cédulas de $20'.format(calc))
elif (cedula == 4):
    calc = valor // 10
    print('O valor desejado pode ser pago com {} cédulas de $10'.format(calc))
elif (cedula == 5):
    calc = valor // 1
    print('O valor desejado pode ser pago com {} cédulas de $1'.format(calc))
else :
    print('O valor não foi reconhecido')