cont = b  = soma = maior = menor = 0
a = ''
c = ''
while a in 'sS':
    b = int(input('Digite um número: '))
    soma = soma +b
    cont = cont +1
    a = str(input('Quer continuar[S/N]? ')).upper().strip()
    while a not in 'SsNn':
        a = str(input('\033[31mErro!!!\033[0m Quer continuar[S/N]? ')).upper().strip()
    if cont ==1:
        maior = menor = b
    else:
        if b > maior:
            maior = b
        if b < menor:
            menor = b

media = soma/cont
print('A média é {:.2f}'.format(media))
print('O menor e o maior valor são: {} e {}'.format(menor,maior))