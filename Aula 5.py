#MANIPULANDO CADEIA DE TEXTOS

#ANÁLISE
#1 - Comando len(frase) comprimento
#2 - Comando frase.count('**') conta quantas vezes aparece a letra nos parênteses na frase
#frase.count('**',0,13) conta quantos caractéres ** tem até o número 12
#frase.find('**) encontra o local de uma ou mais letras específicas no texto

#TRANSFORMAÇÃO


#DESAFIO 22

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seus dados...')

a = nome.upper()
b = nome.lower()
#c = len(nome) - nome.count(' ')
d = nome.find(' ')
print('Seu nome em maiusculo é {}'.format(a))
print('Seu nome em minusculo é {}'.format(b))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(d))

#DESAFIO 23




