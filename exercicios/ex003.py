num1 = input('Digite um numero inteiro: ')

try:
    num = int(num1) 
    if num%2==0:
        print('É um numero par')
    else:
        print('É impar')

except:
    print('Não é um numero ou não é um numero inteiro')

