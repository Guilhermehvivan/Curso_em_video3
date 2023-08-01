from datetime import date
lista = {}
while True:
    a = str(input('Nome:  '))
    b = int(input('Ano de nascimento:  '))
    c = int(input('Carteira de trabalho (Digite 0 caso não tenha):  '))
    lista['Nome'] = a
    lista['Idade'] = date.today().year - b
    lista['CTPS'] = c
    if c == 0:
        break
    else:
        d = int(input('Ano de contratação:  '))
        e = int(input('Salário:  '))
        lista['Contratação'] = d
        lista['Salário'] = e
        lista['Aposentadoria'] = (d + 35) - b
        break
for valores in lista.items():
    print('{} tem o valor {}'.format(valores[0], valores[1]))


