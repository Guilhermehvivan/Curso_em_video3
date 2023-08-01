from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
ranking = []
print('Valores sorteados:  ')
for posicao, valores in jogadores.items():
    print('O {} tirou {}'.format(posicao, valores))
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-'*30)
print('Ranking dos jogadores:  ')
for posicao, valores in enumerate(ranking):
    print('{}° lugar: {} que tirou {}'.format(posicao+1, valores[0], valores[1]))
    sleep(1)

