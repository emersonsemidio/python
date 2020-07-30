a = str(input('Você é maior de idade? (RESPONDA COM SIM OU NÃO) ')).strip().lower()
if a == 'sim':
    print('Parabéns, você já pode ser preso xD xD \n')
else:
    if a == 'não':
        print('Uma pena, você ainda não pode ser preso xD xD \n')
    else:
        print('Resposta inválida\n')

b = int(input('Quantos anos você tem? '))
if b >=30:
    print('Cuidado com o Coronga \n')
else:
    print('Pode ficar mais suave com o coronga \n ')

c = str(input('Qual anime é melhor, Naruto ou Dragon Ball? ')).lower().strip()
if c == 'naruto':
     print('Parabéns, você tem bom gosto \n')
else:
     print('Vá ao psicólogo com urgência\n ')

print('Obrigado por participar de nosso primeiro questionário')












