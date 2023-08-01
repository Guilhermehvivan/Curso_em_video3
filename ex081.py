lista = []
cont = 0
continuar = 'S'
while continuar in 'S':
    x = (int(input('Digite um valor:  ')))
    cont = cont + 1
    continuar = str(input('Quer continuar? [S/N]  ')).upper()
    lista.append(x)
lista.sort(reverse=True)
print('=-'*30)
print('Foram digitados {} números'.format(cont))
print('A lista decrescente é {}'.format(lista))
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')