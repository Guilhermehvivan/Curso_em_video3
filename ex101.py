from datetime import date
def voto():
    idade = date.today().year - n
    if idade < 16:
        return print('Com {} anos: Sem idade para votar'.format(idade))
    if 16 <= idade < 18 or idade >= 60:
        return print('Com {} anos: Não é obrigatório votar'.format(idade))
    if 18 <= idade < 60:
        return print('Com {} anos: O voto é obrigatório'.format(idade))


n = int(input('Digite o seu ano de nascimento:  '))
(voto())



