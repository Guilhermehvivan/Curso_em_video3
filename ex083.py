x = str(input('Digite uma expressão matemática:  '))
lista = []
for y in x:
    if y == '(':
        lista.append('(')
    elif y == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida')
else:
    print('Sua expressão é inválida')