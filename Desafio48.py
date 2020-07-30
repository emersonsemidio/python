cont = 0
soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
         print(c,end=' ')
         cont = cont +1
         soma = soma +c
print('\nA soma de todos {} os números múltiplos de 3 nesse intervalo é {}'.format(cont,soma))
print('\nFIM')
