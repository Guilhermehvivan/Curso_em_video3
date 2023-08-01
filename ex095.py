dicio = {}
lista = []
jogadores = []
continuar = 'S'
while continuar == 'S':
    lista.clear()
    dicio.clear()
    x = str(input('Nome do jogador:  '))
    dicio['nome'] = x
    y = int(input('Quantas partidas {} jogou?  '.format(x)))
    for cont in range(1, y+1):
        z = int(input('   => Quantos gols na partida {}?  '.format(cont)))
        lista.append(z)
        dicio['gols'] = lista[:]
        dicio['total'] = sum(lista)
    jogadores.append(dicio.copy())
    continuar = str(input('Quer continuar?[S/N]  ')).strip().upper()
print('-='*25)
print('cod', end=' ')
print('nome', end='      ')
print('gols', end='      ')
print('total')
print('-'*25)
for p, v in enumerate(jogadores):
    print('{} {}   {}      {}'.format(p, v['nome'], v['gols'], v['total']))
print('-'*25)
while True:
    pergunta = int(input('Mostrar dados de qual jogador (999 para parar)?  '))
    if pergunta != 999 and pergunta <= len(jogadores):
        print('--- Levantamento do jogador {}'.format(jogadores[pergunta]['nome']))
        for posicao, valores in enumerate(jogadores[pergunta]['gols']):
            print('No jogo {} fez {} gols'.format(posicao+1, valores))
    else:
        break


