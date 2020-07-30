print('Grupos de maioriadade')
b = 0
d = 0
for c in range(1,8):
    a = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if 2020 - a >= 18:
        d = d +1
    else:
        b = b +1
print('Temos um total de {} maiores de idade e {} menores de idade'.format(d,b))



