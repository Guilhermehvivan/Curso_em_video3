lista = [[], []]
for x in range(0, 7):
    y = (int(input('Digite o {}° valor:  '.format(x+1))))
    if y % 2 == 0:
        lista[0].append(y)
    else:
        lista[1].append(y)

print('Os valores pares foram {}'.format(sorted(lista[0])))
print('Os valores ímpares foram {}'.format(sorted(lista[1])))