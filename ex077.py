Brasileirao = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Athletico',
               'Sao Paulo', 'Inter', 'Corinthians', 'Fortaleza', 'Goias')
for x in Brasileirao:
    print('\nA palavra {} tem as vogais:  '.format(x), end='')
    for letras in x:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
