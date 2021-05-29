
continua = ''
nomemaisbarato = ''
menorpreco = precototal = 0
maisquemil = 0
cont = 0

while True:
    if continua == 'N':
        break
    print('-' * 20)
    print('Compras da loja')
    print('-' * 20)

    a = str(input('Nome do produto: '))
    precoProduto = input('Preço do produto: R$ ')
    precoProduto = precoProduto.replace(',', '.')
    b = float(precoProduto)
    if b > 1000:
        maisquemil = maisquemil + 1
    precototal = precototal + b
    cont = cont + 1
    if cont == 1:
        menorpreco = b
        nomemaisbarato = a
    else:
        if b < menorpreco:
            menorpreco = b
            nomemaisbarato = a
    continua = str(input('Quer continuar? [S/N] ')).upper()[0]
    while continua not in 'SsNn':
        continua = str(input('Quer continuar? [S/N] ')).upper()[0]

print(f'O preço total foi R${precototal:.2f}\n')
if maisquemil == 1:
    print('1 produto custa mais de R$1000\n')
else:
    print(f'O total de produtos que custam mais de R$1000 {maisquemil}\n')

print(f'O produto mais barato se chama {nomemaisbarato} e custa {menorpreco:.2f}')

