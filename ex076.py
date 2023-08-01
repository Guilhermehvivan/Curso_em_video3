listagem = ('Lápis', 1, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Compasso', 9.99)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end='')
    else:
        print('R${:.2f}'.format(listagem[pos]))