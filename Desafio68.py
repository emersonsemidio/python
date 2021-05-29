import random
d = ''
b = ''
while True:
    if d == 'não':
        break
    a = int(input('Escolha um número de 0 à 10: '))

    while a >10:
        a = int(input('Escolha um número de 0 à 10: '))

    b = str(input('Par ou Ímpar? [P/I] '))[0].upper()
    while b not in 'PIpi':
        b = str(input('Par ou Ímpar? [P/I] '))[0].upper()

    c = random.randint(0, 11)
    total = a + c
    if 1 == total %2 and b == 'I':
        print(f'Você escolheu {a} e o computador escolheu {c}.\n A soma foi {total} e você venceu ')
    elif 0 == total %2 and b == 'P':
        print(f'Você escolheu {a} e o computador escolheu {c}.\n A soma foi {total} e você venceu')
    elif 1 == total %2 and b == 'P':
        print(f'Você escolheu {a} e o computador escolheu {c}.\n A soma foi {total} e você perdeu')
    elif 0 == total %2 and b == 'I':
        print(f'Você escolheu {a} e o computador escolheu {c}.\n A soma foi {total} e você perdeu')

    d = str(input('Você quer continuar jogando?[Responda com "sim" ou "não"]: ')).lower()






