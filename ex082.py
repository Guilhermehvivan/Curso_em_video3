lista = []
listapar = []
listaimpar = []
continuar = 'S'
while continuar in 'S':
    x = (int(input('Digite um valor:  ')))
    continuar = str(input('Quer continuar? [S/N]  ')).upper().strip()
    lista.append(x)
    if x % 2 == 0:
        listapar.append(x)
    else:
        listaimpar.append(x)
print('=-'*30)
print('A lista com todos números é {}'.format(lista))
print('A lista com números pares é {}'.format(listapar))
print('A lista com números ímpares é {}'.format(listaimpar))