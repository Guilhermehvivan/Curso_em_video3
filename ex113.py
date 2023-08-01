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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro. Digite um número real.\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não digitar o número\033[m')
            return 0
        else:
            return n


#Programa principal
inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número real:  ')
print('Você acabou de digitar o número inteiro {} e o número real {}'.format(inteiro, real))


