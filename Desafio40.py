import random
print('Notas de Pedro')
a = random.randint(0,10)
b = random.randint(0,10)
c = (a+b)/2
print('Primeira nota é {}'.format(a))
print('Segunda nota é {}'.format(b))
print('A média da pedro é {}'.format(c))
if c < 5:
    print('\033[1;31mREPROVADO!!!\033[m')
elif c >= 5 and c <7:
    print('RECUPERAÇÃO!')
elif c > 7:
    print('\033[1;34mAPROVADO!!!')