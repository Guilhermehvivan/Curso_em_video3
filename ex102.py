import math
def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :type show: object
    :param n: o número a ser calculado.
    :param show: mostrar ou não a conta.
    :return: o valor do fatorial de um número n.
    """
    x = math.factorial(n)
    if show:
        for c in range(n, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        print(x)
    else:
        return print('O fatorial de {} é {}'.format(n, x))

# Programa principal
(fatorial(8, True))
