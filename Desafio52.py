print('-----Desafio dos números primos-----')
bet = 0
tot = 0
num = int(input('Digite um número inteiro: '))
for c in range(1,num+1):
    if num % c ==0:
        print('\033[31m' ,end=' ')
        tot = tot +1
    else:
        print('\033[33m ',end= ' ')
        bet = bet +1
    print(c,end=' ')

print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot <=2 and tot > 0:
    print('\n\033[mO número é primo'.format(tot))
else:
    print('\n\033[mO número não é primo'.format(bet))
