dicio = {}
def notas (* n, sit = False):
    """

    :param n: notas do aluno
    :param sit: indica se deve ou não adicionar a situação.
    :return: dicionário com informações do aluno
    """
    for c in n:
        dicio['total'] = len(n)
        dicio['maior'] = max(n)
        dicio['menor'] = min(n)
        dicio['média'] = sum(n)/len(n)
        if sit:
            if dicio['média'] >= 7:
                dicio['situação'] = 'Ótima'
            if 5 <= dicio['média'] < 7:
                dicio['situação'] = 'Razoável'
            else:
                dicio['situação'] = 'Ruim'
    return dicio


resp = notas(2, 3, 2, sit=True)
print(resp)
print('-'*30)
help(notas)