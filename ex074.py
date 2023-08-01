import random
aleatorio = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
for x in aleatorio:
    print((x), end=' ')
print('\nO maior valor foi {}'.format(max(aleatorio)))
print('O menor valor foi {}'.format(min(aleatorio)))



