import random
import time

print('[0] para Pedra')
print('[1] para Papel')
print('[2] para Tesoura')
b = str(input('Escolha uma das opções acima '))
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)

lista=['3', '4', '5']
a = random.choice(lista)
if b == '0' and a == '3':
    print('A partida empatou. O computador escolheu pedra')
elif b == '1' and a == '3':
    print('Parabéns! O computador escolheu pedra. Você venceu!')
elif b == '2' and a == '3':
    print('Que pena! O computador escolheu pedra. Você Perdeu!')
elif b == '0' and a == '4':
    print('Que pena! O computador escolheu papel. Você perdeu!')
elif b == '0' and a == '5':
    print('Parabéns! O computador escolheu tesoura. Você venceu!')
elif b == '1' and a == '4':
    print('A partida empatou. O computador escolheu papel')
elif b == '1' and a == '5':
    print('Parabéns! O computador escolheu tesoura. Você venceu!')
elif b == '2' and a == '4':
    print('Parabéns! O computador escolheu papel. Você venceu!')
elif b == '2' and a == '5':
    print('A partida empatou. O computador escolheu tesoura')
else:
    print('Erro! Responda corretamente!')



print('--------Pedra, Papel e Tesoura------------')


