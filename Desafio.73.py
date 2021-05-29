Times = ('São Paulo ', 'Flamengo ', 'Atlético-Mg ', 'Palmeiras ', 'Grêmio ', 'Fluminense ')
print('-=' *20)
print('Os 5 primeiros são ',end = '')


for c in range(0,5):
    print(Times[c],end='')
print('')
print('-=' *20)


print(f'Os 4 últimos são {Times[2:]}')
print('-=' *20)


print(f'O time que em 3° é o {Times[2]}')
print('-=' *20)


