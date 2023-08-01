dicio = {}
lista = []
soma = 0
x = str(input('Nome do jogador:  '))
dicio['nome'] = x
y = int(input('Quantas partidas {} jogou?  '.format(x)))
for cont in range(1, y+1):
    z = int(input('Quantos gols na partida {}?  '.format(cont)))
    soma = soma + z
    lista.append(z)
    dicio['gols'] = lista[:]
    dicio['total'] = soma
print('-='*25)
print(dicio)
print('-='*25)
for valores in dicio.items():
    print('O campo {} tem valor {}'.format(valores[0], valores[1]))
print('-=' * 25)
print('O jogador {} jogou {} jogos'.format(x, y))
for posicao, valores in enumerate(lista):
    print('=> Na partida {}, fez {} gols'.format(posicao+1, valores))
print('Foi um total de {}'.format(soma))