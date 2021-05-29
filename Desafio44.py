print('{:-^20}'.format('----------Lista de compras-----------'))
a = float(input('Preço das compras: R$:  '))
print('----------Formas de pagamento------------')
print('[1] à vista no dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão\n')
b = str(input('Escolha sua forma de pagamento '))
if b in '1':
    print('sua compra de R${:.2f} vai custar R${:.2f}'.format(a,a*0.9))
elif b in '2':
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(a,a*0.95))
elif b in '3':
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(a,a))
elif b in '4':
    c = int(input('Total de Parcelas: '))
    totalparc =  c + (c*20/100)
    precoparc = (a*120/100)/c
    print('Sua compra de R${:.2f} vai custar R${:.2f} com {} parcelas de R${:.2f}'.format(a,a*1.2,c,precoparc))
else:
    print('\033[1;31mERRO, PREENCHA AS INFORMAÇÕES CORRETAMENTE')
