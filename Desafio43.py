a = float(input('Digite seu peso em KG '))
b = float(input('Digite sua altura em metros '))
c = a / b**2
if c > 0 and c <= 18.5:
    print('Abaixo do peso ')
elif c > 18.5 and c <= 25:
    print('Peso ideal ')
elif c > 25 and c <=30:
    print('Sobrepeso ')
elif c > 30 and c <=40:
    print('Obesidade ')
elif c > 40:
    print('Obesidade mórbida')

print('\033[1mObrigado por participar!!!')