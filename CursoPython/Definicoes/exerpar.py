def par_impar(numero):
    if numero % 2 == 0:
        print('É par')
        escolha()
        
    else:
        print('É impar')
        escolha()



def escolha():
    numero = int(input('Escolha um numero: '))
    par_impar(numero)

escolha()
