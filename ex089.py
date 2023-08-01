lista = []
x = 0
continuar = 'S'
while continuar in 'S':
    nome = str(input('Nome:  '))
    nota1 = float(input('Nota 1:  '))
    nota2 = float(input('Nota 2:  '))
    media = ((nota1 + nota2)/2)
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar?[S/N]  ')).upper().strip()
print('-'*30)
print('{:<4}{:<10}{:>8}'.format("N°", "Nome", "Média"))
for i, a in enumerate(lista):
    print('{:<4}{:<10}{:>8.1f}'.format(i, a[0], a[2]))
while x != 999:
    x = int(input('Mostrar notas de qual aluno (999 para interromper)?  '))
    if x <= len(lista) - 1:
        print('Notas do aluno {} foram {}'.format(lista[x][0], lista[x][1]))
