lista = ('Placa-Mãe', 800,
         'Processador', 1000,
         'ssd', 200,
         'Teclado', 120,
         'Mouse', 80,)
for c in range(0, len(lista)):
    if c % 2 ==0:
        print(f'{lista[c]:.<30}', end ='')
    else:
        print(f'R${lista[c]:>5}')


