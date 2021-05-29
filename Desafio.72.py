numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Digite um número entre 0 e 20: '))
if num > 20 or num <0:
    print('Erro!!! ', end='')
    num = int(input('Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numeros[num]}')

