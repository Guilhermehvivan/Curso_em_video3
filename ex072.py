numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
pergunta = int(input('Digite um número de 0 a 20:  '))
lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
while pergunta not in lista:
    pergunta = int(input('Digite corretamente um número de 0 a 20:  '))
print('Você digitou o número {}'.format(numeros[pergunta]))
