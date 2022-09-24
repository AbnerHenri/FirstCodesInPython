
def Add(product, price, quant):
    try:
        a = open('Products.txt', 'at')
    except:
        print('Houve um erro')
    else:
        a.write('Product : {} | Price : R${} | Quantility : {} \r\n' .format(product, price, quant))
        print('Produto Cadastrado com sucesso')
    finally:
        a.close()

def List():
    try:
        a = open('Products.txt', 'rt')
    except:
        print('Houve um erro')
    else:
        print(a.read())
    finally:
        a.close()


# Principal Program

while True:

    product = str(input('Cadastre um produto : '))
    if(product == 'Sair') : break
    elif(product == 'Listar') : List()

    price = input('Informe o preço : ')
    if(price == 'Sair') : break
    elif(price == 'Listar') : List()

    quant = int(input('Informe a quantidade : '))
    if(quant == 'Sair') : break
    elif(quant == 'Listar') : List()

    Add(product, price, quant)

