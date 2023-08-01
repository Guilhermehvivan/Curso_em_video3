from time import sleep
def ajuda (x):
    help(x)
    sleep(1)


def titulo (msg, cor=0):
    tam = len(msg) + 4
    print('~'*tam)
    print('  {}'.format(msg))
    print('~'*tam)
    sleep(1)


comando = ''
while True:
    titulo('Sistema de ajuda PyHelp')
    comando = str(input('Função ou biblioteca:  '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo')