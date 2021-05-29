

sexom = sexof = maiordezoito = 0
a = ''
c = ''
while True:
    if a == 'N':
        break
    print('-----------------')
    print('Cadastre uma pessoa')
    print('-----------------')
    b = int(input('Idade: '))
    c = str(input('Sexo [M/F]: ')).strip().upper()
    while c not in 'MF':
        c = str(input('Sexo [M/F]: ')).strip().upper()
    a = str(input('Quer continuar? [S/N]: ')).upper()
    while a not in 'SN':
        a = str(input('Quer continuar? [S/N]: ')).upper()

    if b > 18:
        maiordezoito = maiordezoito + 1
    elif c == 'M':
        sexom = sexom + 1
    if c in 'Ff' and b < 20:
        sexof = sexof + 1

print(f'Total de pessoas com mais de 18 anos: {maiordezoito}')
print(f'Total de homens cadastrados: {sexom}')
print(f'Total de mulheres com menos de 20 anos: {sexof}')

