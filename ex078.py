lista = []
maiorpos = []
menorpos = []
for cont in range(0, 5):
    lista.append(int(input('Digite um valor para a posição {}:  '.format(cont))))
for posicao, valores in enumerate(lista):
    if valores == max(lista):
        maiorpos.append(posicao)
    if valores == min(lista):
        menorpos.append(posicao)
print('=' * 30)
print(lista)
print('O maior valor é {} e está nas posições {}'.format(max(lista), maiorpos))
print('O menor valor é {} e está nas posições {}'.format(min(lista), menorpos))

