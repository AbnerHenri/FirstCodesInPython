
def verifyString(palavra_tamanho):
    if palavra_tamanho > 10 and palavra_tamanho < 20:
        print('O tamanho da palavra está conforme o esperado')
    else:
        print('O tamanho da palavra não é aceitavel')

palavra = input('Digite uma palavra entre 10 e 20 caracteres : ')
palavra_tam = len(palavra)

verifyString(palavra_tam)
