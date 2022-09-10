frase = input('Digite uma frase : ')
recorte = len(frase) // 2

frase2 = frase[:recorte]

print('A frase recortada fica : {}' .format(frase2))
print('Os ultimos caracteres são : {}' .format(frase2[-2:]))

