b = 0
cont = 0
a = 0
while a != 999:
    cont = cont + 1
    a = int(input('Digite um número [999] para parar: '))
    b = b + a
print('Foram {} digitos e a soma é {}'.format(cont-1,b-999))