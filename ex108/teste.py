from packmoeda import moeda

p = float(input('Digite o preço: R$'))
print('A metade de {} é {}'.format(moeda.moeda(p), moeda.moeda(moeda.metade(p))))
print('O dobro de {} é {}'.format(moeda.moeda(p), moeda.moeda(moeda.dobro(p))))
print('Aumentando 10%, temos {}'.format(moeda.moeda(moeda.aumentar(p, 10))))
print('Reduzindo 13%, temos {}'.format(moeda.moeda(moeda.diminuir(p, 35))))