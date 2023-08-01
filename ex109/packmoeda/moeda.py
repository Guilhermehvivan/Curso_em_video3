def metade(n, formato=False):
    x = n/2
    return x if formato is False else moeda(x)
def dobro(n, formato=False):
    x = n*2
    return x if formato is False else moeda(x)
def aumentar (n, y, formato=False):
    x = n + (n*y/100)
    return x if formato is False else moeda(x)
def diminuir (n, z, formato=False):
    x = n - (n*z/100)
    return x if formato is False else moeda(x)
def moeda(n=0):
    return 'R${}'.format(n)