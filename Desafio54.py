import datetime

print('Grupos de maioriadade')
atual = datetime.datetime.today().year
b = 0
d = 0
cont = 0
c = 0
while cont < 7:
    cont = cont +1
    c = c + 1
    a = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if atual - a >= 18:
        d = d +1
    else:
        b = b +1
print('Temos um total de {} maiores de idade e {} menores de idade'.format(d,b))



