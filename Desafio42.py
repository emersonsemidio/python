a = int(input('Primeiro lado do triângulo '))
b = int(input('Segundo lado do triângulo '))
c = int(input('Terceiro lado do triângulo '))
if a == b and a == c:
    print('Triângulo equilátero ')
elif a + b < c or a + c < b or b + c < a:
    print('Impossível formar triângulo com esses lados')
elif a == b or a == c or b == c:
    print('Triângulo isósceles')
elif a != b != c:
    print('Triângulo escaleno')
elif a + b > c or a + c > b or b + c > a:
    print('Impossível formar triângulo com esses lados')
