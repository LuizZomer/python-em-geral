numero_str = input('ME conte um numero: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float *2}')

except:
    print('Nâo é um numero')