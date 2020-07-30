frase = str(input('Digite a frase: ')).strip().upper()
print('Você digitou a frase {}'.format(frase))
palavras = frase.split()
junto = ''.join(frase)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')