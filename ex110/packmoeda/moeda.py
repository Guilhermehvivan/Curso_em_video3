def metade(n, formato=False):
    x = n/2
    return x if formato is False else moeda(x)
def dobro(n, formato=False):
    x = n*2
    return x if formato is False else moeda(x)
def moeda(n=0):
    return 'R${}'.format(n)
def resumo(n, y, z):
    print('-'*30)
    print('      Resumo do valor')
    print('-'*30)
    print('Preço analisado:   {}'.format(moeda(n)))
    print('Dobro do preço:    {}'.format(moeda(dobro(n))))
    print('Metade do preço:   {}'.format(moeda(metade(n))))
    print('{}% de aumento:    {}'.format(y, moeda(n + (n*y/100))))
    print('{}% de redução:    {}'.format(z, moeda(n - (n*z/100))))
