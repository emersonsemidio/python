cont = soma = 0
while True:
    a = int(input('Digite um número [999 para parar]: '))
    if a == 999:
        break
    cont = cont +1
    soma = soma +a
print(f'Foram digitados {cont} números e a soma foi {soma}!')
