def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro. Digite um número inteiro.\033[m ')
            continue
        else:
            return n


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Arquivo não encontrado')
    else:
        print('Arquivo criado')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print('-'*30)
        print(a.read())
    finally:
        a.close()


def escreverArquivo(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro')
    else:
        try:
            a.write('{} - {} anos\n'.format(nome, idade))
        except:
            print('Erro')
        else:
            print('Registro de {} adicionado'.format(nome))
            a.close()
