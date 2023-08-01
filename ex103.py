def ficha(nome, gols):
    if not nome:
        nome = 'desconhecido'
    if not gols or not gols.isnumeric():
        gols = 0
    print('O jogador {} fez {} gol(s) no campeonato'.format(nome, gols))


a = str(input('Nome do jogador:  ')).strip()
b = str(input('Número de gols:  '))
ficha(a, b)



