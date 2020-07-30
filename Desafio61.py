import time
a = int(input('Digite o primeiro termo: '))
b = int(input('Digite a razão: '))
cont = 0
termo = a
while cont <10:
    print('{}'.format(termo),end=' > ')
    termo = termo + b
    cont = cont +1
    time.sleep(2)
print('FIM')



