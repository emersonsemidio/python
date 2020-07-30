import random
print('-----JOGO DA ADIVINHAÇÃO-----')
cont = 0
a = str(input('Olá, sou seu computador. Vamos brincar um pouco? (responda SIM para prosseguir) ')).upper()
while a != 'SIM':
    a = str(input('\033[31mResposta errada!\033[m Vamos tentar novamente, responda com SIM para proseguir '))
print('Olá, sou eu aqui de novo, já vi que você quer brincar, vamos ver se você consegue me vencer')
print('O jogo consiste em você adivinhar qual número de 0 à 10 eu escolhi')
b = random.randint(0,10)
d = int(input('Informe o número: '))
while d != b:
    if d > b:
        print('Tente um número menor')
    if d < b:
        print('Tente um número maior')
    d = int(input('Informe o número desejado: '))
    cont += 1
if cont == 1:
    print('Parabéns, você acertou em 1 tentativa')
else:
    print('Parabéns, você acertou em {} tentaivas'.format(cont+1))





