palavras = ('EU', 'VOCE', 'VERDADEIRO', 'FALSO', 'MENTIROSO', 'MENTIRA')
fon = ('A', 'E', 'I', 'O', 'U')

for c in palavras:
    if 'A' or 'E' or 'I' or 'O' or 'U' in c:
        print(f'\nNa palavra {c} as vogais são: ')
        for letra in fon:
            if letra in c:
                print(letra, end=' ')
    print()
    print('-'*30)

