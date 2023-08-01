dicio = {}
lista = []
continuar = 'S'
soma = 0
cont = 0
while continuar == 'S':
    dicio.clear()
    dicio['nome'] = str(input('Nome:  '))
    dicio['sexo'] = str(input('Sexo[M/F]:  ')).upper().strip()
    while dicio['sexo'] not in 'MF':
        dicio['sexo'] = str(input('Digite corretamente. [M/F]  ')).upper().strip()
    z = int(input('Idade:  '))
    soma = soma + z
    dicio['idade'] = z
    lista.append(dicio.copy())
    continuar = str(input('Quer continuar?[S/N]  ')).strip().upper()
print('-='*25)
x = len(lista)
print('- O grupo tem {} pessoas'.format(x))
media = soma/x
print('- A média de idade é de {:.2f} anos'.format(media))
print('- As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print('{}'.format(p['nome']), end=' ')
print()
print('- As pessoas que tem idade acima da média são:  ', end='')
for p in lista:
    if p['idade'] >= media:
        for k, v in p.items():
            print('{} = {}'.format(k, v), end=' ')
            print()



