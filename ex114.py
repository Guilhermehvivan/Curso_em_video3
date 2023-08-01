from urllib import request, error
try:
    site = request.urlopen('http://www.pudim.com.br')
except error.URLError:
    print('O site PUDIM não está acessível!')
else:
    print('Consegui acessar o site PUDIM!')
