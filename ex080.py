lista = []
for x in range(0, 5):
    n = int(input('Digite um valor:  '))
    if x == 0 or n > lista[-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao = posicao + 1
print('-'*30)
print(lista)