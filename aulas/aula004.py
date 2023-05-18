n1_str = input('Escreva um numero: ')
n2_str = input('Escreva outro numero: ')

try:
    n1_float = float(n1_str)
    n2_float = float(n2_str)
    try:
        print(f'{n1_float} / {n2_float} = {n1_float / n2_float}')
    except:
        print('Impossivel dividir por zero')
except:
    print('Não é um numero')