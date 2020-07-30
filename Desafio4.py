nome = str(input('Digite algo '))
a = nome.isalpha()
print('Só tem letras? {}'.format(a))
b = nome.isnumeric()
print('Só tem números? {}'.format(b))
c = nome.isalnum()
print('Tem letras e números? {}'.format(c))
d = nome.islower()
print('Está em minúsculo ? {}'.format(d))
e = nome.isupper()
print('Está em maiúsculo? {}'.format(e))
f = len(nome) - nome.count(' ')
print('O que foi digitado tem {} caractéres'.format(f))




