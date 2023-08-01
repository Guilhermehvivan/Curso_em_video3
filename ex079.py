lista = []
continuar = 'S'
while continuar in 'S':
    x = (int(input('Digite um valor:  ')))
    if x not in lista:
        lista.append(x)
        print('Você acrescentou {}'.format(x))
    else:
        print('Este número não será acrescentado')
    continuar = str(input('Quer continuar? [S/N]  ')).upper()
print('Você digitou os valores {}'.format(sorted(lista)))