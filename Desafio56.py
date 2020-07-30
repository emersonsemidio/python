idade1 = 0
sexom = 0
sexof = 0
menosvinte = 0
maioridadehomem = 0
homemmaisvelho = ''
for c in range(1,5):
    print('\033[31m------{}ª Pessoa------\033[m'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    idade1 = idade1 + idade
    sexo = str(input('Sexo: [M/F] : ')).upper()
    if sexo == 'M':
        sexom = sexom +1
    if sexo == 'F':
        sexof = sexof +1
        if idade < 20:
            menosvinte = menosvinte + 1
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemmaisvelho = nome
    if sexo in 'mM' and idade > maioridadehomem:
        maioridadehomem = idade
        homemmaisvelho = nome

a = idade1/4

print('\033[31mA média de idade do grupo é {:.1f} anos'.format(a))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maioridadehomem,homemmaisvelho))

if menosvinte == 1:
    print('Ao todo há 1 mulher com menos de vinte anos no grupo')
elif menosvinte == 0:
    print('Não há mulheres com menos de vinte anos no grupo')
else:
    print('Ao todo há {} mulheres com menos de vinte anos no grupo'.format(menosvinte))

if sexom == 1:
    print('Ao todo há 1 homem no grupo')
elif sexom == 0:
    print('Não há homens no grupo')

else:
    print('Ao todo há {} homens no grupo'.format(sexom))

if sexof == 1:
    print('Ao todo há 1 mulher no grupo')
elif sexof == 0:
    print('Não há mulheres no grupo')
else:
    print('Ao todo há {} mulheres no grupo'.format(sexof))
