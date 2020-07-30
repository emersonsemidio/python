print('               \033[1m ALISTAMENTO MILITAR \033[m               ')
a = int(input('Qual seu ano de nascimento? '))
if a == 2002:
    print('Seu ano de alismento é esse')
    print('\033[1mObrigado por preencher as informações, tenha um bom dia!!!\033[1m')

elif a < 2002 and a > 1910:
    print('Já passou seu ano de alistamento')
    print('Seu alistamento passou há {} anos'.format(2002-a))
    print('\033[1mObrigado por preencher as informações, tenha um bom dia!!!\033[1m')
elif a > 2002 and a < 2020:
    print('Ainda não chegou sua vez de alistamento ')
    print('Faltam {} anos para seu alistamento'.format(a-2002))
    print('\033[1mObrigado por preencher as informações, tenha um bom dia!!!\033[1m')

else:
    print('\033[1;31mERRO, PREENCHA AS INFORMAÇÕES CORRETAMENTE!!!')

