lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input('Digite o valor na posição ({}, {}):  '.format(l, c)))
for l in range(0, 3):
    for c in range(0, 3):
        print('[{}]'.format(lista[l][c]), end='')
        if lista[l][c] % 2 == 0:
            somapar = somapar + lista[l][c]
    print()
print('-'*30)
print('A soma dos valores pares é {}'.format(somapar))
print('A soma dos valores da terceira coluna é {}'.format(lista[0][2]+lista[1][2]+lista[2][2]))
print('O maior valor da segunda linha é {}'.format(max(lista[1])))