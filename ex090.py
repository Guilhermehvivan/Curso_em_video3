aluno = {}
for c in range(0, 1):
    x = str(input('Nome do aluno:  '))
    y = int(input('Média do aluno {}:  '.format(x)))
    aluno['Nome'] = x
    aluno['Média'] = y
    if y >= 7:
        aluno['Situacao'] = 'Aprovado'
    else:
        aluno['Situacao'] = 'Reprovado'
for a, b in aluno.items():
    print('{} é igual a {}'.format(a, b))


