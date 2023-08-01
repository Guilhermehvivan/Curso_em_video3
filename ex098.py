from time import sleep
def contador(i, f, p):
    if p < 0:
        p = p * -1
    if p == 0:
        p = p + 1
    print('\n')
    print('Contagem de {} até {} de {} em {}: '.format(i, f, p, p))
    if i < f:
        cont = i
        while cont <= f:
            print('{}  '.format(cont), end='', flush=True)
            sleep(0.3)
            cont = cont + p
    else:
        cont = i
        while cont >= f:
            print('{}  '.format(cont), end='', flush=True)
            sleep(0.3)
            cont = cont - p


contador(1, 10, 1)
contador(10, 0, 2)
print('\n')
ini = int(input('Digite o início:  '))
fim = int(input('Digite o fim:  '))
passo = int(input('Digite o passo:  '))
contador(ini, fim, passo)
