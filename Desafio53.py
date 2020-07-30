a = str(input('Digite uma frase ')).lower()
if a == ' ':
    print('\033[31mDigite alguma coisa')
elif a [::-1] == a:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')