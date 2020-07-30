import random

options = ['Pedra', 'Papel', 'Tesoura']

print('Escolha uma das opções:')

for i in range(len(options)):
    print(i+1, options[i])

escolhaUsuario = int(input('Digite um numero: '))
escolhaPC = random.choice(options)
index = escolhaUsuario - 1

if options[index] == escolhaPC:
    print('Empate', escolhaPC)
elif options[index] == 'Pedra' and escolhaPC == 'Papel':
    print('Vc perdeu')
elif options[index] == 'Pedra' and escolhaPC == 'Tesoura':
    print('Vc ganhou')
elif options[index] == 'Papel' and escolhaPC == 'Tesoura':
    print('Vc perdeu')
elif options[index] == 'Papel' and escolhaPC == 'Pedra':
    print('Vc ganhou')
elif options[index] == 'Tesoura' and escolhaPC == 'Papel':
    print('Vc ganhou')
elif options[index] == 'Tesoura' and escolhaPC == 'Pedra':
    print('Vc perdeu')


print('Você escolheu {} e o computador escolheu {}'.format(options[index], escolhaPC))


