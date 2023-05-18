
while True:
    print(20*'=')
    print('    Calculadora')
    print(20*'=')
    continuar = input('Deseja calcular[S/N]? ').upper()
    if continuar == 'S':
        numero_str = input('Escolha um numero: ')
        numero_str1 = input('Escolha outro numero: ')

        try:
            numero_1 = float(numero_str)
            numero_2 = float(numero_str1)
            print('1 - Somar\n2 - Subtrair\n3 - multiplicar\n4 - dividir')
            escolha1 = input('Escolha: ')
            try:
                escolha = int(escolha1)
                match escolha:
                    case 1:
                        print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
                    case 2:
                        print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')
                    case 3:
                        print(f'{numero_1} x {numero_2} = {numero_1 * numero_2}')
                    case 4:
                        print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')
                    case _:
                        print('Valor invalido')
            except:
                print('Valor invalido')
        
        except:
            print('Você não colocou um numero')
            
    else:
        break
print('Encerrando')