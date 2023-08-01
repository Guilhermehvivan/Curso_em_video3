from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
total = 1
pergunta = int(input('Quantos jogos você deseja sortear?  '))
while total <= pergunta:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont = cont + 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total = total + 1
for i, l in enumerate(jogos):
    print('Jogo {}: {}'.format(i+1, l))
    sleep(1)

