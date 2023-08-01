lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input('Digite o valor na posição ({}, {}):  '.format(l, c)))
for l in range(0, 3):
    for c in range(0,3):
        print('[{}]'.format(lista[l][c]), end='')
    print()




