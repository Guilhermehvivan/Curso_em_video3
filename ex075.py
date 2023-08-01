a = int(input('Digite o primeiro número:  '))
b = int(input('Digite o segundo número:  '))
c = int(input('Digite o terceiro número:  '))
d = int(input('Digite o quarto número:  '))
lista = (a, b, c, d)
print('O valor 9 apareceu {} vezes'.format(lista.count(9)))
if 3 in lista:
    print('O valor 3 apareceu na posição {}'.format(lista.index(3)+1))
if 3 not in lista:
    print('O valor 3 não apareceu nenhuma vez')
print('Os valores pares foram: ', end='')
for x in lista:
    if x % 2 == 0:
        print(x, end=' ')
