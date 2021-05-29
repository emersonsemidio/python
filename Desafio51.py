print('---------10 TERMOS DE UMA PA----------')
a = int(input('Primeiro termo: '))
b = int(input('Digite a razão da PA: '))
print('Os termos são:')
for c in range(0,10):
    x=a+b*(c)
    print('{}'.format(x), end='    ')



