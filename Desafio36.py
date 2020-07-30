print('                 DIGITE AS INFORMAÇÕES PEDIDAS ABAIXAS\n                  ')
print('Estamos avaliando se sua condição financeira é suficiente para o financiamento da casa dos seus sonhos\n ')
a = int(input('Qual o valor da casa que deseja financiar ? '))
b = int(input('Qual o valor do seu salário mensal ? '))
c = int(input('Em quantos anos deseja parcelar essa casa? '))
d = (a/c)/12
if d >=(3/10)*b:
    print('Você não tem condições de financiar essa casa, tente alguma outra')
    e = int(input('Veja alguma de nossas outras casa '))
    print('                     TENHA UM BOM DIA                ')

else:
    print('Você pode financiar essa casa')
    print('O valor da sua parcela será R$: {:.2f}'.format(d))

print('                     TENHA UM BOM DIA                ')
