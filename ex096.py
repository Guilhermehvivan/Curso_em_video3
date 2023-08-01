def area(l, c):
    tamanho = l*c
    print('A área deste terreno é {}m²'.format(tamanho))

print('Controle de terrenos')
x = float(input('Digite a largura do terreno (m):  '))
y = float(input('Digite o comprimento do terreno (m):   '))
area(x, y)