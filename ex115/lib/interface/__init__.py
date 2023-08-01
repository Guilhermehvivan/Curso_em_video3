def menu(lista):
    print('-'*30)
    print('Cadastro de pessoas'.center(30))
    print('-'*30)
    c = 1
    for item in lista:
        print('{} - {}'.format(c, item))
        c = c + 1
    print('-'*30)
    opc = leiaInt('Escolha uma opção:  ')
    return opc


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro. Digite um número inteiro.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não digitar o número\033[m')
            return 0
        else:
            return n