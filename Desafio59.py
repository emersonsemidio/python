first = int(input('Digite o primeiro valor: '))
second = int(input('Digite o segundo valor: '))
a = 0
while a != 5:
    print('[1] somar')
    print('[2] subtrair')
    print('[3] Maior número')
    print('[4] novos números')
    print('[5] sair do programa')
    a = int(input('Qual sua opção? '))
    if a ==1:
        print('{} + {} é {}'.format(first,second,first + second))
    if a ==2:
        print('{} - {} é {}'.format(first, second, first - second))
    if a ==3 and first != second:
        if first > second:
            print('O {} é maior que {}'.format(first,second))
        if second > first:
            print('O {} é maior que {}'.format(second,first))
    if a ==4:
        int(input('Digite o primeiro valor: '))
        int(input('Digite o segundo valor: '))
    elif a > 5 or a <0:
        print('Opção inválida. Tente novamente')
print('\033[31mVocê saiu do programa')