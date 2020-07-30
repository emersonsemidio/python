a = float(input('Escolha um valor em metros '))
b = a*100
c = a*1000
print('O valor escolhido foi {}'.format(a))
print('Em centímetros é \033[1;35m{:.2f}\033[m'.format(b))
print('O valor em milímetros é \033[1;37m{:.2f}\033[m'.format(c))
