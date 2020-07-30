a = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0]
while a not in 'MF':
   a =  str(input('Dados inválidos. Informe seu sexo corretamente: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(a))

