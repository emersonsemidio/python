print('     Atletas da natação!     ')
a = int(input('Qual a idade do atleta? '))
if a > 0 and a <= 9:
    print('Atleta categoria mirim')
elif a > 9 and a <=14:
    print('Atleta categoria Infantil')
elif a > 14 and a <=19:
    print('Atleta categoria Junior')
else:
    print('Atleta categoria Master')
