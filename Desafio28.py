#DESAFIO 23

import random
lista = [0,1,2,3,4,5]
a = random.choice(lista)


b = int(input('Escolha um número inteiro entre 0 e 5 \n'))
print('O número escolhido foi {}'.format(a))
if b == a:
    print('Parabéns, você acertou o número')
else:
    print('Uma pena, você errou o número')


    print('Obrigado por jogar')
