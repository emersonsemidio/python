import random
print('-----JOGO DA ADIVINHAÇÃO-----')
cont = 0
a = str(input('Olá, sou seu computador. Vamos brincar um pouco? (responda SIM para prosseguir) ')).upper()
while a != 'SIM':
    a = str(input('\033[31mResposta errada!\033[m Vamos tentar novamente, responda com SIM para proseguir '))
print('Olá, sou eu aqui de novo, já vi que você quer brincar, vamos ver se você consegue me vencer')
print('O jogo consiste em você adivinhar qual número de 0 à 10 eu escolhi')
b = random.randint(0,10)
acertou = False
tentativas = 0
while acertou == False:
    d = int(input('Escolha um número: '))
    tentativas = tentativas + 1
    if d == b:
        acertou = True
    else:
        if d > b:
            print('Tente um número menor')
        if d < b:
            print('Tente um número maior')
if tentativas == 1:
    print('Você acertou em 1 tentativa')
else:
    print('Você acertou em {} tentativas'.format(tentativas))



