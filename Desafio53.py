frase = str(input('Digite uma frase ')).lower().strip()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    print(junto[letra])
    inverso = inverso +junto[letra]
print('O inverso de {')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não temos um palíndromo')