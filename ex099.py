from time import sleep
def maior(*num):
    print('\nAnalisando os valores:  ')
    if len(num) > 0:
        maior = max(num)
        print('{}. Foram informados {} números'.format(num, len(num)), flush=True)
        sleep(1)
        print('O maior valor analisado foi {}'.format(maior))
        sleep(0.5)
    else:
        print('Não foi informado nenhum valor')



maior(9, 2, 8, 5, 1)
maior(2, 7, 4)
maior(4, 0)
maior(1)
maior()