pessoas = []
dado = []
cont = 0
continuar = 'S'
while continuar == 'S':
    dado.append(str(input('Digite o nome:  ')))
    dado.append(float(input('Digite o peso em Kg:  ')))
    cont = cont + 1
    continuar = str(input('Quer continuar? [S/N]  ')).strip().upper()
    pessoas.append(dado[:])
    dado.clear()
print('Ao todo são {} pessoas'.format(cont))
for p in pessoas:
    dado.append(p[1])
print('Com {}Kg, as pessoas mais pesadas foram: '.format(max(dado)), end='')
for p in pessoas:
    if p[1] == max(dado):
        print('{}'.format(p[0]), end='')
print('\nCom {}Kg, as pessoas mais leves foram: '.format(min(dado)), end='')
for p in pessoas:
    if p[1] == min(dado):
        print('{}'.format(p[0]), end='')




