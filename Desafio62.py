termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
first = termo
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <=total:
        print('{}'.format(termo),end=' ')
        termo = termo + razao
        cont = cont + 1
    print('\nPausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')