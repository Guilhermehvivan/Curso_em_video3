from packmoeda import moeda

p = float(input('Digite o preço: R$'))
print('A metade de R${} é R${}'.format(p, moeda.metade(p)))
print('O dobro de R${} é R${}'.format(p, moeda.dobro(p)))
print('Aumentando 10%, temos R${}'.format(moeda.aumentar(p, 10)))
print('Reduzindo 13%, temos R${}'.format(moeda.diminuir(p, 13)))