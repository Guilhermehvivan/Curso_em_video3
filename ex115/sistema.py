from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'arquivo1.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Mostrar lista', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        nome = str(input('Nome:  ')).title().strip()
        idade = leiaInt('Idade:  ').strip()
        escreverArquivo(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...')
        break
    else:
        print('Erro. Digite um número válido.')
    sleep(1)