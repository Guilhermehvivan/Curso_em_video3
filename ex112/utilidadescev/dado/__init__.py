def leiaDinheiro(msg):
    ok = False
    while True:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print('\033[0;31mErro. "{}" não é válido.\033[m'.format(n))
        else:
            ok = True
            return float(n)
