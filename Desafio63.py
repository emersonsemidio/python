print('-' * 10)
print('Sequência de Fibonacci: ')
first = 0
second = 1
soma = first + second
cont = 3
a = int(input('Quantos termos você deseja mostrar? '))
print('{} {}'.format(first,second),end=' ')
while cont <= a:
    cont = cont +1
    soma = first + second
    print('{}'.format(soma),end=' ')
    first = second
    second = soma
print('FIM')
